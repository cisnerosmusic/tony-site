# Genera Contarte: la sala de los cuentos y la habitacion de cada uno.
# Lee herramientas/cuentos.json y emite /contarte/index.html y
# /contarte/<slug>/index.html; y, con la capa herramientas/cuentos.en.json,
# su version inglesa en /en/stories/.
#
# Un cuento que ya salio en un libro vive aqui entero y el libro lo enlaza.
# El texto NO se duplica: es la misma regla que las grabaciones, escrita en
# AGENTS.md. Aqui esta la habitacion; alla, el camino hasta ella.
#
# Idiomas. Los cuentos no se traducen nunca: en la version inglesa salen en
# español, marcados con lang="es" y con el aviso de por que. La capa trae
# solo el aparato: la entrada de la sala, la linea de cada cuento, su
# procedencia y los metadatos.
#
# Uso: python herramientas/gen-cuento.py

import json, os, sys, html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=33"
IDIOMAS = json.load(open(os.path.join(RAIZ, "herramientas", "idiomas.json"), encoding="utf-8"))

# Calendario de Contarte. Cuadrado latino de 7x7: cada dia los cuentos salen en
# otro orden, cada cuento pasa exactamente una vez por cada posicion a lo largo
# de la semana, los siete ordenes son distintos y ninguno es la rotacion de
# otro, que es lo que haria evidente la repeticion. Calculado con busqueda y
# horneado aqui; si cambia el numero de cuentos hay que recalcularlo.
CALENDARIO = [
    [4, 5, 6, 0, 3, 1, 2],
    [5, 0, 4, 1, 6, 2, 3],
    [2, 6, 1, 3, 5, 4, 0],
    [6, 3, 2, 4, 0, 5, 1],
    [3, 1, 0, 2, 4, 6, 5],
    [1, 4, 3, 5, 2, 0, 6],
    [0, 2, 5, 6, 1, 3, 4],
]

FAVICON = ('<link rel="icon" href="/favicon.ico" sizes="any">\n'
           '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
           '<link rel="apple-touch-icon" href="/apple-touch-icon.png">')

import navegacion   # menu y pie: una sola definicion para todo el sitio

# Lo que en español estaba escrito aqui. En los demas idiomas lo trae la capa.
ES = {
    "ruta": "/contarte/",
    "h1": "Contarte",
    "frase": "La sala de los relatos.",
    "h2": "Había una vez...",
    "intro": [
        "Esas tres palabras ancestrales anuncian una historia. Aquí viven algunos de mis cuentos, cada uno con un sitio propio y con una mano extendida que invita a recorrerlos.",
        "Los hay libres, todavía sin asideros. Los hay que vienen de libros que esperan ver la luz. Algunos son risueños, otros oscuros. Pero todos están prestos a ofrecer su compañía.",
        "El cuento, ese duende que acompaña a la humanidad desde los albores de los tiempos, todavía regala magias, realidades y hasta miedos.",
    ],
    "aviso": None,
    "leer": "Leer el cuento",
    "volver": "Volver a Contarte",
    "migas": "Contarte",
    "ver_ficha": "Ver la ficha de {}",
    "seo_titulo": "Contarte | Los cuentos de Antonio López Sánchez",
    "seo_desc": "Los cuentos de Antonio López Sánchez, completos y con su propia habitación cada uno.",
}


def esc(t):
    """Texto visible: se dejan las comillas como el autor las escribio."""
    return html.escape(t, quote=False)


def esc_attr(t):
    """Valor de atributo: aqui las comillas SI se escapan, o una comilla en
    un titulo o en un alt parte el HTML en dos."""
    return html.escape(t, quote=True)

TEXTOS = os.path.join(RAIZ, "herramientas", "textos")

