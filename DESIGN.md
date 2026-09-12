---
name: Ala del Mar
description: La casa del escritor Antonio López Sánchez, de noche frente al mar de Alamar; navy en varias tonalidades y serif dorada
colors:
  bg-deep: "#0a0c1f"
  bg-dark: "#0d0f2b"
  bg-section: "#0f1130"
  bg-card: "rgba(16, 18, 42, 0.7)"
  navy: "#1a1d4a"
  navy-light: "#252860"
  gold: "#d4a030"
  gold-bright: "#f0c860"
  gold-dim: "rgba(212, 160, 48, 0.5)"
  gold-faint: "rgba(212, 160, 48, 0.12)"
  text-primary: "#e8e4dc"
  text-secondary: "#c8c3b9"
  text-dim: "#b4aa9b"
  line: "rgba(212, 160, 48, 0.12)"
  line-bright: "rgba(212, 160, 48, 0.25)"
typography:
  display:
    fontFamily: "Cinzel, serif"
    fontSize: "clamp(2rem, 4.5vw, 3.4rem)"
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: "0.12em"
  headline:
    fontFamily: "Cinzel, serif"
    fontSize: "clamp(1.8rem, 4vw, 2.8rem)"
    fontWeight: 400
    letterSpacing: "0.08em"
  seccion:
    fontFamily: "Cinzel, serif"
    fontSize: "clamp(1.2rem, 2.5vw, 1.6rem)"
    fontWeight: 400
    letterSpacing: "0.06em"
  body:
    fontFamily: "Cormorant Garamond, serif"
    fontSize: "1.05rem"
    fontWeight: 300
    lineHeight: 1.9
  lema:
    fontFamily: "Cormorant Garamond, serif"
    fontSize: "1.3rem"
    fontStyle: italic
    fontWeight: 300
    letterSpacing: "0.06em"
  aparato:
    fontFamily: "Space Mono, monospace"
    fontSize: "0.7rem"
    fontWeight: 400
    letterSpacing: "0.1em"
    textTransform: uppercase
components:
  btn:
    backgroundColor: transparent
    textColor: "{colors.gold}"
    borderColor: "{colors.gold-dim}"
    typography: "{typography.aparato}"
    padding: "0.9rem 2.2rem"
  btn-filled:
    backgroundColor: "{colors.navy}"
    borderColor: "{colors.gold-dim}"
    textColor: "{colors.gold-bright}"
  poema:
    backgroundColor: "{colors.bg-card}"
    borderColor: "{colors.line}"
    padding: "clamp(2rem, 5vw, 3.5rem)"
  audio-item:
    backgroundColor: "{colors.bg-card}"
    borderColor: "{colors.line}"
    padding: "2rem 2.2rem"
---

# Design System: Ala del Mar

> **Aviso para quien retome el proyecto.** Este documento describe el sistema **en vivo**, el que corresponde a `styles.css` y a lo que sirve antoniolopezsanchez.art. Una versión anterior de este mismo archivo describía otro mundo completamente distinto, de cuartillas de papel sobre una mesa azul pálido, con añil #1d4e89, Bonum y Courier Prime. **Ese camino fue abandonado.** El autor y el estudio eligieron la dirección navy y oro heredada de la plantilla propia de Index01. Si encuentras en cualquier parte del proyecto referencias a añil, mesa, cuartilla, sello de goma, Bonum o Courier Prime, son fósiles de aquella iteración: no son autoridad y no se restauran.

## Overview

La casa del escritor de noche frente al mar. Fondos azul noche en varias tonalidades, un único acento en oro, serif romana para los nombres y los títulos, serif de lectura para la prosa y la poesía, y monoespaciada solo para el aparato (etiquetas, metadatos, notas, pie). La estructura del sitio es de página larga con secciones anchas, no de documento.

