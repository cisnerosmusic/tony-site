# Generador de paginas de libro para antoniolopezsanchez.art
# Lee un manifiesto JSON y los textos entregados por el autor, y emite
# /libros/<slug>/index.html como HTML estatico del sistema de diseno.
#
# Idiomas. La pagina española sale del manifiesto tal cual, identica a como
# salia antes de que hubiera idiomas. Cada idioma mas sale de una capa,
# herramientas/libros/<idioma>/<slug>.json, que trae solo lo traducible; todo
# lo demas se hereda del manifiesto: cubierta, año, enlaces, imagenes y, sobre
# todo, los fragmentos.
#
# Los fragmentos no se traducen nunca, y no es una norma que haya que
# recordar: la capa no tiene donde ponerlos. En las paginas que no son
# españolas salen con lang="es", que es lo correcto para quien usa lector de
# pantalla, y con un aviso que dice por que estan en español.
#
# Si a una capa le falta algo, el generador se para y dice que falta. Una
# pagina a medias entre dos idiomas es peor que no tenerla.
#
# Los textos de interfaz de cada idioma viven en herramientas/idiomas.json.
#
# Uso:
#   python herramientas/gen-libro.py herramientas/libros/<slug>.json
#       escribe la pagina española y la de cada idioma que tenga capa
#   python herramientas/gen-libro.py --catalogos
#       escribe el catalogo de cada idioma distinto del español
#       (/libros/ se sigue manteniendo a mano)

import json, os, sys, html
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion   # menu y pie: una sola definicion para todo el sitio

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=22"

# Toda gestion de derechos fuera de Cuba pasa por Ernesto Cisneros. Dos destinos
# fijos y ningun otro: decision del autor, 8 de septiembre de 2026. Una pagina
# que declara derechos disponibles y no dice a donde escribir es una fuga
# (regla de PRODUCT.md). El correo es el mismo en todos los idiomas; la pagina
# de representacion va en el idioma de quien lee, y esta en idiomas.json.
DERECHOS_EMAIL = "derechos@antoniolopezsanchez.art"

# Archivos reales, no data URI: Google solo indexa favicons que puede rastrear aparte.
FAVICON = ('<link rel="icon" href="/favicon.ico" sizes="any">\n'
           '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
           '<link rel="apple-touch-icon" href="/apple-touch-icon.png">')

IDIOMAS = json.load(open(os.path.join(RAIZ, "herramientas", "idiomas.json"), encoding="utf-8"))
LENGUAS = [k for k in IDIOMAS if not k.startswith("_")]

# Datos de la ficha que pueden pasar sin traducir: son un numero y un nombre.
INVARIABLES = {"año", "editorial"}


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


def ruta_libro(lang, slug):
    return IDIOMAS[lang]["ruta_libros"] + slug + "/"


def capa(slug, lang):
    """Lo traducido de un libro a un idioma. El español no tiene capa: es el
    manifiesto. Devuelve None si ese libro aun no esta en ese idioma."""
    if lang == "es":
        return {}
    ruta = os.path.join(RAIZ, "herramientas", "libros", lang, slug + ".json")
    if not os.path.exists(ruta):
        return None
    return json.load(open(ruta, encoding="utf-8"))


def validar(m, o, lang):
    """Se para si la capa no cubre todo lo que el manifiesto dice en español."""
    falta = []
    for k in ("tira_sub", "seo_titulo", "seo_desc", "cubierta_alt", "genero"):
        if not o.get(k):
            falta.append(k)
    for k in ("contratapa", "vyv", "contratapa_titulo", "volumenes_titulo", "descarga"):
        if m.get(k) and not o.get(k):
            falta.append(k)
    if len(o.get("premios", [])) != len(m.get("premios", [])):
        falta.append("premios")
    for k in m["ficha"]:
        if k not in INVARIABLES and k not in o.get("ficha", {}):
            falta.append(f"ficha.{k}")
    for k in o.get("ficha", {}):
        if k not in m["ficha"]:
            falta.append(f"ficha.{k} (no existe en el manifiesto)")
    for k in ("galeria", "volumenes", "prensa", "lecturas"):
        if len(o.get(k, [])) != len(m.get(k, [])):
            falta.append(f"{k} ({len(o.get(k, []))} de {len(m.get(k, []))})")
    if "catalogo" in IDIOMAS[lang] and not o.get("catalogo", {}).get("sinopsis"):
        falta.append("catalogo.sinopsis")
    if falta:
        sys.exit(f"capa {lang}/{m['slug']}.json incompleta. Falta: " + ", ".join(falta))


