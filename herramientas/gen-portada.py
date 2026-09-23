# Escribe el Indice de la casa, en la portada, entre los marcadores
#
#   <!-- indice -->
#     <!-- /indice -->
#
# El resto de index.html se sigue editando a mano, igual que /periodista/ con
# su archivo de prensa.
#
# Por que existe. La portada explicaba de donde viene el nombre de la casa y
# no decia que hay dentro, y seis de las diez puertas del menu no dicen lo que
# guardan: nadie que llegue por primera vez sabe que Tinta-ciones es la poesia
# ni que Laureles son los premios. La salida no es un texto que explique como
# leer la web, que en la portada de un escritor se lee como una disculpa, sino
# un indice que sea la propia navegacion, con una linea por sala que diga que
# es.
#
# Hubo una cifra por sala durante unas horas del 22 de septiembre de 2026, y
# Ernesto la quito: una cantidad cambia rapido y envejece a la vista. Basta
# con decir que es cada habitacion.
#
# Lo unico que se comprueba aqui, y es la razon de que esto sea un generador y
# no HTML escrito a mano: que el indice y el menu digan las mismas salas, en el
# mismo orden. Si divergen, el visitante tendria que aprenderse dos ordenes.
#
# Uso: python herramientas/gen-portada.py

import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion
import pagina
from pagina import esc, esc_attr

RAIZ = pagina.RAIZ


def bloque(P):
    ultimo = len(P["entrada"]) - 1
    out = ['  <div class="reveal reveal-right">',
           f'    <h2 class="section-title">{esc(P["titulo"])}</h2>',
           '    <div class="section-divider"></div>']
    for i, p in enumerate(P["entrada"]):
        margen = "2.5rem" if i == ultimo else "1.25rem"
        out.append(f'    <p class="section-text" style="margin-bottom:{margen};">{esc(p)}</p>')
    out.append('    <ul class="lista-obras indice-casa">')
    for s in P["salas"]:
        out += ['      <li>',
                f'        <strong><a href="{esc_attr(s["url"])}">{esc(s["titulo"])}</a></strong>',
                f'        <span class="obra-linea">{esc(s["texto"])}</span>',
                '      </li>']
    out += ['    </ul>', '  </div>']
    return "\n".join(out)


def main():
    P = json.load(open(os.path.join(RAIZ, "herramientas", "portada.json"), encoding="utf-8"))
    indice = [(s["url"], s["titulo"]) for s in P["salas"]]
    if indice != navegacion.MENU:
        sys.exit("el Índice de la casa y el menú ya no dicen lo mismo.\n"
                 f"  índice: {indice}\n  menú:   {navegacion.MENU}")

    ruta = os.path.join(RAIZ, "index.html")
    with open(ruta, encoding="utf-8", newline="") as f:
        html = f.read().replace("\r\n", "\n")
    marca = re.compile(r"(<!-- indice -->).*?(\n *<!-- /indice -->)", re.S)
    if not marca.search(html):
        sys.exit("index.html no tiene los marcadores <!-- indice --> ... <!-- /indice -->")
    nuevo = marca.sub(lambda x: x.group(1) + "\n" + bloque(P) + x.group(2), html)
    if nuevo != html:
        with open(ruta, "w", encoding="utf-8", newline="") as f:
            f.write(nuevo)
    print(f"escrito: / · índice con {len(indice)} salas"
          + ("" if nuevo != html else " · ya estaba al día"))


if __name__ == "__main__":
    main()
