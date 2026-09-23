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

# El lema de la casa tiene fuente propia, y es el unico caso.
#
# "bene scriptus" se escribe en cursiva, y la cursiva completa pesa 28,7 KB. En
# la portada esa cursiva se precargaba, asi que salia a competir por el ancho
# de banda en el mismo instante que el retrato, que es el elemento mayor de la
# primera pantalla: medido el 23 de septiembre de 2026, 94,9 KB pidiendose a la
# vez a los 640 ms, y el retrato tardando 1.193 ms en bajar.
#
# Estas dos palabras necesitan once glifos. Recortada a ellos, la misma cursiva
# pesa 2,6 KB, asi que se precarga esta y la completa deja de ir en la carrera:
# 26,1 KB menos compitiendo con el retrato.
#
# Se puede hacer porque el lema entra con 1,45 s de retardo (ver styles.css):
# no hay prisa por su tipografia, pero si por que sea la correcta desde el
# primer fotograma del fundido, y con 2,6 KB lo es.
#
# El texto se declara aqui y comprobar.py comprueba que la fuente cubra lo que
# las paginas escriben de verdad: si el lema cambia y nadie vuelve a recortar,
# salta.
LEMA_ORIGEN = "cormorant-garamond-400-italic.woff2"
LEMA_DESTINO = "lema.woff2"
LEMA_TEXTO = "bene scriptus"


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

    # Y la fuente del lema, que sale de la misma cursiva pero con once glifos.
    o = os.path.join(ORIGEN, LEMA_ORIGEN)
    d = os.path.join(DESTINO, LEMA_DESTINO)
    letras = sorted(set(LEMA_TEXTO))
    r = subprocess.run([sys.executable, "-m", "fontTools.subset", o,
                        "--unicodes=" + ",".join("U+%04X" % ord(c) for c in letras),
                        "--layout-features=" + FUNCIONES,
                        "--flavor=woff2", "--output-file=" + d],
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"fallo al recortar el lema: {r.stderr.strip()[:200]}")
    print("%-42s %6.1f -> %5.1f KB  (solo «%s», %d glifos)"
          % (LEMA_DESTINO, os.path.getsize(os.path.join(DESTINO, LEMA_ORIGEN)) / 1024,
             os.path.getsize(d) / 1024, LEMA_TEXTO, len(letras)))

    print("Sube el ?v=N de fonts.css si cambio el juego de caracteres.")


if __name__ == "__main__":
    main()
