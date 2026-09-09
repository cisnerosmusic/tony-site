# Generador de paginas de libro para antoniolopezsanchez.art
# Lee un manifiesto JSON y los textos entregados por el autor, y emite
# /libros/<slug>/index.html como HTML estatico del sistema de diseno.
# Uso: python herramientas/gen-libro.py herramientas/libros/<slug>.json

import json, os, sys, html
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion   # menu y pie: una sola definicion para todo el sitio

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"

# Toda gestion de derechos fuera de Cuba pasa por Ernesto Cisneros. Dos destinos
# fijos y ningun otro, en cualquier idioma: decision del autor, 8 de septiembre
# de 2026. Una pagina que declara derechos disponibles y no dice a donde
# escribir es una fuga (regla de PRODUCT.md).
REPRESENTACION = "https://ernestocisneros.art/es/representacion-literaria.html"
DERECHOS_EMAIL = "derechos@antoniolopezsanchez.art"
SALIDA_DERECHOS = (f'<a href="{REPRESENTACION}">Consultas de derechos</a> '
                   f'· <a href="mailto:{DERECHOS_EMAIL}">{DERECHOS_EMAIL}</a>')

# Archivos reales, no data URI: Google solo indexa favicons que puede rastrear aparte.
FAVICON = ('<link rel="icon" href="/favicon.ico" sizes="any">\n'
           '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
           '<link rel="apple-touch-icon" href="/apple-touch-icon.png">')


def esc(t):
    """Texto visible: se dejan las comillas como el autor las escribio."""
    return html.escape(t, quote=False)


def esc_attr(t):
    """Valor de atributo: aqui las comillas SI se escapan, o una comilla en
    un titulo o en un alt parte el HTML en dos."""
    return html.escape(t, quote=True)

TEXTOS = os.path.join(RAIZ, "herramientas", "textos")