Base heredada de [impulses-art-site](https://github.com/cisnerosmusic/impulses-art-site), plantilla propia de Index01, adaptada a esta casa.

## Colors

Paleta nocturna: azules profundos de fondo, un solo oro de acento, y textos cálidos de papel viejo sobre la noche.

### Primary
- **Oro** (#d4a030, `--gold`): el único acento del sistema. Logo de navegación, títulos de sección, nombre de la casa, títulos de libro, subrayado de la página activa, bordes de botón en hover, foco visible.
- **Oro brillante** (#f0c860, `--gold-bright`): hover sobre texto ya dorado, y **el oro cuando va sobre navy**, que es el fondo más claro del sitio: texto del botón sólido y del salto al contenido. Sobre navy el oro normal se queda en 6,73:1 y en el hover del botón baja a 5,72:1.
- **Oro tenue** (rgba(212, 160, 48, 0.5), `--gold-dim`): **solo bordes y superficies, nunca texto.** Borde de botón en reposo y fondo del divisor que respira.
- **Oro velado** (rgba(212, 160, 48, 0.12), `--gold-faint`): relleno de botón en hover. Nunca texto.

### Neutral
- **Noche profunda** (#0a0c1f, `--bg-deep`): fondo del body y del pie. Es el suelo del mundo.
- **Noche de sección** (#0f1130, `--bg-section`): fondo de `.section-alt`, para alternar bloques sin cambiar de mundo.
- **Noche de tarjeta** (rgba(16, 18, 42, 0.7), `--bg-card`): superficie de los contenedores aislados, poema y audio.
- **Navy** (#1a1d4a, `--navy`) y **navy claro** (#252860, `--navy-light`): relleno del botón sólido y su hover. Único uso.
- **Texto principal** (#e8e4dc, `--text-primary`): prosa literaria, versos, nombre del autor. Cálido, no blanco.
- **Texto secundario** (#c8c3b9, `--text-secondary`): prosa de presentación, sinopsis, navegación, `dd` de ficha.
- **Texto tenue** (#b4aa9b, `--text-dim`): aparato de menor jerarquía: metadatos, pies de galería, notas, copyright. Es el texto más pequeño del sitio.
- **Línea** (rgba(212, 160, 48, 0.12), `--line`) y **línea viva** (rgba(212, 160, 48, 0.25), `--line-bright`): hairlines dorados al 12% para separar, al 25% para enmarcar cubiertas y versos.

### Named Rules

**La regla del oro único.** Hay un solo acento en toda la casa. Ningún segundo color entra al sistema: si algo necesita distinguirse, cambia de peso, de familia o de fondo, nunca de color.

**El fondo nunca es negro.** Ningún fondo es #000 ni gris neutro. Siempre es azul de noche, en alguna de sus tonalidades.

**Las líneas son oro al 12%.** Todo separador y todo borde estructural nace del oro rebajado, no de un gris. Es lo que mantiene la unidad del mundo cuando no hay color.

**Ningún texto por debajo de 7:1, y los textos no llevan alfa.** El sitio entero cumple **AAA**: el peor contraste de cualquier texto en cualquier página es 7,76:1. La razón no es solo accesibilidad formal. Una web casi toda navy dispara el atenuado automático de brillo de muchos monitores (CABC en LCD, ABL en OLED), y aunque la ratio de contraste sobrevive matemáticamente a esa atenuación, la percepción no: la sensibilidad del ojo cae en luminancias bajas y esos sistemas suelen aplastar la gamma justo en los grises medios. Por eso **los colores de texto son sólidos, sin transparencia**: la opacidad era lo que los apagaba. Si necesitas un texto más discreto, baja de escalón en la escalera (primary, secondary, dim), nunca le pongas alfa. La escalera es 14,49 / 10,46 / 8,02, y el oro de tinta 7,76.

## Typography

Tres familias, autohospedadas en `fonts/` como woff2 subset latin, sin una sola petición a Google.

### Hierarchy
- **Cinzel 400** (`--font-display`): romana capital. Nombres, títulos de sección, títulos de libro, botones y navegación. Siempre con tracking abierto (0.05em a 0.2em) y con frecuencia en ALTAS. Nunca se usa para leer.
- **Cormorant Garamond 300/400/500, con itálicas 300/400** (`--font-body`): la letra de lectura. Prosa, sinopsis, fragmentos, poemas, lema. El peso por defecto del cuerpo es 300 y la interlínea es ancha (1.7 en el body, 1.9 en la prosa de sección).
- **Space Mono 400** (`--font-mono`): el aparato. Etiquetas de ficha, metadatos de libro, pies de galería, notas, idiomas, copyright. Siempre pequeña (0.6rem a 0.7rem), en ALTAS y con tracking amplio.

El body arranca en 18px con `line-height: 1.7`. Los tamaños grandes usan `clamp()` para escalar con el viewport; el aparato usa pasos literales en rem.

### Named Rules

**Cada familia tiene un solo oficio.** Cinzel nombra, Cormorant lee, Space Mono etiqueta. Una familia nunca invade el trabajo de otra: no hay títulos en Cormorant ni prosa en Cinzel.

**El aparato siempre en altas y con tracking.** Todo lo que es Space Mono va en mayúsculas con `letter-spacing` de 0.06em a 0.14em. Es lo que lo distingue de la lectura sin necesidad de color.

**Los textos literarios respetan su forma original.** `.fragmento-verso` y `.poema-texto` usan `white-space: pre-wrap` para conservar la sangría y los cortes de verso del autor.

## Layout

Página larga y ancha, no documento. `.section` mide `max-width: 1200px` con `padding: 80px 3rem`; las páginas de libro estrechan a `max-width: 860px` con `.libro-pagina`, y la prosa se acota a 62-70ch para que la línea sea legible.

La portada usa `.split`, un grid de dos columnas a `1fr 1fr` con `min-height: 92vh`: retrato a sangre a la izquierda con degradado que lo funde con el fondo por la derecha, y el bloque de nombre a la derecha. Las páginas interiores abren con `.page-header`, centrado, con degradado de `--bg-section` a `--bg-deep`.

Entre secciones puede ir `.banda-mar`, una banda de 42vh con la foto del mar, oscurecida por un degradado de tres paradas para que el texto encima siga legible.

**Un solo breakpoint, a 900px.** Ahí el split cae a una columna con la imagen a 48vh, la navegación se convierte en menú desplegable, `.libro-item` y `.ficha div` pasan a una columna, y los paddings se reducen a 1.5rem.

**La regla de la hoja nueva.** Toda página de libro se genera con `herramientas/gen-libro.py` desde un manifiesto JSON (`herramientas/libros/<slug>.json`); su estructura es fija y en este orden: cubierta dominante, nota de contratapa, **con voz y voto**, fragmentos, presentaciones, prensa y **ficha**, que cierra. El autor pidió ese orden el 8 de septiembre de 2026: su comentario arriba, la ficha de datos al final. Los libros que salieron en varios tomos llevan además un bloque de volúmenes tras la contratapa. No se maquetan páginas de libro a mano.

## Elevation & Depth

La profundidad es atmosférica y sobria: sombras negras difusas bajo las cubiertas, que son los únicos objetos que se levantan del fondo. No hay tarjetas elevadas ni superficies flotantes.

### Shadow Vocabulary
- **Cubierta en lista** (`0 8px 30px rgba(0, 0, 0, 0.45)`): las portadas de `/libros/`, que suben 4px y refuerzan la sombra en hover.
- **Cubierta dominante** (`0 14px 50px rgba(0, 0, 0, 0.55)`): la portada grande al abrir la página de un libro.
- **Resplandor de botón** (`0 0 20px rgba(212, 160, 48, 0.1)`): el único glow del sistema, y solo en hover del botón.

### Named Rules

**Solo los libros tienen sombra.** La sombra está reservada a las cubiertas, que son objetos físicos en un mundo plano. Ningún contenedor, ninguna sección y ningún bloque de texto proyecta sombra.

**Nada se eleva por estado**, salvo la cubierta en hover, que sube 4px. La navegación fija se separa del contenido con `backdrop-filter: blur(12px)` sobre fondo al 92%, no con sombra.

## Shapes

Esquinas vivas en todo: radio 0 en botones, cubiertas, fichas y contenedores. La única geometría curva del sistema es el `outline-offset` del foco. Los bordes son de una sola familia, hairlines de 1px en oro rebajado: `--line` al 12% para separar filas, secciones y pies, `--line-bright` al 25% para enmarcar cubiertas y para la barra vertical del verso.

**La regla de nada redondeado.** Ningún radio, ninguna píldora, ningún círculo decorativo. Si un elemento necesita distinguirse, cambia de fondo o de borde, no de forma.

## Components

### Botón (.btn)
- **Carácter:** placa grabada, no botón de interfaz.
- **Shape:** rectángulo de esquinas vivas, borde 1px en oro tenue, fondo transparente.
- **Tipografía:** Cinzel 0.7rem en ALTAS, tracking 0.12em; padding 0.9rem 2.2rem.
- **Hover:** fondo oro velado, borde a oro pleno, texto a oro brillante, glow de 20px al 10%.
- **Variante `.btn-filled`:** fondo navy, hover a navy claro. Es la acción primaria de la portada.
- **Disabled:** texto en `--text-dim`, borde en `--line`, sin fondo ni sombra.

### Navegación (.nav)
- Fija arriba, fondo `rgba(10, 12, 31, 0.92)` con `backdrop-filter: blur(12px)`, hairline inferior. Logo en Cinzel oro con tracking 0.2em; enlaces en Cinzel 0.7rem ALTAS en texto secundario, a oro en hover, y la página activa con subrayado dorado de 1px vía `::after`.
- **Por debajo de 900px** se colapsa en hamburguesa de tres barras doradas y el menú se despliega fijo bajo la barra. Pendiente de accesibilidad: le faltan `aria-expanded`, `aria-controls` y cierre con Escape. Ver `PENDIENTES.md`, sección 6.

### Cabecera interior (.page-header)
- Bloque centrado de apertura de toda página que no sea la portada: título en Cinzel oro con `clamp(1.8rem, 4vw, 2.8rem)`, bajada en texto secundario acotada a 700px, degradado de sección a noche profunda y hairline inferior.

### Título de sección (.section-title + .section-divider)
- Título en Cinzel oro, y debajo un divisor de 50px por 1px en oro tenue que **respira**: animación `breathe` de 4s que lo lleva de 50px al 50% de opacidad hasta 75px al 100% y vuelve. Se apaga con `prefers-reduced-motion`.

### Ficha (.ficha)
- `dl` en grid de dos columnas con hairlines entre filas. `dt` en Space Mono 0.68rem ALTAS en oro tenue; `dd` en texto secundario acotado a 62ch. Es donde vive la línea de derechos de cada libro.

### Libro en lista (.libro-item)
- Grid de cubierta (`minmax(10rem, 15rem)`) más texto, separados por hairline. Título en Cinzel oro, metadatos en Space Mono tenue con el premio en oro tenue, sinopsis en texto secundario a 62ch. La cubierta sube 4px en hover.

### Fragmentos
- `.fragmento-titulo`: Cormorant 500 en texto principal. `.fragmento`: prosa en texto secundario. `.fragmento-verso`: verso con `white-space: pre-wrap`, barra vertical de 1px en `--line-bright` a la izquierda y sangría de 1.5rem.

### Poema (.poema)
- Contenedor aislado de 620px sobre `--bg-card` con hairline: título en Cinzel oro, texto en Cormorant 300 a 1.15rem con interlínea 1.95 y `pre-wrap`, y crédito al pie en Space Mono oro tenue sobre hairline superior.

### Audio (.audio-item)
- Mismo contenedor que el poema: título en Cinzel oro, metadatos en Space Mono tenue, y `<audio controls preload="none">` a ancho completo. El `preload="none"` no se quita: son ficheros de varios MB.

### Laureles (.laurel-item)
- Grid de año (90px, Cinzel 1.4rem en oro tenue, alineado a la derecha) más contenido, con hairline entre filas. A 900px el año baja a 56px y 1.1rem.

### Galería (.galeria)
- Grid `repeat(auto-fit, minmax(14rem, 1fr))`, imágenes con hairline y pies en Space Mono tenue de 0.65rem.

### Nota (.nota-demo)
- Space Mono 0.65rem en texto tenue. **El nombre engaña:** ya no marca contenido de demostración, ahora lleva notas reales al lector (el aviso de que los textos literarios se publican en su español original). Está pendiente renombrarla a `.nota` antes de clonar la plantilla a otro artista. No la borres pensando que es andamiaje.

### Pie (.footer)
- Centrado sobre noche profunda con hairline superior: índice de las 8 secciones en Cinzel 0.65rem ALTAS, iconos sociales en SVG inline, lema *bene scriptus* en Cormorant itálica oro tenue, y dos líneas de copyright y crédito en Space Mono tenue.

### Motion
- **El único motion del mundo** es la aparición lateral de bloques: `.reveal` entra desde ±60px en X con opacidad 0, y `app.js` le pone `.visible` cuando el `IntersectionObserver` lo ve asomar (threshold 0, rootMargin -8% abajo). Transición de 0.9s. Los bloques más altos que 1.2 viewports se muestran directos, porque un capítulo completo nunca alcanzaría el umbral y el contenido largo jamás debe poder quedar invisible. Sin `IntersectionObserver` todo se muestra.
- El segundo y último movimiento es el `breathe` del `.section-divider`.
- Con `prefers-reduced-motion: reduce` se apagan el reveal, el breathe y el scroll suave.

## Do's and Don'ts

### Do:
- Usa el oro como único acento, y cámbiale la opacidad antes de pensar en otro color.
- Deja respirar: 80px de padding vertical en secciones de escritorio, prosa a 62-70ch.
- Pon `width` y `height` en toda imagen, **con la proporción real del archivo**. Si no coinciden, el navegador reserva un hueco que no es y la maqueta salta al cargar. El comprobador falla cuando no coinciden.
- Un enlace dentro de un texto se distingue por algo más que el color: va subrayado. El oro sobre el texto atenuado del pie no se distingue por luminancia, y un enlace que solo se reconoce por su color falla la WCAG 1.4.1.
- Envuelve los bloques nuevos en `.reveal reveal-left` o `.reveal reveal-right`, alternando el lado.
- Sube el `?v=N` de `styles.css`, `fonts.css` y `app.js` al publicar cambios.
- Genera las páginas de libro con `gen-libro.py`.

### Don't:
- No metas un segundo acento de color, ni rojo, ni verde de estado, ni añil.
- No uses fondos blancos, grises neutros ni #000.
- No redondees nada.
- No cargues fuentes, scripts ni imágenes desde terceros: todo se autohospeda.
- No pongas texto sobre `--gold-faint` ni `--line`: son superficies y bordes, no colores de tinta.
- No maquetes a mano una página de libro.
- No restaures el mundo de cuartillas, mesa azul y añil. Fue abandonado.
