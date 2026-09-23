# Genera /tinta-ciones/de-cimitas/ desde herramientas/decimitas.json.
#
# Una De-Cimita son dos cosas que solo funcionan juntas: una foto del autor y
# una decima escrita a partir de ella. Por eso cada una sale en una sola pieza,
# con la imagen y los diez versos dentro del mismo marco. Separarlas seria
# deshacer la obra.
#
# Los textos vienen todos en un documento del autor y se cortan por sus
# encabezados; el emparejamiento con la foto va declarado en el manifiesto,
# porque los nombres no siempre coinciden.
#
# Idiomas. Las decimas no se traducen nunca. La capa inglesa, decimitas.en.json,
# trae los textos de la sala y la descripcion de cada foto, y la version
# inglesa sale en /en/poetry/decimitas/.
#
# Uso: python herramientas/gen-decimitas.py

import json, os, sys, html
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pagina

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=35"

ES = {
    "ruta": "/tinta-ciones/de-cimitas/",
    "frase": "Una foto y diez versos que le contestan.",
    "titulo_sala": "Lo que mira la décima",
    "entrada": "Otro modo de hacer poesía es buscar la voz oculta, las historias que habitan detrás de una imagen. Aquí van mis fotos vistas y el poema que escucho en ellas.",
    "aviso": None,
    # La segunda tanda trajo decimas francamente eroticas. La sala entera lleva
    # aviso y rating adult, como las dos obras del Farraluque: no se puede
    # avisar decima a decima porque todas viven en la misma pagina.
    "aviso_adultos": "Entre estas décimas hay poesía erótica, escrita para lectores adultos.",
    "titulo_mayor": "Una que se salió del cuadro",
    "entrada_mayor": "Empezó como las demás, mirando una foto. Pero le crecieron tres movimientos, cada uno con su tempo, y ya no cabía en diez versos. Tiene cuarto propio.",
    "sonata_sinopsis": "Tres movimientos en décimas: un preludio, un aguacero y lo que queda después. Con Fito Páez, Noel Nicola y Santiago Feliú asomados a cada uno.",
    "sonata_nota": "Con ella gané el {premio} en 2026.",
    "sonata_boton": "Leer la sonata",
    "sonata_alt": "Atardecer sobre el muro del malecón, con el sol abriéndose paso entre las nubes",
    "premios_url": "/laureles/",
    "migas": ["Tinta-ciones", "De-Cimitas"],
    "seo_titulo": "De-Cimitas: décimas con imagen de Antonio López Sánchez",
    "seo_desc": ("Décimas del poeta cubano Antonio López Sánchez escritas a partir de sus propias "
                 "fotografías: cada imagen con su décima, en una sola pieza."),
}

# El nombre del premio es nombre propio: no se traduce en ninguna lengua.
PREMIO = "Premio Colateral Yasmina Calcines"


def esc(t):
    """Texto visible: se dejan las comillas como el autor las escribio."""
    return html.escape(t, quote=False)


def esc_attr(t):
    """Valor de atributo: aqui las comillas SI se escapan, o una comilla en
    un titulo o en un alt parte el HTML en dos."""
    return html.escape(t, quote=True)


def trocea(texto, titulos):
    """Corta el documento del autor en bloques, uno por encabezado."""
    lineas = texto.replace("\r", "").split("\n")
    marcas = []
    for i, l in enumerate(lineas):
        if l.strip() in titulos:
            marcas.append((i, l.strip()))
    trozos = {}
    for k, (i, t) in enumerate(marcas):
        fin = marcas[k + 1][0] if k + 1 < len(marcas) else len(lineas)
        cuerpo = [l.rstrip() for l in lineas[i + 1:fin]]
        while cuerpo and not cuerpo[0]:
            cuerpo.pop(0)
        while cuerpo and not cuerpo[-1]:
            cuerpo.pop()
        trozos[t] = cuerpo
    return trozos