def leer(ruta):
    # Los manifiestos guardan rutas relativas a herramientas/textos/, para que
    # el generador corra en cualquier maquina y el repositorio sea la fuente
    # completa del sitio.
    if not os.path.isabs(ruta):
        ruta = os.path.join(TEXTOS, ruta.replace("/", os.sep))
    with open(ruta, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n").strip("\n")

def prosa_a_html(texto, clase_p=""):
    # Parrafos: lineas no vacias; la sangria del original se vuelve text-indent CSS.
    parrafos = [l.strip() for l in texto.split("\n") if l.strip()]
    attr = f' class="{clase_p}"' if clase_p else ""
    return "\n".join(f"<p{attr}>{esc(p)}</p>" for p in parrafos)

def dims(ruta_rel):
    with Image.open(os.path.join(RAIZ, ruta_rel.lstrip("/"))) as im:
        return im.size

def generar(manifiesto):
    m = json.load(open(manifiesto, encoding="utf-8"))
    slug, titulo = m["slug"], m["titulo"]
    url = f"{DOMINIO}/libros/{slug}/"
    cw, ch = dims(m["cubierta"])

    contratapa = prosa_a_html(leer(m["contratapa"])) if m.get("contratapa") else ""
    vyv = prosa_a_html(leer(m["vyv"])) if m.get("vyv") else ""

    frags = []
    for f in m.get("fragmentos", []):
        cuerpo = leer(f["archivo"])
        if f["tipo"] == "verso":
            frags.append(f'<h3 class="fragmento-titulo">{esc(f["titulo"])}</h3>\n<div class="fragmento-verso">{esc(cuerpo)}</div>')
        else:
            # quita las dos primeras lineas si son numero de capitulo y titulo repetido
            lineas = cuerpo.split("\n")
            while lineas and (lineas[0].strip().isupper() or lineas[0].strip().rstrip("IVXLC.").strip() == "" ) and len(lineas[0].strip()) < 60:
                lineas.pop(0)
            frags.append(f'<h3 class="fragmento-titulo">{esc(f["titulo"])}</h3>\n<div class="fragmento">{prosa_a_html(chr(10).join(lineas))}</div>')
    fragmentos = "\n".join(frags)

    ficha_items = dict(m["ficha"])
    # Señal editorial discreta: derechos mundiales disponibles fuera de Cuba,
    # salvo que el manifiesto la apague o la reemplace.
    if m.get("derechos", True):
        ficha_items.setdefault("derechos", "Disponibles para ediciones y traducciones fuera de Cuba")
    filas = []
    for k, v in ficha_items.items():
        # La fila de derechos nunca sale sin su via de contacto.
        if k == "derechos":
            filas.append(f'<div><dt>{esc(k)}</dt>'
                         f'<dd>{esc(v).rstrip(".")}. {SALIDA_DERECHOS}</dd></div>')
        else:
            filas.append(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>')
    ficha = "\n".join(filas)

    # Volumenes: para las obras que salieron como juego de varios tomos, cada
    # portada con su titulo y la linea que el autor le puso.
    volumenes = ""
    for v in m.get("volumenes", []):
        vw, vh = dims(v["img"])
        volumenes += (f'<figure><img src="{v["img"]}" width="{vw}" height="{vh}" alt="{esc_attr(v["alt"])}" loading="lazy">'
                      f'<figcaption><strong>{esc(v["titulo"])}</strong><br>{esc(v["pie"])}</figcaption></figure>\n')

    galeria = ""
    for g in m.get("galeria", []):
        gw, gh = dims(g["img"])
        galeria += f'<figure><img src="{g["img"]}" width="{gw}" height="{gh}" alt="{esc_attr(g["alt"])}" loading="lazy"><figcaption>{esc(g["pie"])}</figcaption></figure>\n'

    # Prensa: cada entrada puede ser texto suelto o una ficha con enlace. Ademas de
    # la lista visible, los articulos con URL se declaran como subjectOf del libro en
    # el JSON-LD, que es la propiedad correcta para un texto que habla de la obra;
    # sameAs queda reservado a la identidad del libro mismo.
    prensa_items, subjectof = [], []
    for p in m.get("prensa", []):
        if isinstance(p, str):
            prensa_items.append(f"<li>{esc(p)}</li>")
            continue
        cabeza = (f'<a href="{p["url"]}" target="_blank" rel="noopener">{esc(p["titulo"])}</a>'
                  if p.get("url") else f'<strong>{esc(p["titulo"])}</strong>')
        pie = f' <span class="meta">· {esc(p["pie"])}</span>' if p.get("pie") else ""
        prensa_items.append(f"<li>{cabeza}{pie}</li>")
        if p.get("url"):
            art = {"@type": "NewsArticle", "headline": p["titulo"], "url": p["url"]}
            if p.get("fecha"):
                art["datePublished"] = p["fecha"]
            if p.get("autor"):
                art["author"] = {"@type": "Person", "name": p["autor"]}
            if p.get("medio"):
                art["publisher"] = {"@type": "Organization", "name": p["medio"]}
            subjectof.append(art)
    prensa = "\n".join(prensa_items)
    subjectof_jsonld = (',\n  "subjectOf": '
                        + json.dumps(subjectof, ensure_ascii=False, indent=2).replace("\n", "\n  ")) if subjectof else ""
    # Bajo la cubierta, los caminos para leer: la descarga oficial cuando el libro
    # entero esta en alguna parte, y los cuentos que viven en Contarte con su
    # propia habitacion. El texto no se duplica, se enlaza.
    salidas = []
    d = m.get("descarga")
    if d:
        salidas.append((d["url"], d["texto"], d.get("pie"), True))
    for l in m.get("lecturas", []):
        salidas.append((l["url"], l["texto"], l.get("pie"), False))
    descarga_html = ""
    if salidas:
        botones = "".join(
            f'    <a href="{u}"{" target=\"_blank\" rel=\"noopener\"" if fuera else ""} class="btn btn-filled">{esc(txt)}</a>\n'
            + (f'    <span class="meta">{esc(pie_b)}</span>\n' if pie_b else "")
            for u, txt, pie_b, fuera in salidas)
        descarga_html = '\n  <p class="descarga reveal reveal-left">\n' + botones + '  </p>\n'

    # Una pagina de libro cuelga de Mis libros pero no ES Mis libros: el menu la
    # marca activa y el pie no marca ninguna pagina como actual.
    menu_html = navegacion.menu_html("/libros/")
    nav_html = navegacion.pie_html(None)

    premios_jsonld = json.dumps(m.get("premios", []), ensure_ascii=False)
    # sameAs ata esta ficha al mismo libro en fuentes externas verificadas, para que
    # los buscadores no lo confundan con obras homonimas de otros autores.
    referencias = m.get("referencias", [])
    sameas_jsonld = (',\n  "sameAs": ' + json.dumps(referencias, ensure_ascii=False)) if referencias else ""
    seo_titulo = m.get("seo_titulo") or (titulo + " | Antonio López Sánchez")
    seo_desc = m.get("seo_desc") or m["descripcion"][:155]

    def bloque(id_, titulo_b, cuerpo, lado):
        if not cuerpo.strip():
            return ""
        return (f'  <section class="libro-bloque reveal reveal-{lado}" aria-labelledby="b-{id_}">\n'
                f'    <h2 id="b-{id_}">{titulo_b}</h2>\n'
                f'    <div class="section-divider"></div>\n{cuerpo}\n  </section>\n\n')

    piezas = [
        ("contratapa", m.get("contratapa_titulo", "Nota de contratapa"), contratapa),
        ("volumenes", m.get("volumenes_titulo", "Los libros"),
         f'    <div class="galeria">\n{volumenes}    </div>' if volumenes else ""),
        ("vyv", "Con voz y voto", (vyv + '\n    <p class="vyv-firma">ALS</p>') if vyv else ""),
        ("fragmentos", "Fragmentos", fragmentos),
        ("presentaciones", "Presentaciones", f'    <div class="galeria">\n{galeria}    </div>' if galeria else ""),
        ("prensa", "Prensa", f'    <ul class="lista-obras">\n{prensa}\n    </ul>' if prensa else ""),
        ("ficha", "Ficha", f'    <dl class="ficha">\n{ficha}\n    </dl>'),
    ]
    # El lado del reveal se alterna sobre los bloques que de verdad salen, no sobre
    # la lista completa: asi un libro al que le falte alguno no rompe el zigzag.
    bloques, n = "", 0
    for id_, titulo_b, cuerpo in piezas:
        if not cuerpo.strip():
            continue
        bloques += bloque(id_, titulo_b, cuerpo, "left" if n % 2 == 0 else "right")
        n += 1

    pagina = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(seo_titulo)}</title>
<meta name="description" content="{esc_attr(seo_desc)}">
{FAVICON}
<link rel="canonical" href="{url}">
<meta property="og:type" content="book">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc_attr(seo_titulo)}">
<meta property="og:description" content="{esc_attr(seo_desc)}">
<meta property="og:image" content="{DOMINIO}{m["cubierta"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc_attr(seo_titulo)}">
<meta name="twitter:description" content="{esc_attr(seo_desc)}">
<meta name="twitter:image" content="{DOMINIO}{m["cubierta"]}">
<meta property="og:locale" content="es_ES">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Book",
  "name": {json.dumps(titulo, ensure_ascii=False)},
  "author": {{ "@type": "Person", "name": "Antonio López Sánchez", "url": "{DOMINIO}/" }},
  "datePublished": "{m["anio"]}",
  "publisher": {{ "@type": "Organization", "name": {json.dumps(m["editorial"], ensure_ascii=False)} }},
  "inLanguage": "es",
  "genre": {json.dumps(m["genero"], ensure_ascii=False)},
  "award": {premios_jsonld},
  "image": "{DOMINIO}{m["cubierta"]}",
  "url": "{url}"{sameas_jsonld}{subjectof_jsonld}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Ala del Mar", "item": "{DOMINIO}/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Mis libros", "item": "{DOMINIO}/libros/" }},
    {{ "@type": "ListItem", "position": 3, "name": {json.dumps(titulo, ensure_ascii=False)}, "item": "{url}" }}
  ]
}}
</script>
<meta name="theme-color" content="#0a0c1f">
<link rel="preload" href="/fonts/cinzel-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts.css?v=5">
<link rel="stylesheet" href="/styles.css?v=19">
</head>
<body>

<a class="salto" href="#main">Saltar al contenido</a>

<nav class="nav">
  <a href="/" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="menu-principal">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links" id="menu-principal">
{menu_html}
  </ul>
</nav>

<header class="page-header">
  <h1>{esc(titulo)}</h1>
  <p>{esc(m["tira_sub"])}</p>
</header>

<main id="main">
<div class="section libro-pagina">

  <figure class="cubierta-dominante reveal reveal-right">
    <img src="{m["cubierta"]}" width="{cw}" height="{ch}" alt="{esc_attr(m["cubierta_alt"])}">
  </figure>
{descarga_html}
{bloques}  <p style="margin-top:2rem;"><a href="/libros/" class="btn">Volver a Mis libros</a></p>

</div>
</main>

<footer class="footer">
  <nav class="footer-nav" aria-label="Secciones">
{nav_html}
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
    destino = os.path.join(RAIZ, "libros", slug, "index.html")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(pagina)
    print("escrito:", destino)

if __name__ == "__main__":
    generar(sys.argv[1])
