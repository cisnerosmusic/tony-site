# Pendientes · Ala del Mar

Nota de trabajo para retomar el proyecto. Estado al 8 de septiembre de 2026.

## Dónde quedamos

El sitio está **completo y sirviendo en todo el mundo** desde [antoniolopezsanchez.art](https://antoniolopezsanchez.art), con dominio propio, HTTPS, correo operativo, indexación enviada a Google y Bing, y auditoría de SEO/AEO aplicada.

El 8 de septiembre, además, **se reescribió `DESIGN.md`**, que documentaba con autoridad total un sistema visual abandonado (cuartillas de papel sobre mesa azul, añil, Bonum, Courier Prime) sin una sola coincidencia con el sitio real. Era la única incidencia capaz de hacer que un agente rompiera el sitio activamente en vez de simplemente dejar algo sin hacer. Ahora describe el mundo navy y oro que está en vivo, y lleva un aviso al inicio para que nadie resucite el anterior.

El 8 de septiembre se revisó el repositorio entero y **se corrigió el rumbo del producto en `PRODUCT.md`**: el público de esta web no es Cuba. Allí Tony ya tiene editoriales y circuito; la web se construyó para el afuera, y su lector de mayor valor es el editor, agente o traductor extranjero. De ahí salen los pendientes nuevos de la sección 1, que son los que más pagan. Lee `PRODUCT.md` antes de tocar nada: la jerarquía de la obra ahora depende del idioma.

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

`styles.css` va por `?v=7` en las 28 páginas y en el generador. `fonts.css` se queda en `?v=5` a propósito: las fuentes no cambiaron.

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
- Fecha de ese premio **resuelta el 8 de septiembre**: el autor confirma que
  el evento fue en **2014**, no 2013 como decía el currículo largo. Corregido
  en Laureles. Si aparece 2013 en algún otro sitio, es el error viejo.
- Cuidado con los cuentos de los **dos libros de cuentos realistas por salir**:
  esos son inéditos y solo entran si él lo autoriza expresamente.

## 5. Material que esperamos de Tony

Cuando haya corriente en Alamar y pueda enviar:

- **De-Cimitas**: la sección de décimas con imagen y texto está creada pero vacía. Necesita las décimas y sus imágenes.
- **Inéditos**: hay cinco poemarios y tres cuentos completos guardados (carpeta `tony 1`), pero solo deben publicarse **sinopsis y fragmentos** que él elija.
- **Sinopsis oficiales** de los libros cuyas páginas siguen con texto provisional marcado.
- **Prensa**: el 8 de septiembre envió la primera tanda y está cableada y verificada. Tienen bloque de Prensa 4 de los 14 libros: *Las guerreras de la luz*, *El Escudo de Valnúss*, *Grimorium* y *El otro lado del espejo*, con tres entrevistas de Juventud Rebelde (Alain Gutiérrez 2012, Iyaimí Palomares 2016 y 2019) y la reseña de Habana Radio. Faltan los diez restantes. **Aviso: Habana Radio está caída entera**, error 502 incluso en la raíz, y esa reseña sobrevive solo en la copia del Internet Archive, que es a donde apunta el enlace. Es la prueba de que este archivo también es rescate.
- **Ojos de bruja**: relato por entregas publicado en Cubaliteraria en julio de 2020, las siete partes vivas y comprobadas (`/ojos-de-bruja-i/` a `/ojos-de-bruja-vi/` más `/ojos-de-bruja-vii-y-final/`). No es libro ni poesía, así que no cabe en las secciones actuales: falta decidir si lleva página propia. Tony conserva el texto completo y está por decidir si se aloja aquí, que lo convertiría en el único sitio donde se lee seguido.
- **Dos reseñas descartadas**, decisión del 8 de septiembre: un video de booktuber sobre *Las guerreras de la luz* que el autor considera flojo, y una reseña de *Grimorium* en `diaentp.blogspot.com` que ya no existe (404). El bloque de Prensa es expediente de piezas firmadas en medios identificables; un video de aficionado no añade autoridad y omitirlo no oculta nada.
- **Presentaciones**: más fotos, audios o palabras de lanzamientos, sobre todo de los libros que aún no tienen galería.
- **Plano abierto**: grabaciones de radio y televisión que mencionó tener en localización.
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
- Las páginas de libro se generan con `herramientas/gen-libro.py`; no se editan a mano.
- Al publicar páginas nuevas: actualizar `sitemap.xml`, subir el `?v=N` de `styles.css`, `fonts.css` y `app.js`, y relanzar el ping de IndexNow.
- El meta `msvalidate.01` de la portada no se quita: Bing revalida la propiedad periódicamente.
- Reglas de contenido vigentes en `README.md` y doctrina de producto en `PRODUCT.md`; la voluntad del autor manda sobre cualquier criterio de diseño.
