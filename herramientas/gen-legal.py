# Genera el aviso de derechos, una pagina por idioma, desde herramientas/legal.json
#
# Nace de una decision de Ernesto del 9 de septiembre de 2026: dejar por escrito
# que los derechos ofrecidos en el sitio son unica y exclusivamente los de la
# obra de Antonio Lopez Sanchez, con enfasis en los volumenes colectivos.
#
# Esta pensado para crecer: añadir un idioma es copiar su bloque en el JSON,
# traducirlo y declarar su ruta. El generador emite una pagina por idioma y las
# enlaza entre si con hreflang, mas un x-default al español.
#
# La lista de obras colectivas NO se escribe a mano: se lee de las fichas de
# herramientas/libros/*.json, del mismo campo "autoria" que usa gen-libro.py
# para cambiar la frase de derechos. Asi las dos no pueden contradecirse.
#
# Uso: python herramientas/gen-legal.py

import json, os, sys, html, glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=20"


def esc(t):
    return html.escape(t, quote=False)


def esc_attr(t):
    return html.escape(t, quote=True)


def colectivas():
    """Los libros cuya ficha declara autoria compartida. Misma regla que usa
    gen-libro.py, para que la pagina legal y las fichas digan lo mismo."""
    salida = []
    for p in sorted(glob.glob(os.path.join(RAIZ, "herramientas", "libros", "*.json"))):
        m = json.load(open(p, encoding="utf-8"))
        if any(k.lower().startswith("autor") for k in m["ficha"]):
            salida.append((m["titulo"], f"/libros/{m['slug']}/",
                           m["ficha"].get("autoría") or m["ficha"].get("autoria", "")))
    return salida


