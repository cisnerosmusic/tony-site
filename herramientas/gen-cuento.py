# Genera Contarte: la sala de los cuentos y la habitacion de cada uno.
# Lee herramientas/cuentos.json y emite /contarte/index.html y
# /contarte/<slug>/index.html
#
# Un cuento que ya salio en un libro vive aqui entero y el libro lo enlaza.
# El texto NO se duplica: es la misma regla que las grabaciones, escrita en
# AGENTS.md. Aqui esta la habitacion; alla, el camino hasta ella.
#
# Uso: python herramientas/gen-cuento.py

import json, os, sys, html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=12"

FAVICON = ('<link rel="icon" href="/favicon.ico" sizes="any">\n'
           '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
           '<link rel="apple-touch-icon" href="/apple-touch-icon.png">')

import navegacion   # menu y pie: una sola definicion para todo el sitio

def esc(t):
    return html.escape(t, quote=False)

def leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n").strip("\n")

def cuerpo_cuento(texto, titulo):
    # La primera linea suele repetir el titulo en mayusculas: fuera.
    lineas = [l.strip() for l in texto.split("\n")]
    while lineas and (not lineas[0] or lineas[0].upper() == titulo.upper() or
                      (lineas[0].isupper() and len(lineas[0]) < 70)):
        lineas.pop(0)
    return "\n".join(f"<p>{esc(l)}</p>" for l in lineas if l)

def cabeza(titulo_seo, desc, url, activa, imagen=None):
    img = imagen or f"{DOMINIO}/img/retrato.webp"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(titulo_seo)}</title>
<meta name="description" content="{esc(desc)}">
{FAVICON}
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(titulo_seo)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(titulo_seo)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{img}">
<meta property="og:locale" content="es_ES">
<meta name="theme-color" content="#0a0c1f">
<link rel="preload" href="/fonts/cinzel-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts.css?v=5">
<link rel="stylesheet" href="/styles.css{CSS}">
"""

def menu(activa):
    filas = navegacion.menu_html(activa)
    return f"""</head>
<body>

<a class="salto" href="#main">Saltar al contenido</a>

<nav class="nav">
  <a href="/" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" onclick="document.querySelector('.nav-links').classList.toggle('open')" aria-label="Menú">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links">
{filas}
  </ul>
</nav>
"""

def pie(activa):
    enlaces = navegacion.pie_html(activa)
    return f"""
<footer class="footer">
  <nav class="footer-nav" aria-label="Secciones">
{enlaces}
  </nav>
  <div class="footer-socials">
    <a href="https://www.facebook.com/profile.php?id=100071950279104" target="_blank" rel="noopener" aria-label="Facebook de Antonio López Sánchez"><svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16" aria-hidden="true"><path d="M13.5 22v-8.1h2.72l.41-3.16H13.5V8.72c0-.91.25-1.53 1.56-1.53h1.67V4.36c-.29-.04-1.28-.12-2.43-.12-2.4 0-4.05 1.47-4.05 4.16v2.34H7.53v3.16h2.72V22h3.25z"/></svg></a>
  </div>
  <p class="footer-lema">bene scriptus</p>
  <p class="footer-copy">&copy; 2026 Antonio López Sánchez · Ala del Mar</p>
  <p class="footer-copy">Desarrollado por <a href="https://index01.net" target="_blank" rel="noopener">Index01</a></p>
</footer>

<script src="/app.js?v=7" defer></script>
</body>
</html>
"""

def migas(items):
    lista = ",\n    ".join(
        f'{{ "@type": "ListItem", "position": {i}, "name": {json.dumps(n, ensure_ascii=False)}, "item": "{u}" }}'
        for i, (n, u) in enumerate(items, 1))
    return ('<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n'
            '  "@type": "BreadcrumbList",\n  "itemListElement": [\n    ' + lista + '\n  ]\n}\n</script>\n')

def pagina_cuento(c):
    url = f"{DOMINIO}/contarte/{c['slug']}/"
    texto = cuerpo_cuento(leer(c["archivo"]), c["titulo"])
    p = c.get("procedencia") or {}
    nota = ""
    if p:
        nota = (f'  <p class="cuento-procedencia reveal reveal-left">{esc(p["texto"])}. '
                f'<a href="{p["libro"]}">Ver la ficha de {esc(p["libro_titulo"])}</a></p>\n')

    datos = {"@context": "https://schema.org", "@type": "ShortStory",
             "name": c["titulo"], "url": url, "inLanguage": "es",
             "author": {"@id": f"{DOMINIO}/#antonio"},
             "description": c["seo_desc"]}
    if c.get("anio"): datos["datePublished"] = c["anio"]
    if p: datos["isPartOf"] = {"@type": "Book", "name": p["libro_titulo"], "url": DOMINIO + p["libro"]}

    return (cabeza(c["seo_titulo"], c["seo_desc"], url, "/contarte/")
            + '<script type="application/ld+json">\n' + json.dumps(datos, ensure_ascii=False, indent=2) + '\n</script>\n'
            + migas([("Ala del Mar", DOMINIO + "/"), ("Contarte", DOMINIO + "/contarte/"), (c["titulo"], url)])
            + menu("/contarte/")
            + f"""