def seccion_del_libro(lang, slug):
    """En que seccion del menu cae un libro, segun el catalogo de ese idioma."""
    for g in IDIOMAS[lang].get("catalogo", {}).get("grupos", []):
        if slug in g["libros"]:
            return g.get("seccion")
    return None


def alternos(slug, disponibles):
    """hreflang reciproco entre todas las versiones de un libro, y x-default al
    español. Solo sale si hay mas de un idioma: una pagina sola no tiene pareja."""
    if len(disponibles) < 2:
        return ""
    t = "".join(f'\n<link rel="alternate" hreflang="{l}" href="{DOMINIO}{ruta_libro(l, slug)}">'
                for l in disponibles)
    return t + f'\n<link rel="alternate" hreflang="x-default" href="{DOMINIO}{ruta_libro("es", slug)}">'


def pie_pagina(L):
    return f"""<footer class="footer">
  <nav class="footer-nav" aria-label="{L["secciones_aria"]}">
{{pie}}
  </nav>
  <div class="footer-socials">
    <a href="https://www.facebook.com/profile.php?id=100071950279104" target="_blank" rel="noopener" aria-label="{L["facebook_aria"]}"><svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16" aria-hidden="true"><path d="M13.5 22v-8.1h2.72l.41-3.16H13.5V8.72c0-.91.25-1.53 1.56-1.53h1.67V4.36c-.29-.04-1.28-.12-2.43-.12-2.4 0-4.05 1.47-4.05 4.16v2.34H7.53v3.16h2.72V22h3.25z"/></svg></a>
  </div>
  <p class="footer-lema">bene scriptus</p>
  <p class="footer-copy">&copy; 2026 Antonio López Sánchez · Ala del Mar</p>
  <p class="footer-copy">{L["desarrollado"]} <a href="https://index01.net" target="_blank" rel="noopener">Index01</a></p>
</footer>"""


