# Pendientes · Ala del Mar

Nota de trabajo para retomar el proyecto. Estado al 8 de septiembre de 2026.

## Dónde quedamos

El sitio está **completo y sirviendo en todo el mundo** desde [antoniolopezsanchez.art](https://antoniolopezsanchez.art), con dominio propio, HTTPS, correo operativo, indexación enviada a Google y Bing, y auditoría de SEO/AEO aplicada.

El 8 de septiembre se revisó el repositorio entero y **se corrigió el rumbo del producto en `PRODUCT.md`**: el público de esta web no es Cuba. Allí Tony ya tiene editoriales y circuito; la web se construyó para el afuera, y su lector de mayor valor es el editor, agente o traductor extranjero. De ahí salen los pendientes nuevos de la sección 1, que son los que más pagan. Lee `PRODUCT.md` antes de tocar nada: la jerarquía de la obra ahora depende del idioma.

## 1. El embudo de derechos está roto (lo más urgente)

Los derechos fuera de Cuba están disponibles y los gestiona Ernesto Cisneros. La página de representación existe y está bien hecha, en español y en inglés, en el sitio de Ernesto. El problema es que **desde este sitio no se llega a ella**.

- **Las 14 fichas de libro no enlazan a ninguna parte.** Cada una dice `derechos: Disponibles para ediciones y traducciones fuera de Cuba` y no ofrece a dónde escribir. Son las páginas donde cae la gente desde una búsqueda, así que es la fuga grande. Se arregla con **una línea en `herramientas/gen-libro.py`** y regenerando los 14. Debe enlazar a la página de representación y a `derechos@antoniolopezsanchez.art`.
- **`/en/` no menciona los derechos.** Sus únicos enlaces externos son Index01 y Facebook. Falta un bloque que apunte a `https://ernestocisneros.art/literary-representation.html`, que es la versión inglesa y hoy no la alcanza nadie desde aquí.
- **`/directorio/` enlaza solo a la versión española** de la representación. El enlace tiene que ser consciente del idioma.
- **`derechos@antoniolopezsanchez.art` no aparece en ningún HTML de este sitio**, aunque es una dirección de este dominio y es la que se anuncia en el sitio de Ernesto.

Regla que quedó fijada en `PRODUCT.md`: *ninguna declaración de derechos sin salida, en el idioma de quien lee*.

**El dossier de derechos no se duplica aquí.** El sitio de Tony es la casa y el catálogo; el sitio de Ernesto es el negocio. Esa separación es deliberada.

## 2. Accesibilidad: contraste por debajo de AA

Dos tokens de color no llegan al mínimo de 4,5:1 y afectan al texto más pequeño del sitio (copyright del pie, crédito de Index01, pies de galería, etiquetas `dt` de las fichas, notas):

| Token | Ratio actual | Arreglo |
|---|---|---|
| `--text-dim` | 2,89:1 | subir alfa de 0.5 a 0.72 (queda en 4,68) |
| `--gold-dim` usado como texto | 2,80:1 | subir alfa de 0.5 a 0.72 (queda en 4,51) |

Lighthouse da 100 en accesibilidad, pero eso no garantiza AA en todo. Son dos valores en `:root` de `styles.css`. Ojo: `--gold-dim` también se usa para bordes, donde 0.5 está bien; si el cambio ensucia algún borde, separar en un token propio para texto.

## 3. El generador no es reproducible

`herramientas/gen-libro.py` es la única forma de tocar las páginas de libro, pero **desde un clon limpio no corre**. Las 45 rutas de texto declaradas en los manifiestos de `herramientas/libros/*.json` apuntan a `C:/Users/Ernesto/OneDrive/Imágenes/tony/x/...`, un perfil de Windows que no existe ni en la máquina de casa ni en la de UW. Hoy el pipeline vive en un solo disco.

Arreglo: copiar los `.txt` **ya publicados** a `herramientas/textos/<slug>/` y volver relativas las rutas de los manifiestos.

**Cuidado**: solo el material que ya está en el sitio. Los inéditos no entran en este repositorio, que es público, porque publicarlos les quitaría la condición de inéditos ante concursos y editoriales.

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

## 5. Material que esperamos de Tony

Cuando haya corriente en Alamar y pueda enviar:

- **De-Cimitas**: la sección de décimas con imagen y texto está creada pero vacía. Necesita las décimas y sus imágenes.
- **Inéditos**: hay cinco poemarios y tres cuentos completos guardados (carpeta `tony 1`), pero solo deben publicarse **sinopsis y fragmentos** que él elija.
- **Sinopsis oficiales** de los libros cuyas páginas siguen con texto provisional marcado.
- **Prensa**: enlaces o recortes sobre sus libros para las secciones Prensa, hoy casi vacías.
- **Presentaciones**: más fotos, audios o palabras de lanzamientos, sobre todo de los libros que aún no tienen galería.
- **Plano abierto**: grabaciones de radio y televisión que mencionó tener en localización.
- **Foto de escritor** oficial, si finalmente hace la sesión que quería.
- **Extensión y categoría de edad** de cada título, que es lo que pregunta una editorial extranjera y no se puede inventar.

## 6. Técnico, menor

- **Repo público sin `LICENSE`**, con la obra literaria del autor dentro. Por defecto es "todos los derechos reservados", así que no hay agujero, pero conviene un archivo explícito: código libre, textos © Antonio López Sánchez.
- **Secciones vacías en el sitemap**: `/tinta-ciones/de-cimitas/` e `/ineditos/` están indexadas casi sin contenido. Valorar `noindex` hasta que tengan material.
- **`.nota-demo`**: la clase ya no marca contenido de demo, ahora lleva notas reales. Conviene renombrarla a `.nota` antes de que la plantilla se clone a otro artista, para que nadie la borre pensando que es andamiaje.
- **Hamburger sin `aria-expanded`** (usa `onclick` en línea).
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
