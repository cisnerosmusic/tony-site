# Comprobador del sitio. Se pasa antes de dar por cerrada una tanda.
#
# Existe porque el trabajo va en ciclos: se construye, una instancia evaluadora
# audita, se corrige, y vuelta a empezar. Todo lo que una maquina puede
# comprobar sola no deberia gastar la atencion de nadie. Cada regla de aqui
# nacio de un fallo real que encontro la auditoria, y esta anotado cual.
#
# Uso:  python herramientas/comprobar.py
# Sale con codigo 1 si algo falla, para poder colgarlo de un workflow.

import json, os, re, sys, glob, io, subprocess

# La consola de Windows va en cp1252 y revienta con cualquier simbolo:
# el comprobador no puede fallar por como imprime.
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from collections import Counter, defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://antoniolopezsanchez.art"

# Tipos que schema.org define de verdad. "Poem" NO existe: da 404, y estuvo
# publicado hasta que la auditoria lo cazo.
TIPOS_VALIDOS = {
    "Person", "WebSite", "WebPage", "CollectionPage", "ProfilePage", "ContactPage",
    "Book", "ShortStory", "CreativeWork", "Article", "NewsArticle", "AudioObject",
    "VideoObject", "ImageObject", "Organization", "Place", "Country",
    "BreadcrumbList", "ItemList", "ListItem", "CollegeOrUniversity",
    "EducationalOrganization",
}

fallos, avisos = [], []


def falla(regla, detalle):
    fallos.append((regla, detalle))


def avisa(regla, detalle):
    avisos.append((regla, detalle))


def paginas():
    for p in glob.glob(os.path.join(RAIZ, "**", "*.html"), recursive=True):
        if os.sep + ".git" in p or os.sep + ".impeccable" in p:
            continue
        yield p


def rel(p):
    return os.path.relpath(p, RAIZ).replace("\\", "/")


def leer(p):
    return io.open(p, encoding="utf-8").read()


def url_de(p):
    r = rel(p)
    if r == "404.html":
        return None
    d = os.path.dirname(r)
    return "/" + (d + "/" if d else "")


# ── 1. Enlaces y recursos internos que no existen ────────────────────────
def enlaces_rotos():
    for p in paginas():
        t = leer(p)
        for m in re.finditer(r'(?:href|src)="(/[^"#?]*)', t):
            destino = m.group(1)
            fisico = os.path.join(RAIZ, destino.strip("/").replace("/", os.sep))
            if destino.endswith("/"):
                fisico = os.path.join(fisico, "index.html")
            if not os.path.exists(fisico):
                falla("enlace roto", f"{rel(p)} apunta a {destino}")


# ── 2. El sitemap y las paginas indexables tienen que coincidir ──────────
def sitemap_cuadra():
    t = leer(os.path.join(RAIZ, "sitemap.xml"))
    en_mapa = set(re.findall(r"<loc>([^<]+)</loc>", t))
    indexables = set()
    for p in paginas():
        c = leer(p)
        if "noindex" in c:
            continue
        u = url_de(p)
        if u:
            indexables.add(DOMINIO + u)
    for u in indexables - en_mapa:
        falla("fuera del sitemap", u)
    for u in en_mapa - indexables:
        falla("en el sitemap pero no indexable", u)


# ── 3. JSON-LD: que sea JSON y que los tipos existan ─────────────────────
def datos_estructurados():
    for p in paginas():
        for b in re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
                            leer(p), re.S):
            try:
                d = json.loads(b)
            except Exception as e:
                falla("JSON-LD invalido", f"{rel(p)}: {e}")
                continue
            for tipo in re.findall(r'"@type":\s*"([^"]+)"', b):
                if tipo not in TIPOS_VALIDOS:
                    falla("tipo Schema inexistente", f"{rel(p)}: {tipo}")


# ── 4. Titulos y descripciones: unicos y en rango ────────────────────────
def metadatos():
    titulos, descripciones = Counter(), Counter()
    for p in paginas():
        t = leer(p)
        if "noindex" in t:
            continue
        mt = re.search(r"<title>(.*?)</title>", t, re.S)
        md = re.search(r'<meta name="description" content="([^"]*)"', t)
        if not mt:
            falla("sin title", rel(p)); continue
        if not md:
            falla("sin description", rel(p)); continue
        titulos[mt.group(1).strip()] += 1
        descripciones[md.group(1).strip()] += 1
        if len(mt.group(1)) > 65:
            avisa("title largo", f"{rel(p)}: {len(mt.group(1))} caracteres")
        if len(md.group(1)) > 165:
            avisa("description larga", f"{rel(p)}: {len(md.group(1))} caracteres")
        if len(re.findall(r"<h1[ >]", t)) != 1:
            falla("h1 no unico", rel(p))
    for x, n in list(titulos.items()) + list(descripciones.items()):
        if n > 1:
            falla("metadato duplicado", f'"{x[:60]}" en {n} paginas')


