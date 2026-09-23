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
# Idiomas. Las obras no se traducen nunca. La capa inglesa,
# farraluque.en.json, trae solo el aparato; la version inglesa sale en
# /en/awards/<obra>/.
#
# Uso: python herramientas/gen-farraluque.py

import json, os, sys, html, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pagina

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=44"
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



ES = {
    "ruta": "/laureles/",
    "seccion": "/laureles/",
    "migas": "Laureles",
    "volver": "Volver a Laureles",
    "aviso": AVISO,
    "aviso_idioma": None,
    "premio": PREMIO,
    "poema": {
        "premio_frase": "Con ella gané el Primer Premio en Poesía del {premio}.",
        "genero": "Poesía. Décima. Literatura erótica",
        "award": "Primer Premio en Poesía, {premio}",
        "seo_titulo": "Tres delirios y un desnudo, de Antonio López Sánchez",
        "seo_desc": ("Tres delirios y un desnudo, de Antonio López Sánchez: tríptico en décimas, "
                     "Primer Premio de Poesía del XXX Premio Farraluque, 2026."),
    },
    "cuento": {
        "subtitulo": "Un domingo, y una decisión ya tomada.",
        "premio_frase": "Obtuvo Mención en Cuento en el {premio}.",
        "genero": "Literatura erótica",
        "award": "Mención en Cuento, {premio}",
        "seo_titulo": "Revelaciones, un cuento de Antonio López Sánchez",
        "seo_desc": ("Revelaciones, cuento de Antonio López Sánchez: una mujer falta a misa "
                     "para acudir a una cita. Mención en el XXX Premio Farraluque, 2026."),
    },
}


def envoltura(lang, V, slug, titulo, subtitulo, T, D, datos, cuerpo, capas, sub_es=False, tipo="article"):
    L = pagina.IDIOMAS[lang]
    es = lang == "es"
    la = "" if es else ' lang="es"'
    url = datos["url"]
    # El subtitulo del poema es parte de la obra y se queda en español; el
    # del cuento es aparato y va en el idioma de la pagina.
    la_sub = la if sub_es else ""
    migas = [("Ala del Mar", DOMINIO + L["portada"]), (V["migas"], DOMINIO + V["ruta"]), (titulo, url)]
    return (pagina.cabeza(lang, T, D, url, tipo_og=tipo, imagen=DOMINIO + RETRATO,
                          rutas={l: c["ruta"] + slug + "/" for l, c in capas.items()}, adultos=True)
            + '<script type="application/ld+json">\n' + json.dumps(datos, ensure_ascii=False, indent=2) + '\n</script>\n'
            + pagina.migas(migas)
            + pagina.menu(lang, V["seccion"])
            + f"""
<header class="page-header">
  <h1{la}>{esc(titulo)}</h1>
  <p{la_sub}>{esc(subtitulo)}</p>
</header>

<main id="main">
<div class="section cuento">

{cuerpo}

  <p class="vyv-firma" style="margin-top:2.5rem;">ALS</p>
  <p style="margin-top:2.5rem;"><a href="{V["ruta"]}" class="btn">{esc(V["volver"])}</a></p>

</div>
</main>
"""
            + pagina.pie(lang, None))


def aviso_de(V, frase):
    enlace = f'<a href="{V["ruta"]}">{esc(V["premio"])}</a>'
    t = (f'  <p class="sonata-premio reveal reveal-left">{esc(V["aviso"])} '
         + frase.replace("{premio}", enlace) + '</p>')
    if V.get("aviso_idioma"):
        t += f'\n\n  <p class="nota" style="margin-bottom:2rem;">{esc(V["aviso_idioma"])}</p>'
    return t


