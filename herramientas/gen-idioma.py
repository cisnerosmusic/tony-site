# Genera las paginas propias de un idioma extranjero, las que no salen de
# ninguna sala española: su portada, sus paginas de seccion y su concentrador.
# Hoy, en ingles:
#
#   /en/           portada
#   /en/trova/     la investigacion sobre la Nueva Trova
#   /en/poetry/    la poesia
#   /en/fiction/   novela y cuento
#   /en/author/    el concentrador de toda la obra
#
# /en/rights/ NO se genera aqui: la escribe gen-legal.py junto con la version
# española, para que el aviso de derechos no pueda decir dos cosas distintas.
#
# Se llamaba gen-ingles.py y leia ingles.json. Desde el 22 de septiembre de
# 2026 lee una zona por idioma, herramientas/zona.<idioma>.json, y todo lo que
# antes estaba escrito dentro (las parejas de hreflang, el orden de los grupos
# del catalogo, los rotulos, el alt de la banda de mar) es dato de esa zona.
# El plan son cinco idiomas: español, ingles, frances, italiano y portugues, y
# con el generador atado a uno solo el segundo se habria escrito tres veces.
#
# Añadir un idioma es, entonces: su bloque en idiomas.json, su menu en
# navegacion.py, su zona.<idioma>.json y las capas de cada sala. Ni una linea
# de codigo.
#
# La regla del sitio, que no se negocia: el aparato se traduce y la literatura
# se queda en español. Ni un poema traducido, en ningun idioma.
#
# El orden de las secciones no es el del sitio español y no es un descuido.
# Para el lector anglosajon la puerta de entrada es la investigacion sobre la
# trova, no la fantasia heroica. Lo decidio Ernesto el 9 de septiembre de 2026
# y esta razonado en PRODUCT.md. Cada idioma puede tener el suyo.
#
# No se inventa ni una clase de CSS: las fichas de libro y las tres puertas de
# la portada reutilizan .laurel-item, que ya es una rejilla de etiqueta dorada
# a la izquierda y contenido a la derecha.
#
# Uso: python herramientas/gen-idioma.py

import json, os, sys, html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion
# El marco comun se importa con alias porque aqui hay una funcion pagina().
import pagina as marco

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=38"
RETRATO = "/img/retrato.webp"


def esc(t):
    return html.escape(t, quote=False)


def esc_attr(t):
    return html.escape(t, quote=True)


def boton(e):
    """Un enlace de accion. 'relleno' lo pinta solido, 'externo' le pone el
    rel que exige abrir en otra pestaña."""
    clase = "btn btn-filled" if e.get("relleno") else "btn"
    extra = ' target="_blank" rel="noopener"' if e.get("externo") else ""
    idioma = f' lang="{e["lang"]}"' if e.get("lang") else ""
    return f'<a href="{esc_attr(e["url"])}" class="{clase}"{extra}{idioma}>{esc(e["texto"])}</a>'


def bloque_libro(l):
    """Ficha de un libro, con el año en la columna dorada."""
    titulo = f'<em>{esc(l["titulo"])}</em>'
    if l.get("glosa"):
        titulo += f' <span class="libro-meta">({esc(l["glosa"])})</span>'
    pie = " · ".join(x for x in (l.get("editorial"), l.get("genero")) if x)
    p = [f'  <article class="laurel-item reveal reveal-right">',
         f'    <p class="laurel-anio">{esc(l["anio"])}</p>',
         f'    <div>',
         f'      <h3 class="libro-titulo" lang="es">{titulo}</h3>',
         f'      <p class="libro-meta">{esc(pie)}</p>']
    if l.get("premio"):
        p.append(f'      <p class="libro-meta">{esc(l["premio"])}</p>')
    p.append(f'      <p class="section-text">{l["texto"]}</p>')
    if l.get("url"):
        p.append(f'      <p style="margin-top:1rem;"><a href="{esc_attr(l["url"])}" class="btn">{esc(L()["catalogo"]["ver"])}</a></p>')
    p += ['    </div>', '  </article>']
    return "\n".join(p)