def generar_idioma(m, lang, disponibles):
    L = IDIOMAS[lang]
    es = lang == "es"
    o = capa(m["slug"], lang)
    if not es:
        validar(m, o, lang)

    def T(k, defecto=None):
        """Lo que se lee: del manifiesto en español, de la capa en los demas."""
        return m.get(k, defecto) if es else o.get(k, defecto)

    # Lo que esta en español dentro de una pagina que no lo esta se marca.
    la = "" if es else ' lang="es"'

    slug, titulo = m["slug"], m["titulo"]
    url = DOMINIO + ruta_libro(lang, slug)
    cw, ch = dims(m["cubierta"])

    contratapa = prosa_a_html(leer(T("contratapa"))) if m.get("contratapa") else ""
    vyv = prosa_a_html(leer(T("vyv"))) if m.get("vyv") else ""

    frags = []
    for f in m.get("fragmentos", []):
        cuerpo = leer(f["archivo"])
        if f["tipo"] == "verso":
            frags.append(f'<h3 class="fragmento-titulo"{la}>{esc(f["titulo"])}</h3>\n<div class="fragmento-verso"{la}>{esc(cuerpo)}</div>')
        else:
            # quita las dos primeras lineas si son numero de capitulo y titulo repetido
            lineas = cuerpo.split("\n")
            while lineas and (lineas[0].strip().isupper() or lineas[0].strip().rstrip("IVXLC.").strip() == "" ) and len(lineas[0].strip()) < 60:
                lineas.pop(0)
            frags.append(f'<h3 class="fragmento-titulo"{la}>{esc(f["titulo"])}</h3>\n<div class="fragmento"{la}>{prosa_a_html(chr(10).join(lineas))}</div>')
    fragmentos = "\n".join(frags)
    if fragmentos and L["aviso_fragmentos"]:
        fragmentos = f'<p class="nota-demo">{esc(L["aviso_fragmentos"])}</p>\n' + fragmentos

    ficha_items = dict(m["ficha"]) if es else {
        k: o.get("ficha", {}).get(k, v) for k, v in m["ficha"].items()}
    # Señal editorial discreta: derechos mundiales disponibles fuera de Cuba,
    # salvo que el manifiesto la apague o la reemplace.
    #
    # En los volumenes colectivos la frase cambia, y es importante que cambie:
    # Antonio solo puede ceder lo suyo. Se detecta por el campo "autoria" de la
    # ficha, que es justo el que aparece cuando el libro no es solo de el, asi
    # que no hace falta marcarlo a mano ni puede olvidarse al añadir un titulo.
    colectiva = any(k.lower().startswith("autor") for k in m["ficha"])
    if m.get("derechos", True):
        ficha_items.setdefault("derechos", L["derechos_colectiva"] if colectiva else L["derechos"])
    salida_derechos = (f'<a href="{L["representacion"]}">{L["consulta_derechos"]}</a> '
                       f'· <a href="mailto:{DERECHOS_EMAIL}">{DERECHOS_EMAIL}</a>')
    filas = []
    for k, v in ficha_items.items():
        etiqueta = L["ficha_claves"].get(k, k)
        # La fila de derechos nunca sale sin su via de contacto.
        if k == "derechos":
            filas.append(f'<div><dt>{esc(etiqueta)}</dt>'
                         f'<dd>{esc(v).rstrip(".")}. {salida_derechos}</dd></div>')
        else:
            filas.append(f'<div><dt>{esc(etiqueta)}</dt><dd>{esc(v)}</dd></div>')
    ficha = "\n".join(filas)

    # Volumenes: para las obras que salieron como juego de varios tomos, cada
    # portada con su titulo y la linea que el autor le puso. El titulo de cada
    # tomo no se traduce; su pie y su texto alternativo, si.
    volumenes = ""
    for i, v in enumerate(m.get("volumenes", [])):
        tv = v if es else {**v, **o["volumenes"][i]}
        vw, vh = dims(v["img"])
        volumenes += (f'<figure><img src="{v["img"]}" width="{vw}" height="{vh}" alt="{esc_attr(tv["alt"])}" loading="lazy">'
                      f'<figcaption><strong{la}>{esc(v["titulo"])}</strong><br>{esc(tv["pie"])}</figcaption></figure>\n')

    galeria = ""
    for i, g in enumerate(m.get("galeria", [])):
        tg = g if es else {**g, **o["galeria"][i]}
        gw, gh = dims(g["img"])
        galeria += f'<figure><img src="{g["img"]}" width="{gw}" height="{gh}" alt="{esc_attr(tg["alt"])}" loading="lazy"><figcaption>{esc(tg["pie"])}</figcaption></figure>\n'

    # Prensa: cada entrada puede ser texto suelto o una ficha con enlace. Ademas de
    # la lista visible, los articulos con URL se declaran como subjectOf del libro en
    # el JSON-LD, que es la propiedad correcta para un texto que habla de la obra;
    # sameAs queda reservado a la identidad del libro mismo. El titular del
    # articulo es el que le puso el medio y no se traduce.
    prensa_items, subjectof = [], []
    for i, p in enumerate(m.get("prensa", [])):
        tp = p if es else o["prensa"][i]
        if isinstance(p, str):
            prensa_items.append(f"<li>{esc(tp)}</li>")
            continue
        cabeza = (f'<a href="{p["url"]}" target="_blank" rel="noopener"{la}>{esc(p["titulo"])}</a>'
                  if p.get("url") else f'<strong{la}>{esc(p["titulo"])}</strong>')
        pie = f' <span class="meta">· {esc(tp["pie"])}</span>' if p.get("pie") else ""
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
        td = d if es else {**d, **o["descarga"]}
        salidas.append((d["url"], td["texto"], td.get("pie"), True))
    for i, l in enumerate(m.get("lecturas", [])):
        tl = l if es else {**l, **o["lecturas"][i]}
        salidas.append((l["url"], tl["texto"], tl.get("pie"), False))
    descarga_html = ""
    if salidas:
        botones = "".join(
            f'    <a href="{u}"{" target=\"_blank\" rel=\"noopener\"" if fuera else ""} class="btn btn-filled">{esc(txt)}</a>\n'
            + (f'    <span class="meta">{esc(pie_b)}</span>\n' if pie_b else "")
            for u, txt, pie_b, fuera in salidas)
        descarga_html = '\n  <p class="descarga reveal reveal-left">\n' + botones + '  </p>\n'

    # Una pagina de libro cuelga del catalogo pero no ES el catalogo: el menu la
    # marca activa y el pie no marca ninguna pagina como actual.
    activa = "/libros/" if es else seccion_del_libro(lang, slug)
    menu_html = navegacion.menu_de(lang, activa)
    nav_html = navegacion.pie_de(lang, None)

    premios_jsonld = json.dumps(T("premios", []), ensure_ascii=False)
    # sameAs ata esta ficha al mismo libro en fuentes externas verificadas, para que
    # los buscadores no lo confundan con obras homonimas de otros autores.
    referencias = m.get("referencias", [])
    sameas_jsonld = (',\n  "sameAs": ' + json.dumps(referencias, ensure_ascii=False)) if referencias else ""
    if es:
        seo_titulo = m.get("seo_titulo") or (titulo + L["titulo_sufijo"])
        seo_desc = m.get("seo_desc") or m["descripcion"][:155]
    else:
        seo_titulo, seo_desc = o["seo_titulo"], o["seo_desc"]
    locale = f'<meta property="og:locale" content="{L["locale"]}">'
    if not es:
        locale += '\n<meta property="og:locale:alternate" content="es_ES">'

    def bloque(id_, titulo_b, cuerpo, lado):
        if not cuerpo.strip():
            return ""
        return (f'  <section class="libro-bloque reveal reveal-{lado}" aria-labelledby="b-{id_}">\n'
                f'    <h2 id="b-{id_}">{titulo_b}</h2>\n'
                f'    <div class="section-divider"></div>\n{cuerpo}\n  </section>\n\n')

    B = L["bloques"]
    piezas = [
        ("contratapa", T("contratapa_titulo", B["contratapa"]), contratapa),
        ("volumenes", T("volumenes_titulo", B["volumenes"]),
         f'    <div class="galeria">\n{volumenes}    </div>' if volumenes else ""),
        ("vyv", B["vyv"], (vyv + '\n    <p class="vyv-firma">ALS</p>') if vyv else ""),
        ("fragmentos", B["fragmentos"], fragmentos),
        ("presentaciones", B["presentaciones"], f'    <div class="galeria">\n{galeria}    </div>' if galeria else ""),
        ("prensa", B["prensa"], f'    <ul class="lista-obras">\n{prensa}\n    </ul>' if prensa else ""),
        ("ficha", B["ficha"], f'    <dl class="ficha">\n{ficha}\n    </dl>'),
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
<html lang="{L["lang"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(seo_titulo)}</title>
<meta name="description" content="{esc_attr(seo_desc)}">
{FAVICON}
<link rel="canonical" href="{url}">{alternos(slug, disponibles)}
<meta property="og:type" content="book">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc_attr(seo_titulo)}">
<meta property="og:description" content="{esc_attr(seo_desc)}">
<meta property="og:image" content="{DOMINIO}{m["cubierta"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc_attr(seo_titulo)}">
<meta name="twitter:description" content="{esc_attr(seo_desc)}">
<meta name="twitter:image" content="{DOMINIO}{m["cubierta"]}">
{locale}
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Book",
  "name": {json.dumps(titulo, ensure_ascii=False)},
  "author": {{ "@type": "Person", "name": "Antonio López Sánchez", "url": "{DOMINIO}/" }},
  "datePublished": "{m["anio"]}",
  "publisher": {{ "@type": "Organization", "name": {json.dumps(m["editorial"], ensure_ascii=False)} }},
  "inLanguage": "es",
  "genre": {json.dumps(T("genero"), ensure_ascii=False)},
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
    {{ "@type": "ListItem", "position": 1, "name": "Ala del Mar", "item": "{DOMINIO}{L["portada"]}" }},
    {{ "@type": "ListItem", "position": 2, "name": "{L["catalogo_nombre"]}", "item": "{DOMINIO}{L["ruta_libros"]}" }},
    {{ "@type": "ListItem", "position": 3, "name": {json.dumps(titulo, ensure_ascii=False)}, "item": "{url}" }}
  ]
}}
</script>
<meta name="theme-color" content="#0a0c1f">
<link rel="preload" href="/fonts/cinzel-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts.css?v=5">
<link rel="stylesheet" href="/styles.css{CSS}">
</head>
<body>