def leer(ruta):
    if not os.path.isabs(ruta):
        ruta = os.path.join(TEXTOS, ruta.replace("/", os.sep))
    with open(ruta, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n").strip("\n")

def cuerpo_cuento(texto, titulo):
    # La primera linea suele repetir el titulo en mayusculas: fuera.
    lineas = [l.strip() for l in texto.split("\n")]
    while lineas and (not lineas[0] or lineas[0].upper() == titulo.upper() or
                      (lineas[0].isupper() and len(lineas[0]) < 70)):
        lineas.pop(0)
    return "\n".join(f"<p>{esc(l)}</p>" for l in lineas if l)

def alternos(rutas):
    """hreflang reciproco entre las versiones de una pagina, y x-default al
    español, como en las paginas de libro."""
    if len(rutas) < 2:
        return ""
    t = "".join(f'<link rel="alternate" hreflang="{l}" href="{DOMINIO}{r}">\n' for l, r in rutas.items())
    return t + f'<link rel="alternate" hreflang="x-default" href="{DOMINIO}{rutas["es"]}">\n'

def cabeza(lang, titulo_seo, desc, url, rutas):
    L = IDIOMAS[lang]
    img = f"{DOMINIO}/img/retrato.webp"
    locale = f'<meta property="og:locale" content="{L["locale"]}">'
    if lang != "es":
        locale += '\n<meta property="og:locale:alternate" content="es_ES">'
    return f"""<!DOCTYPE html>
<html lang="{L["lang"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(titulo_seo)}</title>
<meta name="description" content="{esc_attr(desc)}">
{FAVICON}
<link rel="canonical" href="{url}">
{alternos(rutas)}<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc_attr(titulo_seo)}">
<meta property="og:description" content="{esc_attr(desc)}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc_attr(titulo_seo)}">
<meta name="twitter:description" content="{esc_attr(desc)}">
<meta name="twitter:image" content="{img}">
{locale}
<meta name="theme-color" content="#0a0c1f">
<link rel="preload" href="/fonts/cinzel-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts.css?v=6">
<link rel="stylesheet" href="/styles.css{CSS}">
"""

def menu(lang):
    L = IDIOMAS[lang]
    # En ingles los cuentos no tienen entrada propia en el menu: se llega
    # desde la portada inglesa y desde la pagina de ficcion.
    activa = "/contarte/" if lang == "es" else None
    return f"""</head>
<body>

<a class="salto" href="#main">{L["saltar"]}</a>

<nav class="nav">
  <a href="{L["portada"]}" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" type="button" aria-label="{L["abrir_menu"]}" aria-expanded="false" aria-controls="menu-principal">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links" id="menu-principal">
{navegacion.menu_de(lang, activa)}
  </ul>
</nav>
"""

def pie(lang, activa):
    L = IDIOMAS[lang]
    return f"""
<footer class="footer">
  <nav class="footer-nav" aria-label="{L["secciones_aria"]}">
{navegacion.pie_de(lang, activa)}
  </nav>
  <div class="footer-socials">
    <a href="https://www.facebook.com/profile.php?id=100071950279104" target="_blank" rel="noopener" aria-label="{L["facebook_aria"]}"><svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16" aria-hidden="true"><path d="M13.5 22v-8.1h2.72l.41-3.16H13.5V8.72c0-.91.25-1.53 1.56-1.53h1.67V4.36c-.29-.04-1.28-.12-2.43-.12-2.4 0-4.05 1.47-4.05 4.16v2.34H7.53v3.16h2.72V22h3.25z"/></svg></a>
  </div>
  <p class="footer-lema">bene scriptus</p>
  <p class="footer-copy">&copy; 2026 Antonio López Sánchez · Ala del Mar</p>
  <p class="footer-copy">{L["desarrollado"]} <a href="https://index01.net" target="_blank" rel="noopener">Index01</a></p>
</footer>

<script src="/app.js?v=10" defer></script>
</body>
</html>
"""

def migas(items):
    lista = ",\n    ".join(
        f'{{ "@type": "ListItem", "position": {i}, "name": {json.dumps(n, ensure_ascii=False)}, "item": "{u}" }}'
        for i, (n, u) in enumerate(items, 1))
    return ('<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n'
            '  "@type": "BreadcrumbList",\n  "itemListElement": [\n    ' + lista + '\n  ]\n}\n</script>\n')

def rutas_de(capas, slug=None):
    return {l: V["ruta"] + (f"{slug}/" if slug else "") for l, V in capas.items()}

def libro_en(lang, ruta_es):
    """La ficha del libro del que viene un cuento, en el idioma de la pagina."""
    return ruta_es if lang == "es" else ruta_es.replace("/libros/", IDIOMAS[lang]["ruta_libros"], 1)

def pagina_cuento(lang, V, c, capas):
    L = IDIOMAS[lang]
    es = lang == "es"
    t = c if es else {**c, **V["cuentos"][c["slug"]]}
    la = "" if es else ' lang="es"'
    url = f"{DOMINIO}{V['ruta']}{c['slug']}/"
    texto = cuerpo_cuento(leer(c["archivo"]), c["titulo"])
    p = c.get("procedencia") or {}
    nota = ""
    if p:
        texto_p = p["texto"] if es else t["procedencia"]
        nota = (f'  <p class="cuento-procedencia reveal reveal-left">{esc(texto_p)}. '
                f'<a href="{libro_en(lang, p["libro"])}">{esc(V["ver_ficha"].format(p["libro_titulo"]))}</a></p>\n')
    aviso = (f'  <p class="nota" style="margin-bottom:2rem;">{esc(V["aviso"])}</p>\n' if V.get("aviso") else "")

    datos = {"@context": "https://schema.org", "@type": "ShortStory",
             "name": c["titulo"], "url": url, "inLanguage": "es",
             "author": {"@id": f"{DOMINIO}/#antonio"},
             "description": t["seo_desc"]}
    if c.get("anio"): datos["datePublished"] = c["anio"]
    if p: datos["isPartOf"] = {"@type": "Book", "name": p["libro_titulo"], "url": DOMINIO + libro_en(lang, p["libro"])}

    return (cabeza(lang, t["seo_titulo"], t["seo_desc"], url, rutas_de(capas, c["slug"]))
            + '<script type="application/ld+json">\n' + json.dumps(datos, ensure_ascii=False, indent=2) + '\n</script>\n'
            + migas([("Ala del Mar", DOMINIO + L["portada"]), (V["migas"], DOMINIO + V["ruta"]), (c["titulo"], url)])
            + menu(lang)
            + f"""
<header class="page-header">
  <h1{la}>{esc(c["titulo"])}</h1>
</header>

<main id="main">
<div class="section cuento">
{aviso}  <div class="cuento-texto reveal reveal-right"{la}>
{texto}
  </div>
{nota}  <p style="margin-top:2.5rem;"><a href="{V['ruta']}" class="btn">{esc(V["volver"])}</a></p>
</div>
</main>
"""
            + pie(lang, None))

def pagina_indice(lang, V, cuentos, capas):
    L = IDIOMAS[lang]
    es = lang == "es"
    la = "" if es else ' lang="es"'
    url = DOMINIO + V["ruta"]
    def ficha(i, c):
        t = c if es else {**c, **V["cuentos"][c["slug"]]}
        meta = esc(c.get("anio", ""))
        if c.get("procedencia"):
            meta = (meta + " · " if meta else "") + esc(c["procedencia"]["texto"] if es else t["procedencia"])
        meta = f'    <p class="libro-meta">{meta}</p>\n' if meta else ""
        # Fuera del español el titulo se queda en español, con su sentido
        # entre parentesis, como en el catalogo de libros.
        sentido = "" if es else f' <span class="libro-meta">({esc(t["significado"])})</span>'
        return (f'  <article class="cuento-ficha reveal reveal-right" data-cuento="{i}">\n'
                f'    <h3 class="libro-titulo"><a href="{V["ruta"]}{c["slug"]}/"{la}>{esc(c["titulo"])}</a>{sentido}</h3>\n'
                f'{meta}'
                f'    <p class="libro-sinopsis">{esc(t["linea"])}</p>\n'
                f'    <p style="margin-top:1.2rem;"><a href="{V["ruta"]}{c["slug"]}/" class="btn">{esc(V["leer"])}</a></p>\n'
                f'  </article>')
    filas = "\n".join(ficha(i, c) for i, c in enumerate(cuentos))

    # El orden del dia. El script va sin defer, justo detras de la lista, para
    # que se ejecute mientras se analiza la pagina: asi el navegador pinta una
    # sola vez y no se ve el barajado. Sin JavaScript se ven los siete en el
    # orden del manifiesto, que es la degradacion correcta.
    orden_js = (
        '<script>\n'
        '(function(){\n'
        '  var cal = ' + json.dumps(CALENDARIO) + ';\n'
        '  var hoy = cal[new Date().getDay()];\n'
        '  var fichas = document.querySelectorAll(".cuento-ficha");\n'
        '  for (var p = 0; p < hoy.length; p++) {\n'
        '    var f = fichas[hoy[p]];\n'
        '    if (f) f.style.order = p;\n'
        '  }\n'
        '})();\n'
        '</script>')

    lista = {"@context": "https://schema.org", "@type": "ItemList",
             "name": "Cuentos de Antonio López Sánchez" if es else V["seo_titulo"],
             "itemListElement": [
                 {"@type": "ListItem", "position": i,
                  "item": {"@type": "ShortStory", "name": c["titulo"],
                           "url": f"{url}{c['slug']}/",
                           "author": {"@type": "Person", "name": "Antonio López Sánchez"},
                           "inLanguage": "es"}}
                 for i, c in enumerate(cuentos, 1)]}

    ultimo = len(V["intro"]) - 1
    intro = "\n".join(
        f'    <p class="section-text" style="margin-bottom:{"3rem" if i == ultimo else "1.5rem"};">{esc(p)}</p>'
        for i, p in enumerate(V["intro"]))
    if V.get("aviso"):
        intro = intro.replace('style="margin-bottom:3rem;"', 'style="margin-bottom:1.5rem;"') + \
                f'\n    <p class="nota" style="margin-bottom:3rem;">{esc(V["aviso"])}</p>'

    return (cabeza(lang, V["seo_titulo"], V["seo_desc"], url, rutas_de(capas))
            + '<script type="application/ld+json">\n' + json.dumps(lista, ensure_ascii=False, indent=2) + '\n</script>\n'
            + migas([("Ala del Mar", DOMINIO + L["portada"]), (V["migas"], url)])
            + menu(lang)
            + f"""
<header class="page-header">
  <h1>{esc(V["h1"])}</h1>
  <p>{esc(V["frase"])}</p>
</header>

<main id="main">
<div class="section">
  <div class="reveal reveal-right">
    <h2 class="section-title">{esc(V["h2"])}</h2>
    <div class="section-divider"></div>
{intro}
  </div>

  <div class="cuento-lista">
{filas}
  </div>
{orden_js}

</div>
</main>
"""
            + pie(lang, "/contarte/" if es else None))

def main():
    cuentos = json.load(open(os.path.join(RAIZ, "herramientas", "cuentos.json"), encoding="utf-8"))
    capas = {"es": ES}
    for lang in IDIOMAS:
        if lang.startswith("_") or lang == "es":
            continue
        ruta = os.path.join(RAIZ, "herramientas", f"cuentos.{lang}.json")
        if os.path.exists(ruta):
            V = json.load(open(ruta, encoding="utf-8"))
            faltan = [c["slug"] for c in cuentos if c["slug"] not in V["cuentos"]
                      or (c.get("procedencia") and not V["cuentos"][c["slug"]].get("procedencia"))]
            if faltan:
                sys.exit(f"cuentos.{lang}.json incompleto: {', '.join(faltan)}")
            capas[lang] = V
    for lang, V in capas.items():
        base = os.path.join(RAIZ, V["ruta"].strip("/").replace("/", os.sep))
        for c in cuentos:
            destino = os.path.join(base, c["slug"], "index.html")
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "w", encoding="utf-8", newline="") as f:
                f.write(pagina_cuento(lang, V, c, capas))
        with open(os.path.join(base, "index.html"), "w", encoding="utf-8", newline="") as f:
            f.write(pagina_indice(lang, V, cuentos, capas))
        print(f"escrito: {V['ruta']} con {len(cuentos)} cuento(s)")

if __name__ == "__main__":
    main()