def bloque_puerta(d):
    return ('  <article class="laurel-item reveal reveal-right">\n'
            f'    <p class="laurel-anio">{esc(d["numero"])}</p>\n'
            '    <div>\n'
            f'      <h3 class="libro-titulo"><a href="{esc_attr(d["url"])}">{esc(d["titulo"])}</a></h3>\n'
            f'      <p class="section-text">{d["texto"]}</p>\n'
            '    </div>\n'
            '  </article>')


def _manifiesto(*partes):
    with open(os.path.join(RAIZ, "herramientas", *partes), encoding="utf-8") as f:
        return json.load(f)


# Los textos de interfaz ingleses y, sobre todo, el catalogo con sus grupos:
# el concentrador se arma desde ahi, no desde una lista escrita aparte.
IDIOMAS = _manifiesto("idiomas.json")

# El idioma que se esta escribiendo y su zona. Los fija main() en cada pasada.
LANG = "en"
Z = {}

# Todas las zonas, y el indice de hermanas por ruta española. Con dos idiomas
# bastaba con emparejar cada pagina con su española; con tres o mas, la
# francesa tambien tiene que declararse hermana de la inglesa, o cada una le
# dice a los buscadores que la otra no existe. Lo fija main() antes de escribir.
ZONAS = {}
HERMANAS = {}
# Y las que no tienen equivalente español, agrupadas por el campo "hermana_de"
# de la pagina: son hermanas entre ellas y de nadie mas.
HERMANAS_SUELTAS = {}


def L():
    """Los textos de interfaz del idioma en curso."""
    return IDIOMAS[LANG]


def _portada():
    return navegacion.IDIOMAS[LANG]["portada"]


def fila_obra(url, titulo, meta="", linea="", espanol=True):
    """Una obra en el concentrador: titulo enlazado, etiqueta y, si la hay, una
    linea en ingles. Los titulos no se traducen nunca, asi que van marcados con
    lang=es aunque la pagina este en ingles."""
    la = ' lang="es"' if espanol else ""
    fila = (f'      <li>\n'
            f'        <strong{la}><a href="{esc_attr(url)}">{esc(titulo)}</a></strong>')
    if meta:
        fila += f' <span class="meta">{esc(meta)}</span>'
    if linea:
        fila += f'\n        <span class="obra-linea">{esc(linea)}</span>'
    return fila + '\n      </li>'


def lista_obras(filas, densa=False):
    clase = "lista-obras lista-obras-densa" if densa else "lista-obras"
    return f'    <ul class="{clase}">\n' + "\n".join(filas) + '\n    </ul>'


def rotulo(titulo, nota=""):
    p = [f'    <h3 class="obras-grupo">{esc(titulo)}</h3>']
    if nota:
        p.append(f'    <p class="obras-grupo-entrada">{esc(nota)}</p>')
    return "\n".join(p)


def obras_libros():
    """Los catorce libros, por generos y en el orden que pidio Ernesto el 22 de
    septiembre de 2026: primero la ficcion, despues los libros de entrevistas e
    investigacion, y al final poesia y volumenes colectivos."""
    grupos = {g["titulo"]: g for g in L()["catalogo"]["grupos"]}
    orden = Z["orden_libros"]
    faltan = set(grupos) - set(orden)
    if faltan:
        sys.exit(f"grupos del catalogo ingles sin sitio en el concentrador: {sorted(faltan)}")
    out = []
    for nombre in orden:
        g = grupos[nombre]
        out.append(rotulo(nombre, g.get("texto", "")))
        filas = []
        for slug in g["libros"]:
            m = _manifiesto("libros", slug + ".json")
            c = _manifiesto("libros", LANG, slug + ".json")
            glosa = c.get("catalogo", {}).get("glosa")
            titulo = m["titulo"] + (f" ({glosa})" if glosa else "")
            meta = " · ".join(x for x in (m.get("anio"), c.get("genero"), m.get("editorial")) if x)
            filas.append(fila_obra(L()["ruta_libros"] + slug + "/", titulo, meta))
        out.append(lista_obras(filas))
    return "\n".join(out)