def separa_epigrafe(cuerpo):
    """Alguna decima abre con una cita ajena. Sale aparte y con su firma:
    en Señal son dos versos de Polito Ibanez y no del autor."""
    if len(cuerpo) > 2 and cuerpo[1].strip() and not cuerpo[2].strip():
        firma = cuerpo[1].strip()
        if len(firma.split()) <= 4 and firma[0].isupper() and not firma.endswith((",", ";")):
            return [cuerpo[0].strip()], firma, [l for l in cuerpo[3:]]
    return None, None, cuerpo


def dims(rel):
    with Image.open(os.path.join(RAIZ, rel.lstrip("/"))) as im:
        return im.size


def quita_cabecera(cuerpo, d):
    """Saca del cuerpo el subtitulo y la dedicatoria, que en el documento del
    autor van pegados al encabezado y si no se sacan se leen como versos. Se
    declaran en el manifiesto y el generador se para si no aparecen: aqui
    equivocarse es publicar mal una decima."""
    for clave in ("subtitulo", "dedicatoria"):
        if not d.get(clave):
            continue
        while cuerpo and not cuerpo[0].strip():
            cuerpo.pop(0)
        if not cuerpo or cuerpo[0].strip() != d[clave]:
            sys.exit(f"{d['slug']}: esperaba {clave} «{d[clave]}» y vino "
                     f"«{cuerpo[0].strip() if cuerpo else '(nada)'}»")
        cuerpo.pop(0)
    while cuerpo and not cuerpo[0].strip():
        cuerpo.pop(0)
    return cuerpo


def pieza(d, cuerpo, n, alt, la=""):
    img = f"/img/decimitas/{d['slug']}.webp"
    w, h = dims(img)
    epi, firma, versos = separa_epigrafe(quita_cabecera(list(cuerpo), d))
    lado = "right" if n % 2 == 0 else "left"
    partes = [f'  <article class="decimita reveal reveal-{lado}" id="{d["slug"]}">']
    partes.append(f'    <figure class="decimita-foto">')
    partes.append(f'      <img src="{img}" width="{w}" height="{h}" alt="{esc_attr(alt)}" loading="lazy">')
    partes.append(f'    </figure>')
    partes.append(f'    <div class="decimita-texto"{la}>')
    rotulo = (f' <span class="poema-numero">{esc(d["rotulo"])}</span>' if d.get("rotulo") else "")
    partes.append(f'      <h2 class="decimita-titulo">{esc(d["titulo"])}{rotulo}</h2>')
    if d.get("dedicatoria"):
        partes.append(f'      <p class="texto-dedicatoria">{esc(d["dedicatoria"])}</p>')
    if epi:
        partes.append('      <blockquote class="poema-epigrafe">')
        partes.append(f'        <div class="verso">{esc(epi[0])}</div>')
        partes.append(f'        <cite>{esc(firma)}</cite>')
        partes.append('      </blockquote>')
    partes.append('      <div class="verso decimita-versos">'
                  + "\n".join(esc(l) for l in versos).strip("\n") + '</div>')
    partes.append('      <p class="vyv-firma">ALS</p>')
    partes.append('    </div>')
    partes.append('  </article>')
    return "\n".join(partes)


