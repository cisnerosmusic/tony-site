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
    # "Books" y no "Fiction": decision de Ernesto, 21 de septiembre de 2026.
    # El catalogo entero cabe en el menu y la ficcion sigue teniendo su
    # pagina, /en/fiction/, enlazada desde la portada inglesa.
    ("/en/books/", "Books"),
    ("/en/author/", "The author"),
    ("/en/rights/", "Rights"),
]

PIE_EN = MENU_EN


# ── El sitio en frances ───────────────────────────────
#
# Mismo orden que el ingles y por la misma razon: para quien llega de fuera, la
# puerta es la investigacion sobre la Nueva Trova. Las rutas se traducen, menos
# "trova", que es el nombre del movimiento y no se traduce en ningun idioma.

MENU_FR = [
    ("/fr/trova/", "La trova"),
    ("/fr/poesie/", "Poésie"),
    ("/fr/livres/", "Livres"),
    ("/fr/auteur/", "L'auteur"),
    ("/fr/droits/", "Droits"),
]

PIE_FR = MENU_FR




# ── Por idioma ───────────────────────────────────────────────────────────
#
# Los generadores que escriben en varios idiomas piden el menu por codigo de
# idioma, no por nombre de funcion. Un idioma nuevo añade arriba su MENU_xx y
# sus dos funciones, y se registra en este diccionario. Nada mas.

# Un idioma se declara aqui entero y nada mas: su menu, su pie, su portada, la
# etiqueta con que los demas lo enlazan y como se llama su sitio en el pie.
#
# El español y el ingles eran dos parejas de funciones casi iguales, con el
# enlace al otro idioma clavado dentro. Eso es justo lo que impedia que hubiera
# un tercero: con cinco idiomas, cada menu tiene que enlazar a los otros
# cuatro, y no se puede escribir a mano veinte veces. Ahora el enlace de
# idiomas se arma solo, en el orden en que estan declarados aqui.
#
# Con dos idiomas la salida es identica a la de antes, byte a byte: se
# comprobo con un diff de las 117 paginas antes de tocar nada mas.

IDIOMAS = {
    "es": {
        "menu": MENU,
        "pie": PIE,
        "portada": "/",
        "etiqueta": "ES",
        # Como se llama este sitio en su propio idioma, para el pie de los
        # demas: el enlace se lee en la lengua a la que lleva.
        "pie_nombre": "Sitio en español",
        # El pie español no enlaza a los demas idiomas y los extranjeros si.
        # Es como estaba. Cuando esten los cinco habra que decidir si se
        # igualan; hoy el visitante español ya tiene el selector arriba.
        "pie_idiomas": False,
    },
    "en": {
        "menu": MENU_EN,
        "pie": PIE_EN,
        "portada": "/en/",
        "etiqueta": "EN",
        "pie_nombre": "Site in English",
        "pie_idiomas": True,
    },
    "fr": {
        "menu": MENU_FR,
        "pie": PIE_FR,
        "portada": "/fr/",
        "etiqueta": "FR",
        "pie_nombre": "Site en français",
        "pie_idiomas": True,
    },
}


def _otros(lang):
    """Los demas idiomas, en el orden del registro."""
    return [(l, d) for l, d in IDIOMAS.items() if l != lang]


def seccion_de(ruta, lang="es"):
    """Que seccion esta activa para una pagina. Una subpagina marca a su madre:
    /tinta-ciones/en-mi-voz/ enciende Tinta-ciones."""
    candidatas = [h for h, _ in IDIOMAS[lang]["menu"] if ruta.startswith(h)]
    return max(candidatas, key=len) if candidatas else None


def nombre_de(lang, ruta):
    """Como se llama una seccion en su idioma. Lo usan las paginas de libro
    para decir de que sala cuelgan sin repetir aqui el nombre: los tres libros
    de la trova cuelgan de /trova/, no del catalogo, y el camino de miga y el
    boton de volver tienen que decirlo con las mismas palabras que el menu."""
    for h, n in IDIOMAS[lang]["menu"]:
        if h == ruta:
            return n
    return None


def menu_de(lang, activa, sangria="    "):
    filas = []
    for h, n in IDIOMAS[lang]["menu"]:
        # La clase pinta y aria-current informa: quien usa lector de pantalla
        # tambien tiene que saber en que pagina esta.
        marca = ' class="active" aria-current="page"' if h == activa else ""
        filas.append(f'{sangria}<li><a href="{h}"{marca}>{n}</a></li>')
    # Los idiomas no son una sala mas y el menu tiene que decirlo: el primero
    # lleva la clase con que styles.css dibuja la linea que los separa. Con dos
    # idiomas daba igual; con cinco, la barra acaba en cuatro siglas seguidas
    # que se leen como secciones. Lo pidio Ernesto el 23 de septiembre de 2026.
    for n, (l, d) in enumerate(_otros(lang)):
        clase = "nav-idioma nav-idioma-primero" if n == 0 else "nav-idioma"
        filas.append(f'{sangria}<li class="{clase}"><a href="{d["portada"]}" lang="{l}" '
                     f'hreflang="{l}">{d["etiqueta"]}</a></li>')
    return "\n".join(filas)


def pie_de(lang, activa, sangria="    "):
    filas = []
    for h, n in IDIOMAS[lang]["pie"]:
        if h == activa:
            filas.append(f'{sangria}<span aria-current="page">{n}</span>')
        else:
            filas.append(f'{sangria}<a href="{h}">{n}</a>')
    if IDIOMAS[lang]["pie_idiomas"]:
        for l, d in _otros(lang):
            # Cada enlace se lee en la lengua a la que lleva, no en la de la
            # pagina: es lo que ya hacia el pie ingles con "Sitio en español".
            filas.append(f'{sangria}<a href="{d["portada"]}" lang="{l}" '
                         f'hreflang="{l}">{d["pie_nombre"]}</a>')
    return "\n".join(filas)
