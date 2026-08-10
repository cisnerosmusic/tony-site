---
name: Antonio López Sánchez, número especial
description: Web de autor compuesta como número especial de revista literaria cubana, en tres tintas de offset sobre papel.
colors:
  verde: "#0d5a3c"
  verde-tinta: "#0a4530"
  rojo: "#d0342a"
  rojo-texto: "#a8271f"
  rojo-boton: "#b02a20"
  rojo-pagina: "#9c231b"
  tinta: "#201709"
  papel: "#f2e8d0"
  papel-sombra: "#e4d6b4"
typography:
  display:
    fontFamily: "Besley, Georgia, serif"
    fontSize: "clamp(2.7rem, min(11.5vw, 11svh), 9rem)"
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Besley, Georgia, serif"
    fontSize: "clamp(2.6rem, 7vw, 5.5rem)"
    fontWeight: 850
    lineHeight: 0.98
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Besley, Georgia, serif"
    fontSize: "clamp(1.7rem, 3.4vw, 2.6rem)"
    fontWeight: 850
    lineHeight: 1.05
    letterSpacing: "-0.015em"
  entradilla:
    fontFamily: "Besley, Georgia, serif"
    fontSize: "clamp(1.15rem, 2.4vw, 1.5rem)"
    fontWeight: 400
    lineHeight: 1.45
  body:
    fontFamily: "Besley, Georgia, serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  poema:
    fontFamily: "Besley, Georgia, serif"
    fontSize: "1.1rem"
    fontWeight: 400
    lineHeight: 1.75
  label:
    fontFamily: "Archivo, Helvetica Neue, sans-serif"
    fontSize: "0.8rem"
    fontWeight: 600
    letterSpacing: "0.08em"
    fontVariation: '"wdth" 80'
components:
  button-primary:
    backgroundColor: "{colors.rojo-boton}"
    textColor: "{colors.papel}"
    padding: "1.05rem 2.2rem"
  button-primary-hover:
    backgroundColor: "#8d1f18"
  button-directorio:
    backgroundColor: "{colors.verde}"
    textColor: "{colors.papel}"
    padding: "1.05rem 2.2rem"
  button-directorio-hover:
    backgroundColor: "{colors.verde-tinta}"
---

# Design System: Antonio López Sánchez, número especial

## Overview

**Creative North Star: "El Número Especial"**

La web no es un sitio de autor con hero y tarjetas: es un número especial de revista literaria cubana (linaje El Caimán Barbudo, La Gaceta de Cuba) dedicado íntegro a Antonio López Sánchez. Todo el sistema se deriva de la imprenta offset de tirada limitada: tres tintas (verde caimán, rojo offset, tinta cálida) sobre un papel crema que nunca se pinta, se reserva. Las secciones son pliegos a sangre que se hojean en scroll, cada uno con su cabezal, su folio de página y su titular rotundo; las tres tintas cometen a escala de página (verde en portada y periodista, tinta en novelas y directorio, papel en trova, rojo en el poeta).

La densidad es editorial, no de aplicación: texto corrido con capitular, columnas con corondel, sumario con líneas de puntos, fichas con filetes, un poema compuesto con sus espacios reales. La única fotografía admitida es documental: reproducciones de las cubiertas reales de los libros, montadas como encartes y recortes con filete y pie de crédito. No hay sombras, no hay esquinas redondeadas, no hay degradados; la única profundidad legítima es la que produce la tinta al sobreimprimirse (multiply), el misregistro deliberado de las pasadas y la leve rotación de los recortes pegados. El movimiento también viene del taller: al cargar, el número se imprime por pasadas de tinta en orden de imprenta, y la cabecera pierde peso variable al hacer scroll, como materia viva de composición tipográfica.

**Key Characteristics:**
- Tres tintas planas más papel como reserva; ningún cuarto pigmento en las superficies diseñadas.
- Cada tinta comete a escala de pliego: verde, tinta cálida, papel y rojo de página como fondos a sangre.
- Fotografía solo documental: cubiertas reales como encarte, siempre con filete de 1px y crédito en Archivo.
- Besley variable para todo lo que se lee; Archivo condensada para todo el aparato de revista.
- Filetes de 1px como única costura; cero sombras, cero radios.
- Sobreimpresión con `mix-blend-mode: multiply` donde dos tintas se tocan.

## Colors

Una paleta de taller de offset: tres tintas y el papel que las recibe, con variantes de trabajo por tinta para estados, texto y escala de página.

