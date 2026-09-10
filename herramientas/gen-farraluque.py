# Genera las dos obras del XXX Premio Farraluque de Literatura Erotica, 2026:
# el poemario premiado y el cuento que obtuvo mencion.
#
#   /laureles/tres-delirios-y-un-desnudo/   Primer Premio en Poesia
#   /laureles/revelaciones/                 Mencion en Cuento
#
# Viven bajo /laureles/ y no en Tinta-ciones ni en Contarte a proposito. Son
# literatura erotica adulta, y Contarte tiene cuentos infantiles en una rejilla
# que ademas se baraja cada dia: no se pone lo uno junto a lo otro por azar.
# Ambas paginas llevan <meta name="rating" content="adult">, que es la senal
# que los buscadores entienden, y un aviso visible antes del texto.
#
# Dos cosas del original que no se tocan:
#   - "Revelaciones" esta escrito de un tiron, en un solo parrafo de 15.400
#     caracteres. No se le inventan puntos y aparte: si algun dia hay que
#     partirlo, lo parte el autor.
#   - El poema no trae lineas en blanco, pero cada seccion son 40 versos
#     exactos, o sea cuatro decimas. Se agrupan de diez en diez, que es la
#     forma de la decima, no una edicion del texto.
#
# Uso: python herramientas/gen-farraluque.py

import json, os, sys, html, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=22"
RETRATO = "/img/retrato.webp"
PREMIO = "XXX Premio Farraluque de Literatura Erótica, 2026"

AVISO = ("Obra de literatura erótica, escrita para lectores adultos.")


def esc(t):
    return html.escape(t, quote=False)


def lee(nombre):
    ruta = os.path.join(RAIZ, "herramientas", "textos", "laureles", nombre)
    return open(ruta, encoding="utf-8").read().replace("\r", "").split("\n")


def sin_cabecera(lineas, titulo):
    """Quita la portadilla del concurso (premio, seudonimo, obra repetida) y
    la raya que el autor pone al final del manuscrito."""
    i = max(j for j, l in enumerate(lineas) if l.strip().upper() == titulo.upper())
    resto = lineas[i + 1:]
    while resto and not resto[0].strip():
        resto.pop(0)
    while resto and not resto[-1].strip():
        resto.pop()
    if resto and resto[-1].strip() in ("-", "–", "—"):
        resto.pop()
    while resto and not resto[-1].strip():
        resto.pop()
    return resto


def delirios():
    """Las tres partes del triptico. El subtitulo unas veces viene entre
    parentesis en la misma linea y otras en la siguiente."""
    ls = lee("tres-delirios-y-un-desnudo.txt")
    subtitulo = next(l.strip().strip("()") for l in ls if l.startswith("(ÓLEO"))
    ls = sin_cabecera(ls, "(ÓLEO EN RIMAS SOBRE PIEL)")
    marca = re.compile(r"^(PRIMER|SEGUNDO|TERCER) DELIRIO\s*(\(.*\))?$")
    cortes = [i for i, l in enumerate(ls) if marca.match(l.strip())]
    partes = []
    for k, i in enumerate(cortes):
        fin = cortes[k + 1] if k + 1 < len(cortes) else len(ls)
        m = marca.match(ls[i].strip())
        nombre, entre = m.group(1), m.group(2)
        cuerpo = ls[i + 1:fin]
        if entre is None:                       # el tercero lo trae debajo
            entre = cuerpo[0].strip()
            cuerpo = cuerpo[1:]
        versos = [l for l in cuerpo if l.strip()]
        assert len(versos) % 10 == 0, f"{nombre}: {len(versos)} versos, no son decimas"
        decimas = [versos[j:j + 10] for j in range(0, len(versos), 10)]
        partes.append({"nombre": f"{nombre.capitalize()} delirio",
                       "sub": entre.strip("()").capitalize(),
                       "decimas": decimas})
    return subtitulo.capitalize(), partes


