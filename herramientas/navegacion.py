# Fuente unica de la navegacion del sitio.
#
# Existe porque hubo tres definiciones sueltas, una en cada generador y otra a
# mano en las paginas, y derivaron: Contarte faltaba en el pie de quince
# paginas y Entre lectores se colaba en el menu de dos. Ahora se define aqui y
# todo lo demas la importa o la recibe.
#
# La diferencia entre las dos listas es deliberada:
#   MENU son las secciones de primer nivel, las que el autor considera partes
#   de la casa.
#   PIE incluye ademas Entre lectores, que es un album y vive como enlace
#   secundario, no como seccion.

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

PIE = [
    ("/libros/", "Mis libros"),
    ("/ineditos/", "Inéditos"),
    ("/tinta-ciones/", "Tinta-ciones"),
    ("/contarte/", "Contarte"),
    ("/trova/", "La trova"),
    ("/plano-abierto/", "Plano abierto"),
    ("/laureles/", "Laureles"),
    ("/periodista/", "El periodista"),
    ("/entre-lectores/", "Entre lectores"),
    ("/directorio/", "Directorio"),
]


def seccion_de(ruta):
    """Que seccion esta activa para una pagina. Una subpagina marca a su madre:
    /tinta-ciones/en-mi-voz/ enciende Tinta-ciones."""
    candidatas = [h for h, _ in MENU if ruta.startswith(h)]
    return max(candidatas, key=len) if candidatas else None


def menu_html(activa, sangria="    "):
    filas = []
    for h, n in MENU:
        clase = ' class="active"' if h == activa else ""
        filas.append(f'{sangria}<li><a href="{h}"{clase}>{n}</a></li>')
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