### Primary
- **Verde caimán** (#0d5a3c): la tinta identitaria del número. Fondo a sangre de la portada y del pliego "El periodista"; color del botón del directorio y del scrollbar.
- **Verde tinta** (#0a4530): el mismo verde cargado de tinta; solo como estado hover del botón verde.

### Secondary
- **Rojo offset** (#d0342a): la tinta de acento puro. Dibuja la guitarra del emblema, marca la selección de texto y el caret. Demasiado saturado para fondo de página: a esa escala se usa su variante rebajada.
- **Rojo página** (#9c231b): el rojo asentado a escala de pliego. Fondo a sangre de "El poeta"; da contraste 6.3:1 con el papel para lectura larga. Sobre este fondo la selección se invierte a tinta cálida y el foco visible pasa a papel.
- **Rojo texto** (#a8271f): el rojo rebajado para leer sobre papel; titulares y capitulares del pliego claro, y foco visible sobre fondo claro.
- **Rojo botón** (#b02a20): el rojo de impacto de la acción primaria (con hover #8d1f18, más hundido en tinta).

### Neutral
- **Tinta cálida** (#201709): el negro de imprenta con base cálida. Fondo de los pliegos oscuros, texto sobre papel, borde de botones y de recortes sobre papel.
- **Papel** (#f2e8d0): el soporte. Texto sobre tintas, reservas dentro del emblema, fondo del pliego "La trova". No es un color que se aplica: es lo que queda sin imprimir.
- **Papel sombra** (#e4d6b4): papel envejecido para texto secundario sobre verde y para el corondel de las columnas.

### Named Rules
**La Regla de las Tres Tintas.** Todo color diseñado es una de las tres tintas (verde, rojo, tinta cálida) o papel en reserva. No existe un cuarto pigmento, ni degradados, ni transparencias decorativas; las medias tintas se logran con `color-mix()` de una tinta hacia el papel o hacia otra tinta, nunca con colores nuevos.

**La Regla del Encarte.** La única imagen fotográfica del sistema es la reproducción documental de una cubierta real. Entra como cita, no como decoración: siempre enmarcada por un filete de 1px y acompañada de su pie de crédito en Archivo. Sus colores propios no ingresan a la paleta.

**La Regla de la Sobreimpresión.** Cuando dos tintas se superponen no se mezclan digitalmente: se sobreimprimen con `mix-blend-mode: multiply` y el resultado oscuro se acepta como física del offset (las pasadas fantasma del emblema de portada).

## Typography

**Display Font:** Besley variable, 400 a 900, con itálica (fallback Georgia, serif)
**Body Font:** Besley variable (la misma familia compone titulares, texto corrido y poema)
**Label Font:** Archivo variable, 400 a 900, ancho 62% a 125% (fallback Helvetica Neue, sans-serif)

**Character:** Besley pone la voz literaria: rotunda en negro 850 a 900 para titulares, serena en 400 para el texto corrido y el verso. Archivo, condensada y en mayúsculas, es el aparato de la redacción: folios, cabezales, datos editoriales, créditos y botones. Ambas se sirven como woff2 variables locales, sin terceros.

### Hierarchy
- **Display** (900, clamp(2.7rem, min(11.5vw, 11svh), 9rem), 0.92): la cabecera de portada, en mayúsculas, una palabra por línea. Su peso variable baja hasta 650 con el scroll (comportamiento de app.js).
- **Headline** (850, clamp(2.6rem, 7vw, 5.5rem), 0.98): el titular de cada pliego, con `text-wrap: balance`.
- **Title** (850, clamp(1.7rem, 3.4vw, 2.6rem), 1.05): títulos de novela; la obra premiada sube a clamp(2.1rem, 4.2vw, 3.4rem) y el título del poema baja a clamp(1.5rem, 3vw, 2.1rem), por jerarquía editorial.
- **Entradilla** (400, clamp(1.15rem, 2.4vw, 1.5rem), 1.45): el párrafo de entrada de un pliego, caja máxima de 38rem.
- **Body** (400, 1.0625rem, 1.6): texto corrido; sinopsis a máximo 52ch, texto documental a máximo 68ch.
- **Poema** (400, 1.1rem, 1.75): el verso, con `white-space: pre-wrap` porque los espacios internos del poema son significantes y se respetan tal como el autor los compuso.
- **Label** (600 a 700, 0.8rem, 0.08em, mayúsculas, `"wdth" 80`): folios, cabezales, sumario y términos de ficha. Los créditos y datos editoriales (pies de lámina y recorte, datos de obra, crédito del poema) usan la variante a `"wdth" 85`, peso 500 a 600 y tracking 0.03 a 0.08em.

### Named Rules
**La Regla de los Dos Oficios.** Besley compone todo lo que se lee; Archivo compone todo el aparato de revista. Ninguna familia invade el oficio de la otra, y no entra una tercera.

**La Regla del Aparato Condensado.** Todo texto de aparato estructural (folio, cabezal, término de ficha) va en Archivo a `"wdth" 80`, mayúsculas, 0.8rem y tracking 0.08em; los créditos documentales relajan el ancho a `"wdth" 85`. Es una sola voz de redacción repetida en toda la revista.

**La Regla del Verso Intacto.** El texto poético se reproduce con sus espacios y sangrías originales (`white-space: pre-wrap`); la maqueta nunca reescribe la respiración de un poema.

## Layout

El modelo espacial es el pliego: cada sección es una banda a sangre de una sola tinta, con padding horizontal `max(1.5rem, calc((100vw - 72rem) / 2))` que centra un ancho máximo de 72rem sin contenedor extra. El número tiene seis páginas: portada, novelas (p. 2), trova (p. 3), poeta (p. 4), periodista (p. 5) y directorio (p. 6). Dentro del pliego las cajas de lectura se limitan por contenido: 38rem la entradilla y el poema (este centrado), 60rem los cuerpos con recorte, 68rem las obras, y medidas en `ch` (44 a 68ch) para el texto corrido.

La portada es una retícula de filas (`auto minmax(0,1fr) auto auto auto`) que encaja portada completa en 100svh: folios absolutos arriba, cabecera, emblema flexible al centro, oferta, acción y sumario al pie. Decisión registrada: en escritorios de poca altura el emblema comprime hacia su preferencia de 21svh (mínimo 8.5rem); se acepta para que la portada nunca expulse el sumario del primer viewport.

Las obras alternan lámina y texto en retícula de dos columnas (5fr/6fr, la premiada 6fr/5fr con lámina mayor), con orden invertido en las pares. Los cuerpos de trova y periodista montan el recorte en una retícula de `minmax(0, 1fr) minmax(10rem, 14rem)` con gap de 3rem: la columna angosta es siempre la del recorte. El texto documental usa columnas CSS reales (`columns: 2 18rem`) con corondel de 1px. Bajo 44rem todo colapsa a una columna: láminas a la izquierda a 17rem, recortes a 14rem, y el folio derecho de portada desaparece. El ritmo vertical es amplio y editorial: 3.2rem entre obras, 4 a 5rem al cierre de pliego, separadores siempre de 1px.

## Elevation & Depth

No hay sombras de ninguna clase: ni `box-shadow`, ni `text-shadow`, ni desenfoques. La página es papel plano, y la profundidad se produce con los medios de la imprenta: sobreimpresión multiply donde las tintas se cruzan, pasadas fantasma desplazadas (el misregistro del emblema, a 6 o 7px de la pasada buena), filetes de 1px que cosen el aparato editorial, y la leve rotación de los recortes (1.4 grados, o -1.2 la variante izquierda), que se leen como material pegado sobre la página sin proyectar sombra. El hover de los botones se levanta con `translate(2px, -2px)` y el de las obras inclina la lámina 1.2 grados: el papel se despega, la tinta no.

### Named Rules
**La Regla del Papel Plano.** Ninguna superficie proyecta sombra. Si un elemento necesita separarse, lo hace con un filete de 1px, un cambio de tinta, una sobreimpresión o una rotación leve de material pegado.

**La Regla del Filete.** La única costura del sistema es un filete de 1px sólido (en `currentColor`, en tinta o en papel translúcido vía `color-mix`), más la línea de puntos del sumario. Nada más grueso, nada con color propio ajeno a las tintas.

## Shapes

Esquinas vivas de guillotina: `border-radius` 0 en todo el sistema (la única excepción es 1px en el contorno de foco, para que el trazo no se rompa). Las reproducciones de cubierta son rectángulos puros con filete, en su proporción original declarada (`width`/`height` en el HTML). Las formas curvas viven solo dentro del arte impreso del emblema (círculos, radiantes), nunca como contorno de componente. Los recortes se distinguen de las láminas por su rotación estática leve, como recorte de prensa pegado en el número.

## Components

### Buttons
- **Carácter:** tipografía de taller: Archivo 800, mayúsculas, 1.05rem.
- **Shape:** rectángulo puro sin radio, borde filete de 1px en tinta cálida.
- **Primary** ("Abrir el número"): fondo rojo botón (#b02a20), texto papel, padding 1.05rem 2.2rem, flecha SVG inline de 20px.
- **Hover / Focus:** el fondo se hunde a #8d1f18, el botón se despega con `translate(2px, -2px)` y la flecha baja 3px; todo con la curva `--paso` a 0.35s. Foco visible: contorno de 3px en rojo con offset de 3px (papel sobre el pliego rojo, rojo texto sobre papel).
- **Directorio:** misma anatomía en verde caimán con hover verde tinta. Deshabilitado: opacidad 0.65, sin transformaciones, cursor `not-allowed`.

### Cards / Containers
- **La obra** (artículo de novela): retícula lámina más texto, sin fondo propio ni borde de caja; las obras se separan entre sí con filete de papel al 25%. Al hover la lámina rota 1.2 grados (hacia el lado contrario en las pares).
- **La ficha** (dl del periodista): filas de término y definición con filete superior de papel al 35%; términos en voz de aparato condensado.

### Navigation
- **El sumario:** la navegación es el sumario del número, al pie de portada: lista ordenada de cinco entradas con tema, línea de puntos (`border-bottom: 1px dotted`) y folio de página ("p. 2" a "p. 6"). A partir de 54rem se parte en dos columnas. Hover: subrayado del tema. No existe barra de navegación fija ni menú hamburguesa.
- **El cabezal:** cada pliego abre con su línea de folio (título del número a la izquierda, "p. N" a la derecha) sobre filete de 1px en `currentColor`.

### La lámina (signature)
Encarte principal de cada novela: `figure` con la reproducción de la cubierta real (img/*.webp con dimensiones declaradas y `loading="lazy"`, alt descriptivo de la cubierta), filete de 1px en papel al 35% sobre la imagen, y pie de crédito `.lamina-pie` en Archivo `"wdth" 85`, 0.8rem, papel al 75%, que nombra la edición. Ancho máximo 21rem (26rem la obra premiada), centrada en su columna. Conserva el gesto del mundo: al hover de la obra, la lámina se inclina 1.2 grados con la curva `--paso`.

### El recorte
Reproducción secundaria de cubierta, como recorte de prensa pegado: `figure` con rotación estática de 1.4 grados (o -1.2 en la variante `-izq`), imagen con filete de 1px (tinta sobre papel; papel al 45% sobre verde) y `figcaption` de crédito en Archivo `"wdth" 85`. Se monta en la columna angosta (10 a 14rem) de los cuerpos de trova y periodista; bajo 44rem baja a 14rem en flujo.

### El poema
La página literaria del número: caja de 38rem centrada, título en Besley 850, cuerpo `.poema-texto` con `white-space: pre-wrap` que conserva las sangrías y los espacios internos del verso, y crédito en Archivo mayúsculas con filete superior de papel al 40%. Vive sobre el pliego rojo de página, con selección invertida a tinta.

### El emblema (signature)
Medallón radiante de portada: espada y guitarra sobreimpresas en rotaciones opuestas de 38 grados, con pasadas fantasma desplazadas (multiply al 50% y reserva al 40%) que declaran el misregistro de imprenta como firma visual. Toda ilustración nueva del sistema se resuelve como él: geometría plana en las tres tintas con reservas de papel, sin degradados ni trazos que no existan en offset.

### Motion
Una sola curva de easing para todo el sistema: `--paso: cubic-bezier(0.16, 1, 0.3, 1)`. Dos gestos de mundo: al cargar, las pasadas de tinta entran escalonadas cada 0.25s (verde, rojo, papel, negro) como órdenes de impresión; al hacer scroll, la cabecera pierde peso variable de 900 a 650. Ambos se apagan por completo con `prefers-reduced-motion: reduce`.

## Do's and Don'ts

### Do:
- **Do** imprimir cada pliego en una sola tinta de fondo (verde #0d5a3c, papel #f2e8d0, tinta #201709 o rojo página #9c231b) y reservar el rojo puro para acentos y acciones.
- **Do** montar toda reproducción de cubierta como material documental: filete de 1px, pie de crédito en Archivo, y rotación leve si es recorte.
- **Do** resolver toda superposición de tintas con `mix-blend-mode: multiply` y aceptar el oscurecimiento resultante.
- **Do** derivar medias tintas con `color-mix()` desde las tintas existentes, nunca con valores nuevos.
- **Do** componer todo aparato editorial (folios, cabezales, términos, créditos) en Archivo condensada, mayúsculas donde es estructural, 0.8rem.
- **Do** usar la única curva `--paso` para cualquier transición y apagarla bajo `prefers-reduced-motion`.
- **Do** conservar los espacios internos de cualquier texto poético con `white-space: pre-wrap`.

### Don't:
- **Don't** usar sombras (`box-shadow`, `text-shadow`) ni desenfoques: la profundidad es tinta, filete, sobreimpresión y rotación de recorte.
- **Don't** redondear esquinas: `border-radius` 0 en todo componente (solo 1px en el contorno de foco).
- **Don't** introducir colores diseñados fuera de las tres tintas más papel, ni degradados; la fotografía solo entra como reproducción de cubierta real con filete y crédito, y sus colores no ingresan a la paleta.
- **Don't** sumar una tercera familia tipográfica ni usar fuentes del sistema: solo Besley y Archivo locales.
- **Don't** montar navegación de app (barra fija, hamburguesa, tarjetas): la navegación es el sumario y el scroll hojea los pliegos.
- **Don't** usar raya larga en ningún texto visible de la página (regla editorial del proyecto).
