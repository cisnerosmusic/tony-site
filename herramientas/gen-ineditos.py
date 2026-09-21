# Genera la sala de Ineditos: /ineditos/ y una pagina por novela,
# /ineditos/<slug>/, desde herramientas/ineditos.json.
#
# Una novela inedita se enseña como un libro del catalogo, con la misma
# maqueta y los mismos rotulos: sinopsis, Con voz y voto, fragmentos y ficha.
# Lo que no lleva es cubierta, editorial ni año, porque no los tiene.
#
# De cada obra entra solo lo que el autor eligio. Nunca la novela entera: la
# haria perder su condicion de inedita ante concursos y editoriales, y esa es
# una regla del repositorio, escrita en AGENTS.md.
#
# Uso: python herramientas/gen-ineditos.py

import json, os, sys, html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion   # menu y pie: una sola definicion para todo el sitio

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=33"
URL_SALA = DOMINIO + "/ineditos/"

# El mismo destino de derechos que las paginas de libro, leido del mismo
# sitio: si cambia, cambia en todas a la vez.
ES = json.load(open(os.path.join(RAIZ, "herramientas", "idiomas.json"), encoding="utf-8"))["es"]
DERECHOS_EMAIL = "derechos@antoniolopezsanchez.art"

# Mismo aviso y mismo lugar que las obras eroticas del Farraluque.
AVISO_ADULTOS = "Novela con pasajes de sexo explícito, escrita para lectores adultos."

FAVICON = ('<link rel="icon" href="/favicon.ico" sizes="any">\n'
           '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
           '<link rel="apple-touch-icon" href="/apple-touch-icon.png">')

TEXTOS = os.path.join(RAIZ, "herramientas", "textos")


def esc(t):
    """Texto visible: se dejan las comillas como el autor las escribio."""
    return html.escape(t, quote=False)


def esc_attr(t):
    """Valor de atributo: aqui las comillas SI se escapan."""
    return html.escape(t, quote=True)


def leer(ruta):
    with open(os.path.join(TEXTOS, ruta.replace("/", os.sep)), encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n").strip("\n")


def prosa_a_html(texto):
    return "\n".join(f"<p>{esc(l.strip())}</p>" for l in texto.split("\n") if l.strip())


def cuerpo_fragmento(texto, lugar=False):
    """El original abre con su titulo en mayusculas, y a veces con un numero
    romano de capitulo: el titulo ya sale arriba, en el h3, asi que se quitan.

    Con lugar=True, lo que viene justo despues es el lugar y el tiempo de la
    escena ("Residencia Lebruit, / Ciudad de Londres. / Verano, 1824."), en
    lineas cortas y sin sangria, antes del primer parrafo sangrado. Pintado
    como prosa salian tres parrafos de una palabra; va junto, en su bloque.
    No se deduce solo porque en los diarios la linea sin sangria del
    principio es "Querido Diario:", que si es un parrafo."""
    lineas = texto.split("\n")
    while lineas and (not lineas[0].strip() or lineas[0].strip().isupper()
                      or lineas[0].strip().rstrip("IVXLC.").strip() == ""):
        lineas.pop(0)
    cabecera = ""
    if lugar:
        datos = []
        while lineas and lineas[0].strip() and not lineas[0][:1].isspace():
            datos.append(lineas.pop(0).strip())
        if datos:
            cabecera = '<p class="fragmento-lugar">' + "<br>".join(esc(l) for l in datos) + "</p>\n"
    return cabecera + prosa_a_html("\n".join(lineas))


def jsonld(d):
    return ('<script type="application/ld+json">\n'
            + json.dumps(d, ensure_ascii=False, indent=2) + '\n</script>\n')


def migas(items):
    return jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList",
                   "itemListElement": [{"@type": "ListItem", "position": i, "name": n, "item": u}
                                       for i, (n, u) in enumerate(items, 1)]})


