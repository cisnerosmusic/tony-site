# Generador de paginas de libro para antoniolopezsanchez.art
# Lee un manifiesto JSON y los textos entregados por el autor, y emite
# /libros/<slug>/index.html como HTML estatico del sistema de diseno.
# Uso: python herramientas/gen-libro.py herramientas/libros/<slug>.json

import json, os, sys, html
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"

FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%230a0c1f'/%3E%3Ctext x='16' y='23' text-anchor='middle' font-family='Georgia,serif' font-size='19' fill='%23d4a030'%3EA%3C/text%3E%3Crect x='3' y='3' width='26' height='26' fill='none' stroke='%23d4a030' stroke-opacity='0.4' stroke-width='1'/%3E%3C/svg%3E"

NAV = [("/", "Portada"), ("/libros/", "Mis libros"), ("/ineditos/", "Inéditos"),
       ("/tinta-ciones/", "Tinta-ciones"), ("/trova/", "La trova"),
       ("/plano-abierto/", "Plano abierto"), ("/laureles/", "Laureles"), ("/periodista/", "El periodista"),
       ("/directorio/", "Directorio")]

def esc(t):
    return html.escape(t, quote=False)

def leer(ruta):
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
    ficha = "\n".join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in ficha_items.items())

    galeria = ""
    for g in m.get("galeria", []):
        gw, gh = dims(g["img"])
        galeria += f'<figure><img src="{g["img"]}" width="{gw}" height="{gh}" alt="{esc(g["alt"])}" loading="lazy"><figcaption>{esc(g["pie"])}</figcaption></figure>\n'

    prensa = "\n".join(f"<li>{esc(p)}</li>" for p in m.get("prensa", []))
    nav_html = "\n    ".join(f'<a href="{h}">{n}</a>' for h, n in NAV if h != "/")

    premios_jsonld = json.dumps(m.get("premios", []), ensure_ascii=False)
    seo_titulo = m.get("seo_titulo") or (titulo + " | Antonio López Sánchez")
    seo_desc = m.get("seo_desc") or m["descripcion"][:155]

    def bloque(id_, titulo_b, cuerpo, lado):
        if not cuerpo.strip():
            return ""
        return (f'  <section class="libro-bloque reveal reveal-{lado}" aria-labelledby="b-{id_}">\n'
                f'    <h2 id="b-{id_}">{titulo_b}</h2>\n'
                f'    <div class="section-divider"></div>\n{cuerpo}\n  </section>\n\n')

    nota_idioma = '    <p class="nota-demo">Los textos literarios se publican siempre en su idioma original, el español.</p>'
    bloques = "".join([
        bloque("contratapa", m.get("contratapa_titulo", "Nota de contratapa"), contratapa, "left"),
        bloque("vyv", "Con voz y voto", (vyv + '\n    <p class="vyv-firma">ALS</p>') if vyv else "", "right"),
        bloque("fragmentos", "Fragmentos", (fragmentos + "\n" + nota_idioma) if fragmentos else "", "left"),
        bloque("presentaciones", "Presentaciones", f'    <div class="galeria">\n{galeria}    </div>' if galeria else "", "right"),
        bloque("prensa", "Prensa", f'    <ul class="lista-obras">\n{prensa}\n    </ul>' if prensa else "", "left"),
        bloque("ficha", "Ficha", f'    <dl class="ficha">\n{ficha}\n    </dl>', "right"),
    ])

    pagina = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(seo_titulo)}</title>
<meta name="description" content="{esc(seo_desc)}">
<link rel="icon" href="{FAVICON}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="book">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(seo_titulo)}">
<meta property="og:description" content="{esc(seo_desc)}">
<meta property="og:image" content="{DOMINIO}{m["cubierta"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(seo_titulo)}">
<meta name="twitter:description" content="{esc(seo_desc)}">
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
  "url": "{url}"
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
<link rel="stylesheet" href="/styles.css?v=5">
</head>
<body>

<a class="salto" href="#main">Saltar al contenido</a>

<nav class="nav">
  <a href="/" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" onclick="document.querySelector('.nav-links').classList.toggle('open')" aria-label="Menú">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links">
    <li><a href="/libros/" class="active">Mis libros</a></li>
    <li><a href="/ineditos/">Inéditos</a></li>
    <li><a href="/tinta-ciones/">Tinta-ciones</a></li>
    <li><a href="/trova/">La trova</a></li>
    <li><a href="/plano-abierto/">Plano abierto</a></li>
    <li><a href="/laureles/">Laureles</a></li>
    <li><a href="/periodista/">El periodista</a></li>
    <li><a href="/directorio/">Directorio</a></li>
    <li><a href="/en/" lang="en" hreflang="en">EN</a></li>
  </ul>
</nav>

<header class="page-header">
  <h1>{esc(titulo)}</h1>
  <p>{esc(m["tira_sub"])}</p>
</header>

<main id="main">
<div class="section libro-pagina">

  <figure class="cubierta-dominante reveal reveal-right">
    <img src="{m["cubierta"]}" width="{cw}" height="{ch}" alt="{esc(m["cubierta_alt"])}">
  </figure>

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

<script src="/app.js?v=7" defer></script>
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
