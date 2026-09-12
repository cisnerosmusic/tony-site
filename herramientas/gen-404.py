# Genera /404.html, que es uno solo para todo el sitio: GitHub Pages sirve
# siempre ese archivo, venga el error de donde venga, y no admite un 404 por
# carpeta. Asi que la pagina lleva los dos idiomas.
#
# Un script minimo en el <head>, antes de pintar nada, mira si la ruta empieza
# por /en/ y en ese caso marca <html lang="en" class="en"> y cambia el titulo.
# styles.css oculta el idioma que no toca (.solo-es, .solo-en). Sin JavaScript
# se ve el español, que es el idioma por defecto.
#
# Los dos menus y los dos pies salen de navegacion.py, como en el resto del
# sitio, para que el 404 no pueda desalinearse. Cada hamburguesa gobierna el
# menu que nombra en aria-controls, y app.js las cablea por separado.
#
# Todas las rutas son absolutas desde la raiz: este archivo se sirve en
# cualquier direccion, y una ruta relativa se romperia.
#
# Uso: python herramientas/gen-404.py

import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = "?v=23"

IDIOMA = {
    "es": {
        "clase": "solo-es", "portada": "/", "saltar": "Saltar al contenido",
        "abrir": "Abrir menú", "menu": "menu-principal", "secciones": "Secciones",
        "h1": "Esta página se perdió en el librero",
        "sub": "La dirección que buscabas no existe en esta casa, o cambió de habitación.",
        "texto": "Puedes volver a la portada o entrar directamente a los libros, que son la puerta principal.",
        "botones": [("/", "Portada", True), ("/libros/", "Mis libros", False),
                    ("/tinta-ciones/", "Tinta-ciones", False)],
    },
    "en": {
        "clase": "solo-en", "portada": "/en/", "saltar": "Skip to content",
        "abrir": "Open menu", "menu": "menu-principal-en", "secciones": "Sections",
        "h1": "This page got lost in the bookcase",
        "sub": "The address you were looking for does not exist in this house, or it has moved to another room.",
        "texto": "You can go back to the home page, or straight to the books. For a reader arriving in English, the Nueva Trova is the best way in.",
        # El mismo orden que el resto del sitio ingles: la trova primero.
        "botones": [("/en/", "Home", True), ("/en/books/", "Books", False),
                    ("/en/trova/", "The trova", False)],
    },
}


def bloque_nav(lang):
    d = IDIOMA[lang]
    menu = navegacion.menu_de(lang, None)
    return f"""<nav class="nav {d["clase"]}">
  <a href="{d["portada"]}" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" type="button" aria-label="{d["abrir"]}" aria-expanded="false" aria-controls="{d["menu"]}">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links" id="{d["menu"]}">
{menu}
  </ul>
</nav>"""


def bloque_cuerpo(lang):
    d = IDIOMA[lang]
    botones = "\n".join(
        f'    <a href="{u}" class="btn{" btn-filled" if lleno else ""}">{t}</a>'
        for u, t, lleno in d["botones"])
    return f"""<div class="{d["clase"]}">
<header class="page-header">
  <h1>{d["h1"]}</h1>
  <p>{d["sub"]}</p>
</header>
<div class="section" style="text-align:center;">
  <p class="section-text" style="margin:0 auto 2.5rem;">{d["texto"]}</p>
  <div style="display:flex;flex-wrap:wrap;gap:1rem;justify-content:center;">
{botones}
  </div>
</div>
</div>"""


def bloque_pie(lang):
    d = IDIOMA[lang]
    return f"""  <nav class="footer-nav {d["clase"]}" aria-label="{d["secciones"]}">
{navegacion.pie_de(lang, None)}
  </nav>"""


def main():
    pagina = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, follow">
<title>Página no encontrada | Ala del Mar</title>
<script>
  // Antes de pintar: si el error viene de la zona inglesa, la pagina habla ingles.
  if (location.pathname === '/en' || location.pathname.indexOf('/en/') === 0) {{
    document.documentElement.lang = 'en';
    document.documentElement.className = 'en';
    document.title = 'Page not found | Ala del Mar';
  }}
</script>
<meta name="description" content="Esta página no existe en Ala del Mar, la casa de Antonio López Sánchez.">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0a0c1f">
<link rel="preload" href="/fonts/cinzel-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts.css?v=5">
<link rel="stylesheet" href="/styles.css{CSS}">
</head>
<body>

<a class="salto solo-es" href="#main">{IDIOMA["es"]["saltar"]}</a>
<a class="salto solo-en" href="#main">{IDIOMA["en"]["saltar"]}</a>

{bloque_nav("es")}
{bloque_nav("en")}

<main id="main">
{bloque_cuerpo("es")}
{bloque_cuerpo("en")}
</main>

<footer class="footer">
{bloque_pie("es")}
{bloque_pie("en")}
  <p class="footer-lema">bene scriptus</p>
  <p class="footer-copy">&copy; 2026 Antonio López Sánchez · Ala del Mar</p>
</footer>

<script src="/app.js?v=9" defer></script>
</body>
</html>
"""
    with open(os.path.join(RAIZ, "404.html"), "w", encoding="utf-8", newline="") as f:
        f.write(pagina)
    print("escrito: 404.html · español y ingles, segun la ruta")


if __name__ == "__main__":
    main()
