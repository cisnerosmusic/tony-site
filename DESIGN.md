---
name: Antonio López Sánchez, escritor
description: La mesa del escritor, cuartillas mecanografiadas sobre madera café con leche, un solo acento rojo de cinta bicolor
colors:
  mesa: "#eadcc4"
  mesa-sombra: "#d9c8ab"
  papel: "#faf5e9"
  papel-viejo: "#f5edda"
  papel-cebolla: "#f2ede0"
  tinta: "#262019"
  tinta-suave: "#4d4335"
  tinta-carbon: "#3b3327"
  rojo: "#b3372b"
  rojo-profundo: "#922c22"
  rojo-tenue: "#c86a5f"
typography:
  display:
    fontFamily: "IM Fell DW Pica, Georgia, serif"
    fontSize: "clamp(2.7rem, 8.5vw, 5.4rem)"
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "IM Fell DW Pica, Georgia, serif"
    fontSize: "clamp(1.7rem, 4.5vw, 2.4rem)"
    fontWeight: 400
    lineHeight: 1.1
  title:
    fontFamily: "IM Fell DW Pica, Georgia, serif"
    fontSize: "clamp(1.9rem, 5vw, 2.9rem)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: "-0.005em"
  body:
    fontFamily: "EB Garamond, Georgia, serif"
    fontSize: "1.15rem"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: "0.78rem"
    fontWeight: 400
    letterSpacing: "0.06em"
spacing:
  entre-cuartillas: "3rem"
  bajo-cabezal: "2.6rem"
  margen-cuartilla: "clamp(1.4rem, 5vw, 4rem)"
components:
  sello:
    backgroundColor: "transparent"
    textColor: "{colors.rojo}"
    typography: "{typography.label}"
    rounded: "0"
    padding: "0.85rem 1.9rem"
  sello-hover:
    textColor: "{colors.rojo-profundo}"
  sello-disabled:
    textColor: "{colors.rojo-tenue}"
  cuartilla:
    backgroundColor: "{colors.papel}"
    textColor: "{colors.tinta}"
    rounded: "0"
    padding: "1.4rem clamp(1.4rem, 5vw, 4rem) 3.2rem"
    width: "min(100%, 46rem)"
  tira:
    backgroundColor: "{colors.papel-viejo}"
    textColor: "{colors.tinta}"
    rounded: "0"
    padding: "0.9rem 2.4rem 1rem"
---

# Design System: Antonio López Sánchez, escritor

## Overview

**Creative North Star: "La mesa del escritor"**

La web es la mesa de trabajo de un escritor a la vieja usanza: cuartillas mecanografiadas apoyadas sobre una mesa de madera clara color café con leche. No hay pantallas dentro del mundo: todo lo que se ve es papel, tinta y el rojo de la cinta bicolor de la máquina de escribir. Cada sección es una hoja distinta del montón, con su rotación leve, su hoja de abajo asomando y su cabezal mecanografiado, y las secciones se anuncian con tiras de papel viejo recortadas.

El mundo distingue tres voces materiales: la imprenta antigua (IM Fell DW Pica, para nombres y títulos), la prosa impresa (EB Garamond, para leer) y lo mecanografiado (Courier Prime, para cabezales, datos, listas y todo lo que "salió de la máquina"). El papel tiene grano real (ruido SVG en data URI, tile de 220px, fundido sobre el color del papel) y las hojas proyectan una sombra suave doble, nunca dura.

Reemplaza al mundo anterior de revista literaria cubana (Besley/Archivo, tres tintas), descartado por rediseño pedido por el usuario. Rechazos confirmados: web de autor genérica, trozos de cinta adhesiva sobre las cubiertas, pies de foto bajo las cubiertas, numeración "hoja N" en cabezales e índice.

