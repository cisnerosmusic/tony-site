# Genera la sala de Ineditos en cada idioma: /ineditos/ y una pagina por
# novela, /ineditos/<slug>/, desde herramientas/ineditos.json; y su version
# inglesa, /en/unpublished/, desde la capa herramientas/ineditos.en.json.
#
# Una novela inedita se enseña como un libro del catalogo, con la misma
# maqueta y los mismos rotulos: sinopsis, Con voz y voto, fragmentos y ficha.
# Lo que no lleva es cubierta, editorial ni año, porque no los tiene.
#
# De cada obra entra solo lo que el autor eligio. Nunca la novela entera: la
# haria perder su condicion de inedita ante concursos y editoriales, y esa es
# una regla del repositorio, escrita en AGENTS.md.
#
# Idiomas. Como en las paginas de libro, la capa trae solo el aparato:
# presentacion, sinopsis, Con voz y voto, lineas de tarjeta y metadatos. Los
# titulos y los fragmentos no se traducen nunca, y en la pagina inglesa salen
# marcados con lang="es".
#
# Uso: python herramientas/gen-ineditos.py

import json, os, sys, html
from importlib.machinery import SourceFileLoader

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion   # menu y pie: una sola definicion para todo el sitio

# Las convenciones de los textos del autor (fecha al pie, sello de la casa)
# viven en leer-poema.py. El guion del nombre impide un import normal.
leer_poema = SourceFileLoader("leer_poema", os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "leer-poema.py")).load_module()

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=37"
DERECHOS_EMAIL = "derechos@antoniolopezsanchez.art"
IDIOMAS = json.load(open(os.path.join(RAIZ, "herramientas", "idiomas.json"), encoding="utf-8"))

FAVICON = ('<link rel="icon" href="/favicon.ico" sizes="any">\n'
           '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
           '<link rel="apple-touch-icon" href="/apple-touch-icon.png">')

TEXTOS = os.path.join(RAIZ, "herramientas", "textos")

# Lo que en español estaba escrito aqui. En los demas idiomas lo trae la capa.
ES = {
    "ruta": "/ineditos/",
    "h1": "Inéditos",
    "entrar": "Entrar a la novela",
    "volver": "Volver a Inéditos",
    "migas": "Inéditos",
    "bloques": {"sinopsis": "Sinopsis", "vyv": "Con voz y voto", "fragmentos": "Fragmentos", "ficha": "Ficha"},
    "ficha": {"estado": "estado", "estado_valor": "Inédita", "genero": "género", "derechos": "derechos"},
    # Mismo aviso y mismo lugar que las obras eroticas del Farraluque.
    "aviso_adultos": "Novela con pasajes de sexo explícito, escrita para lectores adultos.",
}


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
    # Ni fecha ni sello al final, como en los cuentos y en los poemas: lo pidio
    # Tony el 22 de septiembre de 2026. Hoy ningun fragmento de Ineditos trae
    # uno; esto esta para que no entre callando con el proximo envio.
    while lineas and not lineas[-1].strip():
        lineas.pop()
    if lineas and leer_poema.parece_colofon(lineas[-1]):
        sys.exit(f"un fragmento de Inéditos acaba en «{lineas[-1].strip()}», que parece "
                 "fecha o sello. Si lo es, quítalo del texto; si es parte de la obra, "
                 "dilo en un comentario del manifiesto.")
    return cabecera + prosa_a_html("\n".join(lineas))


def jsonld(d):
    return ('<script type="application/ld+json">\n'
            + json.dumps(d, ensure_ascii=False, indent=2) + '\n</script>\n')


def migas(items):
    return jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList",
                   "itemListElement": [{"@type": "ListItem", "position": i, "name": n, "item": u}
                                       for i, (n, u) in enumerate(items, 1)]})


def alternos(rutas):
    """hreflang reciproco entre las versiones de una pagina, y x-default al
    español, como en las paginas de libro."""
    if len(rutas) < 2:
        return ""
    t = "".join(f'<link rel="alternate" hreflang="{l}" href="{DOMINIO}{r}">\n' for l, r in rutas.items())
    return t + f'<link rel="alternate" hreflang="x-default" href="{DOMINIO}{rutas["es"]}">\n'


