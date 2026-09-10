# Genera el sitio en ingles desde herramientas/ingles.json.
#
#   /en/           portada
#   /en/trova/     la investigacion sobre la Nueva Trova
#   /en/poetry/    la poesia
#   /en/fiction/   novela y cuento
#   /en/author/    biografia y hoja de servicios
#
# /en/rights/ NO se genera aqui: la escribe gen-legal.py junto con la version
# española, para que el aviso de derechos no pueda decir dos cosas distintas.
#
# La regla del sitio, que no se negocia: el aparato va en ingles y la
# literatura se queda en español. Ni un poema traducido.
#
# El orden de las secciones no es el del sitio español y no es un descuido.
# Para el lector anglosajon la puerta de entrada es la investigacion sobre la
# trova, no la fantasia heroica. Lo decidio Ernesto el 9 de septiembre de 2026
# y esta razonado en PRODUCT.md.
#
# No se inventa ni una clase de CSS: las fichas de libro y las tres puertas de
# la portada reutilizan .laurel-item, que ya es una rejilla de etiqueta dorada
# a la izquierda y contenido a la derecha.
#
# Uso: python herramientas/gen-ingles.py

import json, os, sys, html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=22"
RETRATO = "/img/retrato.webp"

# Paginas que si tienen una equivalente de verdad en español. El hreflang solo
# vale si es reciproco y si las dos paginas hablan de lo mismo: /en/fiction/ no
# esta aqui porque /libros/ son los catorce libros y esa son solo las novelas.
PAREJAS = {
    "/en/": "/",
    "/en/trova/": "/trova/",
    "/en/poetry/": "/tinta-ciones/",
    "/en/author/": "/periodista/",
}


def esc(t):
    return html.escape(t, quote=False)


def esc_attr(t):
    return html.escape(t, quote=True)


def boton(e):
    """Un enlace de accion. 'relleno' lo pinta solido, 'externo' le pone el
    rel que exige abrir en otra pestaña."""
    clase = "btn btn-filled" if e.get("relleno") else "btn"
    extra = ' target="_blank" rel="noopener"' if e.get("externo") else ""
    idioma = f' lang="{e["lang"]}"' if e.get("lang") else ""
    return f'<a href="{esc_attr(e["url"])}" class="{clase}"{extra}{idioma}>{esc(e["texto"])}</a>'


def bloque_libro(l):
    """Ficha de un libro, con el año en la columna dorada."""
    titulo = f'<em>{esc(l["titulo"])}</em>'
    if l.get("glosa"):
        titulo += f' <span class="libro-meta">({esc(l["glosa"])})</span>'
    pie = " · ".join(x for x in (l.get("editorial"), l.get("genero")) if x)
    p = [f'  <article class="laurel-item reveal reveal-right">',
         f'    <p class="laurel-anio">{esc(l["anio"])}</p>',
         f'    <div>',
         f'      <h3 class="libro-titulo" lang="es">{titulo}</h3>',
         f'      <p class="libro-meta">{esc(pie)}</p>']
    if l.get("premio"):
        p.append(f'      <p class="libro-meta">{esc(l["premio"])}</p>')
    p.append(f'      <p class="section-text">{l["texto"]}</p>')
    if l.get("url"):
        p.append(f'      <p style="margin-top:1rem;"><a href="{esc_attr(l["url"])}" class="btn">See the book</a></p>')
    p += ['    </div>', '  </article>']
    return "\n".join(p)


def bloque_puerta(d):
    return ('  <article class="laurel-item reveal reveal-right">\n'
            f'    <p class="laurel-anio">{esc(d["numero"])}</p>\n'
            '    <div>\n'
            f'      <h3 class="libro-titulo"><a href="{esc_attr(d["url"])}">{esc(d["titulo"])}</a></h3>\n'
            f'      <p class="section-text">{d["texto"]}</p>\n'
            '    </div>\n'
            '  </article>')