<header class="page-header">
  <h1>{esc(c["titulo"])}</h1>
  <p>{esc(c["linea"])}</p>
</header>

<main id="main">
<div class="section cuento">
  <div class="cuento-texto reveal reveal-right">
{texto}
  </div>
{nota}  <p style="margin-top:2.5rem;"><a href="/contarte/" class="btn">Volver a Contarte</a></p>
</div>
</main>
"""
            + pie(None))

def pagina_indice(cuentos):
    url = f"{DOMINIO}/contarte/"
    filas = "\n".join(
        f'''  <article class="libro-item reveal reveal-right" style="grid-template-columns:1fr;">
    <div>
      <h3 class="libro-titulo"><a href="/contarte/{c["slug"]}/">{esc(c["titulo"])}</a></h3>
      <p class="libro-meta">{esc(c.get("anio",""))}{" · " + esc(c["procedencia"]["texto"]) if c.get("procedencia") else ""}</p>
      <p class="libro-sinopsis">{esc(c["linea"])}</p>
      <p style="margin-top:1.2rem;"><a href="/contarte/{c["slug"]}/" class="btn">Leer el cuento</a></p>
    </div>
  </article>''' for c in cuentos)

    lista = {"@context": "https://schema.org", "@type": "ItemList",
             "name": "Cuentos de Antonio López Sánchez",
             "itemListElement": [
                 {"@type": "ListItem", "position": i,
                  "item": {"@type": "ShortStory", "name": c["titulo"],
                           "url": f"{DOMINIO}/contarte/{c['slug']}/",
                           "author": {"@type": "Person", "name": "Antonio López Sánchez"},
                           "inLanguage": "es"}}
                 for i, c in enumerate(cuentos, 1)]}

    T = "Contarte | Los cuentos de Antonio López Sánchez"
    D = "Los cuentos de Antonio López Sánchez, completos y con su propia habitación cada uno."
    return (cabeza(T, D, url, "/contarte/")
            + '<script type="application/ld+json">\n' + json.dumps(lista, ensure_ascii=False, indent=2) + '\n</script>\n'
            + migas([("Ala del Mar", DOMINIO + "/"), ("Contarte", url)])
            + menu("/contarte/")
            + f"""
<header class="page-header">
  <h1>Contarte</h1>
  <p>La sala del relato breve.</p>
</header>

<main id="main">
<div class="section">
  <div class="reveal reveal-right">
    <h2 class="section-title">Había una vez...</h2>
    <div class="section-divider"></div>
    <p class="section-text" style="margin-bottom:1.5rem;">Con esas tres palabras empezó todo, y todavía funcionan. Aquí viven mis cuentos, cada uno en su propia habitación, para entrar a leerlos enteros.</p>
    <p class="section-text" style="margin-bottom:3rem;">Algunos vienen de un libro y siguen perteneciéndole: desde su cuarto se puede ir al libro, y desde el libro se llega hasta aquí. Otros andan sueltos, esperando el suyo.</p>
  </div>

{filas}

</div>
</main>
"""
            + pie("/contarte/"))

def main():
    cuentos = json.load(open(os.path.join(RAIZ, "herramientas", "cuentos.json"), encoding="utf-8"))
    for c in cuentos:
        destino = os.path.join(RAIZ, "contarte", c["slug"], "index.html")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, "w", encoding="utf-8", newline="") as f:
            f.write(pagina_cuento(c))
        print("escrito:", os.path.relpath(destino, RAIZ))
    with open(os.path.join(RAIZ, "contarte", "index.html"), "w", encoding="utf-8", newline="") as f:
        f.write(pagina_indice(cuentos))
    print(f"escrito: contarte/index.html con {len(cuentos)} cuento(s)")

if __name__ == "__main__":
    main()
