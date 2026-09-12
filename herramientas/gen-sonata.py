# Genera /tinta-ciones/sonata-de-la-lluvia/, la obra con la que el autor gano
# el Premio Colateral Yasmina Calcines del XXVI Concurso Nacional Ala Decima.
#
# No es una De-Cimita: es una sonata en tres movimientos, con su tempo y su
# epigrafe cada uno, de Fito Paez, Noel Nicola y Santiago Feliu. Por eso tiene
# pagina propia y no cabia en la rejilla de foto mas diez versos.
#
# Detalle que no se puede perder: dentro del verso el autor usa espacios
# multiples como puntuacion ("juega a mujer   a vestido"), y la sangria de tres
# espacios marca donde arranca cada decima de la tirada. Todo eso se conserva
# tal cual y se muestra con white-space: pre-wrap.
#
# Uso: python herramientas/gen-sonata.py

import json, os, sys, html, re
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
URL = DOMINIO + "/tinta-ciones/sonata-de-la-lluvia/"
CSS = "?v=23"
FUENTE = os.path.join(RAIZ, "herramientas", "textos", "decimitas", "sonata-de-la-lluvia.txt")
FOTO = "/img/decimitas/sonata-de-la-lluvia.webp"

FIRMAS = ("Fito Páez", "Noel Nicola", "Santiago Feliú")


def esc(t):
    """Texto visible: se dejan las comillas como el autor las escribio."""
    return html.escape(t, quote=False)


def esc_attr(t):
    """Valor de atributo: aqui las comillas SI se escapan, o una comilla en
    un titulo o en un alt parte el HTML en dos."""
    return html.escape(t, quote=True)


def movimientos(texto):
    """Parte la obra en sus tres movimientos, cada uno con numero, titulo,
    tempo, epigrafe con su firma y la tirada de decimas."""
    lineas = texto.replace("\r", "").split("\n")
    cortes = [i for i, l in enumerate(lineas) if re.fullmatch(r"\(I{1,3}\)", l.strip())]
    salida = []
    for k, i in enumerate(cortes):
        fin = cortes[k + 1] if k + 1 < len(cortes) else len(lineas)
        bloque = lineas[i:fin]
        numero = bloque[0].strip().strip("()")
        titulo = bloque[1].strip()
        tempo = bloque[2].strip().strip("()")
        resto = bloque[3:]
        # epigrafe: hasta la linea que es una firma conocida
        epi, firma, j = [], None, 0
        for j, l in enumerate(resto):
            if l.strip() in FIRMAS:
                firma = l.strip(); break
            if l.strip():
                epi.append(l.strip())
        versos = resto[j + 1:] if firma else resto
        while versos and not versos[0].strip():
            versos.pop(0)
        while versos and not versos[-1].strip():
            versos.pop()
        salida.append({"numero": numero, "titulo": titulo, "tempo": tempo,
                       "epigrafe": epi, "firma": firma, "versos": versos})
    return salida


def main():
    texto = open(FUENTE, encoding="utf-8").read()
    movs = movimientos(texto)
    assert len(movs) == 3, f"esperaba 3 movimientos, encontre {len(movs)}"
    with Image.open(os.path.join(RAIZ, FOTO.lstrip("/"))) as im:
        fw, fh = im.size

    piezas = []
    for n, m in enumerate(movs):
        p = [f'  <section class="mov reveal reveal-{"right" if n % 2 == 0 else "left"}" id="mov-{m["numero"].lower()}">']
        p.append(f'    <p class="mov-numero">{esc(m["numero"])} · <span class="mov-tempo">{esc(m["tempo"])}</span></p>')
        p.append(f'    <h2 class="mov-titulo">{esc(m["titulo"].capitalize())}</h2>')
        if m["firma"]:
            p.append('    <blockquote class="poema-epigrafe">')
            p.append('      <div class="verso">' + "\n".join(esc(l) for l in m["epigrafe"]) + '</div>')
            p.append(f'      <cite>{esc(m["firma"])}</cite>')
            p.append('    </blockquote>')
        p.append('    <div class="verso poema-cuerpo">' + "\n".join(esc(l) for l in m["versos"]) + '</div>')
        p.append('  </section>')
        piezas.append("\n".join(p))
    cuerpo = "\n\n".join(piezas)

    T = "Sonata de la lluvia, de Antonio López Sánchez"
    D = ("Sonata de la lluvia, de Antonio López Sánchez: tres movimientos en décimas, "
         "premiada en el XXVI Concurso Nacional Ala Décima.")

    # CreativeWork y no Poem: schema.org/Poem no existe, devuelve 404.
    # El genero se declara aparte, que es como se dice "esto es poesia".
    datos = {"@context": "https://schema.org", "@type": "CreativeWork",
             "name": "Sonata de la lluvia", "url": URL, "inLanguage": "es",
             "author": {"@id": f"{DOMINIO}/#antonio"},
             "genre": "Poesía. Décima",
             "datePublished": "2026",
             "award": "Premio Colateral Yasmina Calcines, XXVI Concurso Nacional Ala Décima, 2026",
             "description": D,
             "image": DOMINIO + FOTO,
             "hasPart": [{"@type": "CreativeWork", "genre": "Décima", "name": m["titulo"].capitalize(),
                          "position": i} for i, m in enumerate(movs, 1)]}

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
<meta property="og:image" content="{DOMINIO}{FOTO}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{T}">
<meta name="twitter:description" content="{D}">
<meta name="twitter:image" content="{DOMINIO}{FOTO}">
<meta property="og:locale" content="es_ES">
<meta name="theme-color" content="#0a0c1f">
<link rel="preload" href="/fonts/cinzel-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts.css?v=5">
<link rel="stylesheet" href="/styles.css{CSS}">
<script type="application/ld+json">
{json.dumps(datos, ensure_ascii=False, indent=2)}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Ala del Mar", "item": "{DOMINIO}/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Tinta-ciones", "item": "{DOMINIO}/tinta-ciones/" }},
    {{ "@type": "ListItem", "position": 3, "name": "De-Cimitas", "item": "{DOMINIO}/tinta-ciones/de-cimitas/" }},
    {{ "@type": "ListItem", "position": 4, "name": "Sonata de la lluvia", "item": "{URL}" }}
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
  <h1>Sonata de la lluvia</h1>
  <p>Tres movimientos en décimas.</p>
</header>

<main id="main">
<div class="section cuento">

  <figure class="sonata-foto reveal reveal-right">
    <img src="{FOTO}" width="{fw}" height="{fh}" alt="Atardecer sobre el muro del malecón, con el sol abriéndose paso entre las nubes" loading="lazy">
  </figure>

  <p class="sonata-premio reveal reveal-left">Con esta obra gané el <a href="/laureles/">Premio Colateral Yasmina Calcines</a>, del XXVI Concurso Nacional Ala Décima, en 2026.</p>

{cuerpo}

  <p class="vyv-firma" style="margin-top:2.5rem;">ALS</p>
  <p style="margin-top:2.5rem;"><a href="/tinta-ciones/de-cimitas/" class="btn">Volver a De-Cimitas</a></p>

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

<script src="/app.js?v=9" defer></script>
</body>
</html>
"""
    destino = os.path.join(RAIZ, "tinta-ciones", "sonata-de-la-lluvia", "index.html")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8", newline="") as f:
        f.write(pagina)
    versos = sum(len([l for l in m["versos"] if l.strip()]) for m in movs)
    print(f"escrito: tinta-ciones/sonata-de-la-lluvia/ · 3 movimientos, {versos} versos")


if __name__ == "__main__":
    main()
