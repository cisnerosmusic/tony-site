# Cuenta las cadenas de texto de cada idioma de fuera.
#
# Por que existe. El README y AGENTS.md llevaban escrita una cifra ("1048
# cadenas por idioma") que nadie podia reproducir: el conteo se habia hecho a
# mano una vez, y cada tanda de contenido la dejaba un poco mas vieja sin que
# se notara. La auditoria del 28 de septiembre de 2026 la encontro desfasada.
#
# Lo que de verdad importa de esa cifra no es el numero, sino que **los cuatro
# idiomas den el mismo**: si uno se queda corto, es que a ese idioma le falta
# una capa, y eso no se ve mirando la pagina, que sale igual de bonita con la
# seccion ausente. Asi que la cifra se cuenta aqui, con un metodo escrito, y
# se puede volver a comprobar en cualquier momento.
#
# Metodo: se cuentan las hojas de texto de todo lo que un idioma trae suyo,
# que son su zona, sus capas de sala, sus catorce capas de libro y su bloque
# de idiomas.json. No se cuentan las notas internas (las claves que empiezan
# por "_"), que no salen a ninguna pagina.
#
# Uso: python herramientas/cadenas.py

import json, os, sys, glob

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = os.path.join(RAIZ, "herramientas")
IDIOMAS = ["en", "fr", "it", "pt"]


def hojas(x):
    """Cuenta las cadenas que hay dentro de un JSON, a cualquier profundidad."""
    if isinstance(x, str):
        return 1
    if isinstance(x, list):
        return sum(hojas(v) for v in x)
    if isinstance(x, dict):
        return sum(hojas(v) for k, v in x.items() if not k.startswith("_"))
    return 0


def cuenta(idioma):
    partes = {}
    zona = os.path.join(H, f"zona.{idioma}.json")
    partes["zona"] = hojas(json.load(open(zona, encoding="utf-8"))) if os.path.exists(zona) else 0

    salas = 0
    for r in sorted(glob.glob(os.path.join(H, f"*.{idioma}.json"))):
        if os.path.basename(r).startswith("zona."):
            continue
        salas += hojas(json.load(open(r, encoding="utf-8")))
    partes["salas"] = salas

    libros = 0
    for r in sorted(glob.glob(os.path.join(H, "libros", idioma, "*.json"))):
        libros += hojas(json.load(open(r, encoding="utf-8")))
    partes["libros"] = libros

    todos = json.load(open(os.path.join(H, "idiomas.json"), encoding="utf-8"))
    partes["interfaz"] = hojas(todos.get(idioma, {}))
    return partes


def main():
    total = {}
    print(f"{'idioma':8} {'zona':>7} {'salas':>7} {'libros':>7} {'interfaz':>9} {'total':>7}")
    for idioma in IDIOMAS:
        p = cuenta(idioma)
        t = sum(p.values())
        total[idioma] = t
        print(f"{idioma:8} {p['zona']:7} {p['salas']:7} {p['libros']:7} {p['interfaz']:9} {t:7}")
    iguales = len(set(total.values())) == 1
    print("\nlos cuatro idiomas dan la misma cifra" if iguales
          else "\nOJO: no coinciden, a algun idioma le falta una capa")
    sys.exit(0 if iguales else 1)


if __name__ == "__main__":
    main()
