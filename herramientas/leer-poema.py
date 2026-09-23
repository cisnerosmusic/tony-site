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
MES = re.compile(r"\b(enero|febrero|marzo|abril|mayo|junio|julio|agosto|"
                 r"septiembre|octubre|noviembre|diciembre)\b", re.IGNORECASE)


def linea_de_fecha(l):
    """Una linea corta que solo carga fecha: con año, o con nombre de mes."""
    l = l.strip()
    return bool(l) and len(l) < 45 and bool(FECHA.search(l) or MES.search(l))


# El sello con que el autor cierra sus textos: «Hallado en Ala del Mar, [fecha].
# bene scriptus». Es el mismo del que sale el nombre de la casa.
SELLO = re.compile(r"^(hallado en\b|bene scriptus$|alamar\b)", re.IGNORECASE)


def parece_colofon(l):
    """Una linea del final que es fecha o sello, no texto de la obra.

    Sirve para detectar, no para borrar a ciegas: el que la use tiene que
    declarar en su manifiesto las lineas exactas que quita, y pararse si
    aparece una que no esperaba. Un cuento puede acabar de verdad con una
    frase corta que lleve un mes dentro, y eso no se recorta por estadistica.
    Lo pidio Tony el 22 de septiembre de 2026 para Contarte y para Ineditos,
    como ya estaba hecho en los poemas."""
    l = l.strip()
    return bool(l) and (linea_de_fecha(l) or bool(SELLO.match(l)))


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
        # El autor fecha a veces en dos tiempos: "1997 MAYO 15" y debajo "2002
        # FEBRERO 25", o parte la fecha en "15 y Junio" y, tras un blanco,
        # "2015". Hallada una, se sigue subiendo mientras arriba haya mas
        # lineas de fecha, para que ninguna se quede colada entre los versos.
        k = corte - 1
        while k >= 0:
            if not cuerpo[k].strip():
                k -= 1
                continue
            if linea_de_fecha(cuerpo[k]):
                corte = k
                k -= 1
                continue
            break
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
