---
name: Ala del Mar
description: La casa del escritor Antonio López Sánchez, cuartillas sobre una mesa azul frente al mar de Alamar
colors:
  mesa: "#dde6ec"
  mesa-fria: "#b9c7d1"
  mesa-sombra: "#d9c8ab"
  papel: "#faf5e9"
  papel-viejo: "#f5edda"
  tinta: "#262019"
  tinta-suave: "#4d4335"
  anil: "#1d4e89"
  anil-profundo: "#163c6a"
  anil-tenue: "#7d97b8"
typography:
  display:
    fontFamily: "Bonum, Bookman Old Style, Georgia, serif"
    fontSize: "clamp(2.7rem, 8.5vw, 5.4rem)"
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: "-0.01em"
  casa:
    fontFamily: "Bonum, Bookman Old Style, Georgia, serif"
    fontSize: "clamp(2.4rem, 7.5vw, 4.6rem)"
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "0.05em"
  headline:
    fontFamily: "Bonum, Bookman Old Style, Georgia, serif"
    fontSize: "clamp(1.5rem, 4vw, 2.1rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "0.06em"
  title:
    fontFamily: "Bonum, Bookman Old Style, Georgia, serif"
    fontSize: "clamp(1.9rem, 5vw, 2.9rem)"
    fontWeight: 400
    lineHeight: 1.05
  seccion:
    fontFamily: "Bonum, Bookman Old Style, Georgia, serif"
    fontSize: "clamp(1.15rem, 2.6vw, 1.45rem)"
    fontWeight: 700
    letterSpacing: "0.08em"
  body:
    fontFamily: "Bonum, Bookman Old Style, Georgia, serif"
    fontSize: "1.15rem"
    fontWeight: 400
    lineHeight: 1.65
  maquina:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: "0.85rem"
    fontWeight: 400
    letterSpacing: "0.06em"
components:
  sello:
    backgroundColor: "transparent"
    textColor: "{colors.anil}"
    typography: "{typography.maquina}"
    padding: "0.85rem 1.9rem"
  sello-hover:
    textColor: "{colors.anil-profundo}"
  sello-menor:
    textColor: "{colors.anil}"
    padding: "0.6rem 1.3rem"
  cuartilla:
    backgroundColor: "{colors.papel}"
    textColor: "{colors.tinta}"
    padding: "1.4rem clamp(1.4rem, 5vw, 4rem) 3.2rem"
  tira:
    backgroundColor: "{colors.papel-viejo}"
    textColor: "{colors.tinta}"
    padding: "0.9rem 2.4rem 1rem"
  vyv:
    backgroundColor: "{colors.papel-viejo}"
    textColor: "{colors.tinta}"
    padding: "1.6rem clamp(1.2rem, 3vw, 2.2rem)"
---

# Design System: Ala del Mar

## Overview

**Creative North Star: "La mesa del escritor frente al mar"**

Ala del Mar es la casa con nombre propio del escritor Antonio López Sánchez, y la web es su mesa de trabajo vista desde arriba: cuartillas de papel cálido apiladas sobre una mesa azul pálido, con la hoja de abajo asomando torcida, sellos de goma entintados en añil, copias al carbón con mancha de café y navegación mecanografiada al pie de cada hoja. Todo lo que se ve es un objeto del oficio de escribir a la vieja usanza; no hay componentes "de web" (hero, cards, badges), hay hojas, tiras, sellos y fichas. Cada hoja interior cierra con el sello de la casa: la línea "bene scriptus" (`.fin`).

La voz es primera persona ("Mis libros", "Escribo fantasía heroica") salvo cuando se declara otra voz. La estructura es multipágina y multiidioma (selector es · en · fr · it · ru, con los idiomas no publicados marcados `.pronto`), pero los textos literarios se publican siempre en español, acompañados de una `.nota-idioma` mecanografiada que lo aclara.