def poema(lang, V, capas):
    es = lang == "es"
    la = "" if es else ' lang="es"'
    P = V["poema"]
    slug = "tres-delirios-y-un-desnudo"
    url = f"{DOMINIO}{V['ruta']}{slug}/"
    subtitulo, partes = delirios()
    piezas = [aviso_de(V, P["premio_frase"])]
    for n, p in enumerate(partes):
        lado = "right" if n % 2 == 0 else "left"
        ident = p["nombre"].lower().replace(" ", "-")
        piezas.append(
            f'  <section class="mov reveal reveal-{lado}" id="{ident}"{la}>\n'
            f'    <p class="mov-numero">{esc(p["nombre"])}</p>\n'
            f'    <h2 class="mov-titulo">{esc(p["sub"])}</h2>\n'
            + "\n".join(f'    <div class="verso poema-cuerpo decima">'
                        + "\n".join(esc(v) for v in d) + '</div>' for d in p["decimas"])
            + '\n  </section>')

    datos = {"@context": "https://schema.org", "@type": "CreativeWork",
             "name": "Tres delirios y un desnudo", "url": url, "inLanguage": "es",
             "author": {"@id": f"{DOMINIO}/#antonio"},
             "genre": P["genero"],
             "datePublished": "2026",
             "isFamilyFriendly": False,
             "award": P["award"].replace("{premio}", V["premio"]),
             "description": P["seo_desc"],
             "hasPart": [{"@type": "CreativeWork", "genre": "Décima",
                          "name": p["sub"], "position": i}
                         for i, p in enumerate(partes, 1)]}
    destino = pagina.escribe(V["ruta"] + slug, envoltura(
        lang, V, slug, "Tres delirios y un desnudo", subtitulo + ".", P["seo_titulo"], P["seo_desc"],
        datos, "\n\n".join(piezas), capas, sub_es=True))
    print(f"escrito: {destino} · {len(partes)} delirios, {sum(len(p['decimas']) for p in partes)} décimas")


def cuento(lang, V, capas):
    es = lang == "es"
    la = "" if es else ' lang="es"'
    C = V["cuento"]
    slug = "revelaciones"
    url = f"{DOMINIO}{V['ruta']}{slug}/"
    ls = sin_cabecera(lee("revelaciones.txt"), "REVELACIONES")
    epi = [l.strip() for l in ls[:2]]
    firma = ls[2].strip()
    assert firma == "Silvio Rodríguez", f"esperaba la firma del epigrafe, vino: {firma}"
    parrafos = [l.strip() for l in ls[3:] if l.strip()]

    cuerpo = (aviso_de(V, C["premio_frase"]) + '\n\n'
              f'  <blockquote class="poema-epigrafe reveal reveal-right"{la}>\n'
              '    <div class="verso">' + "\n".join(esc(l) for l in epi) + '</div>\n'
              f'    <cite>{esc(firma)}</cite>\n'
              '  </blockquote>\n\n'
              f'  <div class="cuento-texto reveal reveal-right"{la}>\n'
              + "\n".join(f"    <p>{esc(p)}</p>" for p in parrafos)
              + '\n  </div>')

    datos = {"@context": "https://schema.org", "@type": "ShortStory",
             "name": "Revelaciones", "url": url, "inLanguage": "es",
             "author": {"@id": f"{DOMINIO}/#antonio"},
             "genre": C["genero"],
             "datePublished": "2026",
             "isFamilyFriendly": False,
             "award": C["award"].replace("{premio}", V["premio"]),
             "description": C["seo_desc"],
             "wordCount": sum(len(p.split()) for p in parrafos)}
    destino = pagina.escribe(V["ruta"] + slug, envoltura(
        lang, V, slug, "Revelaciones", C["subtitulo"], C["seo_titulo"], C["seo_desc"],
        datos, cuerpo, capas))
    print(f"escrito: {destino} · {len(parrafos)} párrafo(s), {datos['wordCount']} palabras")


if __name__ == "__main__":
    capas = {"es": ES, **pagina.lenguas_con_capa("farraluque")}
    for lang, V in capas.items():
        poema(lang, V, capas)
        cuento(lang, V, capas)