<a class="salto" href="#main">{L["saltar"]}</a>

<nav class="nav">
  <a href="{L["portada"]}" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" type="button" aria-label="{L["abrir_menu"]}" aria-expanded="false" aria-controls="menu-principal">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links" id="menu-principal">
{menu_html}
  </ul>
</nav>

<header class="page-header">
  <h1{la}>{esc(titulo)}</h1>
  <p>{esc(T("tira_sub"))}</p>
</header>

<main id="main">
<div class="section libro-pagina">

  <figure class="cubierta-dominante reveal reveal-right">
    <img src="{m["cubierta"]}" width="{cw}" height="{ch}" alt="{esc_attr(T("cubierta_alt"))}">
  </figure>
{descarga_html}
{bloques}  <p style="margin-top:2rem;"><a href="{L["ruta_libros"]}" class="btn">{L["volver"]}</a></p>

</div>
</main>

{pie_pagina(L).replace("{pie}", nav_html)}

<script src="/app.js?v=8" defer></script>
</body>
</html>
"""
    destino = os.path.join(RAIZ, ruta_libro(lang, slug).strip("/").replace("/", os.sep), "index.html")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(pagina)
    print("escrito:", destino)


def generar(manifiesto):
    m = json.load(open(manifiesto, encoding="utf-8"))
    disponibles = [l for l in LENGUAS if capa(m["slug"], l) is not None]
    for lang in disponibles:
        generar_idioma(m, lang, disponibles)


def catalogos():
    """El catalogo de cada idioma que no es el español. Sale de las mismas
    capas que las paginas de libro, asi que no puede contradecirlas, y en el
    orden que ese idioma declara en idiomas.json, que no es el español."""
    manifiestos = {}
    for f in os.listdir(os.path.join(RAIZ, "herramientas", "libros")):
        if f.endswith(".json"):
            m = json.load(open(os.path.join(RAIZ, "herramientas", "libros", f), encoding="utf-8"))
            manifiestos[m["slug"]] = m

    for lang in LENGUAS:
        if lang == "es" or "catalogo" not in IDIOMAS[lang]:
            continue
        L, C = IDIOMAS[lang], IDIOMAS[lang]["catalogo"]
        listados = [s for g in C["grupos"] for s in g["libros"]]
        sin_capa = [s for s in listados if capa(s, lang) is None]
        if sin_capa:
            sys.exit(f"catalogo {lang}: faltan capas de " + ", ".join(sin_capa))
        sueltos = set(manifiestos) - set(listados)
        if sueltos:
            sys.exit(f"catalogo {lang}: libros sin grupo: " + ", ".join(sorted(sueltos)))

        url = DOMINIO + L["ruta_libros"]
        secciones = []
        for n, g in enumerate(C["grupos"]):
            items = []
            for slug in g["libros"]:
                m, o = manifiestos[slug], capa(slug, lang)
                c = o["catalogo"]
                cw, ch = dims(m["cubierta"])
                enlace = ruta_libro(lang, slug)
                glosa = f' <span class="libro-meta">({esc(c["glosa"])})</span>' if c.get("glosa") else ""
                meta = f'{esc(m["editorial"])} · {esc(m["anio"])}'
                if c.get("premio"):
                    meta += f' · <span class="premio">{esc(c["premio"])}</span>'
                items.append(f"""  <article class="libro-item reveal reveal-right">
    <a class="libro-cubierta" href="{enlace}">
      <img src="{m["cubierta"]}" width="{cw}" height="{ch}" alt="{esc_attr(o["cubierta_alt"])}" loading="lazy">
    </a>
    <div>
      <h3 class="libro-titulo"><a href="{enlace}" lang="es">{esc(m["titulo"])}</a>{glosa}</h3>
      <p class="libro-meta">{meta}</p>
      <p class="libro-sinopsis">{esc(c["sinopsis"])}</p>
      <p style="margin-top:1.2rem;"><a href="{enlace}" class="btn">{esc(C["ver"])}</a></p>
    </div>
  </article>""")
            texto = f'\n    <p class="section-text" style="margin-bottom:1.5rem;">{esc(g["texto"])}</p>' if g.get("texto") else ""
            cuerpo = (f'<div class="section">\n  <div class="reveal reveal-{"right" if n % 2 == 0 else "left"}">\n'
                      f'    <h2 class="section-title">{esc(g["titulo"])}</h2>\n'
                      f'    <div class="section-divider"></div>{texto}\n  </div>\n\n'
                      + "\n\n".join(items) + "\n</div>")
            if n % 2:
                cuerpo = '<div class="section-alt">\n' + cuerpo + '\n</div>'
            secciones.append(cuerpo)

        cierre = ""
        if C.get("cierre"):
            k = C["cierre"]
            cierre = f"""

