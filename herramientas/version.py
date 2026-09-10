# Sube el numero de version de un recurso en todo el sitio de una vez.
#
# El "?v=N" de styles.css, app.js y fonts.css es lo que hace que el navegador
# de un lector que ya estuvo aqui se entere de que el archivo cambio. Si se
# sube en unas paginas y en otras no, unos ven el diseno nuevo y otros el
# viejo, y eso no da error en ninguna parte: solo se ve raro. Por eso
# comprobar.py falla cuando hay versiones mezcladas, y por eso esto existe:
# el cambio esta en medio centenar de archivos y a mano se olvida uno.
#
# Uso:  python herramientas/version.py styles.css 21

import glob, io, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def archivos():
    for patron in ("**/*.html", "herramientas/*.py", "herramientas/*.json"):
        for p in glob.glob(os.path.join(RAIZ, patron), recursive=True):
            if os.sep + ".git" in p:
                continue
            if os.path.basename(p) == "version.py":
                continue          # se reescribiria sus propios comentarios
            yield p


def main():
    if len(sys.argv) != 3:
        sys.exit("uso: python herramientas/version.py <recurso> <numero>")
    recurso, nueva = sys.argv[1], sys.argv[2]
    # Coge las dos formas de escribir lo mismo: la que sale en el HTML y la
    # constante CSS de los generadores.
    # que es la misma version escrita de otra manera.
    patrones = [re.compile(re.escape(recurso) + r"\?v=(\d+)")]
    if recurso == "styles.css":
        patrones.append(re.compile(r'(?<=CSS = ")\?v=(\d+)(?=")'))

    tocados, antes = 0, set()
    for p in archivos():
        t = io.open(p, encoding="utf-8").read()
        nuevo = t
        for pat in patrones:
            antes.update(pat.findall(nuevo))
            nuevo = pat.sub(lambda m: m.group(0).replace(m.group(1), nueva), nuevo)
        if nuevo != t:
            io.open(p, "w", encoding="utf-8", newline="").write(nuevo)
            tocados += 1

    if not tocados:
        sys.exit(f"no encontre ninguna referencia a {recurso}")
    print(f"{recurso}: v={' y v='.join(sorted(antes))} -> v={nueva}, en {tocados} archivos")
    print("Regenera despues, y pasa el comprobador.")


if __name__ == "__main__":
    main()
