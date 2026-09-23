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
# Idiomas. La obra no se traduce nunca. La capa inglesa, sonata.en.json, trae
# solo el aparato, y la version inglesa sale en /en/poetry/sonata-de-la-lluvia/.
#
# Uso: python herramientas/gen-sonata.py

import json, os, sys, html, re
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pagina

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
CSS = "?v=42"
FUENTE = os.path.join(RAIZ, "herramientas", "textos", "decimitas", "sonata-de-la-lluvia.txt")
FOTO = "/img/decimitas/sonata-de-la-lluvia.webp"

FIRMAS = ("Fito Páez", "Noel Nicola", "Santiago Feliú")

# El nombre del premio y del concurso son nombres propios: no se traducen.
PREMIO = "Premio Colateral Yasmina Calcines"
PREMIO_COMPLETO = "Premio Colateral Yasmina Calcines, XXVI Concurso Nacional Ala Décima, 2026"

ES = {
    "ruta": "/tinta-ciones/sonata-de-la-lluvia/",
    "frase": "Tres movimientos en décimas.",
    "aviso": None,
    "foto_alt": "Atardecer sobre el muro del malecón, con el sol abriéndose paso entre las nubes",
    "premio": "Con esta obra gané el {premio}, del XXVI Concurso Nacional Ala Décima, en 2026.",
    "premios_url": "/laureles/",
    "volver": "Volver a De-Cimitas",
    "volver_url": "/tinta-ciones/de-cimitas/",
    "migas": ["Tinta-ciones", "De-Cimitas", "Sonata de la lluvia"],
    "migas_urls": ["/tinta-ciones/", "/tinta-ciones/de-cimitas/"],
    "genero": "Poesía. Décima",
    "seo_titulo": "Sonata de la lluvia, de Antonio López Sánchez",
    "seo_desc": ("Sonata de la lluvia, de Antonio López Sánchez: tres movimientos en décimas, "
                 "premiada en el XXVI Concurso Nacional Ala Décima."),
}


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


def pagina_sonata(lang, V, movs, fw, fh, capas):
    L = pagina.IDIOMAS[lang]
    es = lang == "es"
    la = "" if es else ' lang="es"'
    url = DOMINIO + V["ruta"]
    piezas = []
    for n, m in enumerate(movs):
        p = [f'  <section class="mov reveal reveal-{"right" if n % 2 == 0 else "left"}" id="mov-{m["numero"].lower()}"{la}>']
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

    # CreativeWork y no Poem: schema.org/Poem no existe, devuelve 404.
    # El genero se declara aparte, que es como se dice "esto es poesia".
    datos = {"@context": "https://schema.org", "@type": "CreativeWork",
             "name": "Sonata de la lluvia", "url": url, "inLanguage": "es",
             "author": {"@id": f"{DOMINIO}/#antonio"},
             "genre": V["genero"],
             "datePublished": "2026",
             "award": PREMIO_COMPLETO,
             "description": V["seo_desc"],
             "image": DOMINIO + FOTO,
             "hasPart": [{"@type": "CreativeWork", "genre": "Décima", "name": m["titulo"].capitalize(),
                          "position": i} for i, m in enumerate(movs, 1)]}

    premio = V["premio"].replace("{premio}", f'<a href="{V["premios_url"]}">{esc(PREMIO)}</a>')
    aviso = f'  <p class="nota" style="margin-bottom:2rem;">{esc(V["aviso"])}</p>\n\n' if V.get("aviso") else ""
    migas = [("Ala del Mar", DOMINIO + L["portada"])]
    migas += [(n, DOMINIO + u) for n, u in zip(V["migas"][:2], V["migas_urls"])]
    migas.append((V["migas"][2], url))

    return (pagina.cabeza(lang, V["seo_titulo"], V["seo_desc"], url, imagen=DOMINIO + FOTO,
                          rutas={l: c["ruta"] for l, c in capas.items()})
            + '<script type="application/ld+json">\n' + json.dumps(datos, ensure_ascii=False, indent=2) + '\n</script>\n'
            + pagina.migas(migas)
            + pagina.menu(lang, V["migas_urls"][0])
            + f"""
<header class="page-header">
  <h1{la}>Sonata de la lluvia</h1>
  <p>{esc(V["frase"])}</p>
</header>

<main id="main">
<div class="section cuento">

  <figure class="sonata-foto reveal reveal-right">
    <img src="{FOTO}" width="{fw}" height="{fh}" alt="{esc_attr(V["foto_alt"])}" loading="lazy">
  </figure>

  <p class="sonata-premio reveal reveal-left">{premio}</p>

{aviso}{cuerpo}

  <p class="vyv-firma" style="margin-top:2.5rem;">ALS</p>
  <p style="margin-top:2.5rem;"><a href="{V["volver_url"]}" class="btn">{esc(V["volver"])}</a></p>

</div>
</main>
"""
            + pagina.pie(lang, None))


def main():
    texto = open(FUENTE, encoding="utf-8").read()
    movs = movimientos(texto)
    assert len(movs) == 3, f"esperaba 3 movimientos, encontre {len(movs)}"
    with Image.open(os.path.join(RAIZ, FOTO.lstrip("/"))) as im:
        fw, fh = im.size
    capas = {"es": ES, **pagina.lenguas_con_capa("sonata")}
    for lang, V in capas.items():
        destino = pagina.escribe(V["ruta"], pagina_sonata(lang, V, movs, fw, fh, capas))
        versos = sum(len([l for l in m["versos"] if l.strip()]) for m in movs)
        print(f"escrito: {destino} · 3 movimientos, {versos} versos")


if __name__ == "__main__":
    main()
