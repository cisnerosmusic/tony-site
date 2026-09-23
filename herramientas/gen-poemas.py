# Genera /tinta-ciones/poemas-sueltos/ desde herramientas/poemas.json.
#
# Lo delicado aqui no es la maqueta, es la atribucion: ocho de estos poemas son
# glosas que abren con una estrofa de Jose Marti o de Lezama Lima. Esos versos
# NO son del autor. Salen en su propio bloque, con el nombre de quien los
# escribio debajo, para que nadie los lea como suyos.
#
# Idiomas. Los poemas no se traducen nunca. La capa inglesa, poemas.en.json,
# trae solo el aparato, y la version inglesa sale en /en/poetry/poems/ con
# los poemas en español, marcados con lang="es".
#
# Uso: python herramientas/gen-poemas.py

import json, os, sys, html, unicodedata, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion
import pagina
from importlib.machinery import SourceFileLoader
leer_poema = SourceFileLoader("leer_poema", os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "leer-poema.py")).load_module()

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
URL = DOMINIO + "/tinta-ciones/poemas-sueltos/"
CSS = "?v=39"


def esc(t):
    """Texto visible: se dejan las comillas como el autor las escribio."""
    return html.escape(t, quote=False)


def esc_attr(t):
    """Valor de atributo: aqui las comillas SI se escapan, o una comilla en
    un titulo o en un alt parte el HTML en dos."""
    return html.escape(t, quote=True)


# El ancla de cada poema la calcula pagina.py, porque el concentrador ingles
# tiene que escribir esos mismos enlaces y no pueden salir dos resultados.
ancla = pagina.ancla


def bloque(p, ficha, n, la=""):
    """Un poema: titulo, epigrafe ajeno si lo hay, versos y firma.
    El titulo viene del manifiesto, escrito a mano; del archivo solo salen los
    versos, que son lo que no se puede tocar."""
    principal = ficha["titulo"]
    numero = ficha.get("numero", "")
    serie = ficha.get("serie", "")
    id_ = ancla(principal)

    partes = [f'<article class="poema reveal reveal-{"right" if n % 2 == 0 else "left"}" id="{id_}"{la}>']
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
    # El colofon de fecha no sale a la pagina. Se sigue leyendo, y por eso el
    # lector lo separa, para que ninguna fecha se quede colada al final de los
    # versos; pero un poema no se presenta con la fecha en que se escribio.
    partes.append('  <p class="vyv-firma">ALS</p>')
    partes.append('</article>')
    return "\n".join(partes)


ES = {
    "ruta": "/tinta-ciones/poemas-sueltos/",
    "seccion": "/tinta-ciones/",
    "h1": "Poemas sueltos",
    "frase": "Unos lienzos amplios para dibujar mis visiones.",
    "aviso": None,
    "glosas_titulo": "Glosas",
    "glosas_texto": "Las glosas a otros poetas son una práctica habitual entre decimistas. Aquí escojo dos enormes cumbres, José Martí y José Lezama Lima, para dialogar de algún modo con sus versos. Va en esta rimada habitación apenas un botón de muestra de un trabajo mucho mayor, que espera sus páginas. Entretanto, aquí van de regalo algunas de las Glosas Martianas y las Glozama Rimas.",
    "glosas_nota": None,
    "migas": ["Tinta-ciones", "Poemas sueltos"],
    "seo_titulo": "Poemas sueltos de Antonio López Sánchez",
    "seo_desc": "{} poemas del poeta cubano Antonio López Sánchez, entre ellos ocho glosas sobre versos de José Martí y de José Lezama Lima.",
}


def pagina_poemas(lang, V, sueltos, glosas, capas):
    L = pagina.IDIOMAS[lang]
    es = lang == "es"
    # Los poemas son literatura: en una pagina que no es española, cada uno
    # sale entero marcado como español.
    la = "" if es else ' lang="es"'
    url = DOMINIO + V["ruta"]
    cuerpo_sueltos = "\n\n".join(bloque(p, f, i, la) for i, (p, f) in enumerate(sueltos))
    cuerpo_glosas = "\n\n".join(bloque(p, f, i, la) for i, (p, f) in enumerate(glosas))

    titulos = [f["titulo"] for _, f in sueltos + glosas]
    lista = {"@context": "https://schema.org", "@type": "ItemList",
             "name": "Poemas sueltos de Antonio López Sánchez" if es else V["seo_titulo"],
             "itemListElement": [
                 {"@type": "ListItem", "position": i, "name": t}
                 for i, t in enumerate(titulos, 1)]}
    seccion = V["seccion"]
    aviso = (f'\n  <p class="nota" style="margin-bottom:3rem;">{esc(V["aviso"])}</p>\n' if V.get("aviso") else "")
    nota_glosa = (f'\n    <p class="nota" style="margin-bottom:3rem;">{esc(V["glosas_nota"])}</p>' if V.get("glosas_nota") else "")
    margen_glosas = "1.5rem" if V.get("glosas_nota") else "3rem"

    return (pagina.cabeza(lang, V["seo_titulo"], V["seo_desc"].format(len(titulos)), url,
                          rutas={l: c["ruta"] for l, c in capas.items()})
            + '<script type="application/ld+json">\n' + json.dumps(lista, ensure_ascii=False, indent=2) + '\n</script>\n'
            + pagina.migas([("Ala del Mar", DOMINIO + L["portada"]), (V["migas"][0], DOMINIO + seccion), (V["migas"][1], url)])
            + pagina.menu(lang, seccion)
            + f"""
<header class="page-header">
  <h1>{esc(V["h1"])}</h1>
  <p>{esc(V["frase"])}</p>
</header>

<main id="main">
<div class="section poemario">
{aviso}
{cuerpo_sueltos}

  <div class="reveal reveal-right" style="margin-top:4.5rem;">
    <h2 class="section-title">{esc(V["glosas_titulo"])}</h2>
    <div class="section-divider"></div>
    <p class="section-text" style="margin-bottom:{margen_glosas};">{esc(V["glosas_texto"])}</p>{nota_glosa}
  </div>

{cuerpo_glosas}

</div>
</main>
"""
            + pagina.pie(lang, None))


def main():
    cfg = json.load(open(os.path.join(RAIZ, "herramientas", "poemas.json"), encoding="utf-8"))
    carpeta = os.path.join(RAIZ, "herramientas", "textos")

    def carga(ficha):
        ruta = os.path.join(carpeta, ficha["archivo"].replace("/", os.sep))
        return leer_poema.partes(open(ruta, encoding="utf-8").read())

    sueltos = [(carga(f), f) for f in cfg["sueltos"]]
    glosas = [(carga(f), f) for f in cfg["glosas"]]
    capas = {"es": ES, **pagina.lenguas_con_capa("poemas")}
    for lang, V in capas.items():
        destino = pagina.escribe(V["ruta"], pagina_poemas(lang, V, sueltos, glosas, capas))
        print(f"escrito: {destino} · {len(sueltos)} poemas y {len(glosas)} glosas")


if __name__ == "__main__":
    main()
