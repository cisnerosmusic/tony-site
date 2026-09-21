# Recorta las fuentes servidas a lo que el sitio usa de verdad.
#
# Las de Google vienen con el bloque latino entero y con todas las funciones
# OpenType de la familia: versalitas, cifras antiguas, alternativas, swashes.
# Cormorant Garamond trae muchas, y el sitio no usa ninguna: no hay un solo
# font-feature-settings ni font-variant en styles.css. Eran 52 KB de los 217
# que pesaban las fuentes de la portada, y en las fuentes esta el 68% de esa
# pagina: mas que las imagenes, el CSS y el HTML juntos.
#
# Los originales de Google viven en fonts/originales/ y no se sirven. De ahi
# sale cada vez lo que se publica, asi que añadir un caracter o una funcion es
# volver a correr esto, no buscar de nuevo los archivos.
#
# El riesgo de recortar es publicar manana un texto con un caracter que no
# quedo dentro. Por eso comprobar.py verifica que cada caracter que sale en
# el sitio existe en cada fuente servida, y falla si alguno se cae.
#
# Uso: python herramientas/subset-fuentes.py

import os, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEN = os.path.join(RAIZ, "fonts", "originales")
DESTINO = os.path.join(RAIZ, "fonts")

# Latino basico y suplemento enteros, mas la puntuacion tipografica. Es mucho
# mas de lo que el sitio usa hoy (104 caracteres, todos dentro), y esa holgura
# es deliberada: un texto nuevo del autor no deberia romper nada.
UNICODES = "U+0020-007E,U+00A0-00FF,U+0131,U+0152-0153,U+2000-206F,U+20AC,U+2122,U+2212"

# Lo que se conserva: interletraje, ligaduras comunes y formas locales. Todo
# lo demas sobra mientras el sitio no lo pida desde el CSS.
FUNCIONES = "kern,liga,clig,calt,locl"


def main():
    if not os.path.isdir(ORIGEN):
        sys.exit("falta fonts/originales/, que es de donde sale todo esto")
    antes = despues = 0
    for f in sorted(os.listdir(ORIGEN)):
        if not f.endswith(".woff2"):
            continue
        o, d = os.path.join(ORIGEN, f), os.path.join(DESTINO, f)
        r = subprocess.run([sys.executable, "-m", "fontTools.subset", o,
                            "--unicodes=" + UNICODES,
                            "--layout-features=" + FUNCIONES,
                            "--flavor=woff2", "--output-file=" + d],
                           capture_output=True, text=True)
        if r.returncode:
            sys.exit(f"fallo al recortar {f}: {r.stderr.strip()[:200]}")
        antes += os.path.getsize(o)
        despues += os.path.getsize(d)
        print("%-42s %6.1f -> %5.1f KB" % (f, os.path.getsize(o) / 1024, os.path.getsize(d) / 1024))
    print("total: %.0f KB -> %.0f KB, %.0f KB menos" % (antes / 1024, despues / 1024, (antes - despues) / 1024))
    print("Sube el ?v=N de fonts.css si cambio el juego de caracteres.")


if __name__ == "__main__":
    main()
