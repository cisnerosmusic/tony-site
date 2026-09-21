# Genera la postal de cada libro: la imagen que sale al compartir su pagina
# en redes, en WhatsApp o en un correo.
#
# Antes la imagen social era la cubierta, que es vertical, y las redes la
# recortaban por el centro: salia media cara del dibujo y ningun titulo.
# Ernesto fijo el diseño el 21 de septiembre de 2026: la cubierta pequeña a la
# izquierda y el titulo del libro a la derecha, centrado. Debajo del titulo va
# el nombre del autor, porque una postal que circula sola tiene que decir de
# quien es.
#
# Sale en 1200 x 630, que es la medida que piden Facebook, WhatsApp, LinkedIn
# y X para la tarjeta grande, y en JPEG, que es lo que todas leen sin
# sorpresas: con WebP alguna todavia devuelve la tarjeta vacia.
#
# El titulo no se traduce, asi que una postal sirve para las paginas del libro
# en todos los idiomas.
#
# Uso: python herramientas/gen-tarjetas.py

import glob, io, json, os, sys
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, "img", "tarjetas")
ANCHO, ALTO = 1200, 630

# Los mismos colores que styles.css
FONDO_ARRIBA = (10, 12, 31)      # --bg-deep
FONDO_ABAJO = (26, 29, 74)       # --navy
ORO = (212, 160, 48)             # --gold
TEXTO = (200, 195, 185)          # --text-secondary


def fuente(nombre, tam):
    """Pillow no lee WOFF2 en todas las instalaciones: se pasa a TTF en
    memoria desde el original completo, no desde el recortado."""
    tt = TTFont(os.path.join(RAIZ, "fonts", "originales", nombre))
    tt.flavor = None
    b = io.BytesIO()
    tt.save(b)
    b.seek(0)
    return ImageFont.truetype(b, tam)


def fondo():
    """Degradado vertical del navy profundo al navy de la casa."""
    im = Image.new("RGB", (ANCHO, ALTO))
    d = ImageDraw.Draw(im)
    for y in range(ALTO):
        t = y / (ALTO - 1)
        d.line([(0, y), (ANCHO, y)],
               fill=tuple(round(a + (b - a) * t) for a, b in zip(FONDO_ARRIBA, FONDO_ABAJO)))
    return im


def partir(texto, f, ancho, d):
    """Parte el titulo en lineas que quepan en el ancho dado."""
    lineas, actual = [], ""
    for palabra in texto.split():
        prueba = (actual + " " + palabra).strip()
        if d.textlength(prueba, font=f) <= ancho:
            actual = prueba
        else:
            if actual:
                lineas.append(actual)
            actual = palabra
    if actual:
        lineas.append(actual)
    return lineas


def tarjeta(m):
    im = fondo()
    d = ImageDraw.Draw(im)

    # La cubierta, a la izquierda, con un filete dorado tenue como en el sitio
    cub = Image.open(os.path.join(RAIZ, m["cubierta"].lstrip("/"))).convert("RGB")
    alto_c = 420
    ancho_c = round(cub.width * alto_c / cub.height)
    if ancho_c > 320:
        ancho_c = 320
        alto_c = round(cub.height * ancho_c / cub.width)
    cub = cub.resize((ancho_c, alto_c), Image.LANCZOS)
    x_c, y_c = 110, (ALTO - alto_c) // 2
    # Sombra difuminada, como la de la cubierta en la pagina del libro, y no
    # un bloque oscuro pegado detras.
    mascara = Image.new("L", (ANCHO, ALTO), 0)
    ImageDraw.Draw(mascara).rectangle([x_c + 6, y_c + 14, x_c + ancho_c + 6, y_c + alto_c + 14], fill=150)
    mascara = mascara.filter(ImageFilter.GaussianBlur(18))
    im.paste(Image.new("RGB", (ANCHO, ALTO), (2, 3, 10)), (0, 0), mascara)
    im.paste(cub, (x_c, y_c))
    d.rectangle([x_c - 1, y_c - 1, x_c + ancho_c, y_c + alto_c], outline=(88, 70, 34), width=1)

    # El titulo, a la derecha y centrado en su zona. Si lleva subtitulo entre
    # parentesis ("Cuentos de muñecas (¡A leer y a jugar!)"), el subtitulo va
    # en su propia linea y mas pequeño: partido a mitad salia "(¡A" suelto.
    izq = x_c + ancho_c + 80
    der = ANCHO - 90
    zona = der - izq
    titulo, subtitulo = m["titulo"], ""
    if " (" in titulo and titulo.endswith(")"):
        titulo, subtitulo = titulo[:-1].split(" (", 1)
    for tam in range(66, 33, -2):
        f = fuente("cinzel-400.woff2", tam)
        lineas = partir(titulo.upper(), f, zona, d)
        if len(lineas) <= 4:
            break
    interlinea = round(tam * 1.28)
    f_sub = fuente("cinzel-400.woff2", max(26, round(tam * 0.5)))
    lineas_sub = partir(subtitulo.upper(), f_sub, zona, d) if subtitulo else []
    inter_sub = round(f_sub.size * 1.35)

    # En los volumenes colectivos Antonio no es el autor del libro, sino de
    # algunos de sus textos, y la postal no puede decir otra cosa. Se detecta
    # igual que en la ficha, por el campo de autoria, y con la misma formula
    # que el aviso de derechos de esos libros.
    colectiva = any(k.lower().startswith("autor") for k in m["ficha"])
    autor = "Con textos de Antonio López Sánchez" if colectiva else "Antonio López Sánchez"
    f_autor = fuente("cormorant-garamond-400-italic.woff2", 34)

    alto_bloque = (len(lineas) * interlinea + (len(lineas_sub) * inter_sub + 12 if lineas_sub else 0)
                   + 30 + 2 + 32 + 40)
    y = (ALTO - alto_bloque) // 2
    centro = izq + zona / 2
    for l in lineas:
        d.text((centro, y), l, font=f, fill=ORO, anchor="ma")
        y += interlinea
    if lineas_sub:
        y += 12
        for l in lineas_sub:
            d.text((centro, y), l, font=f_sub, fill=ORO, anchor="ma")
            y += inter_sub
    y += 30
    d.line([(centro - 30, y), (centro + 30, y)], fill=ORO, width=2)
    y += 32
    d.text((centro, y), autor, font=f_autor, fill=TEXTO, anchor="ma")
    return im


def main():
    os.makedirs(DESTINO, exist_ok=True)
    for r in sorted(glob.glob(os.path.join(RAIZ, "herramientas", "libros", "*.json"))):
        m = json.load(open(r, encoding="utf-8"))
        destino = os.path.join(DESTINO, m["slug"] + ".jpg")
        tarjeta(m).save(destino, "JPEG", quality=84, optimize=True, progressive=True)
        print("%-44s %5.1f KB" % (os.path.relpath(destino, RAIZ), os.path.getsize(destino) / 1024))


if __name__ == "__main__":
    main()
