# Reparte las grabaciones por las salas que las reclaman, desde un unico
# manifiesto: herramientas/grabaciones.json
#
# El problema que resuelve: un poema leido por el autor pertenece a la vez a
# Plano abierto, por el acto que lo genero, y a En mi voz, porque esta en su
# voz. Duplicar el reproductor esta bien, el archivo de audio es uno solo y la
# pagina que lo rodea es distinta. Lo que NO se duplica es la ficha larga ni el
# marcado de datos: eso vive en la sala canonica y la otra remite a ella.
#
# Cada pagina marca su region con:
#   <!-- grabaciones: <sala> -->  ...  <!-- /grabaciones -->
# y todo lo que hay dentro lo escribe este script. Fuera de esos marcadores no
# se toca nada.
#
# Uso: python herramientas/gen-audios.py

import json, os, re, html

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"

SALAS = {
    "plano-abierto": ("plano-abierto/index.html", "/plano-abierto/", "Plano abierto"),
    "en-mi-voz": ("tinta-ciones/en-mi-voz/index.html", "/tinta-ciones/en-mi-voz/", "En mi voz"),
}

def esc(t):
    return html.escape(t, quote=False)

def bloque(g, sala, n):
    lado = "right" if n % 2 == 0 else "left"
    canonica = g["canonica"]
    if sala == canonica:
        pie = esc(g["ficha"])
    else:
        # En la sala secundaria va la frase corta y el camino a la ficha entera.
        ruta, nombre = SALAS[canonica][1], SALAS[canonica][2]
        pie = f'{esc(g["frase"])} · <a href="{ruta}">dónde y cuándo, en {nombre}</a>'
    return (f'  <article class="audio-item reveal reveal-{lado}">\n'
            f'    <h3>{esc(g["titulo"])}</h3>\n'
            f'    <p class="audio-meta">{pie}</p>\n'
            f'    <audio controls preload="none" src="{g["archivo"]}">\n'
            f'      Tu navegador no reproduce audio; puedes <a href="{g["archivo"]}">descargar la grabación</a>.\n'
            f'    </audio>\n'
            f'  </article>\n')

def datos(g):
    # El AudioObject se declara una sola vez, en la sala canonica.
    d = {"@context": "https://schema.org", "@type": "AudioObject",
         "name": g["titulo"], "contentUrl": DOMINIO + g["archivo"],
         "encodingFormat": "audio/mpeg", "inLanguage": "es",
         "creator": {"@id": DOMINIO + "/#antonio"}}
    if g.get("duracion"): d["duration"] = g["duracion"]
    if g.get("fecha"): d["datePublished"] = g["fecha"]
    d["description"] = g["ficha"]
    return '<script type="application/ld+json">\n' + json.dumps(d, ensure_ascii=False, indent=2) + '\n</script>\n'

def main():
    grabaciones = json.load(open(os.path.join(RAIZ, "herramientas", "grabaciones.json"), encoding="utf-8"))
    for sala, (ruta, _, _) in SALAS.items():
        p = os.path.join(RAIZ, ruta)
        t = open(p, encoding="utf-8").read()
        patron = re.compile(r'<!-- grabaciones: ' + sala + r' -->.*?[ \t]*<!-- /grabaciones -->', re.S)
        if not patron.search(t):
            print("sin marcadores, se salta:", ruta); continue
        mias = [g for g in grabaciones if sala in g["salas"]]
        cuerpo = "\n".join(bloque(g, sala, n) for n, g in enumerate(mias))
        cuerpo += "\n" + "".join(datos(g) for g in mias if g["canonica"] == sala)
        nuevo = (f'<!-- grabaciones: {sala} -->\n' + cuerpo.rstrip("\n") + '\n  <!-- /grabaciones -->')
        t = patron.sub(lambda m: nuevo, t, count=1)
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(t)
        print(f"{ruta}: {len(mias)} grabaciones, "
              f"{sum(1 for g in mias if g['canonica']==sala)} con ficha canónica")

if __name__ == "__main__":
    main()