def pagina_decimitas(lang, V, cfg, trozos, capas):
    L = pagina.IDIOMAS[lang]
    es = lang == "es"
    la = "" if es else ' lang="es"'
    url = DOMINIO + V["ruta"]
    seccion = "/tinta-ciones/" if es else "/en/poetry/"
    sonata = capas[lang]["_sonata_ruta"]

    piezas = "\n\n".join(pieza(d, trozos[d["titulo_doc"]], i,
                               d["alt"] if es else V["alts"][d["slug"]], la)
                         for i, d in enumerate(cfg["decimitas"]))

    lista = {"@context": "https://schema.org", "@type": "ItemList",
             "name": "De-Cimitas de Antonio López Sánchez" if es else V["seo_titulo"],
             "itemListElement": [{"@type": "ListItem", "position": i, "name": d["titulo"]}
                                 for i, d in enumerate(cfg["decimitas"], 1)]}

    margen = "1.5rem" if (V.get("aviso") or V.get("aviso_adultos")) else "3rem"
    aviso = f'\n    <p class="nota" style="margin-bottom:1.5rem;">{esc(V["aviso"])}</p>' if V.get("aviso") else ""
    aviso += (f'\n    <p class="sonata-premio" style="margin-bottom:3rem;">{esc(V["aviso_adultos"])}</p>'
              if V.get("aviso_adultos") else "")
    nota = V["sonata_nota"].replace(
        "{premio}", f'<a href="{V["premios_url"]}">{esc(PREMIO)}</a>')

    return (pagina.cabeza(lang, V["seo_titulo"], V["seo_desc"], url,
                          imagen=f"{DOMINIO}/img/decimitas/baraja-rota.webp",
                          rutas={l: c["ruta"] for l, c in capas.items()},
                          adultos=bool(V.get("aviso_adultos")))
            + '<script type="application/ld+json">\n' + json.dumps(lista, ensure_ascii=False, indent=2) + '\n</script>\n'
            + pagina.migas([("Ala del Mar", DOMINIO + L["portada"]), (V["migas"][0], DOMINIO + seccion), (V["migas"][1], url)])
            + pagina.menu(lang, seccion)
            + f"""
<header class="page-header">
  <h1>De-Cimitas</h1>
  <p>{esc(V["frase"])}</p>
</header>

<main id="main">
<div class="section">
  <div class="reveal reveal-right">
    <h2 class="section-title">{esc(V["titulo_sala"])}</h2>
    <div class="section-divider"></div>
    <p class="section-text" style="margin-bottom:{margen};">{esc(V["entrada"])}</p>{aviso}
  </div>

{piezas}

  <div class="reveal reveal-right" style="margin-top:4.5rem;">
    <h2 class="section-title">{esc(V["titulo_mayor"])}</h2>
    <div class="section-divider"></div>
    <p class="section-text" style="margin-bottom:2.5rem;">{esc(V["entrada_mayor"])}</p>
  </div>

  <article class="decimita decimita-mayor reveal reveal-left" id="sonata-de-la-lluvia">
    <figure class="decimita-foto">
      <img src="/img/decimitas/sonata-de-la-lluvia.webp" width="720" height="540" alt="{esc_attr(V["sonata_alt"])}" loading="lazy">
    </figure>
    <div class="decimita-texto">
      <h2 class="decimita-titulo"{la}>Sonata de la lluvia</h2>
      <p class="libro-sinopsis">{esc(V["sonata_sinopsis"])}</p>
      <p class="decimita-nota">{nota}</p>
      <p style="margin-top:1.4rem;"><a href="{sonata}" class="btn">{esc(V["sonata_boton"])}</a></p>
    </div>
  </article>

</div>
</main>
"""
            + pagina.pie(lang, None))


def main():
    cfg = json.load(open(os.path.join(RAIZ, "herramientas", "decimitas.json"), encoding="utf-8"))
    doc = open(os.path.join(RAIZ, "herramientas", "textos",
                            cfg["documento"].replace("/", os.sep)), encoding="utf-8").read()
    trozos = trocea(doc, {d["titulo_doc"] for d in cfg["decimitas"]})

    faltan = [d["titulo_doc"] for d in cfg["decimitas"] if d["titulo_doc"] not in trozos]
    if faltan:
        print("SIN TEXTO en el documento:", faltan); sys.exit(1)

    capas = {"es": ES, **pagina.lenguas_con_capa("decimitas")}
    # La sonata tiene pagina propia en cada idioma que tenga su capa; donde no,
    # la tarjeta lleva a la española.
    sonatas = {"es": "/tinta-ciones/sonata-de-la-lluvia/"}
    sonatas.update({l: c["ruta"] for l, c in pagina.lenguas_con_capa("sonata").items()})
    for lang, V in capas.items():
        falta_alt = [d["slug"] for d in cfg["decimitas"] if lang != "es" and d["slug"] not in V["alts"]]
        if falta_alt:
            sys.exit(f"decimitas.{lang}.json sin descripcion para: {', '.join(falta_alt)}")
        V["_sonata_ruta"] = sonatas.get(lang, sonatas["es"])
    for lang, V in capas.items():
        destino = pagina.escribe(V["ruta"], pagina_decimitas(lang, V, cfg, trozos, capas))
        print(f"escrito: {destino} · {len(cfg['decimitas'])} de-cimitas")


if __name__ == "__main__":
    main()
