# Escribe el indice de la casa, en la portada, entre los marcadores
#
#   <!-- indice -->
#     <!-- /indice -->
#
# El resto de index.html se sigue editando a mano, igual que /periodista/ con
# su archivo de prensa.
#
# Por que existe. La portada explicaba de donde viene el nombre de la casa y
# no decia que hubiera dentro: catorce libros, once cuentos, cuarenta poemas y
# decimas, veintidos trabajos de prensa. Y seis de las diez puertas del menu
# no dicen lo que guardan: nadie que llegue por primera vez sabe que
# Tinta-ciones es la poesia, ni que Laureles son los premios. La salida no es
# un texto que explique como leer la web, que en la portada de un escritor se
# lee como una disculpa, sino un indice que sea la propia navegacion, con una
# cifra por sala. La cifra hace el trabajo del mapa: dice el tamaño antes de
# entrar, y da una razon para abrir esa puerta y no otra.
#
# Las cifras NO se escriben a mano en ningun sitio: se cuentan aqui desde los
# mismos manifiestos que publican cada sala. Un cuento nuevo cambia el numero
# de Contarte solo, y el comprobador falla si la portada se queda atras.
#
# Uso: python herramientas/gen-portada.py

import glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pagina
from pagina import esc, esc_attr

RAIZ = pagina.RAIZ


def m(*partes):
    with open(os.path.join(RAIZ, "herramientas", *partes), encoding="utf-8") as f:
        return json.load(f)


def cifras():
    """Cada sala, contada desde donde vive de verdad."""
    poemas = m("poemas.json")
    libros = [m("libros", os.path.basename(p)) for p in
              sorted(glob.glob(os.path.join(RAIZ, "herramientas", "libros", "*.json")))]
    # Plano abierto no tiene manifiesto propio: sus piezas son los reproductores
    # y el enlace de video que ya estan en la pagina, asi que se cuentan ahi.
    plano = open(os.path.join(RAIZ, "plano-abierto", "index.html"), encoding="utf-8").read()
    return {
        "libros": len(libros),
        "ineditos": len(m("ineditos.json")["novelas"]),
        "poesia": len(poemas["sueltos"]) + len(poemas["glosas"]) + len(m("decimitas.json")["decimitas"]),
        "cuentos": len(m("cuentos.json")),
        "trova": sum(1 for l in libros if l.get("seccion") == "/trova/"),
        "plano": plano.count("<audio") + plano.count("<video") + plano.count("youtu.be"),
        "premios": len(m("laureles.json")["premios"]),
        "periodismo": len(m("periodismo.json")["trabajos"]),
    }


def bloque():
    P = m("portada.json")
    n = cifras()
    ultimo = len(P["entrada"]) - 1
    out = ['  <div class="reveal reveal-right">',
           f'    <h2 class="section-title">{esc(P["titulo"])}</h2>',
           '    <div class="section-divider"></div>']
    for i, p in enumerate(P["entrada"]):
        margen = "3rem" if i == ultimo else "1.25rem"
        out.append(f'    <p class="section-text" style="margin-bottom:{margen};">{esc(p)}</p>')
    out.append('  </div>')

    for s in P["salas"]:
        if s["cifra"] not in n:
            sys.exit(f"portada.json: no se sabe contar «{s['cifra']}»")
        out += ['',
                '  <article class="laurel-item reveal reveal-right">',
                f'    <p class="laurel-anio">{n[s["cifra"]]}</p>',
                '    <div>',
                f'      <h3 class="libro-titulo"><a href="{esc_attr(s["url"])}">{esc(s["titulo"])}</a></h3>',
                f'      <p class="section-text">{esc(s["texto"])}</p>',
                '    </div>',
                '  </article>']

    c = P["cierre"]
    out += ['', '  <p class="section-text reveal reveal-right" style="margin-top:2.5rem;">'
                f'{esc(c["texto"])} <a href="{esc_attr(c["url"])}">{esc(c["enlace"])}</a>.</p>']
    return "\n".join(out)


def main():
    ruta = os.path.join(RAIZ, "index.html")
    with open(ruta, encoding="utf-8", newline="") as f:
        html = f.read().replace("\r\n", "\n")
    marca = re.compile(r"(<!-- indice -->).*?(\n *<!-- /indice -->)", re.S)
    if not marca.search(html):
        sys.exit("index.html no tiene los marcadores <!-- indice --> ... <!-- /indice -->")
    nuevo = marca.sub(lambda x: x.group(1) + "\n" + bloque() + x.group(2), html)
    if nuevo != html:
        with open(ruta, "w", encoding="utf-8", newline="") as f:
            f.write(nuevo)
    n = cifras()
    print("escrito: / · índice con " + ", ".join(f"{v} {k}" for k, v in n.items())
          + ("" if nuevo != html else " · ya estaba al día"))


if __name__ == "__main__":
    main()
