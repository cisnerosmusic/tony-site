# Genera /tinta-ciones/poemas-sueltos/ desde herramientas/poemas.json.
#
# Lo delicado aqui no es la maqueta, es la atribucion: ocho de estos poemas son
# glosas que abren con una estrofa de Jose Marti o de Lezama Lima. Esos versos
# NO son del autor. Salen en su propio bloque, con el nombre de quien los
# escribio debajo, para que nadie los lea como suyos.
#
# Uso: python herramientas/gen-poemas.py

import json, os, sys, html, unicodedata, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion
from importlib.machinery import SourceFileLoader
leer_poema = SourceFileLoader("leer_poema", os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "leer-poema.py")).load_module()

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
URL = DOMINIO + "/tinta-ciones/poemas-sueltos/"
CSS = "?v=17"


def esc(t):
    return html.escape(t, quote=False)


def ancla(titulo):
    t = unicodedata.normalize("NFKD", titulo.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]


def bloque(p, ficha, n):
    """Un poema: titulo, epigrafe ajeno si lo hay, versos, colofon y firma.
    El titulo viene del manifiesto, escrito a mano; del archivo solo salen los
    versos, que son lo que no se puede tocar."""
    principal = ficha["titulo"]
    numero = ficha.get("numero", "")
    serie = ficha.get("serie", "")
    id_ = ancla(principal)

    partes = [f'<article class="poema reveal reveal-{"right" if n % 2 == 0 else "left"}" id="{id_}">']
    if serie:
        partes.append(f'  <p class="poema-serie">{esc(serie)}</p>')
    partes.append(f'  <h2 class="poema-titulo">{esc(principal)}'
                  + (f' <span class="poema-numero">{esc(numero)}</span>' if numero else "")
                  + '</h2>')
    if p["epigrafe_autor"]:
        versos = "\n".join(esc(l) for l in p["epigrafe"])
        partes.append('  <blockquote class="poema-epigrafe">')
        partes.append(f'    <div class="verso">{versos}</div>')
        partes.append(f'    <cite>{esc(p["epigrafe_autor"])}</cite>')
        partes.append('  </blockquote>')
    cuerpo = "\n".join(esc(l) for l in p["cuerpo"]).strip("\n")
    partes.append(f'  <div class="verso poema-cuerpo">{cuerpo}</div>')
    if p["colofon"]:
        partes.append(f'  <p class="poema-colofon">{esc(" · ".join(p["colofon"]))}</p>')
    partes.append('  <p class="vyv-firma">ALS</p>')
    partes.append('</article>')
    return "\n".join(partes)


def main():
    cfg = json.load(open(os.path.join(RAIZ, "herramientas", "poemas.json"), encoding="utf-8"))
    carpeta = cfg["carpeta"]

    def carga(ficha):
        ruta = os.path.join(carpeta, ficha["archivo"] + ".txt")
        return leer_poema.partes(open(ruta, encoding="utf-8").read())

    sueltos = [(carga(f), f) for f in cfg["sueltos"]]
    glosas = [(carga(f), f) for f in cfg["glosas"]]

    cuerpo_sueltos = "\n\n".join(bloque(p, f, i) for i, (p, f) in enumerate(sueltos))
    cuerpo_glosas = "\n\n".join(bloque(p, f, i) for i, (p, f) in enumerate(glosas))

    titulos = [f["titulo"] for _, f in sueltos + glosas]
    lista = {"@context": "https://schema.org", "@type": "ItemList",
             "name": "Poemas sueltos de Antonio López Sánchez",
             "itemListElement": [
                 {"@type": "ListItem", "position": i, "name": t}
                 for i, t in enumerate(titulos, 1)]}

    T = "Poemas sueltos de Antonio López Sánchez"
    D = (f"{len(titulos)} poemas del poeta cubano Antonio López Sánchez, "
         "entre ellos ocho glosas sobre versos de José Martí y de Lezama Lima.")

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
<meta property="og:image" content="{DOMINIO}/img/retrato.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{T}">
<meta name="twitter:description" content="{D}">
<meta name="twitter:image" content="{DOMINIO}/img/retrato.webp">
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
    {{ "@type": "ListItem", "position": 3, "name": "Poemas sueltos", "item": "{URL}" }}
  ]
}}
</script>
{navegacion.menu_html("/tinta-ciones/").join(['''</head>
<body>

<a class="salto" href="#main">Saltar al contenido</a>

<nav class="nav">
  <a href="/" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" onclick="document.querySelector('.nav-links').classList.toggle('open')" aria-label="Menú">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links">
''', '''
  </ul>
</nav>
'''])}
<header class="page-header">
  <h1>Poemas sueltos</h1>
  <p>Versos que andan por su cuenta, fuera de todo libro.</p>
</header>

<main id="main">
<div class="section poemario">

{cuerpo_sueltos}

  <div class="reveal reveal-right" style="margin-top:4.5rem;">
    <h2 class="section-title">Glosas</h2>
    <div class="section-divider"></div>
    <p class="section-text" style="margin-bottom:3rem;">Glosar es tomar unos versos ajenos y contestarlos, verso a verso, hasta devolverlos al final. Los que abren cada una de estas décimas no son míos: son de José Martí y de José Lezama Lima, y van en su sitio, con su nombre.</p>
  </div>

{cuerpo_glosas}

</div>
</main>
{navegacion.pie_html(None).join(['''
<footer class="footer">
  <nav class="footer-nav" aria-label="Secciones">
''', '''
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
'''])}"""

    destino = os.path.join(RAIZ, "tinta-ciones", "poemas-sueltos", "index.html")
    with open(destino, "w", encoding="utf-8", newline="") as f:
        f.write(pagina)
    print(f"escrito: {os.path.relpath(destino, RAIZ)} · {len(sueltos)} poemas y {len(glosas)} glosas")


if __name__ == "__main__":
    main()