def envoltura(titulo, subtitulo, T, D, datos, migas, cuerpo, tipo="article"):
    pasos = "".join(
        f'\n    {{ "@type": "ListItem", "position": {i}, "name": "{n}", "item": "{u}" }},'
        for i, (n, u) in enumerate(migas, 1)).rstrip(",")
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{T}</title>
<meta name="description" content="{D}">
<meta name="rating" content="adult">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="canonical" href="{datos['url']}">
<meta property="og:type" content="{tipo}">
<meta property="og:url" content="{datos['url']}">
<meta property="og:title" content="{T}">
<meta property="og:description" content="{D}">
<meta property="og:image" content="{DOMINIO}{RETRATO}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{T}">
<meta name="twitter:description" content="{D}">
<meta name="twitter:image" content="{DOMINIO}{RETRATO}">
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
  "itemListElement": [{pasos}
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
{navegacion.menu_html("/laureles/")}
  </ul>
</nav>

<header class="page-header">
  <h1>{esc(titulo)}</h1>
  <p>{esc(subtitulo)}</p>
</header>

<main id="main">
<div class="section cuento">

{cuerpo}

  <p class="vyv-firma" style="margin-top:2.5rem;">ALS</p>
  <p style="margin-top:2.5rem;"><a href="/laureles/" class="btn">Volver a Laureles</a></p>

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


def escribe(carpeta, pagina, resumen):
    destino = os.path.join(RAIZ, "laureles", carpeta, "index.html")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8", newline="") as f:
        f.write(pagina)
    print(f"escrito: laureles/{carpeta}/ · {resumen}")


def poema():
    url = f"{DOMINIO}/laureles/tres-delirios-y-un-desnudo/"
    subtitulo, partes = delirios()
    piezas = [f'  <p class="sonata-premio reveal reveal-left">{esc(AVISO)} '
              f'Con ella gané el Primer Premio en Poesía del '
              f'<a href="/laureles/">{esc(PREMIO)}</a>.</p>']
    for n, p in enumerate(partes):
        lado = "right" if n % 2 == 0 else "left"
        ident = p["nombre"].lower().replace(" ", "-")
        piezas.append(
            f'  <section class="mov reveal reveal-{lado}" id="{ident}">\n'
            f'    <p class="mov-numero">{esc(p["nombre"])}</p>\n'
            f'    <h2 class="mov-titulo">{esc(p["sub"])}</h2>\n'
            + "\n".join(f'    <div class="verso poema-cuerpo decima">'
                        + "\n".join(esc(v) for v in d) + '</div>' for d in p["decimas"])
            + '\n  </section>')

    T = "Tres delirios y un desnudo, de Antonio López Sánchez"
    D = ("Tres delirios y un desnudo, de Antonio López Sánchez: tríptico en décimas, "
         "Primer Premio de Poesía del XXX Premio Farraluque, 2026.")
    datos = {"@context": "https://schema.org", "@type": "CreativeWork",
             "name": "Tres delirios y un desnudo", "url": url, "inLanguage": "es",
             "author": {"@id": f"{DOMINIO}/#antonio"},
             "genre": "Poesía. Décima. Literatura erótica",
             "datePublished": "2026",
             "isFamilyFriendly": False,
             "award": f"Primer Premio en Poesía, {PREMIO}",
             "description": D,
             "hasPart": [{"@type": "CreativeWork", "genre": "Décima",
                          "name": p["sub"], "position": i}
                         for i, p in enumerate(partes, 1)]}
    migas = [("Ala del Mar", DOMINIO + "/"), ("Laureles", DOMINIO + "/laureles/"),
             ("Tres delirios y un desnudo", url)]
    escribe("tres-delirios-y-un-desnudo",
            envoltura("Tres delirios y un desnudo", subtitulo + ".", T, D, datos,
                      migas, "\n\n".join(piezas)),
            f"{len(partes)} delirios, {sum(len(p['decimas']) for p in partes)} décimas")


def cuento():
    url = f"{DOMINIO}/laureles/revelaciones/"
    ls = sin_cabecera(lee("revelaciones.txt"), "REVELACIONES")
    epi = [l.strip() for l in ls[:2]]
    firma = ls[2].strip()
    assert firma == "Silvio Rodríguez", f"esperaba la firma del epigrafe, vino: {firma}"
    parrafos = [l.strip() for l in ls[3:] if l.strip()]

    cuerpo = (f'  <p class="sonata-premio reveal reveal-left">{esc(AVISO)} '
              f'Obtuvo Mención en Cuento en el '
              f'<a href="/laureles/">{esc(PREMIO)}</a>.</p>\n\n'
              '  <blockquote class="poema-epigrafe reveal reveal-right">\n'
              '    <div class="verso">' + "\n".join(esc(l) for l in epi) + '</div>\n'
              f'    <cite>{esc(firma)}</cite>\n'
              '  </blockquote>\n\n'
              '  <div class="cuento-texto reveal reveal-right">\n'
              + "\n".join(f"    <p>{esc(p)}</p>" for p in parrafos)
              + '\n  </div>')

    T = "Revelaciones, un cuento de Antonio López Sánchez"
    D = ("Revelaciones, cuento de Antonio López Sánchez: una mujer falta a misa "
         "para acudir a una cita. Mención en el XXX Premio Farraluque, 2026.")
    datos = {"@context": "https://schema.org", "@type": "ShortStory",
             "name": "Revelaciones", "url": url, "inLanguage": "es",
             "author": {"@id": f"{DOMINIO}/#antonio"},
             "genre": "Literatura erótica",
             "datePublished": "2026",
             "isFamilyFriendly": False,
             "award": f"Mención en Cuento, {PREMIO}",
             "description": D,
             "wordCount": sum(len(p.split()) for p in parrafos)}
    migas = [("Ala del Mar", DOMINIO + "/"), ("Laureles", DOMINIO + "/laureles/"),
             ("Revelaciones", url)]
    escribe("revelaciones",
            envoltura("Revelaciones", "Un domingo, y una decisión ya tomada.",
                      T, D, datos, migas, cuerpo),
            f"{len(parrafos)} párrafo(s), {datos['wordCount']} palabras")


if __name__ == "__main__":
    poema()
    cuento()
