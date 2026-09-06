---
name: Antonio López Sánchez, la mesa del escritor
description: Web de autor compuesta como la mesa de trabajo de un escritor a la vieja usanza, cuartillas mecanografiadas sobre una mesa café con leche, tinta sepia y un solo rojo de cinta bicolor.
colors:
  mesa: "#eadcc4"
  mesa-sombra: "#d9c8ab"
  papel: "#faf5e9"
  papel-viejo: "#f5edda"
  tinta: "#262019"
  tinta-suave: "#4d4335"
  rojo: "#b3372b"
  rojo-tenue: "#c86a5f"
  raya-azul: "rgba(124, 152, 176, 0.75)"
typography:
  display:
    fontFamily: "IM Fell DW Pica, Georgia, serif"
    fontSize: "clamp(2.7rem, 8.5vw, 5.4rem)"
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "IM Fell DW Pica, Georgia, serif"
    fontSize: "clamp(1.9rem, 5vw, 2.9rem)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: "-0.005em"
  title:
    fontFamily: "IM Fell DW Pica, Georgia, serif"
    fontSize: "clamp(1.7rem, 4.5vw, 2.4rem)"
    fontWeight: 400
    lineHeight: 1.1
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
  renglon: "1.9rem"
  entre-cuartillas: "3rem"
components:
  sello:
    backgroundColor: "transparent"
    textColor: "{colors.rojo}"
    padding: "0.85rem 1.9rem"
  cuartilla:
    backgroundColor: "{colors.papel}"
    textColor: "{colors.tinta}"
    padding: "1.4rem clamp(1.4rem, 5vw, 4rem) 3.2rem"
  tira:
    backgroundColor: "{colors.papel-viejo}"
    textColor: "{colors.tinta}"
    padding: "0.9rem 2.4rem 1rem"
---

# Design System: Antonio López Sánchez, la mesa del escritor

## Overview

**Creative North Star: "La mesa del escritor a la vieja usanza"**

Todo lo que se ve es un objeto físico sobre una mesa café con leche: cuartillas de papel con grano, tiras de papel viejo como separadores, fotos sujetas con cinta adhesiva, un sello de goma como botón, una hoja rayada de libreta con margen rojo. La web no tiene "secciones" en el sentido web: tiene hojas numeradas de un manuscrito que el visitante hojea de arriba abajo. La gramática de manuscrito (cabezal mecanografiado arriba de cada hoja, numeración "hoja N", índice con puntos de guía) es estructural, no decorativa.

Tres voces tipográficas reparten el mundo: IM Fell DW Pica es la imprenta antigua (nombre y títulos), EB Garamond la prosa impresa (cuerpo de lectura), Courier Prime la máquina de escribir del sujeto (todo lo que el autor "tecleó": cabezales, índice, datos editoriales, el poema). La tinta es sepia casi negra y hay un solo acento: el rojo de la cinta bicolor de máquina.

Este mundo reemplaza por completo al anterior (número de revista literaria en tres tintas, Besley y Archivo, sobreimpresión multiply, doctrina de cero sombras). Ese mundo es anti-referencia: nada de él se hereda.

**Key Characteristics:**
- Materialidad literal: cada superficie es papel con grano sobre mesa, con sombra física suave.
- Una sola columna de cuartillas centradas, ligeramente rotadas en alternancia.
- Un solo acento (rojo cinta bicolor) sobre una gama sepia de mesa, papel y tinta.
- Monospace legítimo: Courier Prime es la voz del sujeto, nunca disfraz decorativo.
- Un solo movimiento en todo el sitio: el oficio mecanografiándose al cargar.

## Colors

Gama sepia de mesa, papel y tinta con un único acento rojo; el azul de renglón es material de la hoja rayada, no un color de interfaz.

