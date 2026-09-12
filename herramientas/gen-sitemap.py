# Genera sitemap.xml desde las paginas del sitio y la historia de git.
#
# Se escribia a mano, y la revision del 12 de septiembre de 2026 encontro el
# lastmod atrasado en 41 de 60 URLs: se regeneraban paginas y nadie volvia a
# tocar la fecha. Ahora la fecha sale de git: la del ultimo commit que cambio
# la pagina, o la de hoy si la pagina tiene cambios sin commitear.
#
# Los alternates por idioma salen de la propia pagina, de sus
# <link rel="alternate" hreflang>, asi que el sitemap no puede contradecir lo
# que declaran las paginas.
#
# Entran todas las paginas salvo el 404 y las que llevan noindex.
#
# Uso:
#   python herramientas/gen-sitemap.py              escribe sitemap.xml
#   python herramientas/gen-sitemap.py --comprobar  sale con 1 si esta desactualizado

import datetime, glob, io, os, re, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"
DESTINO = os.path.join(RAIZ, "sitemap.xml")


def git(*args):
    return subprocess.run(["git", *args], cwd=RAIZ, capture_output=True,
                          text=True, encoding="utf-8").stdout


def paginas():
    for p in glob.glob(os.path.join(RAIZ, "**", "*.html"), recursive=True):
        rel = os.path.relpath(p, RAIZ).replace("\\", "/")
        if rel.startswith((".git/", ".impeccable/", ".claude/")) or rel == "404.html":
            continue
        t = io.open(p, encoding="utf-8").read()
        if "noindex" in t:
            continue
        yield rel, t


def url_de(rel):
    d = os.path.dirname(rel)
    return "/" + (d + "/" if d else "")


def generar():
    hoy = datetime.date.today().isoformat()
    # Una sola llamada para saber que esta sin commitear, con los archivos
    # nuevos uno a uno (sin -uall git daria la carpeta y no el archivo).
    sucios = {l[3:].strip('"') for l in git("status", "--porcelain", "--untracked-files=all").splitlines()}
    filas = []
    for rel, t in paginas():
        if rel in sucios:
            fecha = hoy
        else:
            fecha = git("log", "-1", "--format=%cd", "--date=short", "--", rel).strip() or hoy
        alternos = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', t)
        filas.append((url_de(rel), fecha, alternos))

    # Primero el español, con la portada delante; luego el ingles igual.
    filas.sort(key=lambda f: (f[0].startswith("/en/"), f[0] not in ("/", "/en/"), f[0]))

    salida = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
              'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for u, fecha, alternos in filas:
        salida.append("  <url>")
        salida.append(f"    <loc>{DOMINIO}{u}</loc>")
        salida.append(f"    <lastmod>{fecha}</lastmod>")
        for lang, href in alternos:
            salida.append(f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{href}"/>')
        salida.append("  </url>")
    salida.append("</urlset>")
    return "\n".join(salida) + "\n", len(filas), sum(1 for f in filas if f[2])


def main():
    texto, n, con_pareja = generar()
    if "--comprobar" in sys.argv:
        actual = io.open(DESTINO, encoding="utf-8").read().replace("\r\n", "\n") if os.path.exists(DESTINO) else ""
        if actual != texto:
            print("sitemap.xml no esta al dia: regenera con python herramientas/gen-sitemap.py")
            sys.exit(1)
        print(f"sitemap.xml al dia: {n} URLs")
        return
    io.open(DESTINO, "w", encoding="utf-8", newline="").write(texto)
    print(f"escrito: sitemap.xml · {n} URLs, {con_pareja} con alternates por idioma")


if __name__ == "__main__":
    main()