def obras_periodismo():
    """Los veintidos trabajos de prensa. Solo tienen pagina española, asi que
    el enlace sale marcado: lo que se traduce es la linea, no el titular."""
    cfg = _manifiesto("periodismo.json")
    capa = _manifiesto(f"periodismo.{LANG}.json")
    out = []
    for g in cfg["grupos"]:
        suyos = [t for t in cfg["trabajos"] if t["grupo"] == g["clave"]]
        if not suyos:
            continue
        out.append(rotulo(capa["grupos"][g["clave"]]))
        filas = []
        for t in suyos:
            fecha = capa["fechas"].get(t.get("fecha", ""), t.get("fecha", ""))
            medio = capa["medios"].get(t.get("medio", ""), t.get("medio", ""))
            meta = " · ".join(x for x in (medio, fecha) if x)
            linea = capa["trabajos"].get(t["slug"])
            if not linea:
                sys.exit(f"periodismo.en.json sin línea para {t['slug']}")
            filas.append(fila_obra(f"/periodista/{t['slug']}/", t["titulo"], meta, linea))
        out.append(lista_obras(filas))
    return "\n".join(out)


def obras_cuentos():
    cuentos = _manifiesto("cuentos.json")
    capa = _manifiesto(f"cuentos.{LANG}.json")
    filas = []
    for c in cuentos:
        t = capa["cuentos"][c["slug"]]
        titulo = c["titulo"] + (f" ({t['significado']})" if t.get("significado") else "")
        filas.append(fila_obra(capa["ruta"] + c["slug"] + "/", titulo, "", t["linea"]))
    return lista_obras(filas)


def obras_poemas():
    """Poemas y glosas. No tienen pagina propia: viven todos en la sala, cada
    uno con su ancla, y el ancla la calcula pagina.py."""
    p = _manifiesto("poemas.json")
    capa = _manifiesto(f"poemas.{LANG}.json")
    out = []
    for clave in ("sueltos", "glosas"):
        nombre = Z["rotulos_poemas"][clave]
        out.append(rotulo(nombre, capa["glosas_texto"] if clave == "glosas" else ""))
        out.append(lista_obras([fila_obra(f'{capa["ruta"]}#{marco.ancla(x["titulo"])}', x["titulo"])
                                for x in p[clave]], densa=True))
    return "\n".join(out)


def obras_decimitas():
    cfg = _manifiesto("decimitas.json")
    capa = _manifiesto(f"decimitas.{LANG}.json")
    filas = [fila_obra(f'{capa["ruta"]}#{d["slug"]}', d["titulo"]) for d in cfg["decimitas"]]
    return lista_obras(filas, densa=True)


def obras_ineditos():
    cfg = _manifiesto("ineditos.json")
    capa = _manifiesto(f"ineditos.{LANG}.json")
    filas = []
    for n in cfg["novelas"]:
        t = capa["novelas"][n["slug"]]
        filas.append(fila_obra(capa["ruta"] + n["slug"] + "/", n["titulo"],
                               t.get("genero", ""), t.get("linea", "")))
    return lista_obras(filas)


def bloque_obras(clave):
    """Las listas del concentrador. Todas salen de los manifiestos que ya
    existen: si entra un libro, un cuento o un trabajo, aparece aqui solo.
    Escribirlas a mano en ingles.json seria tener el dato dos veces, y el
    segundo envejeceria sin que nadie lo notara."""
    hacer = {"libros": obras_libros, "periodismo": obras_periodismo,
             "cuentos": obras_cuentos, "poemas": obras_poemas,
             "decimitas": obras_decimitas, "ineditos": obras_ineditos}
    if clave not in hacer:
        sys.exit(f"tipo de obras desconocido: {clave}")
    return hacer[clave]()


def dims(rel):
    from PIL import Image
    with Image.open(os.path.join(RAIZ, rel.lstrip("/"))) as im:
        return im.size


