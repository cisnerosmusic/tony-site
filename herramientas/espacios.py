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


def indice():
    """clave -> (linea con rachas, de que original sale)."""
    out, leidos = {}, 0
    for raiz, _, fs in os.walk(ORIGINALES):
        for f in fs:
            if not f.lower().endswith((".rtf", ".docx")) or f.startswith("~$"):
                continue
            p = os.path.join(raiz, f)
            try:
                t = texto_de(p)
            except Exception:
                continue          # un original ilegible no para la auditoria
            leidos += 1
            for l in t.replace(" ", " ").replace("\r", "").split("\n"):
                l = l.rstrip()
                if RACHA.search(l):
                    k = clave(l)
                    if len(k) >= 12:
                        out.setdefault(k, (l, os.path.relpath(p, ORIGINALES)))
    return out, leidos


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


def main():
    if not os.path.isdir(ORIGINALES):
        print(f"No encuentro los originales en {ORIGINALES}")
        return 1
    orig, leidos = indice()
    print(f"{leidos} originales leidos · {len(orig)} lineas con rachas indexadas\n")

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
    if not arreglos and not pendientes:
        print("El verso publicado conserva el espaciado de los originales.")
        return 0
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
