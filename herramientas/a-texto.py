# Convierte a texto plano los originales que manda el autor, que llegan en RTF
# o en DOCX segun el dia. Deja un .txt junto al original, con la misma
# separacion por parrafos que espera el generador de cuentos.
#
# Uso: python herramientas/a-texto.py "<carpeta>"

import os, re, sys, zipfile, html


def de_rtf(bruto):
    """RTF a texto con la libreria striprtf.

    Aqui hubo un parser propio y se comio texto de verdad: en Proclama Real
    perdio las dos primeras palabras, y en tres cuentos partio los titulos
    acentuados. Para textos literarios del autor no se improvisa un conversor:
    se usa uno probado y se compara el resultado contra el original."""
    from striprtf.striprtf import rtf_to_text
    return rtf_to_text(bruto.decode("cp1252", errors="replace"), errors="ignore")


def de_rtf_casero(bruto):
    """Version propia, ya NO se usa. Se conserva solo como referencia de por
    que no conviene: ver el comentario de de_rtf()."""
    t = bruto.decode("cp1252", errors="replace")
    salida, i, n = [], 0, len(t)
    pila_ignora = []
    profundidad = 0
    saltar = 0
    while i < n:
        c = t[i]
        if c == "\\":
            m = re.match(r"\\([a-zA-Z]+)(-?\d+)? ?", t[i:])
            if m:
                palabra, arg = m.group(1), m.group(2)
                i += m.end()
                if palabra in ("par", "line", "pard"):
                    if palabra != "pard" or not salida or salida[-1] != "\n":
                        salida.append("\n")
                elif palabra == "tab":
                    salida.append("\t")
                elif palabra == "u" and arg:
                    salida.append(chr(int(arg) % 65536))
                    saltar = 1          # el caracter de reemplazo que sigue
                elif palabra in ("fonttbl","colortbl","stylesheet","info","pict",
                                 "listtable","listoverridetable","rsidtbl",
                                 "generator","themedata","colorschememapping",
                                 "latentstyles","datastore","xmlnstbl","filetbl"):
                    pila_ignora.append(profundidad)
                continue
            m = re.match(r"\\'([0-9a-fA-F]{2})", t[i:])
            if m:
                if saltar: saltar -= 1
                else: salida.append(bytes([int(m.group(1),16)]).decode("cp1252", errors="replace"))
                i += m.end(); continue
            if i+1 < n and t[i+1] == "*":
                # {\*\loquesea ...} es un destino ignorable del formato: fuera
                # el grupo entero. Sin esto se colaban los asteriscos y los
                # restos de las tablas de tema al principio y al final.
                pila_ignora.append(profundidad)
                i += 2; continue
            if i+1 < n and t[i+1] in "\\{}":
                salida.append(t[i+1]); i += 2; continue
            i += 1; continue
        if c == "{":
            profundidad += 1; i += 1; continue
        if c == "}":
            if pila_ignora and pila_ignora[-1] == profundidad:
                pila_ignora.pop()
            profundidad -= 1; i += 1; continue
        if c in "\r\n":
            i += 1; continue
        if pila_ignora:
            i += 1; continue
        if saltar:
            saltar -= 1; i += 1; continue
        salida.append(c); i += 1
    return "".join(salida)


def de_docx(ruta):
    with zipfile.ZipFile(ruta) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"<w:tab[^>]*/>", "\t", xml)
    xml = re.sub(r"<w:br[^>]*/>", "\n", xml)
    xml = re.sub(r"<[^>]+>", "", xml)
    return html.unescape(xml)


def limpiar(t):
    t = t.replace("\u00a0", " ").replace("\r", "")
    lineas = [re.sub(r"[ \t]+", " ", l).strip() for l in t.split("\n")]
    return "\n".join(l for l in lineas if l) + "\n"


def main(carpeta):
    for f in sorted(os.listdir(carpeta)):
        p = os.path.join(carpeta, f)
        base, ext = os.path.splitext(f)
        if ext.lower() == ".rtf":
            texto = de_rtf(open(p, "rb").read())
        elif ext.lower() == ".docx":
            texto = de_docx(p)
        else:
            continue
        texto = limpiar(texto)
        destino = os.path.join(carpeta, base + ".txt")
        open(destino, "w", encoding="utf-8", newline="\n").write(texto)
        palabras = len(texto.split())
        print(f"  {base[:52]:54} {len(texto):7} car · {palabras:5} palabras")


if __name__ == "__main__":
    main(sys.argv[1])
