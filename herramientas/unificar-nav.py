# Reescribe el menu superior y el pie de todas las paginas en español desde
# herramientas/navegacion.py, que es la unica definicion.
#
# Las paginas generadas (libros y cuentos) ya la importan, asi que esto es para
# las que se editan a mano. Correrlo dos veces no cambia nada.
#
# Quedan fuera a proposito:
#   /en/                paginas en ingles, con su propia navegacion
#   /novelas/, /poeta/  redirecciones blandas, sin cabecera ni pie
#   /404.html           lo escribe gen-404.py, con los dos idiomas
#
# Uso: python herramientas/unificar-nav.py [--comprobar]

import io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import navegacion

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FUERA = ("en/", "novelas/", "poeta/", "404.html")


def ruta_web(rel):
    d = os.path.dirname(rel)
    return "/" + (d + "/" if d else "")


def main(solo_comprobar=False):
    tocadas, revisadas = [], 0
    for base, _, files in os.walk(RAIZ):
        if ".git" in base or ".impeccable" in base:
            continue
        for f in files:
            if not f.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(base, f), RAIZ).replace("\\", "/")
            if any(rel.startswith(x) for x in FUERA):
                continue
            p = os.path.join(base, f)
            t = io.open(p, encoding="utf-8").read()
            if '<ul class="nav-links"' not in t:
                continue
            revisadas += 1
            activa = navegacion.seccion_de(ruta_web(rel))
            # El pie solo marca pagina actual si es la portada de la seccion
            activa_pie = activa if rel.endswith("index.html") and ruta_web(rel) == activa else None

            patron_menu = re.compile(r'(<ul class="nav-links"[^>]*>\n).*?(\n  </ul>)', re.S)
            if not patron_menu.search(t):
                # Sin esto, un cambio en el marcado del menu haria que el
                # reemplazo no encajase y --comprobar diera un falso aprobado.
                print("  AVISO, no encuentro el menu en:", rel)
                continue
            nuevo = patron_menu.sub(
                lambda m: m.group(1) + navegacion.menu_html(activa) + m.group(2), t)
            nuevo = re.sub(r'(<nav class="footer-nav" aria-label="Secciones">\n).*?(\n  </nav>)',
                           lambda m: m.group(1) + navegacion.pie_html(activa_pie) + m.group(2), nuevo, flags=re.S)
            if nuevo != t:
                tocadas.append(rel)
                if not solo_comprobar:
                    io.open(p, "w", encoding="utf-8", newline="").write(nuevo)

    print(f"paginas revisadas: {revisadas}")
    if solo_comprobar:
        print(f"desalineadas: {len(tocadas)}")
        for x in tocadas:
            print("  ", x)
        sys.exit(1 if tocadas else 0)
    print(f"paginas corregidas: {len(tocadas)}")
    for x in tocadas:
        print("  ", x)


if __name__ == "__main__":
    main("--comprobar" in sys.argv)