### Primary
- **Rojo cinta bicolor** (#b3372b): el único acento del mundo. Tinta roja de máquina: el sello de goma, los premios en los datos editoriales, el crédito del poema, la línea del margen de libreta (en su versión tenue), la línea superior de la ficha de archivo, selección de texto, caret y focus ring.
- **Rojo tenue** (#c86a5f): el mismo rojo desgastado, para el margen de la hoja rayada y el estado disabled del sello.

### Neutral
- **Mesa café con leche** (#eadcc4): el fondo del sitio, la madera clara de la mesa. Nunca es superficie de contenido.
- **Sombra de mesa** (#d9c8ab): bordes finos, filetes divisores, puntos de guía del índice y marco de las fotos.
- **Papel de cuartilla** (#faf5e9): la superficie de contenido principal; siempre lleva el grano encima.
- **Papel viejo** (#f5edda): las tiras separadoras y las hojas de abajo del montón.
- **Tinta sepia** (#262019): el texto principal, casi negro pero caliente.
- **Tinta suave** (#4d4335): la tinta secundaria de cabezales, pies de foto, notas y colofón.
- **Azul de renglón** (rgba(124, 152, 176, 0.75)): exclusivo de los renglones de la hoja rayada; jamás aparece fuera de ella.

### Named Rules
**La regla de la cinta bicolor.** La máquina solo tiene dos tintas: sepia y rojo. Cualquier tercer color de interfaz rompe el mundo. El rojo marca lo excepcional (premios, la acción, el margen); si abunda, deja de significar.

**La regla del grano.** El grano de papel (`var(--grano)`, tile SVG de 220px de ruido tibio) es material obligatorio de toda cuartilla y toda tira: se compone como primera capa del background sobre el color de papel. Papel sin grano es papel falso.

## Typography

**Display Font:** IM Fell DW Pica (con Georgia)
**Body Font:** EB Garamond variable 400 a 800, romana e itálica (con Georgia)
**Label/Mono Font:** Courier Prime 400/700 e itálica (con Courier New)

**Character:** Tres siglos en una mesa: tipo de imprenta antigua con sus irregularidades (Fell) para lo que va en grande, garalda serena para la prosa impresa, y máquina de escribir para todo lo que el sujeto tecleó. Las tres familias están autohospedadas en woff2.

### Hierarchy
- **Display** (400, clamp(2.7rem, 8.5vw, 5.4rem), 1.02): el nombre del autor en la primera cuartilla. Solo IM Fell, solo peso 400: la imprenta antigua no conoce la negrita.
- **Headline** (400, clamp(1.9rem, 5vw, 2.9rem), 1.05): títulos de obra dentro de las cuartillas.
- **Title** (400, clamp(1.7rem, 4.5vw, 2.4rem), 1.1): titulares de las tiras separadoras.
- **Body** (400, 1.15rem, 1.65): prosa en EB Garamond, máximo 58ch. La primera prosa de una hoja puede abrir con capitular Fell (::first-letter, 3.1em).
- **Label** (400, 0.78rem, 0.06em de tracking): cabezales mecanografiados y notas en Courier Prime, en tinta suave. La variante de acción (sello) sube a 700, 1rem, 0.14em, mayúsculas.

### Named Rules
**La regla de la máquina.** Courier Prime es la máquina de escribir del sujeto: aparece solo en lo que el autor tecleó (cabezales, índice, datos editoriales, listas, poema, notas, colofón). Es monospace legítimo, con contenido diegético; nunca se usa como textura decorativa ni como "estética tech".

**La regla del cabezal.** Toda cuartilla abre con su cabezal mecanografiado (autor y sección a la izquierda, "hoja N" a la derecha) y la numeración de hojas es continua en todo el sitio. Es la gramática del manuscrito: una hoja sin cabezal no pertenece al montón.

## Layout

Una sola columna de cuartillas de ancho min(100%, 46rem) centradas sobre la mesa, separadas 3rem entre sí dentro de una sección y con tiras separadoras entre secciones (margin 4.5rem arriba, 2.8rem abajo). El body respira con padding clamp(1.2rem, 4vw, 3.5rem) arriba y 4rem abajo.

Dentro de una cuartilla de obra, grid de dos columnas: texto (1fr) y foto (minmax(9.5rem, 12.5rem)) con gap clamp(1.4rem, 4vw, 2.8rem). La hoja rayada define su propio sistema: `--renglon: 1.9rem` gobierna el line-height de todo su contenido y `--margen-libreta: clamp(2.4rem, 7vw, 4.6rem)` sitúa la línea roja vertical; todo el contenido arranca a la derecha de esa línea (padding-left: margen + 1.4rem).

Un solo breakpoint, 40rem: el grid de obra colapsa a una columna, la foto se centra a máximo 13rem, las rotaciones de sección se apagan (la hoja de abajo conserva la suya) y la hoja rayada compacta renglón y margen.

### Named Rules
**La regla del margen rojo.** En la hoja rayada nada pisa el margen: la línea roja vive en `--margen-libreta` y todo contenido, cabezal incluido, empieza a su derecha.

## Elevation & Depth

La profundidad es física, no tonal: papel que descansa sobre una mesa. Cada cuartilla proyecta una sombra suave de dos capas y trae debajo su "hoja de abajo" (::after en papel viejo, rotada y desplazada unos píxeles, z-index -1); la portada añade una tercera hoja (::before) para leerse como montón. Las fotos llevan sombra mínima de contacto. No hay glows, ni sombras duras desplazadas, ni elevación por hover.

### Shadow Vocabulary
- **Sombra de hoja** (`box-shadow: 0 2px 4px rgba(84, 62, 34, 0.1), 0 6px 18px rgba(84, 62, 34, 0.13)`): la sombra estándar de cuartillas y tiras sobre la mesa. Siempre en tono madera cálido, nunca gris neutro.
- **Sombra de contacto** (`box-shadow: 0 1px 3px rgba(84, 62, 34, 0.18)`): fotos pegadas sobre el papel.

### Named Rules
**La regla de la rotación en el contenedor.** La rotación de las hojas vive siempre en la sección contenedora (section:nth-of-type(odd) 0.35deg, even -0.3deg), nunca en la propia cuartilla: un transform en la cuartilla crea stacking context y la hoja de abajo (::after con z-index -1) tapa el grano y los renglones del fondo propio. Bug real ya sufrido en este build; no se repite.

## Shapes

Esquinas rectas en todo: el papel cortado no tiene border-radius (el único radio del sitio es 1px en el focus ring). El lenguaje de forma es la rotación leve: hojas, tiras, fotos y sello viven entre 0.25deg y 2deg de giro, alternando el signo por sección para que la mesa se sienta usada y no maquetada. Los bordes son filetes de 1px en sombra de mesa (divisores de listas, ficha, índice, marco de foto); el sello es el único elemento con borde doble (border 2px + outline 1px separados 3px, la doble línea del sello de goma).

## Components

### Sello (acción primaria)
Un sello de goma estampado: la única forma de botón del mundo.
- **Shape:** rectángulo recto con doble línea roja (border 2px + outline 1px con offset 3px), rotado -2deg.
- **Estilo:** fondo transparente, texto Courier Prime 700 en mayúsculas (0.14em de tracking) en rojo cinta, padding 0.85rem 1.9rem.
- **Entintado:** lleva obligatoriamente la máscara `var(--entintado)` (mask-image, 260px por 140px): las calvas de tinta son lo que lo hace sello y no botón con borde.
- **Hover / Active:** se aprieta contra el papel (scale 0.97 / 0.94, manteniendo la rotación) y oscurece a #922c22. Focus visible con outline rojo a 5px.
- **Disabled:** rojo tenue (#c86a5f) en texto, borde y doble línea; cursor not-allowed.

### Cuartilla (contenedor principal)
- **Corner Style:** recto, sin radio.
- **Background:** `var(--grano)` sobre papel (#faf5e9); la variante rayada añade renglones repeating-linear-gradient en azul de renglón.
- **Shadow Strategy:** sombra de hoja + hoja de abajo en ::after (ver Elevation & Depth).
- **Internal Padding:** 1.4rem arriba, clamp(1.4rem, 5vw, 4rem) lateral, 3.2rem abajo.
- **Cabezal:** obligatorio (ver La regla del cabezal).

### Tira (separador de sección)
Recorte de papel viejo con el titular: width fit-content centrado, grano sobre papel viejo, sombra de hoja, rotación entre -1.2deg y 1deg, titular Fell con subtítulo mecanografiado en tinta suave.

### Foto con cinta adhesiva
Las imágenes (cubiertas de libros) van pegadas: rotación de 1.8 a 2deg alternando signo, borde 1px sombra de mesa, sombra de contacto, y dos tiras de cinta adhesiva semitransparente (::before/::after a ±42deg en las esquinas superiores). Al hover de la cuartilla, la foto se endereza suavemente (0.6deg). Pie de foto mecanografiado, 0.74rem, centrado.

### Índice (navegación)
Índice mecanografiado de manuscrito: lista ordenada de enlaces Courier Prime 0.95rem, cada línea con título, puntos de guía (border-bottom dotted en sombra de mesa) y "hoja N" al final. Sin subrayado en reposo; hover subraya solo el título. Es la única navegación del sitio, dentro de la primera cuartilla.

### Ficha de archivo
Para datos tabulares (el periodista): dl en grid de dos columnas (término minmax(6.5rem, 9rem) + definición), filetes de 1px entre filas, términos mecanografiados en tinta suave, y la cuartilla coronada por un filete rojo de 3px.

### Motion
Un solo movimiento en el mundo: el oficio se mecanografía solo al cargar (app.js), con cadencia irregular de tecla (34 a 74ms, pausa de 220ms tras coma), cursor de bloque parpadeante que se retira 2.6s después de terminar, y aria-label con el texto completo desde el inicio. Con prefers-reduced-motion el texto aparece directo y las transiciones se apagan. El easing global es `--paso` (cubic-bezier(0.16, 1, 0.3, 1)), solo para microtransiciones de sello, foto y salto de foco.

## Do's and Don'ts

### Do:
- **Do** componer toda superficie de papel como `var(--grano)` + color de papel; el grano es material, no adorno.
- **Do** poner la rotación de hojas en la sección contenedora y las rotaciones propias solo en elementos sin ::after de fondo (tiras, fotos, sello).
- **Do** enmascarar todo sello de goma con `var(--entintado)`.
- **Do** abrir cada cuartilla nueva con cabezal mecanografiado y número de hoja continuo.
- **Do** mantener las sombras en tono madera rgba(84, 62, 34, x), nunca negro neutro.
- **Do** respetar los 58ch de la prosa y el sistema de renglón (`--renglon`) dentro de la hoja rayada.

### Don't:
- **Don't** introducir un tercer color de tinta: solo sepia y rojo cinta bicolor (el azul de renglón es material de la libreta, no tinta de interfaz).
- **Don't** aplicar transform a `.cuartilla`: crea stacking context y la hoja de abajo tapa el fondo propio (bug documentado).
- **Don't** usar Courier Prime como decoración fuera de lo que el sujeto tecleó.
- **Don't** usar pesos bold en IM Fell ni sustituir las tres familias por fuentes de sistema o CDN: todo va autohospedado en woff2.
- **Don't** añadir motion más allá del mecanografiado de carga y las microtransiciones existentes; nada de reveals por scroll ni parallax.
- **Don't** resucitar el mundo anterior: tres tintas de revista (verde y rojo de offset), Besley/Archivo, sobreimpresión multiply o la doctrina de cero sombras son anti-referencia.
- **Don't** usar border-radius en el papel: el corte es recto; el único radio permitido es el 1px del focus ring.
