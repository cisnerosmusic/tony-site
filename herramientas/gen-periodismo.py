# Genera el archivo de prensa: la habitacion de cada trabajo periodistico en
# /periodista/<slug>/ y el bloque que los lista dentro de /periodista/.
#
# El periodista es una pagina escrita a mano, con su ficha de redaccion y su
# trayectoria, y sigue siendolo: aqui solo se reescribe lo que hay entre los
# marcadores
#
#   <!-- trabajos -->
#     <!-- /trabajos -->
#
# Es la misma tecnica que gen-audios.py usa con las grabaciones, y por la misma
# razon: el dato vive una sola vez, en el manifiesto, y el resto de la pagina
# se sigue editando a mano. Correrlo dos veces no cambia nada.
#
# De momento solo en español. Los trabajos son periodismo cultural cubano
# escrito en español y, como la literatura, no se traducen; el dia que haya
# version inglesa sera una capa periodismo.en.json con el aparato, como en
# todas las demas salas.
#
# Uso: python herramientas/gen-periodismo.py

import json, os, re, sys, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pagina
from pagina import esc, esc_attr, cabeza, menu, pie, migas

RAIZ = pagina.RAIZ
DOMINIO = pagina.DOMINIO
RUTA = "/periodista/"
TEXTOS = os.path.join(RAIZ, "herramientas", "textos")

VOLVER = "Volver a El periodista"
LEER = "Leer el trabajo"