# ── 5. Una sola version de CSS y de JS en todo el sitio ──────────────────
def versiones():
    for recurso in ("styles.css", "app.js", "fonts.css"):
        vistas = defaultdict(list)
        for p in paginas():
            for v in re.findall(recurso + r"\?v=(\d+)", leer(p)):
                vistas[v].append(rel(p))
        if len(vistas) > 1:
            falla("versiones mezcladas", f"{recurso}: " +
                  ", ".join(f"v={v} en {len(ps)}" for v, ps in sorted(vistas.items())))


# ── 6. Lo generado coincide con los generadores ──────────────────────────
# Se compara el HTML antes y despues de regenerar, no contra git: tener
# trabajo sin commitear es normal, que un generador ya no reproduzca su
# pagina no lo es.
def generado_al_dia():
    antes = {rel(p): leer(p) for p in paginas()}
    ordenes = [["python", "herramientas/gen-cuento.py"],
               ["python", "herramientas/gen-poemas.py"],
               ["python", "herramientas/gen-decimitas.py"],
               ["python", "herramientas/gen-sonata.py"],
               ["python", "herramientas/gen-farraluque.py"],
               ["python", "herramientas/gen-audios.py"],
               ["python", "herramientas/gen-legal.py"]]
    for m in sorted(glob.glob(os.path.join(RAIZ, "herramientas", "libros", "*.json"))):
        ordenes.append(["python", "herramientas/gen-libro.py", os.path.relpath(m, RAIZ)])
    for o in ordenes:
        r = subprocess.run(o, cwd=RAIZ, capture_output=True, text=True)
        if r.returncode:
            falla("generador con error", f"{' '.join(o[1:])}: {r.stderr.strip()[:120]}")
    despues = {rel(p): leer(p) for p in paginas()}
    sucios = [k for k, v in despues.items() if antes.get(k) != v]
    if sucios:
        falla("HTML desactualizado", "regenerar cambia: " + ", ".join(sucios[:6]))


# ── 7. Higiene que la auditoria ya pillo una vez ─────────────────────────
def higiene():
    # Rutas absolutas de una maquina concreta
    for p in glob.glob(os.path.join(RAIZ, "herramientas", "**", "*.*"), recursive=True):
        if os.path.basename(p) == "comprobar.py":
            continue          # contiene la cadena porque la busca
        if p.endswith((".json", ".py")) and "C:/Users" in leer(p):
            falla("ruta absoluta", rel(p))
    # Raya larga en texto publico
    for p in paginas():
        cuerpo = re.sub(r"<script.*?</script>", "", leer(p), flags=re.S)
        cuerpo = re.sub(r"<[^>]+>", "", cuerpo)
        if "\u2014" in cuerpo:
            falla("raya larga en texto publico", rel(p))
    # Imagenes sin alt o sin medidas, que provocan saltos de maqueta
    for p in paginas():
        for img in re.findall(r"<img [^>]*>", leer(p)):
            if "alt=" not in img:
                falla("imagen sin alt", f"{rel(p)}: {img[:60]}")
            if "width=" not in img or "height=" not in img:
                avisa("imagen sin medidas", f"{rel(p)}: {img[:60]}")
    # Enlaces externos sin rel noopener
    for p in paginas():
        for a in re.findall(r"<a [^>]*target=\"_blank\"[^>]*>", leer(p)):
            if "noopener" not in a:
                falla("target _blank sin noopener", f"{rel(p)}: {a[:70]}")
    # Menu: nada de onclick, y el script que lo sustituye tiene que estar
    for p in paginas():
        t = leer(p)
        if "classList.toggle" in t and "app.js" not in t:
            falla("menu sin script", rel(p))
        if "nav-hamburger" in t and "aria-expanded" not in t:
            falla("hamburguesa sin aria-expanded", rel(p))
        if "nav-hamburger" in t and "app.js" not in t:
            falla("menu sin app.js", rel(p))


# ── 8. La navegacion, con el comprobador que ya existe ───────────────────
def navegacion_alineada():
    r = subprocess.run(["python", "herramientas/unificar-nav.py", "--comprobar"],
                       cwd=RAIZ, capture_output=True, text=True)
    if r.returncode:
        falla("navegacion desalineada", r.stdout.strip().splitlines()[-1] if r.stdout else "")


def main():
    enlaces_rotos()
    sitemap_cuadra()
    datos_estructurados()
    metadatos()
    versiones()
    higiene()
    navegacion_alineada()
    generado_al_dia()

    if avisos:
        print(f"\nAVISOS ({len(avisos)}), no bloquean:")
        for regla, d in avisos[:20]:
            print(f"  - {regla}: {d}")
        if len(avisos) > 20:
            print(f"  - y {len(avisos)-20} mas")

    if fallos:
        print(f"\nFALLOS ({len(fallos)}):")
        for regla, d in fallos:
            print(f"  FALLO  {regla}: {d}")
        print("\nNo cerrar la tanda con fallos abiertos.")
        sys.exit(1)

    n = len(list(paginas()))
    print(f"\nTodo en orden: {n} páginas comprobadas, 0 fallos, {len(avisos)} avisos.")


if __name__ == "__main__":
    main()