def bloque_galeria(fotos):
    """Un album de fotos con su pie, como las galerias del sitio español."""
    filas = []
    for f in fotos:
        w, h = dims(f["img"])
        filas.append(f'    <figure><img src="{f["img"]}" width="{w}" height="{h}" alt="{esc_attr(f["alt"])}" '
                     f'loading="lazy"><figcaption>{esc(f["pie"])}</figcaption></figure>')
    return '  <div class="galeria reveal reveal-left">\n' + "\n".join(filas) + '\n  </div>'


def articulo_medio(titulo, meta, cuerpo, n):
    lado = "right" if n % 2 == 0 else "left"
    return (f'  <article class="audio-item reveal reveal-{lado}">\n'
            f'    <h3>{titulo}</h3>\n'
            f'    <p class="audio-meta">{meta}</p>\n'
            f'{cuerpo}'
            f'  </article>')


def reproductor(src, capa):
    return (f'    <audio controls preload="none" src="{src}">\n'
            f'      {capa["sin_audio"].format(src)}\n'
            f'    </audio>\n')


def bloque_medios(items, capa):
    """Grabaciones y videos escritos en la propia pagina: los de radio y
    television que en español viven a mano en Plano abierto."""
    salida = []
    for n, m in enumerate(items):
        la = f' lang="{m["lang"]}"' if m.get("lang") else ""
        titulo = f'<span{la}>{esc(m["titulo"])}</span>' if la else esc(m["titulo"])
        if m["tipo"] == "audio":
            cuerpo = reproductor(m["src"], capa)
        elif m["tipo"] == "video":
            cuerpo = (f'    <video controls preload="none" poster="{m["poster"]}" width="{m["ancho"]}" height="{m["alto"]}">\n'
                      f'      <source src="{m["src"]}" type="video/mp4">\n'
                      f'      {m["sin_video"].format(m["src"])}\n'
                      f'    </video>\n')
        else:
            cuerpo = f'    <p><a href="{m["url"]}" target="_blank" rel="noopener" class="btn">{esc(m["boton"])}</a></p>\n'
        salida.append(articulo_medio(titulo, esc(m["meta"]), cuerpo, n))
    return "\n\n".join(salida)


def bloque_grabaciones(sala, capa):
    """Las grabaciones de una sala, leidas de grabaciones.json, que es donde
    viven una sola vez; la capa inglesa trae solo sus textos. Como en
    español, la ficha larga va en la sala canonica y la otra remite a ella."""
    todas = json.load(open(os.path.join(RAIZ, "herramientas", "grabaciones.json"), encoding="utf-8"))
    salida = []
    for n, g in enumerate(x for x in todas if sala in x["salas"]):
        t = capa["grabaciones"][g["id"]]
        nombre = t.get("titulo", g["titulo"])
        titulo = esc(nombre) if "titulo" in t else f'<span lang="es">{esc(nombre)}</span>'
        if g.get("sin_titulo"):
            titulo = f'<em lang="es">{esc(g["titulo"])}…</em>'
        if g["canonica"] == sala:
            meta = esc(t["ficha"])
        else:
            c = capa["salas"][g["canonica"]]
            meta = f'{esc(t["frase"])} · <a href="{c["ruta"]}">{esc(capa["donde"].format(c["nombre"]))}</a>'
        salida.append(articulo_medio(titulo, meta, reproductor(g["archivo"], capa), n))
    return "\n\n".join(salida)


