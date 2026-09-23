# Genera Contarte: la sala de los cuentos y la habitacion de cada uno.
# Lee herramientas/cuentos.json y emite /contarte/index.html y
# /contarte/<slug>/index.html; y, con la capa herramientas/cuentos.en.json,
# su version inglesa en /en/stories/.
#
# Un cuento que ya salio en un libro vive aqui entero y el libro lo enlaza.
# El texto NO se duplica: es la misma regla que las grabaciones, escrita en
# AGENTS.md. Aqui esta la habitacion; alla, el camino hasta ella.
#
# Idiomas. Los cuentos no se traducen nunca: en la version inglesa salen en
# español, marcados con lang="es" y con el aviso de por que. La capa trae
# solo el aparato: la entrada de la sala, la linea de cada cuento, su
# procedencia y los metadatos.
#
# Uso: python herramientas/gen-cuento.py

import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pagina
from pagina import esc, esc_attr, cabeza, menu, pie, migas, IDIOMAS

RAIZ = pagina.RAIZ
DOMINIO = pagina.DOMINIO

# Calendario de Contarte. Rectangulo latino de 7 x 11: cada dia los cuentos
# salen en otro orden, ningun cuento repite posicion en toda la semana, los
# siete ordenes son distintos y ninguno es la rotacion de otro, que es lo que
# haria evidente la repeticion. Con siete cuentos era un cuadrado y cada uno
# pasaba por todas las posiciones; con once ya no caben, asi que la propiedad
# es la de arriba. Calculado con busqueda y horneado aqui; si cambia el numero
# de cuentos hay que recalcularlo.
CALENDARIO = [
    [9, 10, 7, 5, 4, 1, 8, 0, 2, 6, 3],
    [10, 0, 1, 7, 8, 3, 9, 5, 6, 4, 2],
    [0, 7, 3, 6, 2, 5, 1, 8, 10, 9, 4],
    [5, 2, 10, 0, 3, 9, 6, 4, 8, 1, 7],
    [8, 4, 2, 9, 1, 10, 3, 7, 0, 5, 6],
    [4, 3, 6, 1, 9, 0, 5, 2, 7, 10, 8],
    [2, 9, 8, 4, 6, 7, 10, 3, 5, 0, 1],
]

# Lo que en español estaba escrito aqui. En los demas idiomas lo trae la capa.
ES = {
    "ruta": "/contarte/",
    "h1": "Contarte",
    "frase": "La sala de los relatos.",
    "h2": "Había una vez...",
    "intro": [
        "Esas tres palabras ancestrales anuncian una historia. Aquí viven algunos de mis cuentos, cada uno con un sitio propio y con una mano extendida que invita a recorrerlos.",
        "Los hay libres, todavía sin asideros. Los hay que vienen de libros que esperan ver la luz. Algunos son risueños, otros oscuros. Pero todos están prestos a ofrecer su compañía.",
        "El cuento, ese duende que acompaña a la humanidad desde los albores de los tiempos, todavía regala magias, realidades y hasta miedos.",
    ],
    "aviso": None,
    # No todo lo que pide aviso lo pide por lo mismo: un cuento erotico entre
    # adultos y el delirio de una menor que acaba en suicidio no se avisan con
    # la misma frase. El manifiesto elige cual con el campo «adultos».
    "avisos_adultos": {
        "erotico": "Cuento de literatura erótica, escrito para lectores adultos.",
        "duro": "Cuento para lectores adultos: el delirio sexualizado de una menor, y una muerte por su propia mano.",
    },
    "leer": "Leer el cuento",
    "volver": "Volver a Contarte",
    "migas": "Contarte",
    "ver_ficha": "Ver la ficha de {}",
    "seo_titulo": "Contarte | Los cuentos de Antonio López Sánchez",
    "seo_desc": "Los cuentos de Antonio López Sánchez, completos y con su propia habitación cada uno.",
}

TEXTOS = os.path.join(RAIZ, "herramientas", "textos")