Esta identidad reemplaza por completo la iteración anterior (IM Fell + EB Garamond con acento rojo). El rojo fue retirado del sistema; el único acento es el añil de bolígrafo.

**Key Characteristics:**
- Mesa azul pálido (#dde6ec) como fondo universal; nunca blanco puro ni gris neutro.
- Papel con grano SVG y hoja de abajo asomando; rotaciones alternas de fracciones de grado.
- Una sola familia impresa (Bonum) y una mecanografiada (Courier Prime); jerarquía por caja y puntaje, no por cambio de fuente.
- Un solo acento: añil #1d4e89. Sellos de goma con máscara de entintado.
- Un solo motion: el oficio mecanografiándose al cargar la portada, con reduced-motion respetado.

## Colors

Paleta de escritorio: azules fríos de mesa, papeles cálidos, tinta sepia y un único añil de bolígrafo.

### Primary
- **Añil de bolígrafo** (#1d4e89, `--anil`): el único acento del sistema. Sellos de goma, enlaces de idiomas, línea de premio (`.maquina-azul`), firma del autor (`.vyv-firma`), crédito del poema, borde superior de la ficha de archivo, foco visible, selección de texto y caret.
- **Añil profundo** (#163c6a): estado hover/active del sello; no tiene otro uso.
- **Añil tenue** (#7d97b8, `--anil-tenue`): añil desactivado (sello `:disabled`, idiomas `.pronto` vía opacidad).

### Neutral
- **Mesa azul pálido** (#dde6ec, `--mesa`): fondo del body en todas las páginas. La mesa siempre se ve entre hojas.
- **Mesa fría** (#b9c7d1, `--mesa-fria`): contornos finos de fotos y cubiertas (outline 1px), borde de la cubierta dominante.
- **Sombra de mesa** (#d9c8ab, `--mesa-sombra`): hairlines cálidos: separadores de listas, fichas, índice al pie, borde de cubiertas pequeñas.
- **Papel de cuartilla** (#faf5e9, `--papel`): superficie principal de toda hoja (`.cuartilla`), marco blanco-hueso de las fotos.
- **Papel viejo** (#f5edda, `--papel-viejo`): la hoja de abajo del montón, las tiras separadoras y el bloque "Con voz y voto" (`.vyv`).
- **Tinta** (#262019, `--tinta`): texto impreso; también el cursor de máquina.
- **Tinta suave** (#4d4335, `--tinta-suave`): metadatos, cabezales, notas, colofón, `.fin`.

### Named Rules
**La regla del añil único.** Hay un solo acento en toda la casa: el añil #1d4e89, aplicado a lo que un escritor marcaría con su bolígrafo o su sello. El rojo #b3372b de la iteración anterior fue retirado; no vuelve. Ningún segundo acento entra al sistema.

**La mesa nunca es blanca.** Ningún fondo es #fff ni gris neutro: o es mesa azul, o es papel cálido con grano (`--grano` sobre `--papel` o `--papel-viejo`).

## Typography

**Display Font:** Bonum, es decir TeX Gyre Bonum, clon libre de Bookman Old Style, la letra del autor (fallback "Bookman Old Style", Georgia, serif). Cuatro cortes locales: 400, 700, italic, bold italic.
**Body Font:** la misma Bonum; el mundo imprime todo con una sola familia.
**Label/Mono Font:** Courier Prime (fallback "Courier New", monospace), en 400, 700 e italic locales. Es "lo mecanografiado": cabezales, navegación, notas, sellos, versos en máquina.

**Character:** Bonum es redonda, ancha y libresca; Courier Prime aporta el tecleo documental. La jerarquía se construye con una sola fuente impresa: los títulos de sección van en ALTAS de Bonum y lo subordinado baja de puntaje (regla pedida por el propio autor).

### Hierarchy
- **Display / nombre de autor** (400, clamp(2.7rem, 8.5vw, 5.4rem), lh 1.02): `.nombre`; título mayor en caja normal, tracking -0.01em.
- **Casa** (700, clamp(2.4rem, 7.5vw, 4.6rem), ALTAS, tracking 0.05em, color añil): `.casa-nombre`, solo para "Ala del Mar" en la portada.
- **Headline / tira** (700, clamp(1.5rem, 4vw, 2.1rem), ALTAS, tracking 0.06em): títulos de sección sobre tira de papel viejo.
- **Titular menor** (700, clamp(1.3rem, 3vw, 1.7rem), ALTAS, tracking 0.07em): `.titular-menor`, encabezados dentro de hoja.
- **Title / obra** (400, clamp(1.9rem, 5vw, 2.9rem), lh 1.05): títulos de libro (`.obra-texto h3`), caja normal.
- **Sección de página de libro** (700, clamp(1.15rem, 2.6vw, 1.45rem), ALTAS, tracking 0.08em, hairline inferior): `.bloque > h2`.
- **Body** (400, 1.15rem, lh 1.65): prosa en Bonum; máximo 58ch (62ch en fragmentos). Capitular en `.prosa-inicial::first-letter` (3.1em).
- **Label / máquina** (Courier Prime 400 a 700, 0.75 a 1rem, tracking 0.06 a 0.14em, ALTAS solo en sellos, `.indice-titulo` y `.fragmento-titulo`): metadatos, navegación, notas de idioma.
- **Lema** (Bonum italic, clamp(1.05rem, 2.6vw, 1.35rem), tinta suave): "bene scriptus" bajo el nombre de la casa.

### Named Rules
**La regla de las ALTAS.** Los títulos de sección van en la misma Bonum en mayúsculas con tracking positivo; lo subordinado se distingue por menor puntaje, nunca por otra fuente decorativa. Es la regla del autor y ordena toda la jerarquía.

**Dos letras, dos oficios.** Bonum imprime (prosa, títulos, versos impresos); Courier Prime mecanografía (cabezales, índices, sellos, fichas, notas, versos en máquina `.fragmento-verso`). Ningún texto usa una tercera familia.

## Layout

Una columna de hojas centradas: cada `.cuartilla` mide `min(100%, 46rem)` con padding interno `1.4rem clamp(1.4rem, 5vw, 4rem) 3.2rem` y 3rem de separación entre hojas. El body respira con `clamp(1.2rem, 4vw, 3.5rem)` arriba y 4rem abajo, dejando ver la mesa. Las secciones alternan rotaciones (impar +0.35deg, par -0.3deg) aplicadas al contenedor, nunca a la cuartilla misma (un transform propio crearía stacking context y taparía la hoja de abajo).

Grids internos de dos columnas: portada (`minmax(0,1fr)` + retrato `minmax(11rem,15rem)`; en `.portada-casa` el retrato va a la izquierda), obra (texto + cubierta `minmax(9.5rem,12.5rem)`), fichas (`dt` estrecho + `dd`). Galería en `repeat(auto-fit, minmax(12rem, 1fr))`. Un solo breakpoint a 40rem: los grids caen a una columna, las rotaciones de sección se anulan (la hoja de abajo conserva la suya) y las fotos se centran con ancho acotado.

La navegación es doble: el índice mecanografiado de la portada y el `.indice-pie` al pie de cada hoja con las 8 entradas fijas (Portada, Mis libros, Inéditos, Tinta-ciones, La trova, Plano abierto, El periodista, Directorio), con la página actual en `aria-current` subrayada en bold.

**La regla de la hoja nueva.** Toda página de libro nueva se genera con `herramientas/gen-libro.py` desde un manifiesto JSON (`herramientas/libros/<slug>.json`); su estructura es fija y en este orden: CUBIERTA dominante, NOTA DE CONTRATAPA, FICHA, FRAGMENTOS, PRESENTACIONES, PRENSA, CON VOZ Y VOTO. No se maquetan hojas de libro a mano.

## Elevation & Depth

La profundidad es física, no atmosférica: una hoja de papel proyecta una sombra corta sobre la mesa y deja ver la hoja de abajo del montón (pseudo-elemento `::after` en papel viejo, rotado y desplazado unos píxeles, con z-index -1; la portada añade una tercera hoja con `::before`). No hay glows, blurs de color ni elevaciones por estado.

### Shadow Vocabulary
- **Sombra de hoja** (`box-shadow: 0 2px 4px rgba(52, 63, 75, 0.11), 0 6px 18px rgba(52, 63, 75, 0.14)`, `--sombra-hoja`): toda cuartilla, tira, foto enmarcada y cubierta dominante.
- **Hoja de abajo** (`0 2px 8px rgba(52, 63, 75, 0.09)`): el ::after del montón.
- **Objeto apoyado** (`0 1px 3px` a `0 1px 4px`, rgba fría u ocre según el objeto): cubiertas pequeñas, galería, hoja `.vyv`.

### Named Rules
**La regla del papel apilado.** La única fuente de profundidad es papel sobre papel: sombra corta más hoja de abajo asomando. Nada "flota" ni se eleva al hacer hover; lo más que hace una cubierta es enderezarse (`.cuartilla:hover .foto`).

## Shapes

Esquinas vivas en todo: papel, fotos, sellos y fichas tienen radio 0 (la única excepción es el `border-radius: 1px` del contorno de foco). La geometría del mundo es la rotación leve y alterna: hojas ±0.3deg, hoja de abajo ±1deg, tiras ±1.2deg, fotos ±2deg, sello -2deg, siempre alternando el signo entre elementos consecutivos. Los bordes son de dos familias: marcos de foto (borde grueso de papel 5-6px + outline 1px mesa fría) y hairlines de 1px en mesa-sombra para separar filas y pies. El sello lleva doble trazo: border 2px + outline 1px separado 3px, con máscara de entintado SVG (`--entintado`) que le come calvas de tinta.

**La regla de nada redondeado.** Ningún radio, ninguna píldora, ningún círculo decorativo. Si un elemento necesita distinguirse, se rota o cambia de papel, no de forma.

## Components

### Sello (botón/enlace primario)
- **Carácter:** sello de goma entintado en añil, siempre un poco torcido.
- **Shape:** rectángulo de esquinas vivas rotado -2deg; border 2px añil + outline 1px a 3px; máscara `--entintado` (260x140px) que simula el entintado irregular.
- **Tipografía:** Courier Prime 700, 1rem, ALTAS, tracking 0.14em; padding 0.85rem 1.9rem; fondo transparente.
- **Hover / Active:** se aprieta contra el papel (scale 0.97 / 0.94) y oscurece a añil profundo (#163c6a); transición 0.3s con `--paso`.
- **Disabled:** todo en añil tenue (#7d97b8), cursor not-allowed.
- **Variante `.sello-menor`:** 0.82rem, padding 0.6rem 1.3rem, tracking 0.12em.

### Cuartilla (contenedor universal)
- Papel #faf5e9 con grano SVG, `--sombra-hoja`, sin radio; hoja de abajo en papel viejo vía ::after. Abre con `.cabezal` mecanografiado (0.78rem, tinta suave) y cierra con `.indice-pie` y, en hojas interiores, `.fin`.

### Tira separadora
- Título de sección sobre tira de papel viejo con grano, `width: fit-content` centrada, rotada (-1.2deg / +1deg alternado), con subtítulo mecanografiado opcional.

### Índice al pie (navegación)
- Courier Prime 0.85rem, flex con wrap, hairline superior en mesa-sombra; enlaces sin subrayado hasta hover; página actual en `aria-current` con bold y subrayado. Siempre las 8 secciones.

### Idiomas
- Línea mecanografiada `es · en · fr · it · ru` bajo el nombre del autor: actual en `aria-current`, publicados como enlace añil, futuros como `.pronto` (opacidad 0.55, title "pronto").

### Ficha / Ficha de libro
- `dl` en grid de dos columnas con hairlines entre filas; `dt` mecanografiado 0.8rem en tinta suave; `.ficha-archivo` lleva borde superior de 3px en añil. La ficha de libro (`.ficha-libro`) es la variante generada por gen-libro.py.

### Fragmentos
- `.fragmento`: prosa con sangría francesa (text-indent 1.6em salvo primer párrafo), máximo 62ch. `.fragmento-verso`: verso mecanografiado con `white-space: pre-wrap` que respeta la sangría original. `.fragmento-titulo`: rótulo Courier 700 en ALTAS. Todo fragmento literario en otra hoja idiomática lleva `.nota-idioma`.

### Con voz y voto (.vyv)
- La voz del autor sobre hoja vieja: papel viejo con grano, rotada 0.4deg, sombra mínima, firma mecanografiada en añil (`.vyv-firma`).

### Copia al carbón (.carbon)
- Hoja de segunda para el poeta: papel más frío (#f2ede0) con mancha de café (`img/mancha.svg`) fundida por `background-blend-mode: multiply`; el tipeo en tinta de carbón (#3b3327) con text-shadow de 0.6px que lo difumina un punto.

### Galería
- Fotos con marco de papel de 5px + outline mesa fría, rotaciones alternas ±0.9deg, pies mecanografiados de 0.75rem.

### Motion
- **El único motion del mundo:** el `.oficio` de la portada se mecanografía solo al cargar (app.js): cadencia 34-74ms por tecla, pausa de 220ms tras coma, cursor de bloque parpadeando (`parpadeo`, 1s steps) que desaparece a los 2.6s. Con `prefers-reduced-motion` el texto aparece directo y todas las transiciones y el cursor se apagan. Easing global `--paso: cubic-bezier(0.16, 1, 0.3, 1)`.

## Do's and Don'ts

### Do:
- **Do** generar toda página de libro nueva con `herramientas/gen-libro.py` y su manifiesto JSON; la estructura CUBIERTA / CONTRATAPA / FICHA / FRAGMENTOS / PRESENTACIONES / PRENSA / CON VOZ Y VOTO es fija.
- **Do** escribir en primera persona salvo voz declarada (prensa, presentaciones de terceros van citadas o enlazadas, nunca apropiadas).
- **Do** publicar los textos literarios siempre en español, con `.nota-idioma` cuando la hoja está en otro idioma.
- **Do** cerrar cada hoja interior con `.fin` ("bene scriptus", Courier, aria-hidden) y abrirla con su `.cabezal`.
- **Do** alternar el signo de las rotaciones entre elementos consecutivos y aplicarlas al contenedor de sección, no a la cuartilla.
- **Do** respetar `prefers-reduced-motion` en cualquier motion nuevo (que en principio no debería existir: el tecleo es el único).

### Don't:
- **Don't** usar raya larga en ningún texto visible de la página; comas, dos puntos o paréntesis (la raya corta de diálogo dentro de fragmentos literarios del autor es material citado y se respeta).
- **Don't** mencionar Palabra Nueva en ninguna parte del sitio.
- **Don't** introducir un segundo acento de color: el rojo fue retirado y ningún color fuera de la paleta mesa/papel/tinta/añil entra al sistema.
- **Don't** usar fondos blancos puros, esquinas redondeadas, glows, ni tipografías fuera de Bonum y Courier Prime.
- **Don't** fabricar sinopsis, reseñas, testimonios o datos de contacto: lo sintético se etiqueta (`.nota-demo`) y lo biográfico debe ser verificable.
- **Don't** titular secciones en caja baja o con otra fuente: sección nueva = ALTAS de Bonum con tracking, subordinado = menor puntaje.
