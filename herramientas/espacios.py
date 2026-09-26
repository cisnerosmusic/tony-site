# Audita, y si se le pide repara, el espaciado del verso contra los originales.
#
# Tony usa los espacios multiples como puntuacion: "Y que traigas   mensajera".
# styles.css pinta el verso con white-space: pre-wrap justamente por eso. Aun
# asi el recurso se perdio dos veces sin que nadie lo notara: a-texto.py
# colapsaba las rachas al convertir, y al transcribir a mano se "corrigio" a
# puntuacion convencional. Se recuperaron 133 versos en 21 poemas el 25 de
# septiembre de 2026. Esto queda para que la siguiente tanda se cace sola.
#
# Uso: python herramientas/espacios.py            audita, no escribe
#      python herramientas/espacios.py --aplicar  restituye los huecos
#
# Que hace: indexa cada linea de los originales del autor que lleva racha de
# espacios, la busca en los .txt del repo ignorando espaciado y puntuacion, y
# donde el repo va sin racha trasplanta SOLO los huecos. Las palabras no se
# tocan nunca: `git diff -w` tiene que salir vacio despues de aplicar.
#
# Que NO toca, a proposito:
#   - la prosa, que ahi las rachas son descuido de mecanografia;
#   - el epigrafe, que son versos de otro poeta y llevan su puntuacion
#     canonica, no el tecleo de Tony (Marti, Lezama);
#   - el titulo, que los generadores lo buscan por texto exacto contra los
#     manifiestos y meterle espacios rompe el troceo;
#   - cualquier linea donde no cuadre el numero de palabras: se anota para
#     mirarla a mano y no se decide sola.

import io, os, re, sys, unicodedata, zipfile, html as html_lib
from collections import defaultdict
from importlib.machinery import SourceFileLoader

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXTOS = os.path.join(RAIZ, "herramientas", "textos")
# Los originales del autor viven fuera del repo: no son material publicable.
ORIGINALES = os.path.join(os.path.expanduser("~"), "OneDrive", "Imágenes", "tony")
VERSO = ("poemas", "decimitas", "laureles")
# La prosa no lleva rachas, pero si lleva pausas: la linea en blanco del autor.
PROSA = os.path.join(TEXTOS, "cuentos")
RACHA = re.compile(r"\S  +\S")
APLICAR = "--aplicar" in sys.argv

leer_poema = SourceFileLoader("leer_poema", os.path.join(
    RAIZ, "herramientas", "leer-poema.py")).load_module()


def clave(l):
    """Identidad de la linea, ciega al espaciado y a la puntuacion."""
    l = unicodedata.normalize("NFKD", l).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", l)).strip()


def texto_de(p):
    if p.lower().endswith(".rtf"):
        from striprtf.striprtf import rtf_to_text
        return rtf_to_text(io.open(p, encoding="latin-1").read(), errors="ignore")
    x = zipfile.ZipFile(p).read("word/document.xml").decode("utf-8")
    x = re.sub(r"</w:p>", "\n", x)
    x = re.sub(r"<w:tab[^>]*/>", "\t", x)
    x = re.sub(r"<w:br[^>]*/>", "\n", x)
    return html_lib.unescape(re.sub(r"<[^>]+>", "", x))


def limpio(t):
    """Sin duros ni retornos de carro: el texto tal como se lee."""
    return t.replace(chr(160), chr(32)).replace(chr(13), '')


def originales():
    """Todos los originales del autor, en lineas: ruta -> [linea, ...].

    Solo ve lo que esta suelto en disco. Un documento que siga dentro de un
    zip no existe para esto, y su texto sale «limpio» sin que nadie lo haya
    mirado: por eso el documento de un zip se extrae siempre."""
    docs = {}
    for raiz, _, fs in os.walk(ORIGINALES):
        for f in fs:
            if not f.lower().endswith((".rtf", ".docx")) or f.startswith("~$"):
                continue
            q = os.path.join(raiz, f)
            try:
                t = texto_de(q)
            except Exception:
                continue          # un original ilegible no para la auditoria
            docs[q] = [l.rstrip() for l in limpio(t).split(chr(10))]
    return docs


def indice(docs):
    """clave -> (linea con rachas, de que original sale)."""
    out = {}
    for q, L in docs.items():
        for l in L:
            if RACHA.search(l):
                k = clave(l)
                if len(k) >= 12:
                    out.setdefault(k, (l, os.path.relpath(q, ORIGINALES)))
    return out


def trasplante(linea, fuente):
    """La linea del repo con los huecos y la sangria del original.

    None si no cuadra el numero de palabras: entonces no es una cuestion de
    espaciado y la decide una persona."""
    pal = linea.strip().split()
    h = re.findall(r"\s+", fuente.strip())
    if len(pal) != len(h) + 1:
        return None
    return re.match(r"[ \t]*", fuente).group(0) + "".join(
        p + g for p, g in zip(pal, h + [""]))