def seccion_html(s, n):
    lado = "right" if n % 2 == 0 else "left"
    dentro = [f'  <div class="reveal reveal-{lado}">',
              f'    <h2 class="section-title">{esc(s["titulo"])}</h2>',
              '    <div class="section-divider"></div>']
    # El ritmo de la portada española: 1,25 entre parrafos de un mismo bloque y
    # 2 antes de lo que cierra la seccion (firma, lista o botones). Poner 1,25 a
    # todos, que es lo que hacia esto al principio, aplana la pagina y le quita
    # la respiracion antes de cada fila de acciones.
    parrafos = s.get("parrafos", [])
    for i, p in enumerate(parrafos):
        margen = "2rem" if i == len(parrafos) - 1 else "1.25rem"
        dentro.append(f'    <p class="section-text" style="margin-bottom:{margen};">{p}</p>')
    if s.get("firma"):
        dentro.append(f'    <p class="vyv-firma">{esc(s["firma"])}</p>')
    if s.get("lista"):
        dentro.append('    <ul class="lista-obras">')
        for x in s["lista"]:
            dentro.append(f'      <li>{x}</li>')
        dentro.append('    </ul>')
    if s.get("obras"):
        dentro.append(bloque_obras(s["obras"]))
    if s.get("enlaces"):
        dentro.append('    <div style="display:flex;flex-wrap:wrap;gap:1rem;margin-top:1.6rem;">')
        for e in s["enlaces"]:
            dentro.append("      " + boton(e))
        dentro.append('    </div>')
    dentro.append('  </div>')

    for l in s.get("libros", []):
        dentro.append("")
        dentro.append(bloque_libro(l))
    for d in s.get("puertas", []):
        dentro.append("")
        dentro.append(bloque_puerta(d))
    if s.get("galeria") or s.get("medios") or s.get("grabaciones"):
        capa = json.load(open(os.path.join(RAIZ, "herramientas", f"grabaciones.{LANG}.json"), encoding="utf-8"))
        if s.get("figura"):
            f = s["figura"]
            w, h = dims(f["img"])
            dentro += ["", f'  <figure class="reveal reveal-right" style="max-width:420px;margin:0 0 2.5rem;">',
                       f'    <img src="{f["img"]}" width="{w}" height="{h}" alt="{esc_attr(f["alt"])}" loading="lazy">',
                       f'    <figcaption class="audio-meta" style="margin-top:0.7rem;">{esc(f["pie"])}</figcaption>',
                       '  </figure>']
        if s.get("galeria"):
            dentro += ["", bloque_galeria(s["galeria"])]
        if s.get("medios"):
            dentro += ["", bloque_medios(s["medios"], capa)]
        if s.get("grabaciones"):
            dentro += ["", bloque_grabaciones(s["grabaciones"], capa)]

    ancla = f' id="{s["ancla"]}"' if s.get("ancla") else ""
    cuerpo = f'<div class="section"{ancla}>\n' + "\n".join(dentro) + '\n</div>'
    if s.get("alt"):
        cuerpo = '<div class="section-alt">\n' + cuerpo + '\n</div>'
    return cuerpo


def portada_hero(d):
    acciones = "\n        ".join(boton(a) for a in d["acciones"])
    return f"""<div class="split">
  <div class="split-image" style="background-image:url('{RETRATO}');" role="img" aria-label="Antonio López Sánchez over Havana Bay"></div>
  <div class="split-content">
    <div class="reveal reveal-right">
      <h1>
        <span class="casa-nombre">Ala del Mar</span>
        <span class="lema">bene scriptus</span>
        <span class="casa-autor">Antonio López Sánchez</span>
      </h1>
    </div>
    <div class="reveal reveal-left" style="transition-delay:0.25s;">
      <p class="oficio">{esc(d["oficio"])}</p>
      <div class="hero-acciones">
        {acciones}
      </div>
      <p class="nota" style="margin-top:2rem;">{esc(d["aviso_idioma"])}</p>
    </div>
  </div>
</div>

<div class="banda-mar reveal reveal-left" role="img" aria-label="{esc_attr(Z["banda_mar_alt"])}"></div>"""


def persona():
    # La Person vive una sola vez, en la portada. Se lee de alli para que el
    # mainEntity de /en/author/ no pueda desviarse del original.
    with open(os.path.join(RAIZ, "index.html"), encoding="utf-8") as f:
        s = f.read()
    for trozo in s.split('<script type="application/ld+json">')[1:]:
        d = json.loads(trozo.split("</script>", 1)[0])
        if d.get("@type") == "Person":
            return {k: d[k] for k in ("@type", "@id", "name", "alternateName",
                                      "url", "image", "sameAs") if k in d}
    sys.exit("gen-idioma: no hay Person en index.html")


