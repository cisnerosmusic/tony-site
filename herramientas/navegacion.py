# Fuente unica de la navegacion del sitio.
#
# Existe porque hubo tres definiciones sueltas, una en cada generador y otra a
# mano en las paginas, y derivaron: Contarte faltaba en el pie de quince
# paginas y Entre lectores se colaba en el menu de dos. Ahora se define aqui y
# todo lo demas la importa o la recibe.
#
# Menu y pie llevan exactamente las mismas secciones. Entre lectores NO esta en
# ninguno de los dos: es un album, no una seccion, y por decision de Ernesto
# (8 de septiembre de 2026) se llega a el solo desde Mis libros. Si alguien lo
# echa de menos aqui, esa es la razon, no un olvido.

MENU = [
    ("/libros/", "Mis libros"),
    ("/ineditos/", "Inéditos"),
    ("/tinta-ciones/", "Tinta-ciones"),
    ("/contarte/", "Contarte"),
    ("/trova/", "La trova"),
    ("/plano-abierto/", "Plano abierto"),
    ("/laureles/", "Laureles"),
    ("/periodista/", "El periodista"),
    ("/directorio/", "Directorio"),
]

# El pie lleva ademas el aviso de derechos, que es una pagina legal y no una
# seccion de la casa: por eso esta abajo y no en el menu de arriba.
PIE = MENU + [("/derechos/", "Derechos")]


def seccion_de(ruta):
    """Que seccion esta activa para una pagina. Una subpagina marca a su madre:
    /tinta-ciones/en-mi-voz/ enciende Tinta-ciones."""
    candidatas = [h for h, _ in MENU if ruta.startswith(h)]
    return max(candidatas, key=len) if candidatas else None


def menu_html(activa, sangria="    "):
    filas = []
    for h, n in MENU:
        # La clase pinta y aria-current informa: quien usa lector de pantalla
        # tambien tiene que saber en que pagina esta.
        marca = ' class="active" aria-current="page"' if h == activa else ""
        filas.append(f'{sangria}<li><a href="{h}"{marca}>{n}</a></li>')
    filas.append(f'{sangria}<li><a href="/en/" lang="en" hreflang="en">EN</a></li>')
    return "\n".join(filas)


def pie_html(activa, sangria="    "):
    filas = []
    for h, n in PIE:
        if h == activa:
            filas.append(f'{sangria}<span aria-current="page">{n}</span>')
        else:
            filas.append(f'{sangria}<a href="{h}">{n}</a>')
    return "\n".join(filas)


# ── El sitio en ingles ───────────────────────────────────────────────────
#
# No es el espanol traducido y no lleva las mismas secciones. El orden lo fijo
# Ernesto el 9 de septiembre de 2026 y responde a un mercado distinto: para el
# lector anglosajon la puerta de entrada es la investigacion sobre la Nueva
# Trova, no la fantasia heroica. Esta razonado en PRODUCT.md.
#
# Estuvo escrito a mano dentro de gen-legal.py, que era la cuarta definicion
# suelta de navegacion del proyecto. Vive aqui por lo mismo que la espanola.

MENU_EN = [
    ("/en/trova/", "The trova"),
    ("/en/poetry/", "Poetry"),
    ("/en/fiction/", "Fiction"),
    ("/en/author/", "The author"),
    ("/en/rights/", "Rights"),
]

PIE_EN = MENU_EN


def seccion_en_de(ruta):
    candidatas = [h for h, _ in MENU_EN if ruta.startswith(h)]
    return max(candidatas, key=len) if candidatas else None


def menu_en_html(activa, sangria="    "):
    filas = []
    for h, n in MENU_EN:
        marca = ' class="active" aria-current="page"' if h == activa else ""
        filas.append(f'{sangria}<li><a href="{h}"{marca}>{n}</a></li>')
    filas.append(f'{sangria}<li><a href="/" lang="es" hreflang="es">ES</a></li>')
    return "\n".join(filas)


def pie_en_html(activa, sangria="    "):
    filas = []
    for h, n in PIE_EN:
        if h == activa:
            filas.append(f'{sangria}<span aria-current="page">{n}</span>')
        else:
            filas.append(f'{sangria}<a href="{h}">{n}</a>')
    filas.append(f'{sangria}<a href="/" lang="es" hreflang="es">Sitio en español</a>')
    return "\n".join(filas)


# ── Por idioma ───────────────────────────────────────────────────────────
#
# Los generadores que escriben en varios idiomas piden el menu por codigo de
# idioma, no por nombre de funcion. Un idioma nuevo añade arriba su MENU_xx y
# sus dos funciones, y se registra en este diccionario. Nada mas.

_POR_IDIOMA = {
    "es": (menu_html, pie_html),
    "en": (menu_en_html, pie_en_html),
}


def menu_de(lang, activa, sangria="    "):
    return _POR_IDIOMA[lang][0](activa, sangria)


def pie_de(lang, activa, sangria="    "):
    return _POR_IDIOMA[lang][1](activa, sangria)