def pausas(docs):
    """La linea en blanco entre dos parrafos de prosa tambien es del autor.

    En «Cantar el cuento (III)» separa la narracion de la voz que le habla a
    Olga en segunda persona. a-texto.py las descartaba en prosa y ocho cuentos
    perdieron veintinueve. Aqui solo se insertan blancos: ninguna linea con
    texto se toca, y se comprueba antes de escribir."""
    hechas = 0
    for f in sorted(os.listdir(PROSA)):
        if not f.endswith(".txt"):
            continue
        p = os.path.join(PROSA, f)
        lineas = io.open(p, encoding="utf-8").read().split("\n")
        vivas = [l for l in lineas if l.strip()]
        claves = {clave(l) for l in vivas if len(clave(l)) >= 12}
        mejor, cuantas = None, 0
        for q, L in docs.items():
            c = len({clave(l) for l in L if len(clave(l)) >= 12} & claves)
            if c > cuantas:
                cuantas, mejor = c, q
        if not mejor or cuantas < len(claves) * 0.8:
            continue                      # sin original fiable no se juzga
        L = docs[mejor]
        donde = {}
        for i, l in enumerate(L):
            k = clave(l)
            if len(k) >= 12:
                donde.setdefault(k, i)

        # Las lineas cortas que son unicas en los dos lados: en «Aquelarre»
        # las pausas van justo antes de los numerales «(II)», «(III)».
        def unicas(lista):
            c = {}
            for i, l in enumerate(lista):
                s = l.strip()
                if s and len(clave(s)) < 12:
                    c.setdefault(s, []).append(i)
            return {s: v[0] for s, v in c.items() if len(v) == 1}
        cortas = unicas(L)
        corto = {s: i for s, i in cortas.items() if s in unicas(lineas)}

        nuevas, n = [], 0
        for l in lineas:
            k = clave(l)
            i = donde.get(k) if len(k) >= 12 else corto.get(l.strip())
            if l.strip() and i and nuevas and nuevas[-1].strip() and not L[i - 1].strip():
                nuevas.append("")
                n += 1
            nuevas.append(l)
        if [x for x in nuevas if x.strip()] != vivas:
            print(f"  {f}: el cotejo movio texto, se deja como esta")
            continue
        if n:
            hechas += n
            print(f"  {n:3} pausas  {f}   ({os.path.basename(mejor)[:38]})")
            if APLICAR:
                io.open(p, "w", encoding="utf-8", newline="\n").write("\n".join(nuevas))
    return hechas


def main():
    if not os.path.isdir(ORIGINALES):
        print(f"No encuentro los originales en {ORIGINALES}")
        return 1
    docs = originales()
    orig = indice(docs)
    print(f"{len(docs)} originales leidos · {len(orig)} lineas con rachas indexadas\n")

    arreglos, informe, pendientes = 0, [], []
    for raiz, _, fs in os.walk(TEXTOS):
        if os.path.basename(raiz) not in VERSO:
            continue
        for f in sorted(fs):
            if not f.endswith(".txt"):
                continue
            p = os.path.join(raiz, f)
            rel = os.path.relpath(p, RAIZ)
            bruto = io.open(p, encoding="utf-8").read()
            lineas = bruto.split("\n")
            try:
                P = leer_poema.partes(bruto)
                veda = {l.strip() for l in P["epigrafe"] + P["titulo"] if l.strip()}
            except Exception:
                veda = set()
            veda |= {l.strip() for l in lineas if l.strip().isupper()}
            n = 0
            for i, l in enumerate(lineas):
                if RACHA.search(l) or not l.strip() or l.strip() in veda:
                    continue
                k = clave(l)
                if len(k) < 12 or k not in orig:
                    continue
                cruda, de = orig[k]
                nueva = trasplante(l, cruda)
                if nueva is None:
                    pendientes.append((rel, i + 1, l.strip(), cruda.strip(), de))
                    continue
                if nueva != l:
                    lineas[i] = nueva
                    n += 1
            if n:
                arreglos += n
                informe.append((rel, n))
                if APLICAR:
                    io.open(p, "w", encoding="utf-8", newline="\n").write("\n".join(lineas))

    print("APLICADO\n" if APLICAR else "AUDITORIA (no se ha escrito nada)\n")
    print("Pausas de prosa que faltan:")
    faltan = pausas(docs)
    if not faltan:
        print("  ninguna: los cuentos conservan las lineas en blanco del autor.")
    print()

    if not arreglos and not pendientes:
        print("El verso publicado conserva el espaciado de los originales.")
        return 0 if not faltan else 1
    print(f"{arreglos} versos sin el espaciado del original, en {len(informe)} textos:")
    for rel, n in sorted(informe, key=lambda t: -t[1]):
        print(f"  {n:4}  {rel}")
    if pendientes:
        print(f"\n{len(pendientes)} lineas que no cuadran en palabras (a mano):")
        for rel, ln, a, b, de in pendientes:
            print(f"  {rel}:{ln}\n     repo |{a}|\n     Tony |{b}|   ({de})")
    if not APLICAR and arreglos:
        print("\nPara restituirlos: python herramientas/espacios.py --aplicar")
        print("Despues: regenerar, y `git diff -w` tiene que salir vacio.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