def pagina(clave, cfg, todos):
    d = cfg[clave]
    url = DOMINIO + d["ruta"]
    alternos = "\n".join(
        f'<link rel="alternate" hreflang="{o["lang"]}" href="{DOMINIO}{o["ruta"]}">'
        for o in cfg.values() if isinstance(o, dict) and o.get("ruta"))
    alternos += f'\n<link rel="alternate" hreflang="x-default" href="{DOMINIO}{cfg["es"]["ruta"]}">'

    bloques = []
    for s in d["secciones"]:
        b = ['  <section class="legal-bloque reveal reveal-right">']
        b.append(f'    <h2>{esc(s["titulo"])}</h2>')
        for par in s["parrafos"]:
            b.append(f'    <p>{esc(par)}</p>')
        if s.get("lista_colectivas"):
            b.append('    <ul class="lista-obras">')
            for titulo, ruta, autoria in todos:
                extra = f' <span class="meta">· {esc(autoria)}</span>' if autoria else ""
                b.append(f'      <li><a href="{ruta}">{esc(titulo)}</a>{extra}</li>')
            b.append('    </ul>')
        if s.get("enlaces"):
            enlaces = " ".join(
                f'<a href="{e["url"]}"' + (' target="_blank" rel="noopener"' if e.get("externo") else "")
                + f' class="btn">{esc(e["texto"])}</a>'
                for e in s["enlaces"])
            b.append(f'    <p class="legal-enlaces">{enlaces}</p>')
        b.append('  </section>')
        bloques.append("\n".join(b))

    datos = {"@context": "https://schema.org", "@type": "WebPage",
             "name": d["seo_titulo"], "description": d["seo_desc"],
             "url": url, "inLanguage": d["lang"],
             "isPartOf": {"@id": f"{DOMINIO}/#sitio"},
             "about": {"@id": f"{DOMINIO}/#antonio"}}

    # El menu completo solo existe en español; la pagina inglesa hereda el suyo.
    if d["lang"] == "es":
        menu = navegacion.menu_html(None)
        pie = navegacion.pie_html(None)
    else:
        menu = ('    <li><a href="/libros/" lang="es">My books</a></li>\n'
                '    <li><a href="/tinta-ciones/" lang="es">Tinta-ciones</a></li>\n'
                '    <li><a href="/contarte/" lang="es">Contarte</a></li>\n'
                '    <li><a href="/trova/" lang="es">The trova</a></li>\n'
                '    <li><a href="/en/rights/" class="active" aria-current="page">Rights</a></li>\n'
                '    <li><a href="/directorio/" lang="es">Contact</a></li>\n'
                '    <li><a href="/" lang="es">ES</a></li>')
        pie = ('    <a href="/en/">Home</a>\n'
               '    <a href="/libros/" lang="es">My books</a>\n'
               '    <a href="/tinta-ciones/" lang="es">Tinta-ciones</a>\n'
               '    <a href="/contarte/" lang="es">Contarte</a>\n'
               '    <a href="/trova/" lang="es">The trova</a>\n'
               '    <span aria-current="page">Rights</span>\n'
               '    <a href="/directorio/" lang="es">Contact</a>')

    etiqueta_menu = "Open menu" if d["lang"] == "en" else "Abrir menú"
    saltar = "Skip to content" if d["lang"] == "en" else "Saltar al contenido"

    return f"""<!DOCTYPE html>
<html lang="{d["lang"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(d["seo_titulo"])}</title>
<meta name="description" content="{esc_attr(d["seo_desc"])}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="canonical" href="{url}">
{alternos}
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc_attr(d["seo_titulo"])}">
<meta property="og:description" content="{esc_attr(d["seo_desc"])}">
<meta property="og:image" content="{DOMINIO}/img/retrato.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc_attr(d["seo_titulo"])}">
<meta name="twitter:description" content="{esc_attr(d["seo_desc"])}">
<meta name="twitter:image" content="{DOMINIO}/img/retrato.webp">
<meta name="theme-color" content="#0a0c1f">
<link rel="preload" href="/fonts/cinzel-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts.css?v=5">
<link rel="stylesheet" href="/styles.css{CSS}">
<script type="application/ld+json">
{json.dumps(datos, ensure_ascii=False, indent=2)}
</script>
</head>
<body>

<a class="salto" href="#main">{saltar}</a>

<nav class="nav">
  <a href="/" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" type="button" aria-label="{etiqueta_menu}" aria-expanded="false" aria-controls="menu-principal">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links" id="menu-principal">
{menu}
  </ul>
</nav>

<header class="page-header">
  <h1>{esc(d["titulo"])}</h1>
  <p>{esc(d["subtitulo"])}</p>
</header>

<main id="main">
<div class="section legal">

  <p class="legal-intro reveal reveal-right">{esc(d["intro"])}</p>

{chr(10).join(bloques)}

</div>
</main>

<footer class="footer">
  <nav class="footer-nav" aria-label="Secciones">
{pie}
  </nav>
  <div class="footer-socials">
    <a href="https://www.facebook.com/profile.php?id=100071950279104" target="_blank" rel="noopener" aria-label="Facebook de Antonio López Sánchez"><svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16" aria-hidden="true"><path d="M13.5 22v-8.1h2.72l.41-3.16H13.5V8.72c0-.91.25-1.53 1.56-1.53h1.67V4.36c-.29-.04-1.28-.12-2.43-.12-2.4 0-4.05 1.47-4.05 4.16v2.34H7.53v3.16h2.72V22h3.25z"/></svg></a>
  </div>
  <p class="footer-lema">bene scriptus</p>
  <p class="footer-copy">&copy; 2026 Antonio López Sánchez · Ala del Mar</p>
  <p class="footer-copy">Desarrollado por <a href="https://index01.net" target="_blank" rel="noopener">Index01</a></p>
</footer>

<script src="/app.js?v=8" defer></script>
</body>
</html>
"""


def main():
    cfg = json.load(open(os.path.join(RAIZ, "herramientas", "legal.json"), encoding="utf-8"))
    idiomas = {k: v for k, v in cfg.items() if isinstance(v, dict) and v.get("ruta")}
    todos = colectivas()
    for clave in idiomas:
        d = idiomas[clave]
        destino = os.path.join(RAIZ, d["ruta"].strip("/").replace("/", os.sep), "index.html")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, "w", encoding="utf-8", newline="") as f:
            f.write(pagina(clave, idiomas, todos))
        print(f"escrito: {d['ruta']} ({d['lang']})")
    print(f"obras colectivas listadas: {len(todos)}")


if __name__ == "__main__":
    main()