def cabeza(lang, titulo, desc, url, tipo_og, rutas):
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
<title>{esc(titulo)}</title>
<meta name="description" content="{esc_attr(desc)}">
{FAVICON}
<link rel="canonical" href="{url}">
{alternos(rutas)}<meta property="og:type" content="{tipo_og}">
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


def menu(lang):
    L = IDIOMAS[lang]
    # En ingles Ineditos no tiene entrada propia en el menu: son libros, y se
    # llega desde el catalogo, que es la entrada que se enciende.
    activa = "/ineditos/" if lang == "es" else L["ruta_libros"]
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


def bloque(id_, titulo, cuerpo, lado):
    return (f'  <section class="libro-bloque reveal reveal-{lado}" aria-labelledby="b-{id_}">\n'
            f'    <h2 id="b-{id_}">{titulo}</h2>\n'
            f'    <div class="section-divider"></div>\n{cuerpo}\n  </section>\n\n')


def rutas_de(capas, slug=None):
    return {l: V["ruta"] + (f"{slug}/" if slug else "") for l, V in capas.items()}


def pagina_novela(lang, V, n, capas):
    """n es la novela en español; su capa, si no es español, en V["novelas"]."""
    L = IDIOMAS[lang]
    es = lang == "es"
    t = n if es else {**n, **V["novelas"][n["slug"]]}
    la = "" if es else ' lang="es"'
    url = f"{DOMINIO}{V['ruta']}{n['slug']}/"
    B = V["bloques"]

    frags = "\n".join(f'<h3 class="fragmento-titulo"{la}>{esc(f["titulo"])}</h3>\n'
                      f'<div class="fragmento"{la}>{cuerpo_fragmento(leer(f["archivo"]), n.get("lugar", False))}</div>'
                      for f in n["fragmentos"])
    if L["aviso_fragmentos"]:
        frags = f'<p class="nota">{esc(L["aviso_fragmentos"])}</p>\n' + frags
    F = V["ficha"]
    derechos = (f'{esc(L["derechos"])}. <a href="{L["representacion"]}">{esc(L["consulta_derechos"])}</a> '
                f'· <a href="mailto:{DERECHOS_EMAIL}">{DERECHOS_EMAIL}</a>')
    ficha = ('    <dl class="ficha">\n'
             f'<div><dt>{esc(F["estado"])}</dt><dd>{esc(F["estado_valor"])}</dd></div>\n'
             f'<div><dt>{esc(F["genero"])}</dt><dd>{esc(t["genero"].split(" · ")[0])}</dd></div>\n'
             f'<div><dt>{esc(F["derechos"])}</dt><dd>{derechos}</dd></div>\n'
             '    </dl>')

    piezas = [("sinopsis", B["sinopsis"], prosa_a_html(leer(t["sinopsis"]))),
              ("vyv", B["vyv"], prosa_a_html(leer(t["vyv"])) + '\n    <p class="vyv-firma">ALS</p>'),
              ("fragmentos", B["fragmentos"], frags),
              ("ficha", B["ficha"], ficha)]
    cuerpo = "".join(bloque(i, ti, c, "left" if k % 2 == 0 else "right")
                     for k, (i, ti, c) in enumerate(piezas))
    aviso = (f'  <p class="sonata-premio reveal reveal-left">{esc(V["aviso_adultos"])}</p>\n\n'
             if n.get("adultos") else "")

    datos = {"@context": "https://schema.org", "@type": "Book",
             "name": n["titulo"], "url": url, "inLanguage": "es",
             "genre": t["genero"].split(" · ")[0],
             "author": {"@id": f"{DOMINIO}/#antonio"},
             "description": t["seo_desc"]}

    return (cabeza(lang, t["seo_titulo"], t["seo_desc"], url, "book", rutas_de(capas, n["slug"]))
            + jsonld(datos)
            + migas([("Ala del Mar", DOMINIO + L["portada"]), (V["migas"], DOMINIO + V["ruta"]), (n["titulo"], url)])
            + menu(lang)
            + f"""
<header class="page-header">
  <h1{la}>{esc(n["titulo"])}</h1>
</header>

<main id="main">
<div class="section libro-pagina">

{aviso}{cuerpo}  <p style="margin-top:2rem;"><a href="{V['ruta']}" class="btn">{esc(V["volver"])}</a></p>

</div>
</main>
"""
            + pie(lang, None))