def cabeza(titulo, desc, url, tipo_og):
    img = f"{DOMINIO}/img/retrato.webp"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc_attr(desc)}">
{FAVICON}
<link rel="canonical" href="{url}">
<meta property="og:type" content="{tipo_og}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc_attr(titulo)}">
<meta property="og:description" content="{esc_attr(desc)}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc_attr(titulo)}">
<meta name="twitter:description" content="{esc_attr(desc)}">
<meta name="twitter:image" content="{img}">
<meta property="og:locale" content="es_ES">
<meta name="theme-color" content="#0a0c1f">
<link rel="preload" href="/fonts/cinzel-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts.css?v=6">
<link rel="stylesheet" href="/styles.css{CSS}">
"""


def menu():
    return f"""</head>
<body>

<a class="salto" href="#main">Saltar al contenido</a>

<nav class="nav">
  <a href="/" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="menu-principal">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links" id="menu-principal">
{navegacion.menu_html("/ineditos/")}
  </ul>
</nav>
"""


def pie(activa):
    return f"""
<footer class="footer">
  <nav class="footer-nav" aria-label="Secciones">
{navegacion.pie_html(activa)}
  </nav>
  <div class="footer-socials">
    <a href="https://www.facebook.com/profile.php?id=100071950279104" target="_blank" rel="noopener" aria-label="Facebook de Antonio López Sánchez"><svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16" aria-hidden="true"><path d="M13.5 22v-8.1h2.72l.41-3.16H13.5V8.72c0-.91.25-1.53 1.56-1.53h1.67V4.36c-.29-.04-1.28-.12-2.43-.12-2.4 0-4.05 1.47-4.05 4.16v2.34H7.53v3.16h2.72V22h3.25z"/></svg></a>
  </div>
  <p class="footer-lema">bene scriptus</p>
  <p class="footer-copy">&copy; 2026 Antonio López Sánchez · Ala del Mar</p>
  <p class="footer-copy">Desarrollado por <a href="https://index01.net" target="_blank" rel="noopener">Index01</a></p>
</footer>

<script src="/app.js?v=10" defer></script>
</body>
</html>
"""


def bloque(id_, titulo, cuerpo, lado):
    return (f'  <section class="libro-bloque reveal reveal-{lado}" aria-labelledby="b-{id_}">\n'
            f'    <h2 id="b-{id_}">{titulo}</h2>\n'
            f'    <div class="section-divider"></div>\n{cuerpo}\n  </section>\n\n')


def pagina_novela(n):
    url = f"{URL_SALA}{n['slug']}/"
    frags = "\n".join(f'<h3 class="fragmento-titulo">{esc(f["titulo"])}</h3>\n'
                      f'<div class="fragmento">{cuerpo_fragmento(leer(f["archivo"]), n.get("lugar", False))}</div>'
                      for f in n["fragmentos"])
    derechos = (f'{esc(ES["derechos"])}. <a href="{ES["representacion"]}">{esc(ES["consulta_derechos"])}</a> '
                f'· <a href="mailto:{DERECHOS_EMAIL}">{DERECHOS_EMAIL}</a>')
    ficha = ('    <dl class="ficha">\n'
             '<div><dt>estado</dt><dd>Inédita</dd></div>\n'
             f'<div><dt>género</dt><dd>{esc(n["genero"].split(" · ")[0])}</dd></div>\n'
             f'<div><dt>derechos</dt><dd>{derechos}</dd></div>\n'
             '    </dl>')

    piezas = [("sinopsis", "Sinopsis", prosa_a_html(leer(n["sinopsis"]))),
              ("vyv", "Con voz y voto", prosa_a_html(leer(n["vyv"])) + '\n    <p class="vyv-firma">ALS</p>'),
              ("fragmentos", "Fragmentos", frags),
              ("ficha", "Ficha", ficha)]
    cuerpo = "".join(bloque(i, t, c, "left" if k % 2 == 0 else "right")
                     for k, (i, t, c) in enumerate(piezas))
    aviso = (f'  <p class="sonata-premio reveal reveal-left">{esc(AVISO_ADULTOS)}</p>\n\n'
             if n.get("adultos") else "")

    datos = {"@context": "https://schema.org", "@type": "Book",
             "name": n["titulo"], "url": url, "inLanguage": "es",
             "genre": n["genero"].split(" · ")[0],
             "author": {"@id": f"{DOMINIO}/#antonio"},
             "description": n["seo_desc"]}

    return (cabeza(n["seo_titulo"], n["seo_desc"], url, "book")
            + jsonld(datos)
            + migas([("Ala del Mar", DOMINIO + "/"), ("Inéditos", URL_SALA), (n["titulo"], url)])
            + menu()
            + f"""
