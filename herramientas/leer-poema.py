# Analiza un poema en texto plano y separa sus partes: titulo, epigrafe con su
# autor, cuerpo y colofon de fecha y lugar.
#
# Existe por una razon concreta: varios poemas del autor son glosas que abren
# con una estrofa de Jose Marti o de Lezama Lima. Esos versos NO son suyos y no
# pueden salir en la pagina como si lo fueran. El epigrafe se detecta y se
# marca aparte, con su atribucion visible.
#
# Uso: python herramientas/leer-poema.py "<carpeta>"   (informe, no escribe nada)

import os, re, sys, io, json

POETAS = ("José Martí", "José Lezama Lima", "Jose Marti", "Lezama Lima")
FECHA = re.compile(r"\b(1[89]\d{2}|20\d{2})\b")


def partes(texto):
    lineas = [l.rstrip() for l in texto.replace("\r", "").split("\n")]
    while lineas and not lineas[0]:
        lineas.pop(0)

    # Titulo: las primeras lineas seguidas en mayusculas o con numeracion romana
    titulo = []
    i = 0
    while i < len(lineas) and lineas[i]:
        l = lineas[i].strip()
        romano = re.fullmatch(r"\(?[IVXL]+\)?", l)
        if l.isupper() or romano:
            titulo.append(l); i += 1
        else:
            break
    while i < len(lineas) and not lineas[i]:
        i += 1

    # Epigrafe: bloque que termina en el nombre de un poeta
    epigrafe, autor = [], None
    j = i
    bloque = []
    while j < len(lineas):
        l = lineas[j].strip()
        if l in POETAS:
            epigrafe, autor = bloque, l
            j += 1
            while j < len(lineas) and not lineas[j]:
                j += 1
            i = j
            break
        if not l and bloque and len(bloque) > 6:
            break                      # demasiado largo para ser epigrafe
        bloque.append(lineas[j]); j += 1

    # Colofon: ultimas lineas con año
    cuerpo = lineas[i:]
    while cuerpo and not cuerpo[-1]:
        cuerpo.pop()
    # Colofon: el autor lo escribe como fecha y a veces lugar o circunstancia,
    # y no siempre la fecha va la ultima ("26 y Marzo del 2012 / Alamar", o
    # "20 y junio y 2025 / (en solsticio y apagon)"). Se busca la fecha entre
    # las tres ultimas lineas y se toma desde ahi hasta el final.
    colofon = []
    ultimas = [k for k in range(len(cuerpo) - 1, max(-1, len(cuerpo) - 5), -1) if cuerpo[k].strip()]
    corte = next((k for k in ultimas if FECHA.search(cuerpo[k]) and len(cuerpo[k].strip()) < 45), None)
    if corte is not None:
        colofon = [l.strip() for l in cuerpo[corte:] if l.strip()]
        cuerpo = cuerpo[:corte]
        while cuerpo and not cuerpo[-1]:
            cuerpo.pop()

    return {"titulo": titulo,
            "epigrafe": [l for l in epigrafe if l.strip()],
            "epigrafe_autor": autor,
            "cuerpo": cuerpo,
            "colofon": colofon}


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    carpeta = sys.argv[1]
    for f in sorted(os.listdir(carpeta)):
        if not f.endswith(".txt"):
            continue
        p = partes(open(os.path.join(carpeta, f), encoding="utf-8").read())
        print("=" * 74)
        print(f[:-4])
        print("-" * 74)
        print("  TÍTULO   :", " / ".join(p["titulo"]) or "(ninguno)")
        if p["epigrafe_autor"]:
            print("  EPÍGRAFE :", len(p["epigrafe"]), "versos de", p["epigrafe_autor"])
            for l in p["epigrafe"]:
                print("             ", l)
        print("  CUERPO   :", len([l for l in p["cuerpo"] if l.strip()]), "versos")
        print("             ", (p["cuerpo"][0] if p["cuerpo"] else "")[:64])
        print("             ...", (p["cuerpo"][-1] if p["cuerpo"] else "")[:64])
        print("  COLOFÓN  :", " · ".join(p["colofon"]) or "(ninguno)")
        print()