def seccion_html(s, n):
    lado = "right" if n % 2 == 0 else "left"
    dentro = [f'  <div class="reveal reveal-{lado}">',
              f'    <h2 class="section-title">{esc(s["titulo"])}</h2>',
              '    <div class="section-divider"></div>']
    for p in s.get("parrafos", []):
        dentro.append(f'    <p class="section-text" style="margin-bottom:1.25rem;">{p}</p>')
    if s.get("firma"):
        dentro.append(f'    <p class="vyv-firma">{esc(s["firma"])}</p>')
    if s.get("lista"):
        dentro.append('    <ul class="lista-obras">')
        for x in s["lista"]:
            dentro.append(f'      <li>{x}</li>')
        dentro.append('    </ul>')
    if s.get("enlaces"):
        dentro.append('    <div style="display:flex;flex-wrap:wrap;gap:1rem;margin-top:1.6rem;">')
        for e in s["enlaces"]:
            dentro.append("      " + boton(e))
        dentro.append('    </div>')
    dentro.append('  </div>')

    for l in s.get("libros", []):
        dentro.append("")
        dentro.append(bloque_libro(l))
    for d in s.get("puertas", []):
        dentro.append("")
        dentro.append(bloque_puerta(d))

    ancla = f' id="{s["ancla"]}"' if s.get("ancla") else ""
    cuerpo = f'<div class="section"{ancla}>\n' + "\n".join(dentro) + '\n</div>'
    if s.get("alt"):
        cuerpo = '<div class="section-alt">\n' + cuerpo + '\n</div>'
    return cuerpo


def portada_hero(d):
    acciones = "\n        ".join(boton(a) for a in d["acciones"])
    return f"""<div class="split">
  <div class="split-image" style="background-image:url('{RETRATO}');" role="img" aria-label="Antonio López Sánchez over Havana Bay"></div>
  <div class="split-content">
    <div class="reveal reveal-right">
      <h1>
        <span class="casa-nombre">Ala del Mar</span>
        <span class="lema">bene scriptus</span>
        <span class="casa-autor">Antonio López Sánchez</span>
      </h1>
    </div>
    <div class="reveal reveal-left" style="transition-delay:0.25s;">
      <p class="oficio">{esc(d["oficio"])}</p>
      <div class="hero-acciones">
        {acciones}
      </div>
      <p class="nota-demo" style="margin-top:2rem;">{esc(d["aviso_idioma"])}</p>
    </div>
  </div>
</div>

<div class="banda-mar reveal reveal-left" role="img" aria-label="The sea at dusk"></div>"""


def datos_estructurados(d, url):
    tipo = "ProfilePage" if d["ruta"] == "/en/author/" else (
        "WebPage" if not d.get("es_portada") else "WebSite")
    base = {"@context": "https://schema.org", "@type": tipo,
            "name": d["seo_titulo"], "description": d["seo_desc"],
            "url": url, "inLanguage": "en",
            "about": {"@id": f"{DOMINIO}/#antonio"}}
    if d.get("es_portada"):
        base["@id"] = f"{DOMINIO}/en/#site"
    else:
        base["isPartOf"] = {"@id": f"{DOMINIO}/#sitio"}
    return base


def migas(d, url):
    pasos = [("Ala del Mar", DOMINIO + "/en/")]
    if not d.get("es_portada"):
        pasos.append((d["titulo"], url))
    filas = "".join(
        f'\n    {{ "@type": "ListItem", "position": {i}, "name": "{esc_attr(n)}", "item": "{u}" }},'
        for i, (n, u) in enumerate(pasos, 1)).rstrip(",")
    return ('<script type="application/ld+json">\n{\n'
            '  "@context": "https://schema.org",\n'
            '  "@type": "BreadcrumbList",\n'
            f'  "itemListElement": [{filas}\n  ]\n'
            '}\n</script>')