<header class="page-header">
  <h1>{esc(n["titulo"])}</h1>
</header>

<main id="main">
<div class="section libro-pagina">

{aviso}{cuerpo}  <p style="margin-top:2rem;"><a href="/ineditos/" class="btn">Volver a Inéditos</a></p>

</div>
</main>
"""
            + pie(None))


def pagina_sala(cfg):
    def tarjeta(n):
        return (f'  <article class="cuento-ficha reveal reveal-right">\n'
                f'    <h3 class="libro-titulo"><a href="/ineditos/{n["slug"]}/">{esc(n["titulo"])}</a></h3>\n'
                f'    <p class="libro-meta">{esc(n["genero"])}</p>\n'
                f'    <p class="libro-sinopsis">{esc(n["linea"])}</p>\n'
                f'    <p style="margin-top:1.2rem;"><a href="/ineditos/{n["slug"]}/" class="btn">Entrar a la novela</a></p>\n'
                f'  </article>')

    parrafos = [l.strip() for l in leer(cfg["presentacion"]).split("\n") if l.strip()]
    presentacion = "\n".join(
        f'    <p class="section-text" style="margin-bottom:{"3rem" if i == len(parrafos) - 1 else "1.25rem"};">{esc(p)}</p>'
        for i, p in enumerate(parrafos))

    lista = {"@context": "https://schema.org", "@type": "CollectionPage",
             "name": cfg["seo_titulo"], "description": cfg["seo_desc"], "url": URL_SALA,
             "inLanguage": "es", "isPartOf": {"@id": f"{DOMINIO}/#sitio"},
             "mainEntity": {"@type": "ItemList", "itemListElement": [
                 {"@type": "ListItem", "position": i, "url": f"{URL_SALA}{n['slug']}/", "name": n["titulo"]}
                 for i, n in enumerate(cfg["novelas"], 1)]}}

    return (cabeza(cfg["seo_titulo"], cfg["seo_desc"], URL_SALA, "website")
            + jsonld(lista)
            + migas([("Ala del Mar", DOMINIO + "/"), ("Inéditos", URL_SALA)])
            + menu()
            + f"""
<header class="page-header">
  <h1>Inéditos</h1>
  <p>{esc(cfg["frase"])}</p>
</header>

<main id="main">
<div class="section">
  <div class="reveal reveal-right">
    <h2 class="section-title">{esc(cfg["sala_titulo"])}</h2>
    <div class="section-divider"></div>
{presentacion}
  </div>

  <div class="cuento-lista">
{chr(10).join(tarjeta(n) for n in cfg["novelas"])}
  </div>

</div>
</main>
"""
            + pie("/ineditos/"))


def main():
    cfg = json.load(open(os.path.join(RAIZ, "herramientas", "ineditos.json"), encoding="utf-8"))
    for n in cfg["novelas"]:
        destino = os.path.join(RAIZ, "ineditos", n["slug"], "index.html")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, "w", encoding="utf-8", newline="") as f:
            f.write(pagina_novela(n))
        print("escrito:", os.path.relpath(destino, RAIZ))
    with open(os.path.join(RAIZ, "ineditos", "index.html"), "w", encoding="utf-8", newline="") as f:
        f.write(pagina_sala(cfg))
    print(f"escrito: ineditos/index.html con {len(cfg['novelas'])} novela(s)")


if __name__ == "__main__":
    main()