def datos_estructurados(d, url):
    tipo = "ProfilePage" if d["ruta"] == Z["ruta_autor"] else (
        "WebPage" if not d.get("es_portada") else "WebSite")
    base = {"@context": "https://schema.org", "@type": tipo,
            "name": d["seo_titulo"], "description": d["seo_desc"],
            "url": url, "inLanguage": LANG,
            "about": {"@id": f"{DOMINIO}/#antonio"}}
    if d.get("es_portada"):
        base["@id"] = f"{DOMINIO}{_portada()}#site"
    else:
        base["isPartOf"] = {"@id": f"{DOMINIO}/#sitio"}
    if tipo == "ProfilePage":
        # Google exige mainEntity con la persona dentro de la propia pagina
        # (Search Console, 11 de septiembre de 2026). about con un @id no basta.
        base["mainEntity"] = persona()
        del base["about"]
    return base


def migas(d, url):
    pasos = [("Ala del Mar", DOMINIO + _portada())]
    if not d.get("es_portada"):
        pasos.append((d["titulo"], url))
    filas = "".join(
        f'\n    {{ "@type": "ListItem", "position": {i}, "name": "{esc_attr(n)}", "item": "{u}" }},'
        for i, (n, u) in enumerate(pasos, 1)).rstrip(",")
    return ('<script type="application/ld+json">\n{\n'
            '  "@context": "https://schema.org",\n'
            '  "@type": "BreadcrumbList",\n'
            f'  "itemListElement": [{filas}\n  ]\n'
            '}\n</script>')


def pagina(d):
    url = DOMINIO + d["ruta"]
    T, D = d["seo_titulo"], d["seo_desc"]

    alternos = ""
    if d["ruta"] in Z["parejas"]:
        es = Z["parejas"][d["ruta"]]
        # La propia primero, luego el español, luego las demas: el orden que ya
        # tenia el ingles cuando era el unico idioma extranjero.
        rutas = {LANG: d["ruta"], "es": es}
        rutas.update(HERMANAS[es])
        alternos = "".join(f'\n<link rel="alternate" hreflang="{l}" href="{DOMINIO}{r}">'
                           for l, r in rutas.items())
        alternos += f'\n<link rel="alternate" hreflang="x-default" href="{DOMINIO}{es}">'
    elif d.get("hermana_de"):
        # Paginas que no tienen equivalente español y si lo tienen entre ellas:
        # hoy /en/fiction/ y /fr/fiction/, que son la misma pagina en dos
        # idiomas y estuvieron sin decirselo. Sin x-default, porque no hay
        # version por defecto a la que mandar a quien no hable ninguna.
        rutas = dict(HERMANAS_SUELTAS[d["hermana_de"]])
        propia = rutas.pop(LANG)
        alternos = f'\n<link rel="alternate" hreflang="{LANG}" href="{DOMINIO}{propia}">'
        alternos += "".join(f'\n<link rel="alternate" hreflang="{l}" href="{DOMINIO}{r}">'
                            for l, r in rutas.items())

    if d.get("es_portada"):
        cabecera = portada_hero(d)
    else:
        cabecera = (f'<header class="page-header">\n  <h1>{esc(d["titulo"])}</h1>\n'
                    f'  <p>{esc(d["subtitulo"])}</p>\n</header>')

    secciones = "\n\n".join(seccion_html(s, n) for n, s in enumerate(d.get("secciones", [])))
    activa = navegacion.seccion_de(d["ruta"], LANG)

    # El locale de la pagina y el de todos los demas idiomas del sitio.
    locales = f'<meta property="og:locale" content="{L()["locale"]}">'
    for l in IDIOMAS:
        if not l.startswith("_") and l != LANG:
            locales += f'\n<meta property="og:locale:alternate" content="{IDIOMAS[l]["locale"]}">'

    cuerpo_main = f'<main id="main">\n\n{secciones}\n\n</main>'
    if d.get("es_portada"):
        cuerpo_main = f'<main id="main">\n\n{cabecera}\n\n{secciones}\n\n</main>'
        cabecera = ""

    return f"""<!DOCTYPE html>
<html lang="{L()["lang"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{T}</title>
<meta name="description" content="{esc_attr(D)}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="canonical" href="{url}">{alternos}
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc_attr(T)}">
<meta property="og:description" content="{esc_attr(D)}">
<meta property="og:image" content="{DOMINIO}{RETRATO}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc_attr(T)}">
<meta name="twitter:description" content="{esc_attr(D)}">
<meta name="twitter:image" content="{DOMINIO}{RETRATO}">
{locales}
<meta name="theme-color" content="#0a0c1f">
<link rel="preload" href="/fonts/cinzel-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/cormorant-garamond-300.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts.css?v=6">
<link rel="stylesheet" href="/styles.css{CSS}">
<script type="application/ld+json">
{json.dumps(datos_estructurados(d, url), ensure_ascii=False, indent=2)}
</script>
{migas(d, url)}
</head>
<body>

<a class="salto" href="#main">{esc(L()["saltar"])}</a>

<nav class="nav">
  <a href="{_portada()}" class="nav-logo">Ala del Mar</a>
  <button class="nav-hamburger" type="button" aria-label="{esc_attr(L()["abrir_menu"])}" aria-expanded="false" aria-controls="menu-principal">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links" id="menu-principal">
{navegacion.menu_de(LANG, activa)}
  </ul>
</nav>

{cabecera}
{cuerpo_main}

<footer class="footer">
  <nav class="footer-nav" aria-label="{esc_attr(L()["secciones_aria"])}">
{navegacion.pie_de(LANG, activa)}
  </nav>
  <div class="footer-socials">
    <a href="https://www.facebook.com/profile.php?id=100071950279104" target="_blank" rel="noopener" aria-label="{esc_attr(L()["facebook_aria"])}"><svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16" aria-hidden="true"><path d="M13.5 22v-8.1h2.72l.41-3.16H13.5V8.72c0-.91.25-1.53 1.56-1.53h1.67V4.36c-.29-.04-1.28-.12-2.43-.12-2.4 0-4.05 1.47-4.05 4.16v2.34H7.53v3.16h2.72V22h3.25z"/></svg></a>
  </div>
  <p class="footer-lema">bene scriptus</p>
  <p class="footer-copy">&copy; 2026 Antonio López Sánchez · Ala del Mar</p>
  <p class="footer-copy">{esc(L()["desarrollado"])} <a href="https://index01.net" target="_blank" rel="noopener">Index01</a></p>
</footer>

<script src="/app.js?v=11" defer></script>
</body>
</html>
"""