def pagina(d):
    url = DOMINIO + d["ruta"]
    T, D = d["seo_titulo"], d["seo_desc"]

    alternos = ""
    if d["ruta"] in PAREJAS:
        es = DOMINIO + PAREJAS[d["ruta"]]
        alternos = (f'\n<link rel="alternate" hreflang="en" href="{url}">'
                    f'\n<link rel="alternate" hreflang="es" href="{es}">'
                    f'\n<link rel="alternate" hreflang="x-default" href="{es}">')

    if d.get("es_portada"):
        cabecera = portada_hero(d)
    else:
        cabecera = (f'<header class="page-header">\n  <h1>{esc(d["titulo"])}</h1>\n'
                    f'  <p>{esc(d["subtitulo"])}</p>\n</header>')

    secciones = "\n\n".join(seccion_html(s, n) for n, s in enumerate(d.get("secciones", [])))
    activa = navegacion.seccion_en_de(d["ruta"])

    cuerpo_main = f'<main id="main">\n\n{secciones}\n\n</main>'
    if d.get("es_portada"):
        cuerpo_main = f'<main id="main">\n\n{cabecera}\n\n{secciones}\n\n</main>'
        cabecera = ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{T}</title>
<meta name="description" content="{esc_attr(D)}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="canonical" href="{url}">{alternos}
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc_attr(T)}">
<meta property="og:description" content="{esc_attr(D)}">
<meta property="og:image" content="{DOMINIO}{RETRATO}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc_attr(T)}">
<meta name="twitter:description" content="{esc_attr(D)}">
<meta name="twitter:image" content="{DOMINIO}{RETRATO}">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="es_ES">
<meta name="theme-color" content="#0a0c1f">
<link rel="preload" href="/fonts/cinzel-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts.css?v=5">
<link rel="stylesheet" href="/styles.css{CSS}">
<script type="application/ld+json">
{json.dumps(datos_estructurados(d, url), ensure_ascii=False, indent=2)}
</script>
{migas(d, url)}
</head>
<body>

<a class="salto" href="#main">Skip to content</a>

<nav class="nav">
  <a href="/en/" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="menu-principal">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links" id="menu-principal">
{navegacion.menu_en_html(activa)}
  </ul>
</nav>

{cabecera}
{cuerpo_main}

<footer class="footer">
  <nav class="footer-nav" aria-label="Sections">
{navegacion.pie_en_html(activa)}
  </nav>
  <div class="footer-socials">
    <a href="https://www.facebook.com/profile.php?id=100071950279104" target="_blank" rel="noopener" aria-label="Antonio López Sánchez on Facebook"><svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16" aria-hidden="true"><path d="M13.5 22v-8.1h2.72l.41-3.16H13.5V8.72c0-.91.25-1.53 1.56-1.53h1.67V4.36c-.29-.04-1.28-.12-2.43-.12-2.4 0-4.05 1.47-4.05 4.16v2.34H7.53v3.16h2.72V22h3.25z"/></svg></a>
  </div>
  <p class="footer-lema">bene scriptus</p>
  <p class="footer-copy">&copy; 2026 Antonio López Sánchez · Ala del Mar</p>
  <p class="footer-copy">Developed by <a href="https://index01.net" target="_blank" rel="noopener">Index01</a></p>
</footer>

<script src="/app.js?v=8" defer></script>
</body>
</html>
"""


def main():
    cfg = json.load(open(os.path.join(RAIZ, "herramientas", "ingles.json"), encoding="utf-8"))
    for d in cfg["paginas"]:
        destino = os.path.join(RAIZ, d["ruta"].strip("/").replace("/", os.sep), "index.html")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, "w", encoding="utf-8", newline="") as f:
            f.write(pagina(d))
        n = len(d.get("secciones", []))
        print(f"escrito: {d['ruta']} · {n} secciones")


if __name__ == "__main__":
    main()