**Key Characteristics:**
- Todo objeto visible es papel sobre mesa; cero cromo de interfaz
- Un solo acento: el rojo de cinta bicolor (#b3372b), siempre en Courier
- Tres tipografías con roles materiales estrictos (imprenta / prosa / máquina)
- Rotaciones leves (0.3° a 2°) y sombras suaves como única profundidad
- Un solo motion: el oficio se mecanografía al cargar

## Colors

Paleta de materiales: dos maderas, tres papeles, tres tintas y un rojo de cinta con sus estados.

### Primary
- **Rojo de cinta bicolor** (#b3372b): el único acento del mundo. Premios y menciones en texto mecanografiado (`.maquina-roja`), el sello de goma, el crédito del poema, el borde superior de la ficha de archivo, `::selection`, `caret-color` y el anillo de foco. Nunca aparece en Garamond ni en IM Fell.
- **Rojo profundo** (#922c22): estado hover/active del sello.
- **Rojo tenue** (#c86a5f): sello deshabilitado.

### Neutral
- **Mesa café con leche** (#eadcc4): el fondo del documento, la madera. Nunca lleva texto directamente encima salvo nada: todo texto vive sobre papel.
- **Sombra de mesa** (#d9c8ab): bordes de foto, filetes divisores (índice, lista mecanografiada, ficha, colofón) y el tinte de las hojas más viejas del montón.
- **Papel de cuartilla** (#faf5e9): la hoja principal, siempre con el grano SVG encima.
- **Papel viejo** (#f5edda): las hojas de abajo del montón y las tiras separadoras.
- **Papel cebolla** (#f2ede0): solo la hoja de copia al carbón (El poeta); más frío y delgado que la cuartilla.
- **Tinta sepia** (#262019): el texto. Casi negro, nunca negro puro.
- **Tinta suave** (#4d4335): cabezales, datos secundarios, numeración, colofón, notas de demo.
- **Tinta de carbón** (#3b3327): solo el tipeo de la copia al carbón, con `text-shadow: 0 0 0.6px rgba(59,51,39,0.55)` para difuminarla un punto.

### Named Rules
**The Cinta Bicolor Rule.** El rojo es la tinta roja de la máquina: solo existe en texto Courier, en el sello y en filetes de archivo. Jamás tiñe fondos, titulares de imprenta ni prosa Garamond.

**The Todo Es Papel Rule.** Ningún texto se apoya sobre la mesa. Todo contenido vive dentro de una cuartilla, una tira o el pie, siempre con grano de papel.

## Typography

**Display Font:** IM Fell DW Pica (con Georgia, serif)
**Body Font:** EB Garamond variable 400-800 (con Georgia, serif)
**Label/Mono Font:** Courier Prime 400/700 (con Courier New, monospace)

**Character:** Tres oficios de la letra: la imprenta antigua e irregular de IM Fell para lo que merece portada, la prosa serena de Garamond para leer, y la máquina de escribir para todo lo que el autor teclearía él mismo. Las tres son de época; ninguna es geométrica ni de sistema.

### Hierarchy
- **Display** (400, clamp(2.7rem, 8.5vw, 5.4rem), 1.02): solo el nombre del autor en la portada. `text-wrap: balance`.
- **Headline** (400, clamp(1.7rem, 4.5vw, 2.4rem) a clamp(2rem, 5vw, 2.8rem), 1.1): títulos de sección en las tiras y en el pie.
- **Title** (400, clamp(1.9rem, 5vw, 2.9rem), 1.05): títulos de obra dentro de las cuartillas.
- **Body** (400, 1.15rem, 1.65): prosa Garamond; sinopsis y prosa a máximo 58ch, cierre a 44ch.
- **Label** (400, 0.78rem a 1.05rem, letter-spacing 0.06em a 0.14em): todo lo mecanografiado (clases `.maquina` / `.maquina-roja`): cabezales, datos editoriales, numeración romana, listas, ficha, colofón. El poema completo es label a 0.98rem con line-height 1.85 y `white-space: pre-wrap`.

### Named Rules
**The Tres Manos Rule.** IM Fell solo para nombres y títulos (incluida la letra capitular `::first-letter` de la prosa inicial); Garamond solo para prosa corrida; Courier para todo dato, cabezal, lista y acción. Un texto nunca mezcla dos manos dentro de la misma frase salvo la convención número/dato en las listas.

**The Mayúscula Propia Rule.** En texto mecanografiado, mayúscula inicial obligatoria en nombres propios, premios y editoriales; el minúsculas-todo solo se permite en rótulos cortos de una palabra como "índice" o los `dt` de la ficha.

**The Sin Numeración Rule.** Los cabezales mecanografiados llevan autor y sección ("A. López Sánchez · Las novelas"), nunca "hoja N". El índice es una lista simple sin números visibles (`list-style: none`).

## Layout

Una sola columna de hojas: cada cuartilla mide `min(100%, 46rem)` centrada, con padding interno `1.4rem clamp(1.4rem, 5vw, 4rem) 3.2rem` y 3rem de aire entre cuartillas consecutivas. El body respira `clamp(1.2rem, 4vw, 3.5rem)` arriba y 4rem abajo sobre la mesa.

Las secciones alternan rotación: impares +0.35°, pares -0.3°. La rotación vive en la `section` contenedora, no en la cuartilla (un transform propio crearía stacking context y la hoja de abajo taparía el grano). Dentro de las obras, `.obra-cuerpo` es grid de dos columnas: texto flexible y foto de `minmax(9.5rem, 12.5rem)`, gap `clamp(1.4rem, 4vw, 2.8rem)`.

Un solo breakpoint (max-width: 40rem): las rotaciones de sección se anulan (las hojas de abajo conservan la suya), la obra pasa a una columna y la foto se centra a máximo 13rem.

## Elevation & Depth

Profundidad de papel apilado, nunca de interfaz. La sombra canónica de hoja es doble y suave: `0 2px 4px rgba(84, 62, 34, 0.1), 0 6px 18px rgba(84, 62, 34, 0.13)` (var `--sombra-hoja`), en tono madera, jamás gris ni negra. La segunda capa de profundidad es física: cada cuartilla lleva una hoja de abajo (`::after` en papel viejo, rotada ~1° y desplazada unos píxeles, z-index -1) y la portada suma una tercera hoja (`::before`) para leer como montón. Las fotos llevan sombra mínima `0 1px 3px rgba(84, 62, 34, 0.18)` más borde de 1px en sombra de mesa.

### Shadow Vocabulary
- **Sombra de hoja** (`box-shadow: 0 2px 4px rgba(84,62,34,0.1), 0 6px 18px rgba(84,62,34,0.13)`): cuartillas y tiras.
- **Hoja de abajo** (`box-shadow: 0 2px 8px rgba(84,62,34,0.08)`): el ::after del montón.
- **Foto revelada** (`box-shadow: 0 1px 3px rgba(84,62,34,0.18)`): cubiertas de libro.

### Named Rules
**The Sombra Tibia Rule.** Toda sombra usa la base rgba(84, 62, 34, x): sombra de madera bajo papel. Nada de sombras duras con offset, nada de rgba(0,0,0,x).

## Shapes

Radio cero en todo: el papel se corta recto (el único radius del sistema es el 1px del anillo de foco). La forma característica es el rectángulo levemente rotado: cuartillas heredan ±0.3° de su sección, tiras ±1° a 1.2°, fotos ±1.8° a 2°, el sello -2°. Los filetes son líneas de 1px en sombra de mesa; la ficha de archivo se distingue con un borde superior de 3px en rojo. El grano de papel (`--grano`, ruido fractal SVG en data URI) se apila como primera capa de background sobre cada superficie de papel.

## Components

### Sello de goma (acción única)
El botón del mundo es un sello de goma entintado: Courier 700, 1rem, mayúsculas con tracking 0.14em, rojo sobre transparente, doble marco (border 2px + outline 1px con offset 3px), rotado -2°, padding 0.85rem 1.9rem.
- **Entintado:** `mask-image: var(--entintado)` (ruido SVG 260x140) le come calvas de tinta; ningún sello se estampa perfecto.
- **Hover:** se aprieta (`scale(0.97)`) y oscurece a rojo profundo (#922c22); **active** `scale(0.94)`.
- **Focus:** outline 2px rojo, offset 5px.
- **Disabled:** todo pasa a rojo tenue (#c86a5f), cursor not-allowed.

### Cuartilla
- **Corner Style:** recto, sin radius.
- **Background:** grano SVG sobre papel #faf5e9 (variante carbón: mancha de café + grano sobre #f2ede0, ver abajo).
- **Shadow Strategy:** sombra de hoja + hoja de abajo en ::after (ver Elevation & Depth).
- **Internal Padding:** 1.4rem arriba, clamp(1.4rem, 5vw, 4rem) lateral, 3.2rem abajo.
- **Cabezal:** primera línea siempre, Courier 0.78rem en tinta suave, 2.6rem de aire debajo (1.9rem en la copia al carbón, 1.8rem en móvil).

### Tira separadora
Recorte de papel viejo que anuncia cada sección: `width: fit-content` centrada, grano + papel viejo, sombra de hoja, rotación -1.2° (pares +1°). Contiene el h2 en IM Fell y una línea Courier de 0.82rem en tinta suave.

### Foto de cubierta
`figure.foto` rotada ±1.8° a 2°, sin cinta adhesiva, sin figcaption ni texto debajo (decisión confirmada por el usuario; el alt cuenta la cubierta). Imagen con borde 1px sombra de mesa y sombra mínima. Al hover de la cuartilla la foto se endereza a 0.6° (`transition: transform 0.4s var(--paso)`).

### Copia al carbón (hoja del poeta)
La única hoja en papel cebolla #f2ede0: la mancha de café (img/mancha.svg, 16rem, esquina superior derecha desbordada) se funde a la fibra con `background-blend-mode: multiply` sobre el grano y el papel; `overflow: clip` recorta el desborde. El tipeo va en tinta de carbón #3b3327 con text-shadow difusor; el poema conserva su sangrado con `pre-wrap`; el crédito en rojo.

### Ficha de archivo (el periodista)
`dl` con borde superior de 3px rojo en la cuartilla; cada par dt/dd en grid `minmax(6.5rem, 9rem) / 1fr` con filete de 1px arriba; dt en Courier 0.8rem tinta suave, dd en Garamond a 58ch.

### Lista mecanografiada (la trova)
`ul` sin viñetas con filetes de 1px arriba y abajo de cada ítem; número y datos en Courier tinta suave, título de obra en Garamond `strong` 600.

### Índice
Nav de portada sobre filete: rótulo "índice" en Courier mayúsculas tracking 0.14em, lista `ol` sin numeración visible, enlaces Courier 0.95rem sin subrayado que lo ganan al hover.

### Motion (grammar del mundo)
Un solo motion narrativo: el oficio de la portada se mecanografía al cargar (app.js), tecla a tecla con cadencia irregular (34-74ms, pausa de 220ms tras coma), cursor de bloque parpadeante (`steps(1)`, 1s) que desaparece 2.6s después de terminar; con `prefers-reduced-motion` el texto aparece directo y el cursor no anima. El easing único de las transiciones es `cubic-bezier(0.16, 1, 0.3, 1)` (var `--paso`). Todo lo demás es estático: el papel no se anima.

## Do's and Don'ts

### Do:
- **Do** poner todo contenido sobre papel con grano (`var(--grano)` como primera capa de background) y sombra de hoja; la mesa nunca lleva texto.
- **Do** usar Courier Prime para cualquier texto que el autor teclearía (datos, cabezales, listas, acciones, notas) y reservar el rojo #b3372b exclusivamente para ese registro mecanografiado y el sello.
- **Do** rotar levemente cada objeto (secciones ±0.3°, tiras ±1.2°, fotos ±2°, sello -2°) y anular las rotaciones de sección bajo 40rem.
- **Do** escribir mayúscula inicial en nombres propios, premios y editoriales dentro del texto mecanografiado.
- **Do** respetar reduced-motion: tipeo directo, cursor quieto, transiciones apagadas.

### Don't:
- **Don't** añadir trozos de cinta adhesiva, pies de foto ni texto alguno bajo las cubiertas (rechazo confirmado por el usuario).
- **Don't** numerar hojas: nada de "hoja N" en cabezales ni números visibles en el índice.
- **Don't** usar negro puro, sombras grises o con offset duro, bordes redondeados ni degradados: la profundidad es papel apilado y sombra tibia rgba(84,62,34,x).
- **Don't** introducir un segundo acento ni llevar el rojo a fondos, titulares IM Fell o prosa Garamond.
- **Don't** añadir más motion que el tipeo de carga; ningún elemento entra animado al hacer scroll.
