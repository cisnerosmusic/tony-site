# Genera /tinta-ciones/de-cimitas/ desde herramientas/decimitas.json.
#
# Una De-Cimita son dos cosas que solo funcionan juntas: una foto del autor y
# una decima escrita a partir de ella. Por eso cada una sale en una sola pieza,
# con la imagen y los diez versos dentro del mismo marco. Separarlas seria
# deshacer la obra.
#
# Los textos vienen todos en un documento del autor y se cortan por sus
# encabezados; el emparejamiento con la foto va declarado en el manifiesto,
# porque los nombres no siempre coinciden.
#
# Uso: python herramientas/gen-decimitas.py

import json, os, sys, html
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
URL = DOMINIO + "/tinta-ciones/de-cimitas/"
CSS = "?v=22"


def esc(t):
    """Texto visible: se dejan las comillas como el autor las escribio."""
    return html.escape(t, quote=False)


def esc_attr(t):
    """Valor de atributo: aqui las comillas SI se escapan, o una comilla en
    un titulo o en un alt parte el HTML en dos."""
    return html.escape(t, quote=True)


def trocea(texto, titulos):
    """Corta el documento del autor en bloques, uno por encabezado."""
    lineas = texto.replace("\r", "").split("\n")
    marcas = []
    for i, l in enumerate(lineas):
        if l.strip() in titulos:
            marcas.append((i, l.strip()))
    trozos = {}
    for k, (i, t) in enumerate(marcas):
        fin = marcas[k + 1][0] if k + 1 < len(marcas) else len(lineas)
        cuerpo = [l.rstrip() for l in lineas[i + 1:fin]]
        while cuerpo and not cuerpo[0]:
            cuerpo.pop(0)
        while cuerpo and not cuerpo[-1]:
            cuerpo.pop()
        trozos[t] = cuerpo
    return trozos


def separa_epigrafe(cuerpo):
    """Alguna decima abre con una cita ajena. Sale aparte y con su firma:
    en Señal son dos versos de Polito Ibanez y no del autor."""
    if len(cuerpo) > 2 and cuerpo[1].strip() and not cuerpo[2].strip():
        firma = cuerpo[1].strip()
        if len(firma.split()) <= 4 and firma[0].isupper() and not firma.endswith((",", ";")):
            return [cuerpo[0].strip()], firma, [l for l in cuerpo[3:]]
    return None, None, cuerpo


def dims(rel):
    with Image.open(os.path.join(RAIZ, rel.lstrip("/"))) as im:
        return im.size


def pieza(d, cuerpo, n):
    img = f"/img/decimitas/{d['slug']}.webp"
    w, h = dims(img)
    epi, firma, versos = separa_epigrafe(cuerpo)
    lado = "right" if n % 2 == 0 else "left"
    partes = [f'  <article class="decimita reveal reveal-{lado}" id="{d["slug"]}">']
    partes.append(f'    <figure class="decimita-foto">')
    partes.append(f'      <img src="{img}" width="{w}" height="{h}" alt="{esc_attr(d["alt"])}" loading="lazy">')
    partes.append(f'    </figure>')
    partes.append(f'    <div class="decimita-texto">')
    partes.append(f'      <h2 class="decimita-titulo">{esc(d["titulo"])}</h2>')
    if epi:
        partes.append('      <blockquote class="poema-epigrafe">')
        partes.append(f'        <div class="verso">{esc(epi[0])}</div>')
        partes.append(f'        <cite>{esc(firma)}</cite>')
        partes.append('      </blockquote>')
    partes.append('      <div class="verso decimita-versos">'
                  + "\n".join(esc(l) for l in versos).strip("\n") + '</div>')
    partes.append('      <p class="vyv-firma">ALS</p>')
    partes.append('    </div>')
    partes.append('  </article>')
    return "\n".join(partes)


