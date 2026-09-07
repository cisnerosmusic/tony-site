# Pendientes · Ala del Mar

Nota de trabajo para retomar el proyecto. Estado al 6 de septiembre de 2026.

## Dónde quedamos

El sitio está **completo y sirviendo en todo el mundo** desde [antoniolopezsanchez.art](https://antoniolopezsanchez.art), con dominio propio, HTTPS, correo operativo, indexación enviada a Google y Bing, y auditoría de SEO/AEO aplicada. Lo que sigue no es reparación: es crecimiento.

## 1. Traducciones (el trabajo grande)

No es un detalle ni un adorno: es la vía para que la obra de Tony llegue a los lectores y editores que no leen español. Se hace con calma y bien.

**Idiomas acordados**: español (base) más **inglés, francés e italiano**, y **portugués** como cuarta lengua (muy rentable por cercanía y por el mercado de Brasil y Portugal).

**Ruso descartado** (decisión de Ernesto, sep 2026): Cinzel y Space Mono no tienen cirílico, solo Cormorant Garamond. Traducir al ruso obligaría a cambiar la tipografía de titulares y del aparato, y eso rompería el sistema visual conseguido. Verificado: francés, italiano, portugués y español caben enteros en las fuentes actuales, así que esas cuatro lenguas no cuestan ni un cambio de diseño.

**Qué se traduce y qué no** (regla firme del autor):

- **Se traduce**: navegación, títulos y subtítulos de sección, textos de presentación, la bienvenida de La casa, etiquetas de ficha, notas de prensa y derechos, y los metadatos SEO de cada página.
- **NO se traduce, queda siempre en español**: poemas, fragmentos de novela y de ensayo, y cualquier texto literario. Salvo rarísimas excepciones que decidiría el propio Tony.
- **Títulos de los libros**: se mantienen en su forma original; si hace falta, se glosa el significado entre paréntesis la primera vez.
- **"Ala del Mar" y "bene scriptus"** nunca se traducen: son el nombre de la casa y el sello del autor.

**Trabajo estimado**: unas 10 páginas de contenido general por idioma. Hoy existe `/en/` solo con la portada; el resto de secciones inglesas están por hacer.

**Cómo montarlo**:

- Estructura de URLs por prefijo, como la que ya usa el inglés: `/fr/`, `/it/`, `/pt/`.
- `hreflang` recíproco en el `<head>` de cada página con su equivalente en los demás idiomas, más `x-default` apuntando al español.
- Añadir cada URL nueva a `sitemap.xml` con sus alternates.
- Un aviso breve en cada portada traducida explicando que los textos literarios se publican en su español original.
- El selector de idioma del menú crece de dos a cinco entradas: conviene revisar que la barra siga cabiendo en pantallas medianas.

## 2. Material que esperamos de Tony

Cuando haya corriente en Alamar y pueda enviar:

- **De-Cimitas**: la sección de décimas con imagen y texto está creada pero vacía. Necesita las décimas y sus imágenes.
- **Inéditos**: hay cinco poemarios y tres cuentos completos guardados (carpeta `tony 1`), pero solo deben publicarse **sinopsis y fragmentos** que él elija; publicarlos íntegros les quitaría la condición de inéditos ante concursos y editoriales.
- **Sinopsis oficiales** de los libros cuyas páginas siguen con texto provisional marcado.
- **Prensa**: enlaces o recortes sobre sus libros para las secciones Prensa, hoy casi vacías.
- **Presentaciones**: más fotos, audios o palabras de lanzamientos, sobre todo de los libros que aún no tienen galería.
- **Plano abierto**: grabaciones de radio y televisión que mencionó tener en localización.
- **Foto de escritor** oficial, si finalmente hace la sesión que quería.

## 3. Técnico, menor

- **Formspree** (opcional): formulario de consultas de derechos en las páginas de representación de ernestocisneros.art, para tener historial además de la notificación por correo. Requiere crear la cuenta y pasar el ID del formulario.
- **Verificación del dominio en la cuenta de GitHub** (opcional): un registro TXT que impide que otro usuario reclame el dominio si el repo se despublica.
- **Solicitar indexación manual** en Search Console de portada, `/libros/` y `/libros/las-guerreras-de-la-luz/` si aún no se hizo.
- **Backlinks de autoridad**, que es lo que más moverá el posicionamiento y no es trabajo técnico: que EcuRed enlace el sitio en la ficha del autor, que él lo publique en su Facebook, y que aparezca en las páginas de sus editoriales.

## 4. Recordatorios de mantenimiento

- Las páginas de libro se generan con `herramientas/gen-libro.py`; no se editan a mano.
- Al publicar páginas nuevas: actualizar `sitemap.xml`, subir el `?v=N` de `styles.css`, `fonts.css` y `app.js`, y relanzar el ping de IndexNow.
- El meta `msvalidate.01` de la portada no se quita: Bing revalida la propiedad periódicamente.
- Reglas de contenido vigentes en `README.md`; la voluntad del autor manda sobre cualquier criterio de diseño.