<div class="section-alt">
<div class="section">
  <div class="reveal reveal-right">
    <h2 class="section-title">{esc(k["titulo"])}</h2>
    <div class="section-divider"></div>
    <p class="section-text" style="margin-bottom:2rem;">{esc(k["texto"])}</p>
    <div style="display:flex;flex-wrap:wrap;gap:1rem;">
      <a href="mailto:{DERECHOS_EMAIL}" class="btn btn-filled">{esc(k["boton_correo"])}</a>
      <a href="{L["representacion"]}" target="_blank" rel="noopener" class="btn">{esc(k["boton_representacion"])}</a>
    </div>
  </div>
</div>
</div>"""

        datos = {"@context": "https://schema.org", "@type": "CollectionPage",
                 "name": C["seo_titulo"], "description": C["seo_desc"], "url": url,
                 "inLanguage": L["lang"], "about": {"@id": f"{DOMINIO}/#antonio"},
                 "mainEntity": {"@type": "ItemList", "numberOfItems": len(listados),
                                "itemListElement": [
                                    {"@type": "ListItem", "position": i,
                                     "url": DOMINIO + ruta_libro(lang, s),
                                     "name": manifiestos[s]["titulo"]}
                                    for i, s in enumerate(listados, 1)]}}
        es_url = DOMINIO + IDIOMAS["es"]["ruta_libros"]
        pagina = f"""<!DOCTYPE html>