def main():
    cfg = json.load(open(os.path.join(RAIZ, "herramientas", "decimitas.json"), encoding="utf-8"))
    doc = open(os.path.join(RAIZ, "herramientas", "textos",
                            cfg["documento"].replace("/", os.sep)), encoding="utf-8").read()
    trozos = trocea(doc, {d["titulo_doc"] for d in cfg["decimitas"]})

    faltan = [d["titulo_doc"] for d in cfg["decimitas"] if d["titulo_doc"] not in trozos]
    if faltan:
        print("SIN TEXTO en el documento:", faltan); sys.exit(1)

    piezas = "\n\n".join(pieza(d, trozos[d["titulo_doc"]], i)
                         for i, d in enumerate(cfg["decimitas"]))

    lista = {"@context": "https://schema.org", "@type": "ItemList",
             "name": "De-Cimitas de Antonio López Sánchez",
             "itemListElement": [{"@type": "ListItem", "position": i, "name": d["titulo"]}
                                 for i, d in enumerate(cfg["decimitas"], 1)]}

    T = "De-Cimitas: décimas con imagen de Antonio López Sánchez"
    D = ("Décimas del poeta cubano Antonio López Sánchez escritas a partir de sus propias "
         "fotografías: cada imagen con su décima, en una sola pieza.")

    pagina = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{T}</title>
<meta name="description" content="{D}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="article">
<meta property="og:url" content="{URL}">
<meta property="og:title" content="{T}">
<meta property="og:description" content="{D}">
<meta property="og:image" content="{DOMINIO}/img/decimitas/baraja-rota.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{T}">
<meta name="twitter:description" content="{D}">
<meta name="twitter:image" content="{DOMINIO}/img/decimitas/baraja-rota.webp">
<meta property="og:locale" content="es_ES">
<meta name="theme-color" content="#0a0c1f">
<link rel="preload" href="/fonts/cinzel-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts.css?v=5">
<link rel="stylesheet" href="/styles.css{CSS}">
<script type="application/ld+json">
{json.dumps(lista, ensure_ascii=False, indent=2)}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Ala del Mar", "item": "{DOMINIO}/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Tinta-ciones", "item": "{DOMINIO}/tinta-ciones/" }},
    {{ "@type": "ListItem", "position": 3, "name": "De-Cimitas", "item": "{URL}" }}
  ]
}}
</script>
</head>
<body>

<a class="salto" href="#main">Saltar al contenido</a>

<nav class="nav">
  <a href="/" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="menu-principal">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links" id="menu-principal">
{navegacion.menu_html("/tinta-ciones/")}
  </ul>
</nav>

<header class="page-header">
  <h1>De-Cimitas</h1>
  <p>Una foto y diez versos que le contestan.</p>
</header>

<main id="main">
<div class="section">
  <div class="reveal reveal-right">
    <h2 class="section-title">Lo que mira la décima</h2>
    <div class="section-divider"></div>
    <p class="section-text" style="margin-bottom:3rem;">Otro modo de hacer poesía es buscar la voz oculta, las historias que habitan detrás de una imagen. Aquí van mis fotos vistas y el poema que escucho en ellas.</p>
  </div>

{piezas}

  <div class="reveal reveal-right" style="margin-top:4.5rem;">
    <h2 class="section-title">Una que se salió del cuadro</h2>
    <div class="section-divider"></div>
    <p class="section-text" style="margin-bottom:2.5rem;">Empezó como las demás, mirando una foto. Pero le crecieron tres movimientos, cada uno con su tempo, y ya no cabía en diez versos. Tiene cuarto propio.</p>
  </div>

  <article class="decimita decimita-mayor reveal reveal-left" id="sonata-de-la-lluvia">
    <figure class="decimita-foto">
      <img src="/img/decimitas/sonata-de-la-lluvia.webp" width="720" height="540" alt="Atardecer sobre el muro del malecón, con el sol abriéndose paso entre las nubes" loading="lazy">
    </figure>
    <div class="decimita-texto">
      <h2 class="decimita-titulo">Sonata de la lluvia</h2>
      <p class="libro-sinopsis">Tres movimientos en décimas: un preludio, un aguacero y lo que queda después. Con Fito Páez, Noel Nicola y Santiago Feliú asomados a cada uno.</p>
      <p class="decimita-nota">Con ella gané el <a href="/laureles/">Premio Colateral Yasmina Calcines</a> en 2026.</p>
      <p style="margin-top:1.4rem;"><a href="/tinta-ciones/sonata-de-la-lluvia/" class="btn">Leer la sonata</a></p>
    </div>
  </article>

</div>
</main>

<footer class="footer">
  <nav class="footer-nav" aria-label="Secciones">
{navegacion.pie_html(None)}
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
    destino = os.path.join(RAIZ, "tinta-ciones", "de-cimitas", "index.html")
    with open(destino, "w", encoding="utf-8", newline="") as f:
        f.write(pagina)
    print(f"escrito: {os.path.relpath(destino, RAIZ)} · {len(cfg['decimitas'])} de-cimitas")


if __name__ == "__main__":
    main()
