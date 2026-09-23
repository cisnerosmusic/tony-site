# El marco comun de una pagina del sitio, en cualquier idioma: cabecera,
# menu, pie y camino de miga.
#
# Existe porque cada generador llevaba su propia copia de estas plantillas,
# y al traer el ingles habia que triplicarlas. Los textos de interfaz salen
# de herramientas/idiomas.json; el menu y el pie, de navegacion.py.
#
# La salida en español es identica, byte a byte, a la que escribian los
# generadores con sus copias: se comprobo con un diff antes de cambiarlos.

import html, json, os, re, sys, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=38"
IDIOMAS = json.load(open(os.path.join(RAIZ, "herramientas", "idiomas.json"), encoding="utf-8"))

FAVICON = ('<link rel="icon" href="/favicon.ico" sizes="any">\n'
           '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
           '<link rel="apple-touch-icon" href="/apple-touch-icon.png">')


def esc(t):
    """Texto visible: se dejan las comillas como el autor las escribio."""
    return html.escape(t, quote=False)


def esc_attr(t):
    """Valor de atributo: aqui las comillas SI se escapan."""
    return html.escape(t, quote=True)


def ancla(titulo):
    """El id de un poema o de una decima dentro de su sala.

    Vive aqui, y no en el generador que lo pinta, porque desde que /en/author/
    es un concentrador hay dos sitios que lo calculan: el que escribe el id y
    el que escribe el enlace. Si cada uno lo hiciera a su manera, los enlaces
    del concentrador apuntarian a anclas que no existen y nada lo avisaria."""
    t = unicodedata.normalize("NFKD", titulo.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]


def lenguas_con_capa(base):
    """Las lenguas, ademas del español, que tienen capa para un manifiesto:
    herramientas/<base>.<idioma>.json."""
    out = {}
    for lang in IDIOMAS:
        if lang.startswith("_") or lang == "es":
            continue
        r = os.path.join(RAIZ, "herramientas", f"{base}.{lang}.json")
        if os.path.exists(r):
            out[lang] = json.load(open(r, encoding="utf-8"))
    return out


def alternos(rutas):
    """hreflang reciproco entre las versiones de una pagina, y x-default al
    español. Una pagina sin pareja no lleva ninguno."""
    if len(rutas) < 2:
        return ""
    t = "".join(f'<link rel="alternate" hreflang="{l}" href="{DOMINIO}{r}">\n' for l, r in rutas.items())
    return t + f'<link rel="alternate" hreflang="x-default" href="{DOMINIO}{rutas["es"]}">\n'


def cabeza(lang, titulo, desc, url, tipo_og="article", imagen=None, rutas=None, adultos=False):
    """adultos=True añade <meta name="rating" content="adult">, la señal que
    los buscadores entienden para la literatura erotica."""
    L = IDIOMAS[lang]
    img = imagen or f"{DOMINIO}/img/retrato.webp"
    locale = f'<meta property="og:locale" content="{L["locale"]}">'
    if lang != "es":
        locale += '\n<meta property="og:locale:alternate" content="es_ES">'
    return f"""<!DOCTYPE html>
<html lang="{L["lang"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc_attr(desc)}">
{'<meta name="rating" content="adult">' + chr(10) if adultos else ""}{FAVICON}
<link rel="canonical" href="{url}">
{alternos(rutas or {})}<meta property="og:type" content="{tipo_og}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc_attr(titulo)}">
<meta property="og:description" content="{esc_attr(desc)}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc_attr(titulo)}">
<meta name="twitter:description" content="{esc_attr(desc)}">
<meta name="twitter:image" content="{img}">
{locale}
<meta name="theme-color" content="#0a0c1f">
<link rel="preload" href="/fonts/cinzel-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts.css?v=6">
<link rel="stylesheet" href="/styles.css{CSS}">
"""


def migas(items):
    lista = ",\n    ".join(
        f'{{ "@type": "ListItem", "position": {i}, "name": {json.dumps(n, ensure_ascii=False)}, "item": "{u}" }}'
        for i, (n, u) in enumerate(items, 1))
    return ('<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n'
            '  "@type": "BreadcrumbList",\n  "itemListElement": [\n    ' + lista + '\n  ]\n}\n</script>\n')


def menu(lang, activa):
    L = IDIOMAS[lang]
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

<script src="/app.js?v=11" defer></script>
</body>
</html>
"""


def escribe(ruta_web, contenido):
    destino = os.path.join(RAIZ, ruta_web.strip("/").replace("/", os.sep), "index.html")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8", newline="") as f:
        f.write(contenido)
    return os.path.relpath(destino, RAIZ)
