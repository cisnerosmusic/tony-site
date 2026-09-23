# Escribe llms.txt, el mapa del sitio para los modelos de lenguaje.
#
# Existe porque el archivo se escribio a mano y se quedo atras: el 22 de
# septiembre de 2026 seguia diciendo que Contarte tenia siete cuentos cuando ya
# eran once, que De-Cimitas tenia siete decimas cuando eran veinte, que
# Ineditos era "obras que esperan editorial" cuando ya estaban las cuatro
# novelas publicadas con sinopsis y fragmentos, y no sabia que existiera el
# archivo de prensa. Doce dias de retraso que nadie veia, porque llms.txt no se
# mira nunca: lo leen ChatGPT y Perplexity, no las personas.
#
# Asi que ahora se genera. Las listas salen de los mismos manifiestos que el
# sitio, y la prosa que no sale de ningun otro sitio vive en llms.json, con {n}
# donde va un numero. Si entra un libro, un cuento o un trabajo, aparece aqui
# solo, y el comprobador falla si el archivo no esta al dia.
#
# Uso: python herramientas/gen-llms.py

import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pagina

RAIZ = pagina.RAIZ
D = pagina.DOMINIO


def m(*partes):
    with open(os.path.join(RAIZ, "herramientas", *partes), encoding="utf-8") as f:
        return json.load(f)


def sin_html(t):
    """Los textos de los manifiestos traen enlaces: aqui sobran, porque cada
    entrada ya lleva el suyo delante."""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()


def main():
    P = m("llms.json")
    # El catalogo español esta escrito a mano y no declara grupos; el ingles si,
    # y es el mismo reparto por generos. Se usa ese para ordenar, que ademas es
    # el orden que ya tenia este archivo.
    libros_cfg = m("idiomas.json")["en"]
    cuentos = m("cuentos.json")
    poemas = m("poemas.json")
    decimitas = m("decimitas.json")["decimitas"]
    prensa = m("periodismo.json")
    ineditos = m("ineditos.json")
    laureles = m("laureles.json")["premios"]

    # El orden de los libros es el del catalogo español, que es el que el autor
    # y Ernesto fijaron; aqui solo se recorre.
    slugs = [s for g in libros_cfg["catalogo"]["grupos"] for s in g["libros"]]
    libros = [m("libros", s + ".json") for s in slugs]

    n = {"libros": len(libros), "cuentos": len(cuentos),
         "poemas": len(poemas["sueltos"]), "glosas": len(poemas["glosas"]),
         "decimitas": len(decimitas), "periodismo": len(prensa["trabajos"]),
         "ineditos": len(ineditos["novelas"])}

    def con_numeros(t):
        for k, v in n.items():
            t = t.replace("{" + k + "}", str(v))
        if "{" in t:
            sys.exit(f"llms.json tiene un hueco que no se sabe rellenar: {t[:80]}")
        return t

    L = [f'# {P["titulo"]}', "", f'> {P["resumen"]}', "", "Datos verificables del autor:", ""]
    L += [f"- {con_numeros(x)}" for x in P["datos"]]

    T = P["traduccion"]
    L += ["", f'## {T["titulo"]}', ""] + [f"- {x}" for x in T["lineas"]]

    S = P["secciones"]
    E = P["entradas"]

    L += ["", S["libros"], ""]
    for l in libros:
        ficha = ", ".join(x for x in (l.get("genero_frase"), l.get("editorial"), l.get("anio")) if x)
        premio = (" " + ". ".join(l["premios"]) + ".") if l.get("premios") else ""
        # En los volumenes colectivos hay que decir que el libro no es suyo: es
        # la misma regla del catalogo y del aviso de derechos, y se detecta por
        # el mismo campo, para que no puedan contradecirse.
        autoria = next((v for k, v in l.get("ficha", {}).items() if k.lower().startswith("autor")), "")
        autoria = f" {autoria}." if autoria else ""
        L.append(f'- [{l["titulo"]}]({D}/libros/{l["slug"]}/): {ficha}.{autoria}{premio}')

    L += ["", S["premios"], "", f'- [Laureles]({D}/laureles/): {len(laureles)} premios y menciones entre '
          f'{laureles[-1]["anio"]} y {laureles[0]["anio"]}.']
    for p in laureles:
        L.append(f'  - {p["anio"]}: {p["titulo"]}. {sin_html(p["texto"])}')

    L += ["", S["poesia"], "",
          f'- [Tinta-ciones]({D}/tinta-ciones/): {E["tinta_ciones"]}',
          f'- [Poemas sueltos]({D}/tinta-ciones/poemas-sueltos/): {con_numeros(E["poemas_sueltos"])}']
    for x in poemas["sueltos"] + poemas["glosas"]:
        L.append(f'  - [{x["titulo"]}]({D}/tinta-ciones/poemas-sueltos/#{pagina.ancla(x["titulo"])})')
    L.append(f'- [De-Cimitas]({D}/tinta-ciones/de-cimitas/): {con_numeros(E["decimitas"])}')
    for d in decimitas:
        L.append(f'  - [{d["titulo"]}]({D}/tinta-ciones/de-cimitas/#{d["slug"]})')
    L.append(f'- [Sonata de la lluvia]({D}/tinta-ciones/sonata-de-la-lluvia/): tres movimientos en '
             'décimas, Premio Colateral Yasmina Calcines del XXVI Concurso Nacional Ala Décima, 2026.')
    L.append(f'- [En mi voz]({D}/tinta-ciones/en-mi-voz/): {E["en_mi_voz"]}')

    L += ["", S["cuentos"], "", f'- [Contarte]({D}/contarte/): {con_numeros(E["contarte"])}']
    for c in cuentos:
        L.append(f'  - [{c["titulo"]}]({D}/contarte/{c["slug"]}/): {c["linea"]}')

    L += ["", S["periodismo"], "", f'- [El periodista]({D}/periodista/): {con_numeros(E["periodista"])}']
    for g in prensa["grupos"]:
        suyos = [t for t in prensa["trabajos"] if t["grupo"] == g["clave"]]
        if not suyos:
            continue
        L.append(f'  - {g["titulo"]}:')
        for t in suyos:
            ficha = " · ".join(x for x in (t.get("medio"), t.get("fecha")) if x)
            L.append(f'    - [{t["titulo"]}]({D}/periodista/{t["slug"]}/)'
                     + (f" ({ficha})" if ficha else "") + f': {t["linea"]}')

    L += ["", S["ineditos"], "", f'- [Inéditos]({D}/ineditos/): {con_numeros(E["ineditos"])}']
    for x in ineditos["novelas"]:
        L.append(f'  - [{x["titulo"]}]({D}/ineditos/{x["slug"]}/): {x["linea"]}')

    L += ["", S["apariciones"], ""] + [f"- {x}" for x in P["apariciones"]]

    L += ["", S["otras"], "",
          f'- [La trova]({D}/trova/): {E["trova"]}',
          f'- [Directorio]({D}/directorio/): {E["directorio"]}']

    L += ["", S["ingles"], "", P["ingles_entrada"], ""] + [f"- {x}" for x in P["ingles"]]

    L += ["", S["notas"], ""] + [f"- {x}" for x in P["notas"]]

    destino = os.path.join(RAIZ, "llms.txt")
    with open(destino, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L).rstrip("\n") + "\n")
    print(f"escrito: llms.txt · {len(L)} líneas · "
          + ", ".join(f"{v} {k}" for k, v in n.items()))


if __name__ == "__main__":
    main()