def leer(ruta):
    with open(os.path.join(TEXTOS, ruta.replace("/", os.sep)), encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n").strip("\n")


def saca(lineas, esperadas, slug, que):
    """Quita del cuerpo lineas que el manifiesto ya declara aparte, y se para
    si no son exactamente las declaradas."""
    for e in esperadas:
        while lineas and not lineas[0]:
            lineas.pop(0)
        if not lineas or lineas[0] != e:
            sys.exit(f"{slug}: esperaba en {que} la línea «{e}» y vino "
                     f"«{lineas[0] if lineas else '(nada)'}»")
        lineas.pop(0)


def cuerpo(t, texto):
    """El cuerpo del trabajo, con sus intertitulos y, si es entrevista, con las
    preguntas marcadas aparte."""
    lineas = [l.strip() for l in texto.split("\n")]

    def pelado(s):
        """Mayusculas y sin tildes. Los titulares llegan en mayusculas y a
        veces sin acentuar: «TROVA ELECTRICA» por «Trova eléctrica». Sin esto,
        el titular se colaba otra vez dentro del cuerpo."""
        return "".join(c for c in unicodedata.normalize("NFD", s.upper())
                       if not unicodedata.combining(c))

    def quita_cabecera():
        """Fuera el antetitulo, el titular en mayusculas, la firma y el credito
        de foto, que ya salen en la cabecera de la pagina."""
        fuera = {pelado(t["titulo"]), pelado(t.get("antetitulo", "")), ""}
        while lineas and (pelado(lineas[0]) in fuera
                          or lineas[0].lower().startswith("por:")
                          or lineas[0].lower().startswith("por ant")
                          or (t.get("credito") and lineas[0] == t["credito"])):
            lineas.pop(0)

    quita_cabecera()
    partes = []
    if t.get("nota"):
        # En la entrevista a Varela la entradilla va ANTES del antetitulo y del
        # titular, asi que la cabecera se limpia otra vez despues de sacarla.
        saca(lineas, [t["nota"]], t["slug"], "la entradilla")
        partes.append(f'  <p class="periodismo-nota">{esc(t["nota"])}</p>')
        quita_cabecera()
    if t.get("dedicatoria"):
        saca(lineas, t["dedicatoria"], t["slug"], "la dedicatoria")
        partes.append('  <p class="texto-dedicatoria">'
                      + "<br>\n  ".join(esc(l) for l in t["dedicatoria"]) + '</p>')
    if t.get("epigrafe"):
        e = t["epigrafe"]
        saca(lineas, e["versos"] + [e["autor"]], t["slug"], "el epígrafe")
        partes.append('  <blockquote class="poema-epigrafe">\n'
                      + "\n".join(f'    <div class="verso">{esc(v)}</div>' for v in e["versos"])
                      + f'\n    <cite>{esc(e["autor"])}</cite>\n  </blockquote>')

    subtitulos = list(t.get("subtitulos", []))
    preguntas = set(t.get("preguntas", []))
    nota_final = t.get("nota_final")
    vistos_sub, vistas_preg = [], set()
    for l in lineas:
        if not l:
            continue
        if l in subtitulos:
            partes.append(f'  <h2 class="periodismo-sub">{esc(l)}</h2>')
            vistos_sub.append(l)
        elif l in preguntas or (t.get("dialogo") and l.startswith("– ") and l.rstrip().endswith("?")):
            partes.append(f'  <p class="periodismo-pregunta">{esc(l)}</p>')
            if l in preguntas:
                vistas_preg.add(l)
        elif nota_final and l == nota_final:
            partes.append(f'  <p class="periodismo-nota periodismo-nota-final">{esc(l)}</p>')
            nota_final = None
        else:
            partes.append(f"<p>{esc(l)}</p>")

    if sorted(vistos_sub) != sorted(subtitulos):
        sys.exit(f"{t['slug']}: intertitulos declarados que no estan en el texto: "
                 f"{sorted(set(subtitulos) - set(vistos_sub))}")
    if vistas_preg != preguntas:
        sys.exit(f"{t['slug']}: preguntas declaradas que no estan en el texto: "
                 f"{sorted(preguntas - vistas_preg)}")
    if nota_final:
        sys.exit(f"{t['slug']}: la nota final declarada no aparece en el texto")
    return "\n".join(partes)


def ficha(t):
    """Medio y fecha. De nueve trabajos no consta donde salieron, asi que la
    ficha calla el medio en vez de inventarlo; la lista de esos nueve esta en
    PENDIENTES.md, a la espera de que Tony la complete."""
    return " · ".join(x for x in (t.get("medio"), t.get("fecha")) if x)


def pagina_trabajo(t):
    url = f"{DOMINIO}{RUTA}{t['slug']}/"
    datos = {"@context": "https://schema.org", "@type": "Article",
             "headline": t["titulo"], "url": url, "inLanguage": "es",
             "author": {"@id": f"{DOMINIO}/#antonio"},
             "description": t["seo_desc"]}
    if t.get("medio"):
        datos["publisher"] = {"@type": "Organization", "name": t["medio"]}
    ante = (f'  <p class="page-antetitulo">{esc(t["antetitulo"])}</p>\n'
            if t.get("antetitulo") else "")
    f = ficha(t)
    credito = f'  <p class="periodismo-credito">{esc(t["credito"])}</p>\n' if t.get("credito") else ""

    # Sin el «| Antonio López Sánchez» del resto del sitio: los titulares de
    # prensa ya son largos y con el sufijo todos pasaban de los 70 caracteres,
    # que es donde el buscador corta. La firma va dentro de cada titulo.
    return (cabeza("es", t["seo_titulo"], t["seo_desc"], url)
            + '<script type="application/ld+json">\n' + json.dumps(datos, ensure_ascii=False, indent=2) + '\n</script>\n'
            + migas([("Ala del Mar", DOMINIO + "/"), ("El periodista", DOMINIO + RUTA), (t["titulo"], url)])
            + menu("es", RUTA)
            + f"""
<header class="page-header">
{ante}  <h1>{esc(t["titulo"])}</h1>
</header>

<main id="main">
<div class="section cuento">
  <p class="periodismo-ficha">{esc(f)}</p>
{credito}  <div class="cuento-texto periodismo-texto reveal reveal-right">
{cuerpo(t, leer(t["archivo"]))}
  </div>
  <p style="margin-top:2.5rem;"><a href="{RUTA}" class="btn">{esc(VOLVER)}</a></p>
</div>
</main>
"""
            + pie("es", None))


def bloque_indice(cfg):
    """Lo que va entre los marcadores de /periodista/."""
    S = cfg["seccion"]
    ultimo = len(S["entrada"]) - 1
    out = ['  <div class="reveal reveal-right">',
           f'    <h2 class="section-title">{esc(S["titulo"])}</h2>',
           '    <div class="section-divider"></div>']
    for i, p in enumerate(S["entrada"]):
        margen = "3rem" if i == ultimo else "1.5rem"
        out.append(f'    <p class="section-text" style="margin-bottom:{margen};">{esc(p)}</p>')
    out.append('  </div>')

    for g in cfg["grupos"]:
        suyos = [t for t in cfg["trabajos"] if t["grupo"] == g["clave"]]
        if not suyos:
            continue
        out.append('')
        out.append('  <div class="reveal reveal-right" style="margin-top:3.5rem;">')
        out.append(f'    <h3 class="periodismo-grupo">{esc(g["titulo"])}</h3>')
        out.append(f'    <p class="periodismo-grupo-entrada">{esc(g["entrada"])}</p>')
        out.append('  </div>')
        out.append('')
        out.append('  <div class="cuento-lista">')
        for t in suyos:
            f = ficha(t)
            meta = f'    <p class="libro-meta">{esc(f)}</p>\n' if f else ""
            ante = (f'<span class="libro-meta">{esc(t["antetitulo"])}</span> '
                    if t.get("antetitulo") else "")
            out.append(f'  <article class="cuento-ficha reveal reveal-right">\n'
                       f'    <h4 class="libro-titulo">{ante}<a href="{RUTA}{t["slug"]}/">{esc(t["titulo"])}</a></h4>\n'
                       f'{meta}'
                       f'    <p class="libro-sinopsis">{esc(t["linea"])}</p>\n'
                       f'    <p style="margin-top:1.2rem;"><a href="{RUTA}{t["slug"]}/" class="btn">{esc(LEER)}</a></p>\n'
                       f'  </article>')
        out.append('  </div>')
    return "\n".join(out)


def mete_en_indice(bloque):
    ruta = os.path.join(RAIZ, "periodista", "index.html")
    with open(ruta, encoding="utf-8", newline="") as f:
        html = f.read().replace("\r\n", "\n")
    marca = re.compile(r"(<!-- trabajos -->).*?(\n *<!-- /trabajos -->)", re.S)
    if not marca.search(html):
        sys.exit("periodista/index.html no tiene los marcadores <!-- trabajos --> ... <!-- /trabajos -->")
    nuevo = marca.sub(lambda m: m.group(1) + "\n" + bloque + m.group(2), html)
    if nuevo != html:
        with open(ruta, "w", encoding="utf-8", newline="") as f:
            f.write(nuevo)
    return nuevo != html


def main():
    cfg = json.load(open(os.path.join(RAIZ, "herramientas", "periodismo.json"), encoding="utf-8"))
    claves = {g["clave"] for g in cfg["grupos"]}
    for t in cfg["trabajos"]:
        if t["grupo"] not in claves:
            sys.exit(f"{t['slug']}: grupo desconocido «{t['grupo']}»")
        pagina.escribe(RUTA + t["slug"] + "/", pagina_trabajo(t))
    cambio = mete_en_indice(bloque_indice(cfg))
    print(f"escrito: {RUTA} con {len(cfg['trabajos'])} trabajo(s)"
          + ("" if cambio else " · el índice ya estaba al día"))


if __name__ == "__main__":
    main()