<html lang="{L["lang"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(C["seo_titulo"])}</title>
<meta name="description" content="{esc_attr(C["seo_desc"])}">
{FAVICON}
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es" href="{es_url}">
<link rel="alternate" hreflang="{L["lang"]}" href="{url}">
<link rel="alternate" hreflang="x-default" href="{es_url}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc_attr(C["seo_titulo"])}">
<meta property="og:description" content="{esc_attr(C["seo_desc"])}">
<meta property="og:image" content="{DOMINIO}/img/retrato.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc_attr(C["seo_titulo"])}">
<meta name="twitter:description" content="{esc_attr(C["seo_desc"])}">
<meta name="twitter:image" content="{DOMINIO}/img/retrato.webp">
<meta property="og:locale" content="{L["locale"]}">
<meta property="og:locale:alternate" content="es_ES">
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
    {{ "@type": "ListItem", "position": 1, "name": "Ala del Mar", "item": "{DOMINIO}{L["portada"]}" }},
    {{ "@type": "ListItem", "position": 2, "name": "{L["catalogo_nombre"]}", "item": "{url}" }}
  ]
}}
</script>
</head>
<body>

<a class="salto" href="#main">{L["saltar"]}</a>

<nav class="nav">
  <a href="{L["portada"]}" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" type="button" aria-label="{L["abrir_menu"]}" aria-expanded="false" aria-controls="menu-principal">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links" id="menu-principal">
{navegacion.menu_de(lang, None)}
  </ul>
</nav>

<header class="page-header">
  <h1>{esc(C["titulo"])}</h1>
  <p>{esc(C["subtitulo"])}</p>
</header>

<main id="main">

<div class="section">
  <div class="reveal reveal-right">
    <p class="section-text">{esc(C["intro"])}</p>
  </div>
</div>

{chr(10).join(chr(10) + s for s in secciones).lstrip(chr(10))}{cierre}

</main>

{pie_pagina(L).replace("{pie}", navegacion.pie_de(lang, None))}

<script src="/app.js?v=8" defer></script>
</body>
</html>
"""
        destino = os.path.join(RAIZ, L["ruta_libros"].strip("/").replace("/", os.sep), "index.html")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, "w", encoding="utf-8") as f:
            f.write(pagina)
        print(f"escrito: {L['ruta_libros']} · {len(listados)} libros en {len(C['grupos'])} grupos")


if __name__ == "__main__":
    if sys.argv[1:] == ["--catalogos"]:
        catalogos()
    else:
        generar(sys.argv[1])
