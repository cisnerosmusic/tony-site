# Pendientes · Ala del Mar

Nota de trabajo para retomar el proyecto. Estado al 8 de septiembre de 2026.

## Dónde quedamos

El sitio está **completo y sirviendo en todo el mundo** desde [antoniolopezsanchez.art](https://antoniolopezsanchez.art), con dominio propio, HTTPS, correo operativo, indexación enviada a Google y Bing, y auditoría de SEO/AEO aplicada.

El 8 de septiembre, además, **se reescribió `DESIGN.md`**, que documentaba con autoridad total un sistema visual abandonado (cuartillas de papel sobre mesa azul, añil, Bonum, Courier Prime) sin una sola coincidencia con el sitio real. Era la única incidencia capaz de hacer que un agente rompiera el sitio activamente en vez de simplemente dejar algo sin hacer. Ahora describe el mundo navy y oro que está en vivo, y lleva un aviso al inicio para que nadie resucite el anterior.

El 8 de septiembre se revisó el repositorio entero y **se corrigió el rumbo del producto en `PRODUCT.md`**: el público de esta web no es Cuba. Allí Tony ya tiene editoriales y circuito; la web se construyó para el afuera, y su lector de mayor valor es el editor, agente o traductor extranjero. De ahí salen los pendientes nuevos de la sección 1, que son los que más pagan. Lee `PRODUCT.md` antes de tocar nada: la jerarquía de la obra ahora depende del idioma.

## 0. La tarde del 8 de septiembre: entró el contenido

Por la mañana el sitio era una casa bien construida y medio vacía. Por la tarde
Tony mandó material sin parar y dejó de estarlo. Lo que hay ahora, todo en vivo:

| Sala | Qué tiene | Motor |
|---|---|---|
| **Contarte** (nueva) | 7 cuentos completos, uno por habitación | `gen-cuento.py` + `cuentos.json` |
| **Poemas sueltos** | 20 poemas, 8 de ellos glosas | `gen-poemas.py` + `poemas.json` + `leer-poema.py` |
| **De-Cimitas** | 7 piezas de foto y décima | `gen-decimitas.py` + `decimitas.json` |
| **Sonata de la lluvia** (nueva) | 150 versos en 3 movimientos | `gen-sonata.py` |
| **Entre lectores** (nueva) | 11 fotos de ferias y firmas | a mano |
| **Plano abierto** | 1 programa de TV, 2 de radio, lectura y concierto | `gen-audios.py` + `grabaciones.json` |
| **4 fichas de libro** | prensa verificada con enlace | `gen-libro.py` |

**40 páginas HTML, 37 URLs en el sitemap, unos 98 MB de medios.**

Reglas que salieron de esta tanda y que conviene no re-descubrir:

- **La atribución es lo primero.** Ocho poemas glosan a Martí y a Lezama, una
  décima cita a Polito Ibáñez y la sonata lleva epígrafes de Fito Páez, Noel
  Nicola y Santiago Feliú. Esos versos **no son del autor** y salen siempre en
  bloque aparte, con la firma de quien los escribió.
- **En verso no se normaliza nada.** El autor usa espacios múltiples dentro del
  verso como puntuación y sangría de tres espacios para abrir cada décima de una
  tirada. Todo se muestra con `white-space: pre-wrap`. `a-texto.py --verso`
  conserva además las líneas en blanco, que separan estrofas.
- **Los títulos de poema van escritos a mano en el manifiesto.** En los
  originales están en mayúsculas y pasarlos a minúsculas por programa rompe los
  nombres propios y confunde el nombre de la serie con el del poema.
- **Un texto vive una sola vez.** Si pertenece a dos salas, se repite el
  reproductor o el enlace, nunca el texto ni el marcado de datos. Ver AGENTS.md.

### Lo que se quedó fuera a propósito

- **Dos cuentos**, *Cantar el cuento III* y *La urna del tío*, que el autor marcó
  en el nombre del archivo como pertenecientes a libros en proceso editorial.
  Necesitan su palabra antes de publicarse.
- **Proclama Real**, por la decisión ya escrita en los innegociables.
- **Los diplomas del Farraluque**: sus datos entraron como texto en Laureles, las
  fotos no. Eran fotos de folios y bajaban la autoridad de la página en vez de
  subirla.
- **Inéditos sigue vacía, y está bien así.** Es la única sala sin contenido y el
  autor se toma su tiempo. No se llena con relleno.

## 1. El embudo de derechos (HECHO el 8 de septiembre)

**Decisión del autor, por teléfono el 8 de septiembre de 2026: toda gestión de derechos fuera de Cuba pasa por Ernesto Cisneros, y todo el mundo va a dos destinos y ningún otro, sea cual sea el idioma:**

1. `https://ernestocisneros.art/es/representacion-literaria.html`
2. `derechos@antoniolopezsanchez.art`

Estaban los dos declarados y no se llegaba a ninguno. Ya se cerró: **16 páginas ofrecen ahora salida de derechos** donde antes había cero.

- Las 14 fichas de libro llevan la salida dentro del contenido, no solo en el menú. La emite `herramientas/gen-libro.py` desde las constantes `REPRESENTACION`, `DERECHOS_EMAIL` y `SALIDA_DERECHOS`. **Si cambia un destino, se cambia ahí y en ningún otro sitio.**
- `/directorio/` ofrece los dos botones y publica la dirección.
- `/en/` tiene sección propia "Rights and representation", con entrada en el menú, en el pie y en la portada.

**Sincronía VERIFICADA el 8 de septiembre desde la Máquina 1**, en el commit `30cfae3`, que es la única que puede ejecutar el generador. Se regeneraron los 14 manifiestos y `git status` quedó vacío: el HTML publicado y `gen-libro.py` producen exactamente lo mismo, byte a byte, incluida la fila de derechos y el `?v=7`. El parcheo a mano de la Máquina 2 fue correcto.

Sigue en pie la fragilidad de fondo: si alguien toca `SALIDA_DERECHOS` sin poder regenerar, hay que volver a parchear a mano o divergen en silencio. Eso se acaba cuando el punto 3 esté resuelto.

**Pendiente de decisión:** `/en/` apunta a la versión **inglesa** de la página de representación (`/literary-representation.html`), no a la española. Es el mismo destino en el idioma del lector, y mandar a un editor anglófono a una página en español contradice el propósito del sitio. Si Ernesto prefiere el `/es/` literal en todas partes, es cambiar un `href` en `en/index.html`.

Regla fijada en `PRODUCT.md`: *ninguna declaración de derechos sin salida, en el idioma de quien lee*.

**El dossier de derechos no se duplica aquí.** El sitio de Tony es la casa y el catálogo; el sitio de Ernesto es el negocio. Esa separación es deliberada.

## 2. Accesibilidad: contraste (HECHO el 8 de septiembre, nivel AAA)

**El sitio entero cumple AAA.** El peor contraste de cualquier texto en cualquier página es **7,76:1**, cuando el mínimo AA es 4,5 y el AAA es 7.

| Token | Antes | Ahora |
|---|---|---|
| `--text-primary` | 14,49:1 | 14,49:1 (sin tocar) |
| `--text-secondary` | 5,64:1 | **10,46:1** (`#c8c3b9`) |
| `--text-dim` | 2,89:1 | **8,02:1** (`#b4aa9b`) |
| oro como texto | 2,80:1 | **7,76:1** (`--gold`) |
| oro sobre navy (botón sólido) | 6,73:1, y 5,72:1 en hover | **9,96:1** y 8,47:1 (`--gold-bright`) |

**Por qué AAA y no AA.** No es purismo. Una web casi toda navy dispara el atenuado automático de brillo de muchos monitores (CABC en LCD, ABL en OLED). La ratio de contraste sobrevive matemáticamente a esa atenuación, pero la percepción no: la sensibilidad del ojo cae en luminancias bajas y esos sistemas suelen aplastar la gamma justo en los grises medios. Un usuario con un monitor así veía el aparato del sitio casi negro sobre negro y se iba. Con la escalera actual el texto aguanta la atenuación.

**Los textos ya no llevan alfa.** Esa era la causa real: los colores base siempre fueron correctos, la transparencia era lo que los apagaba. Quitarla dio la escalera sola. Regla que quedó en `DESIGN.md`: si un texto tiene que ser más discreto, se baja de escalón (primary, secondary, dim), **nunca se le pone opacidad**.

`--gold-dim` sigue existiendo pero ahora es estrictamente borde y superficie. El token que había creado unas horas antes para el oro de tinta se eliminó: con objetivo AAA el oro de texto es simplemente `--gold`, y el sistema quedó más simple que por la mañana.

`styles.css` iba por `?v=7` cuando se escribió esto; al cerrar el 8 de septiembre va por **`?v=19`**, y sube con cada cambio de hoja de estilos en las 40 páginas y en los seis generadores a la vez. `fonts.css` se queda en `?v=5` a propósito: las fuentes no han cambiado.

Verificado midiendo el contraste real de cada nodo de texto renderizado, no los tokens en teoría, en 13 páginas incluido el 404.

**Contraverificación independiente desde la Máquina 1, commit `30cfae3`**, calculando la matriz completa de tinta contra fondo con la fórmula WCAG. Confirma el AAA: sobre los tres fondos que existen de verdad (`--bg-deep`, `--bg-dark`, `--bg-section`) el peor par es `--gold` sobre `--bg-section`, **7,76:1**, y sobre `--bg-card` compuesto sobre el fondo profundo (`#0e1027`) el oro da **7,91:1**. Los pares flojos que aparecen en la teoría, `--text-dim` y `--gold` sobre `--navy` (6,95:1 y 6,73:1) y sobre `--navy-light` (5,91:1 y 5,72:1), **no se renderizan nunca**: `--navy` y `--navy-light` solo se usan como fondo en tres reglas, el salto al contenido y `.btn-filled` con su hover, y las tres llevan `--gold-bright` encima (9,96:1 y 8,47:1). La afirmación de AAA se sostiene.

**Hallazgo abierto, contraste de borde.** `--gold-dim` a alfa 0,5 compuesto sobre `--bg-deep` da `#6f5628`, **2,80:1** contra el fondo, por debajo del 3:1 que la WCAG 1.4.11 pide a los límites de un control. Afecta al borde de `.btn` (`styles.css:282`) y de `.btn-filled` (`styles.css:294`). No impide usar el botón, cuyo texto va a 12:1, pero el borde en sí es el elemento que queda corto. Arreglo de una línea: subir el alfa de `--gold-dim` de 0,5 a **0,55**, que da 3,14:1 con un cambio visual casi imperceptible. No lo aplico porque toca el peso visual de los botones y esa es decisión de diseño de Ernesto.

## 3. El generador no es reproducible

`herramientas/gen-libro.py` es la única forma de tocar las páginas de libro, pero **desde un clon limpio no corre**. Las 45 rutas de texto declaradas en los manifiestos de `herramientas/libros/*.json` apuntan a `C:/Users/Ernesto/OneDrive/Imágenes/tony/x/...`, un perfil de Windows que no existe ni en la máquina de casa ni en la de UW. Hoy el pipeline vive en un solo disco.

Arreglo: copiar los `.txt` **ya publicados** a `herramientas/textos/<slug>/` y volver relativas las rutas de los manifiestos.

**Cuidado**: solo el material que ya está en el sitio. Los inéditos no entran en este repositorio, que es público, porque publicarlos les quitaría la condición de inéditos ante concursos y editoriales.

**Cómo verificar que la regeneración salió bien.** Este es el paso que no se puede saltar. Las 14 páginas actuales tienen dos cambios hechos a mano el 8 de septiembre que el generador ya sabe reproducir: la salida de derechos en la ficha y `styles.css?v=7`. Al regenerar por primera vez, el diff **tiene que salir vacío o casi vacío**. Si aparecen diferencias masivas, no es que el generador esté mal: es que algún `.txt` copiado no es el mismo que se uso para publicar.

Procedimiento:

```bash
git status --short            # limpio antes de empezar
python herramientas/gen-libro.py herramientas/libros/grimorium.json
git diff --stat               # una sola pagina, para probar
```

La fila de derechos regenerada debe quedar exactamente así, en una sola línea:

```html
<div><dt>derechos</dt><dd>Disponibles para ediciones y traducciones fuera de Cuba. <a href="https://ernestocisneros.art/es/representacion-literaria.html">Consultas de derechos</a> · <a href="mailto:derechos@antoniolopezsanchez.art">derechos@antoniolopezsanchez.art</a></dd></div>
```

Si esa página sale idéntica, se regeneran las 13 restantes. Si sale distinta, **para y revisa el `.txt` antes de regenerar el resto**: es más fácil arreglar una que catorce.

**Esa comprobación ya se hizo el 8 de septiembre desde la Máquina 1, en el commit `30cfae3`, y salió limpia**: las 14 regeneradas, `git status` vacío. Así que el parcheo a mano está validado y el aviso de sincronía del punto 1 quedó cerrado. Lo que sigue abierto es lo otro, que el pipeline vive en un solo disco: mientras las rutas apunten al OneDrive, la Máquina 2 no puede tocar el generador sin dejar que HTML y generador diverjan a ciegas.

`gen-libro.py` necesita Pillow (`pip install Pillow`): lee las dimensiones reales de cada imagen para emitir `width` y `height`, que es de donde sale el CLS 0 del sitio.

## 3 bis. El orden de trabajo para mañana, 9 de septiembre

Fijado con Ernesto al cerrar la jornada del 8, y en este orden:

1. **Revisar el SEO de cada página, una por una.** La última auditoría es del 8
   por la mañana y desde entonces han nacido siete páginas de cuento, la sonata,
   Contarte, Entre lectores y De-Cimitas. Hay que comprobar en cada una título,
   descripción, canónica, tarjetas sociales y JSON-LD, y volver a enviar el
   sitemap y el ping de IndexNow.
2. **Actualizar `README.md` y estos pendientes** cada vez que se cierre algo, no
   al final. (El README se puso al día el 8 por la noche.)
3. **Empezar la versión inglesa en serio.**

### La versión inglesa no es la española traducida

Es la regla que ya está en `PRODUCT.md` y que conviene tener delante desde la
primera línea: **la prioridad del mundo anglosajón es distinta de la del mundo
hispanohablante.**

- En español manda la **fantasía heroica**: es lo que tiene circuito, premios y
  lectores, y por eso abre Mis libros.
- En inglés lo que abre puertas primero es **la trova**: hay editoriales
  universitarias, departamentos de estudios latinoamericanos y de música, y
  revistas académicas que buscan exactamente lo que Tony lleva veinte años
  documentando. *Convertida en canción*, *Trovadoras* y *La canción de la Nueva
  Trova* son, para ese lector, la puerta de entrada, no una sección lateral.
- El segundo argumento en inglés es que **los derechos mundiales están libres**,
  que ya tiene su sección en `/en/`.

Traducir el aparato, nunca la literatura: navegación, presentaciones, fichas,
notas de prensa y metadatos. Los poemas, los cuentos y los fragmentos se quedan
en español, con su aviso. Hoy `/en/` es solo la portada.

## 4. Traducciones

Es la vía para que la obra llegue a los lectores y editores que no leen español. Se hace con calma y bien.

**El inglés es la prioridad real y va primero.** Francés, italiano y portugués después. Ruso descartado (decisión de Ernesto, sep 2026): Cinzel y Space Mono no tienen cirílico y traducir al ruso obligaría a cambiar la tipografía de titulares, lo que rompería el sistema visual. Verificado que francés, italiano, portugués y español caben enteros en las fuentes actuales.

**Qué se traduce y qué no** (regla firme del autor):

- **Se traduce**: navegación, títulos y subtítulos de sección, textos de presentación, la bienvenida de La casa, etiquetas de ficha, notas de prensa y derechos, y los metadatos SEO de cada página.
- **NO se traduce, queda siempre en español**: poemas, fragmentos de novela y de ensayo, y cualquier texto literario. Salvo rarísimas excepciones que decidiría el propio Tony.
- **Títulos de los libros**: se mantienen en su forma original; si hace falta, se glosa el significado entre paréntesis la primera vez.
- **"Ala del Mar" y "bene scriptus"** nunca se traducen.

**El inglés no es el español traducido.** Es el mismo catálogo en otro orden: en español la fantasía va delante, en inglés va delante la trova, por el circuito de editoriales universitarias y de música. Está razonado en `PRODUCT.md`.

**Cómo montarlo**:

- Estructura de URLs por prefijo, como la que ya usa el inglés: `/fr/`, `/it/`, `/pt/`.
- `hreflang` recíproco en el `<head>` de cada página, más **`x-default` apuntando al español, que hoy falta** tanto en las páginas como en `sitemap.xml`.
- Añadir cada URL nueva a `sitemap.xml` con sus alternates.
- Un aviso breve en cada portada traducida explicando que los textos literarios se publican en su español original.
- El selector de idioma del menú crece de dos a cinco entradas: revisar que la barra siga cabiendo en pantallas medianas.
- Hoy existe `/en/` solo con la portada; el resto de secciones inglesas están por hacer.

Vale la pena añadir a la ficha dos campos que el editor extranjero pide y hoy no están: **derechos vendidos** (además de disponibles) y **muestra traducida: sí / no**.

## 4 bis. Contarte, la sala de los cuentos (abierta el 8 de septiembre)

Sección de primer nivel, en el menú, con página propia por cuento. Motor en
`herramientas/gen-cuento.py` desde `herramientas/cuentos.json`: emite el índice
y la habitación de cada cuento, con `ShortStory` e `isPartOf` al libro cuando
viene de uno.

**Estrena con La muñeca y el príncipe**, que estaba como fragmento dentro de
*Cuentos de muñecas* y se mudó entero aquí. El libro se quedó sin bloque de
Fragmentos y ganó un botón que lleva al cuento; el texto no está dos veces,
según la regla de AGENTS.md. Son 19.330 caracteres, el cuento completo, ya
publicado en 2015, así que no toca la condición de inédito de nada.

La sala es de lectura, no de catálogo: medida de línea de unos 68 caracteres,
cuerpo 1,18rem, interlineado 1,95 y sangría de primera línea. Clases
`.section.cuento`, `.cuento-texto` y `.cuento-procedencia` en `styles.css`.

**Pendiente aquí:**

- **Cuatro cuentos más**, pedidos al autor el 8 de septiembre.
- **Proclama Real no se publica.** Decisión del autor y de Ernesto, 8 de
  septiembre de 2026. En Laureles se queda la mención del premio; el texto no
  entra en este repositorio, que es público. Los motivos se hablan con
  Ernesto, no se escriben aquí. Ver los innegociables de `AGENTS.md`.
- **Las tres fechas de ese premio no son un error, no las "arregles".** El
  autor lo aclaró el 8 de septiembre: escribió *Proclama Real* en **2009**, el
  concurso fue **El Dinosaurio 2013** y el fallo se dio a conocer en **2014**.
  Por eso la entrada vive bajo 2014 y nombra un concurso de 2013. Parece una
  errata y no lo es: yo mismo la "corregí" a 2014 y hubo que revertirlo. La
  ficha lo explica ahora en su propio texto para que no vuelva a pasar.
- Cuidado con los cuentos de los **dos libros de cuentos realistas por salir**:
  esos son inéditos y solo entran si él lo autoriza expresamente.

## 5. Material que esperamos de Tony

Cuando haya corriente en Alamar y pueda enviar:

- ~~De-Cimitas vacía~~ **RESUELTO el 8 de septiembre**: siete piezas de foto y décima, más *Sonata de la lluvia* con página propia. Falta saber si hay más décimitas: el autor dijo tener «cientos», y solo llegaron ocho fotos.
- **Inéditos**: hay cinco poemarios y tres cuentos completos guardados (carpeta `tony 1`), pero solo deben publicarse **sinopsis y fragmentos** que él elija.
- **Sinopsis oficiales** de los libros cuyas páginas siguen con texto provisional marcado.
- **Prensa**: el 8 de septiembre envió la primera tanda y está cableada y verificada. Tienen bloque de Prensa 4 de los 14 libros: *Las guerreras de la luz*, *El Escudo de Valnúss*, *Grimorium* y *El otro lado del espejo*, con tres entrevistas de Juventud Rebelde (Alain Gutiérrez 2012, Iyaimí Palomares 2016 y 2019) y la reseña de Habana Radio. Faltan los diez restantes. **Aviso: Habana Radio está caída entera**, error 502 incluso en la raíz, y esa reseña sobrevive solo en la copia del Internet Archive, que es a donde apunta el enlace. Es la prueba de que este archivo también es rescate.
- **Ojos de bruja** (sigue abierto, y ahora hay dónde ponerlo: Contarte): relato por entregas publicado en Cubaliteraria en julio de 2020, las siete partes vivas y comprobadas (`/ojos-de-bruja-i/` a `/ojos-de-bruja-vi/` más `/ojos-de-bruja-vii-y-final/`). No es libro ni poesía, así que no cabe en las secciones actuales: falta decidir si lleva página propia. Tony conserva el texto completo y está por decidir si se aloja aquí, que lo convertiría en el único sitio donde se lee seguido.
- **Dos reseñas descartadas**, decisión del 8 de septiembre: un video de booktuber sobre *Las guerreras de la luz* que el autor considera flojo, y una reseña de *Grimorium* en `diaentp.blogspot.com` que ya no existe (404). El bloque de Prensa es expediente de piezas firmadas en medios identificables; un video de aficionado no añade autoridad y omitirlo no oculta nada.
- **Presentaciones**: más fotos, audios o palabras de lanzamientos, sobre todo de los libros que aún no tienen galería.
- ~~Plano abierto sin grabaciones~~ **RESUELTO el 8 de septiembre**: el programa de televisión *Entre libros* (2019), los dos de Habana Radio de Fernando Rodríguez Sosa (2018), la lectura en la UNEAC de Santa Clara (2022) y *Mar de papel* del concierto de Rita del Prado (1999). Sigue pendiente el corte de *Aviso*, de ese mismo concierto: el autor pidió dejar solo desde donde él dice «esto se llama aviso», y hay dos cortes candidatos esperando que lo escuche y elija.
- **Foto de escritor** oficial, si finalmente hace la sesión que quería.
- **Extensión y categoría de edad** de cada título, que es lo que pregunta una editorial extranjera y no se puede inventar.

## 6. Técnico, menor

- **Repo público sin `LICENSE`**, con la obra literaria del autor dentro. Por defecto es "todos los derechos reservados", así que no hay agujero, pero conviene un archivo explícito: código libre, textos © Antonio López Sánchez.
- **Secciones vacías en el sitemap**: `/tinta-ciones/de-cimitas/` e `/ineditos/` están indexadas casi sin contenido. Valorar `noindex` hasta que tengan material.
- **`.nota-demo`**: la clase ya no marca contenido de demo, ahora lleva notas reales. Conviene renombrarla a `.nota` antes de que la plantilla se clone a otro artista, para que nadie la borre pensando que es andamiaje.
- **Menú móvil, la deficiencia más repetida del sitio.** Las 28 páginas con hamburguesa carecen de `aria-expanded`, `aria-controls`, sincronización accesible del estado abierto y cerrado, y cierre con Escape. Hoy se abre con un `onclick` en línea que solo hace toggle de una clase. No impide usar el sitio, pero es lo que más se repite.
- **Tarjetas sociales mal proporcionadas.** Las 14 páginas de libro declaran `twitter:card: summary_large_image` con la cubierta como imagen, y las cubiertas son verticales (640x961, ratio 0.67, cuando ese formato pide ~1.91). Las redes van a recortarlas por el centro y se pierden el título y el nombre del autor. O se pasan esas páginas a `summary`, o se genera una tarjeta horizontal por libro.
- **No hay pruebas ni workflows de GitHub Actions.** El README declara cifras de Lighthouse excelentes y no hay razón para dudarlas, pero no son reproducibles desde el repositorio. Un workflow que corra Lighthouse CI y valide el JSON-LD en cada push cerraría ese hueco y serviría de red para el trabajo entre dos máquinas.
- **`/novelas/` y `/poeta/` son redirecciones blandas**: `meta refresh` con `noindex` y canonical, que responden 200. Están correctas para lo que son y GitHub Pages no permite un 301 real, pero conviene saber que no son redirecciones de servidor.
- **Formspree** (opcional): formulario de consultas de derechos, para tener historial además de la notificación por correo.
- **Verificación del dominio en la cuenta de GitHub** (opcional): un registro TXT que impide que otro usuario reclame el dominio si el repo se despublica.
- **Backlinks de autoridad**, que es lo que más moverá el posicionamiento y no es trabajo técnico: que EcuRed enlace el sitio, que Tony lo publique en su Facebook, y que aparezca en las páginas de sus editoriales.

## 7. Fuera de este repo

- **Bug en `ernestocisneros-site`**: `es/representacion-literaria.html` declara dos `hreflang="en"` en conflicto, uno a `literary-representation.html` y otro a `books.html`. Con alternates contradictorios los buscadores tienden a descartar el grupo entero. Revisar si el patrón se repite en las siete lenguas.
- **Orden de géneros en la página inglesa de representación**: hoy dice "Heroic fantasy sagas, a horror novel, children's fantasy, poetry, and essays on the Cuban Nueva Trova". Para el comprador en inglés conviene invertirlo y poner la trova delante.
- **Documento de representación firmado** entre Tony y Ernesto, con territorio, plazo, comisión y rendición de cuentas. La editorial va a pedir prueba de autoridad para licenciar y un acuerdo de palabra no pasa ese filtro. Conviene tenerlo antes de la primera negociación.

## 8. Recordatorios de mantenimiento

- **Dos máquinas, un repositorio.** El trabajo se reparte entre la máquina de casa y la de UnlimitedWraps, con instancias distintas. Lo común son los repos: **si algo tiene que sobrevivir al cambio de máquina, va en este archivo o en el repo, nunca solo en la memoria del asistente, que es local a cada máquina.** Hacer `git pull` antes de empezar.
- **Casi nada se edita ya a mano.** Los seis generadores y sus manifiestos:

  | Generador | Qué escribe | Manifiesto |
  |---|---|---|
  | `gen-libro.py` | las 14 fichas de libro | `libros/*.json` |
  | `gen-cuento.py` | Contarte y cada cuento | `cuentos.json` |
  | `gen-poemas.py` | Poemas sueltos | `poemas.json` |
  | `gen-decimitas.py` | De-Cimitas | `decimitas.json` |
  | `gen-sonata.py` | Sonata de la lluvia | el propio .txt |
  | `gen-audios.py` | las grabaciones, en las dos salas que las reclaman | `grabaciones.json` |

  Auxiliares: `navegacion.py` (única definición del menú y el pie),
  `unificar-nav.py` (reescribe la navegación de las páginas a mano, con
  `--comprobar` para fallar si algo se desalinea), `a-texto.py` (RTF y DOCX a
  texto, con `--verso`) y `leer-poema.py` (separa título, epígrafe, cuerpo y
  colofón).

- **Ritual al terminar cualquier tanda**, en este orden:

  ```bash
  for f in herramientas/libros/*.json; do python herramientas/gen-libro.py "$f"; done
  python herramientas/gen-cuento.py && python herramientas/gen-poemas.py
  python herramientas/gen-decimitas.py && python herramientas/gen-sonata.py
  python herramientas/gen-audios.py && python herramientas/unificar-nav.py --comprobar
  ```

  Si `--comprobar` no dice `desalineadas: 0`, algo quedó a medias.
- **`a-texto.py` usa striprtf, no un parser propio.** Hubo uno y se comía texto:
  perdió las dos primeras palabras de un cuento y partió tres títulos
  acentuados. Para textos del autor no se improvisa un conversor, y el
  resultado se compara contra el original antes de publicar.
- Al publicar páginas nuevas: actualizar `sitemap.xml`, subir el `?v=N` de `styles.css`, `fonts.css` y `app.js`, y relanzar el ping de IndexNow.
- El meta `msvalidate.01` de la portada no se quita: Bing revalida la propiedad periódicamente.
- Reglas de contenido vigentes en `README.md` y doctrina de producto en `PRODUCT.md`; la voluntad del autor manda sobre cualquier criterio de diseño.