def main():
    global LANG, Z, ZONAS, HERMANAS, HERMANAS_SUELTAS
    # Una zona por idioma: herramientas/zona.<idioma>.json. El español no
    # tiene, porque sus paginas de seccion estan escritas a mano.
    zonas = marco.lenguas_con_capa("zona")
    if not zonas:
        sys.exit("no hay ninguna zona: falta herramientas/zona.<idioma>.json")

    # Quien es hermana de quien: se agrupa por la ruta española, que es la
    # unica clave que todos los idiomas comparten.
    ZONAS = zonas
    HERMANAS, HERMANAS_SUELTAS = {}, {}
    for lang, cfg in zonas.items():
        for propia, es in cfg["parejas"].items():
            HERMANAS.setdefault(es, {})[lang] = propia
        for d in cfg["paginas"]:
            if d.get("hermana_de"):
                HERMANAS_SUELTAS.setdefault(d["hermana_de"], {})[lang] = d["ruta"]

    for lang, cfg in zonas.items():
        LANG, Z = lang, cfg
        if lang not in IDIOMAS:
            sys.exit(f"zona.{lang}.json existe pero {lang} no esta en idiomas.json")
        if lang not in navegacion.IDIOMAS:
            sys.exit(f"zona.{lang}.json existe pero {lang} no tiene menu en navegacion.py")
        for d in cfg["paginas"]:
            destino = os.path.join(RAIZ, d["ruta"].strip("/").replace("/", os.sep), "index.html")
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "w", encoding="utf-8", newline="") as f:
                f.write(pagina(d))
            n = len(d.get("secciones", []))
            print(f"escrito: {d['ruta']} · {n} secciones")


if __name__ == "__main__":
    main()
