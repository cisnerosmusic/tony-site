# Genera Laureles, los premios del autor, en cada idioma: /laureles/ desde
# herramientas/laureles.json y /en/awards/ desde laureles.en.json.
#
# Estuvo escrita a mano. Paso a generarse el 21 de septiembre de 2026, cuando
# los premios iban a vivir en tres sitios a la vez (Laureles, su version
# inglesa y la pagina inglesa del autor): tres listas que tarde o temprano
# se contradicen. Ahora hay una por idioma, y el generador se para si una
# capa no trae los mismos premios, en el mismo orden y con los mismos años.
#
# Uso: python herramientas/gen-laureles.py

import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pagina
from pagina import esc, DOMINIO

RAIZ = pagina.RAIZ


def pagina_laureles(lang, V, capas):
    L = pagina.IDIOMAS[lang]
    es = lang == "es"
    url = DOMINIO + V["ruta"]
    # Los textos traen sus propios enlaces y cursivas, ya en HTML.
    items = "\n\n".join(
        f'  <article class="laurel-item reveal reveal-right">\n'
        f'    <p class="laurel-anio">{esc(p["anio"])}</p>\n'
        f'    <div>\n'
        f'      <h2>{p["titulo"]}</h2>\n'
        f'      <p>{p["texto"]}</p>\n'
        f'    </div>\n'
        f'  </article>' for p in V["premios"])

    datos = {"@context": "https://schema.org", "@type": "WebPage",
             "name": V["seo_titulo"], "description": V["seo_desc"], "url": url,
             "inLanguage": L["lang"], "isPartOf": {"@id": f"{DOMINIO}/#sitio"},
             "about": {"@id": f"{DOMINIO}/#antonio"}}
    # En ingles los premios cuelgan de The author, que es donde un editor
    # extranjero los busca; en español, Laureles tiene entrada propia.
    activa = "/laureles/" if es else "/en/author/"
    return (pagina.cabeza(lang, V["seo_titulo"], V["seo_desc"], url, tipo_og="profile",
                          rutas={l: c["ruta"] for l, c in capas.items()})
            + '<script type="application/ld+json">\n' + json.dumps(datos, ensure_ascii=False, indent=2) + '\n</script>\n'
            + pagina.migas([("Ala del Mar", DOMINIO + L["portada"]), (V["h1"], url)])
            + pagina.menu(lang, activa)
            + f"""
<header class="page-header">
  <h1>{esc(V["h1"])}</h1>
  <p>{esc(V["frase"])}</p>
</header>

<main id="main">
<div class="section">

{items}

  <p class="nota" style="margin-top:3rem;">{esc(V["nota"])}</p>
</div>
</main>
"""
            + pagina.pie(lang, "/laureles/" if es else None))


def main():
    es = json.load(open(os.path.join(RAIZ, "herramientas", "laureles.json"), encoding="utf-8"))
    capas = {"es": es, **pagina.lenguas_con_capa("laureles")}
    for lang, V in capas.items():
        if [p["anio"] for p in V["premios"]] != [p["anio"] for p in es["premios"]]:
            sys.exit(f"laureles.{lang}.json no trae los mismos premios que laureles.json")
    for lang, V in capas.items():
        destino = pagina.escribe(V["ruta"], pagina_laureles(lang, V, capas))
        print(f"escrito: {destino} · {len(V['premios'])} premios")


if __name__ == "__main__":
    main()
