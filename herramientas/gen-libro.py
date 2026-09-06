# Generador de paginas de libro para antoniolopezsanchez.art
# Lee un manifiesto JSON y los textos entregados por el autor, y emite
# /libros/<slug>/index.html como HTML estatico del sistema de diseno.
# Uso: python herramientas/gen-libro.py herramientas/libros/<slug>.json

import json, os, sys, html
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"

FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect x='4' y='2' width='24' height='28' fill='%23faf5e9'/%3E%3Crect x='4' y='2' width='24' height='28' fill='none' stroke='%23d9c8ab' stroke-width='1'/%3E%3Ctext x='16' y='23' text-anchor='middle' font-family='Georgia,serif' font-size='18' fill='%23262019'%3EA%3C/text%3E%3Crect x='19' y='4' width='7' height='7' fill='none' stroke='%231d4e89' stroke-width='1.5' transform='rotate(8 22.5 7.5)'/%3E%3C/svg%3E"

NAV = [("/", "Portada"), ("/libros/", "Mis libros"), ("/ineditos/", "Inéditos"),
       ("/tinta-ciones/", "Tinta-ciones"), ("/trova/", "La trova"),
       ("/plano-abierto/", "Plano abierto"), ("/periodista/", "El periodista"),
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
            frags.append(f'<h3 class="fragmento-titulo">{esc(f["titulo"])}</h3>\n<div class="fragmento-verso maquina">{esc(cuerpo)}</div>')
        else:
            # quita las dos primeras lineas si son numero de capitulo y titulo repetido
            lineas = cuerpo.split("\n")
            while lineas and (lineas[0].strip().isupper() or lineas[0].strip().rstrip("IVXLC.").strip() == "" ) and len(lineas[0].strip()) < 60:
                lineas.pop(0)
            frags.append(f'<h3 class="fragmento-titulo">{esc(f["titulo"])}</h3>\n<div class="fragmento">{prosa_a_html(chr(10).join(lineas))}</div>')
    fragmentos = "\n".join(frags)

    ficha = "\n".join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in m["ficha"].items())

    galeria = ""
    for g in m.get("galeria", []):
        gw, gh = dims(g["img"])
        galeria += f'<figure><img src="{g["img"]}" width="{gw}" height="{gh}" alt="{esc(g["alt"])}" loading="lazy"><figcaption>{esc(g["pie"])}</figcaption></figure>\n'

    prensa = "\n".join(f"<li>{esc(p)}</li>" for p in m.get("prensa", []))
    nav_html = "\n    ".join(
        f'<span aria-current="page">{n}</span>' if h == "/libros/" else f'<a href="{h}">{n}</a>'
        for h, n in NAV)

    premios_jsonld = json.dumps(m.get("premios", []), ensure_ascii=False)

    pagina = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(titulo)}, {esc(m["genero_frase"])} de Antonio López Sánchez</title>
<meta name="description" content="{esc(m["descripcion"])}">
<link rel="icon" href="{FAVICON}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="book">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(titulo)}, de Antonio López Sánchez">
<meta property="og:description" content="{esc(m["descripcion"])}">
<meta property="og:image" content="{DOMINIO}{m["cubierta"]}">
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
  "image": "{DOMINIO}{m["cubierta"]}"
}}
</script>
<link rel="preload" href="/fonts/bonum-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/courier-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/styles.css">
</head>
<body>

<a class="salto" href="#contenido">Saltar al contenido</a>

<div class="tira">
  <h1 id="contenido">{esc(titulo)}</h1>
  <p class="maquina">{esc(m["tira_sub"])}</p>
</div>

<main>
<article class="cuartilla">
  <p class="cabezal"><span>Ala del Mar · Mis libros · {esc(titulo)}</span></p>

  <figure class="cubierta-dominante">
    <img src="{m["cubierta"]}" width="{cw}" height="{ch}" alt="{esc(m["cubierta_alt"])}">
  </figure>

  <section class="bloque" aria-labelledby="b-contratapa">
    <h2 id="b-contratapa">Nota de contratapa</h2>
    <div class="contratapa">{contratapa}</div>
  </section>

  <section class="bloque" aria-labelledby="b-ficha">
    <h2 id="b-ficha">Ficha</h2>
    <dl class="ficha-libro">
{ficha}
    </dl>
  </section>

  <section class="bloque" aria-labelledby="b-fragmentos">
    <h2 id="b-fragmentos">Fragmentos</h2>
{fragmentos}
    <p class="nota-idioma">Los textos literarios se publican siempre en su idioma original, el español.</p>
  </section>

  <section class="bloque" aria-labelledby="b-presentaciones">
    <h2 id="b-presentaciones">Presentaciones</h2>
    <div class="galeria">
{galeria}
    </div>
  </section>

  <section class="bloque" aria-labelledby="b-prensa">
    <h2 id="b-prensa">Prensa</h2>
    <ul class="catalogo">
{prensa}
    </ul>
  </section>

  <section class="bloque" aria-labelledby="b-vyv">
    <h2 id="b-vyv">Con voz y voto</h2>
    <div class="vyv">
{vyv}
      <p class="vyv-firma">A. López Sánchez</p>
    </div>
  </section>

  <p class="volver"><a href="/libros/">Volver a Mis libros</a></p>

  <nav class="indice-pie maquina" aria-label="Navegación del manuscrito">
    {nav_html}
  </nav>
  <p class="fin maquina" aria-hidden="true">bene scriptus</p>
</article>
</main>

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