def leer(ruta):
    if not os.path.isabs(ruta):
        ruta = os.path.join(TEXTOS, ruta.replace("/", os.sep))
    with open(ruta, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n").strip("\n")


def quita(lineas, esperadas, cuento, que):
    """Saca del cuerpo las lineas que el manifiesto ya declara aparte, y se
    para si no son exactamente las que dice. Se declaran en el manifiesto y no
    se adivinan con heuristicas: una dedicatoria de tres lineas y un primer
    parrafo corto se parecen demasiado, y aqui equivocarse es publicar mal un
    texto del autor."""
    for e in esperadas:
        while lineas and not lineas[0]:
            lineas.pop(0)
        if not lineas or lineas[0] != e:
            sys.exit(f"{cuento}: esperaba en {que} la línea «{e}» y vino "
                     f"«{lineas[0] if lineas else '(nada)'}»")
        lineas.pop(0)


def cuerpo_cuento(texto, c):
    # La primera linea suele repetir el titulo en mayusculas: fuera. Tambien
    # el numero de la serie, «(III)», que va en el titulo de la pagina.
    lineas = [l.strip() for l in texto.split("\n")]
    while lineas and (not lineas[0] or lineas[0].upper() == c["titulo"].upper() or
                      (lineas[0].isupper() and len(lineas[0]) < 70)):
        lineas.pop(0)
    partes = []
    if c.get("dedicatoria"):
        quita(lineas, c["dedicatoria"], c["slug"], "la dedicatoria")
        partes.append('  <p class="texto-dedicatoria">'
                      + "<br>\n  ".join(esc(l) for l in c["dedicatoria"]) + '</p>')
    if c.get("epigrafe"):
        e = c["epigrafe"]
        quita(lineas, e["versos"] + [e["autor"]], c["slug"], "el epígrafe")
        partes.append('  <blockquote class="poema-epigrafe">\n'
                      + "\n".join(f'    <div class="verso">{esc(v)}</div>' for v in e["versos"])
                      + f'\n    <cite>{esc(e["autor"])}</cite>\n  </blockquote>')
    partes += [f"<p>{esc(l)}</p>" for l in lineas if l]
    return "\n".join(partes)


def rutas_de(capas, slug=None):
    return {l: V["ruta"] + (f"{slug}/" if slug else "") for l, V in capas.items()}


def libro_en(lang, ruta_es):
    """La ficha del libro del que viene un cuento, en el idioma de la pagina."""
    return ruta_es if lang == "es" else ruta_es.replace("/libros/", IDIOMAS[lang]["ruta_libros"], 1)


def pagina_cuento(lang, V, c, capas):
    L = IDIOMAS[lang]
    es = lang == "es"
    t = c if es else {**c, **V["cuentos"][c["slug"]]}
    la = "" if es else ' lang="es"'
    url = f"{DOMINIO}{V['ruta']}{c['slug']}/"
    texto = cuerpo_cuento(leer(c["archivo"]), c)
    # La procedencia puede venir de un libro que ya tiene ficha en el sitio o
    # de uno que todavia esta en proceso editorial y no tiene pagina adonde
    # mandar a nadie. En ese caso sale la linea sola, sin enlace.
    p = c.get("procedencia") or {}
    nota = ""
    if p:
        texto_p = p["texto"] if es else t["procedencia"]
        ficha = (f' <a href="{libro_en(lang, p["libro"])}">'
                 f'{esc(V["ver_ficha"].format(p["libro_titulo"]))}</a>') if p.get("libro") else ""
        nota = f'  <p class="cuento-procedencia reveal reveal-left">{esc(texto_p)}.{ficha}</p>\n'
    aviso = (f'  <p class="nota" style="margin-bottom:2rem;">{esc(V["aviso"])}</p>\n' if V.get("aviso") else "")
    if c.get("adultos"):
        aviso += f'  <p class="sonata-premio">{esc(V["avisos_adultos"][c["adultos"]])}</p>\n\n'

    datos = {"@context": "https://schema.org", "@type": "ShortStory",
             "name": c["titulo"], "url": url, "inLanguage": "es",
             "author": {"@id": f"{DOMINIO}/#antonio"},
             "description": t["seo_desc"]}
    if c.get("anio"): datos["datePublished"] = c["anio"]
    if c.get("adultos"): datos["isFamilyFriendly"] = False
    if p and p.get("libro"):
        datos["isPartOf"] = {"@type": "Book", "name": p["libro_titulo"],
                             "url": DOMINIO + libro_en(lang, p["libro"])}

    return (cabeza(lang, t["seo_titulo"], t["seo_desc"], url,
                   rutas=rutas_de(capas, c["slug"]), adultos=bool(c.get("adultos")))
            + '<script type="application/ld+json">\n' + json.dumps(datos, ensure_ascii=False, indent=2) + '\n</script>\n'
            + migas([("Ala del Mar", DOMINIO + L["portada"]), (V["migas"], DOMINIO + V["ruta"]), (c["titulo"], url)])
            + menu(lang, "/contarte/" if es else None)
            + f"""
<header class="page-header">
  <h1{la}>{esc(c["titulo"])}</h1>
</header>

<main id="main">
<div class="section cuento">
{aviso}  <div class="cuento-texto reveal reveal-right"{la}>
{texto}
  </div>
{nota}  <p style="margin-top:2.5rem;"><a href="{V['ruta']}" class="btn">{esc(V["volver"])}</a></p>
</div>
</main>
"""
            + pie(lang, None))


def pagina_indice(lang, V, cuentos, capas):
    L = IDIOMAS[lang]
    es = lang == "es"
    la = "" if es else ' lang="es"'
    url = DOMINIO + V["ruta"]
    def ficha(i, c):
        t = c if es else {**c, **V["cuentos"][c["slug"]]}
        meta = esc(c.get("anio", ""))
        if c.get("procedencia"):
            meta = (meta + " · " if meta else "") + esc(c["procedencia"]["texto"] if es else t["procedencia"])
        meta = f'    <p class="libro-meta">{meta}</p>\n' if meta else ""
        # Fuera del español el titulo se queda en español, con su sentido
        # entre parentesis, como en el catalogo de libros.
        sentido = "" if es else f' <span class="libro-meta">({esc(t["significado"])})</span>'
        return (f'  <article class="cuento-ficha reveal reveal-right" data-cuento="{i}">\n'
                f'    <h3 class="libro-titulo"><a href="{V["ruta"]}{c["slug"]}/"{la}>{esc(c["titulo"])}</a>{sentido}</h3>\n'
                f'{meta}'
                f'    <p class="libro-sinopsis">{esc(t["linea"])}</p>\n'
                f'    <p style="margin-top:1.2rem;"><a href="{V["ruta"]}{c["slug"]}/" class="btn">{esc(V["leer"])}</a></p>\n'
                f'  </article>')
    filas = "\n".join(ficha(i, c) for i, c in enumerate(cuentos))

    # El orden del dia. El script va sin defer, justo detras de la lista, para
    # que se ejecute mientras se analiza la pagina: asi el navegador pinta una
    # sola vez y no se ve el barajado. Sin JavaScript se ven en el orden del
    # manifiesto, que es la degradacion correcta.
    orden_js = (
        '<script>\n'
        '(function(){\n'
        '  var cal = ' + json.dumps(CALENDARIO) + ';\n'
        '  var hoy = cal[new Date().getDay()];\n'
        '  var fichas = document.querySelectorAll(".cuento-ficha");\n'
        '  for (var p = 0; p < hoy.length; p++) {\n'
        '    var f = fichas[hoy[p]];\n'
        '    if (f) f.style.order = p;\n'
        '  }\n'
        '})();\n'
        '</script>')

    lista = {"@context": "https://schema.org", "@type": "ItemList",
             "name": "Cuentos de Antonio López Sánchez" if es else V["seo_titulo"],
             "itemListElement": [
                 {"@type": "ListItem", "position": i,
                  "item": {"@type": "ShortStory", "name": c["titulo"],
                           "url": f"{url}{c['slug']}/",
                           "author": {"@type": "Person", "name": "Antonio López Sánchez"},
                           "inLanguage": "es"}}
                 for i, c in enumerate(cuentos, 1)]}

    ultimo = len(V["intro"]) - 1
    intro = "\n".join(
        f'    <p class="section-text" style="margin-bottom:{"3rem" if i == ultimo else "1.5rem"};">{esc(p)}</p>'
        for i, p in enumerate(V["intro"]))
    if V.get("aviso"):
        intro = intro.replace('style="margin-bottom:3rem;"', 'style="margin-bottom:1.5rem;"') + \
                f'\n    <p class="nota" style="margin-bottom:3rem;">{esc(V["aviso"])}</p>'

    return (cabeza(lang, V["seo_titulo"], V["seo_desc"], url, rutas=rutas_de(capas))
            + '<script type="application/ld+json">\n' + json.dumps(lista, ensure_ascii=False, indent=2) + '\n</script>\n'
            + migas([("Ala del Mar", DOMINIO + L["portada"]), (V["migas"], url)])
            + menu(lang, "/contarte/" if es else None)
            + f"""
<header class="page-header">
  <h1>{esc(V["h1"])}</h1>
  <p>{esc(V["frase"])}</p>
</header>

<main id="main">
<div class="section">
  <div class="reveal reveal-right">
    <h2 class="section-title">{esc(V["h2"])}</h2>
    <div class="section-divider"></div>
{intro}
  </div>

  <div class="cuento-lista">
{filas}
  </div>
{orden_js}

</div>
</main>
"""
            + pie(lang, "/contarte/" if es else None))


def main():
    cuentos = json.load(open(os.path.join(RAIZ, "herramientas", "cuentos.json"), encoding="utf-8"))
    if len(cuentos) != len(CALENDARIO[0]):
        sys.exit(f"el calendario de Contarte es de {len(CALENDARIO[0])} cuentos y hay {len(cuentos)}: "
                 "hay que recalcularlo (ver la cabecera de este archivo)")
    capas = {"es": ES}
    for lang, V in pagina.lenguas_con_capa("cuentos").items():
        faltan = [c["slug"] for c in cuentos if c["slug"] not in V["cuentos"]
                  or (c.get("procedencia") and not V["cuentos"][c["slug"]].get("procedencia"))]
        if faltan:
            sys.exit(f"cuentos.{lang}.json incompleto: {', '.join(faltan)}")
        capas[lang] = V
    for lang, V in capas.items():
        for c in cuentos:
            pagina.escribe(V["ruta"] + c["slug"] + "/", pagina_cuento(lang, V, c, capas))
        pagina.escribe(V["ruta"], pagina_indice(lang, V, cuentos, capas))
        print(f"escrito: {V['ruta']} con {len(cuentos)} cuento(s)")


if __name__ == "__main__":
    main()