def pagina_sala(lang, V, cfg, capas):
    L = IDIOMAS[lang]
    es = lang == "es"
    la = "" if es else ' lang="es"'
    url_sala = DOMINIO + V["ruta"]

    def tarjeta(n):
        t = n if es else {**n, **V["novelas"][n["slug"]]}
        enlace = f'{V["ruta"]}{n["slug"]}/'
        # Fuera del español el titulo se queda en español, con su sentido
        # entre parentesis, como en el catalogo.
        sentido = "" if es else f' <span class="libro-meta">({esc(t["significado"])})</span>'
        return (f'  <article class="cuento-ficha reveal reveal-right">\n'
                f'    <h3 class="libro-titulo"><a href="{enlace}"{la}>{esc(n["titulo"])}</a>{sentido}</h3>\n'
                f'    <p class="libro-meta">{esc(t["genero"])}</p>\n'
                f'    <p class="libro-sinopsis">{esc(t["linea"])}</p>\n'
                f'    <p style="margin-top:1.2rem;"><a href="{enlace}" class="btn">{esc(V["entrar"])}</a></p>\n'
                f'  </article>')

    parrafos = [l.strip() for l in leer(V["presentacion"]).split("\n") if l.strip()]
    presentacion = "\n".join(
        f'    <p class="section-text" style="margin-bottom:{"3rem" if i == len(parrafos) - 1 else "1.25rem"};">{esc(p)}</p>'
        for i, p in enumerate(parrafos))

    lista = {"@context": "https://schema.org", "@type": "CollectionPage",
             "name": V["seo_titulo"], "description": V["seo_desc"], "url": url_sala,
             "inLanguage": L["lang"], "isPartOf": {"@id": f"{DOMINIO}/#sitio"},
             "mainEntity": {"@type": "ItemList", "itemListElement": [
                 {"@type": "ListItem", "position": i, "url": f"{url_sala}{n['slug']}/", "name": n["titulo"]}
                 for i, n in enumerate(cfg["novelas"], 1)]}}

    return (cabeza(lang, V["seo_titulo"], V["seo_desc"], url_sala, "website", rutas_de(capas))
            + jsonld(lista)
            + migas([("Ala del Mar", DOMINIO + L["portada"]), (V["migas"], url_sala)])
            + menu(lang)
            + f"""
<header class="page-header">
  <h1>{esc(V["h1"])}</h1>
  <p>{esc(V["frase"])}</p>
</header>

<main id="main">
<div class="section">
  <div class="reveal reveal-right">
    <h2 class="section-title">{esc(V["sala_titulo"])}</h2>
    <div class="section-divider"></div>
{presentacion}
  </div>

  <div class="cuento-lista">
{chr(10).join(tarjeta(n) for n in cfg["novelas"])}
  </div>

</div>
</main>
"""
            + pie(lang, "/ineditos/" if es else None))


def main():
    cfg = json.load(open(os.path.join(RAIZ, "herramientas", "ineditos.json"), encoding="utf-8"))
    capas = {"es": {**ES, **{k: cfg[k] for k in ("frase", "sala_titulo", "presentacion", "seo_titulo", "seo_desc")}}}
    for lang in IDIOMAS:
        if lang.startswith("_") or lang == "es":
            continue
        ruta = os.path.join(RAIZ, "herramientas", f"ineditos.{lang}.json")
        if os.path.exists(ruta):
            V = json.load(open(ruta, encoding="utf-8"))
            faltan = [n["slug"] for n in cfg["novelas"] if n["slug"] not in V["novelas"]]
            if faltan:
                sys.exit(f"ineditos.{lang}.json no trae: {', '.join(faltan)}")
            capas[lang] = V

    for lang, V in capas.items():
        base = os.path.join(RAIZ, V["ruta"].strip("/").replace("/", os.sep))
        for n in cfg["novelas"]:
            destino = os.path.join(base, n["slug"], "index.html")
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "w", encoding="utf-8", newline="") as f:
                f.write(pagina_novela(lang, V, n, capas))
        with open(os.path.join(base, "index.html"), "w", encoding="utf-8", newline="") as f:
            f.write(pagina_sala(lang, V, cfg, capas))
        print(f"escrito: {V['ruta']} con {len(cfg['novelas'])} novela(s)")


if __name__ == "__main__":
    main()
