# Ala del Mar · Antonio López Sánchez

Sitio oficial del escritor cubano **Antonio López Sánchez** (La Habana, 1973): novelista de fantasía heroica y horror, poeta y periodista cultural. En vivo en **[antoniolopezsanchez.art](https://antoniolopezsanchez.art)**.

La casa se llama *Ala del Mar* por la fórmula con que el autor cierra sus libros desde Alamar, el barrio habanero frente al mar donde vive y escribe: *"Hallado en Ala del Mar, [fecha]. bene scriptus"*.

## Cómo está hecho

Sitio estático: HTML, CSS y JS propios, sin frameworks, sin dependencias en tiempo de ejecución y **sin una sola petición a terceros** (tipografías, imágenes y audio autohospedados). Alojado en GitHub Pages con dominio propio y HTTPS forzado.

Lighthouse: **100/100/100/100** en escritorio y **99/100/100/100** en móvil, con CLS 0 y bloqueo 0.

## Mundo visual

Base heredada del template propio de Index01 ([impulses-art-site](https://github.com/cisnerosmusic/impulses-art-site)), adaptado a esta casa: fondos azul noche en varias tonalidades (`#0a0c1f` a `#252860`), acento en oro (`#d4a030`), Cinzel para los nombres y títulos, Cormorant Garamond para la lectura y Space Mono para el aparato. Navegación fija con desenfoque, aparición lateral de bloques, retrato del autor a sangre en la portada y una banda de mar entre secciones.

## Estructura

| Ruta | Contenido |
|------|-----------|
| `/` | Portada: la casa, el autor y su bienvenida |
| `/en/` | Portada en inglés |
| `/libros/` | Los 14 libros publicados, cada uno con su propia página |
| `/ineditos/` | Obras que esperan editorial |
| `/tinta-ciones/` | Poesía: `poemas-sueltos/`, `de-cimitas/`, `en-mi-voz/` |
| `/trova/` | Su obra documental sobre la Nueva Trova |
| `/plano-abierto/` | Radio, televisión y prensa fuera de los libros |
| `/laureles/` | Los premios |
| `/periodista/` | Ficha y trayectoria en la prensa cultural cubana |
| `/directorio/` | Contacto del autor y consultas de derechos |

Archivos de raíz: `index.html`, `styles.css`, `app.js`, `fonts.css`, `robots.txt`, `sitemap.xml`, `llms.txt`, `404.html`, `CNAME` y la clave de IndexNow. Recursos en `fonts/` (7 woff2), `img/` (33 WebP) y `audio/` (2 grabaciones del autor).

## Añadir un libro

Las páginas de libro **no se escriben a mano**: se generan desde un manifiesto.

```bash
python herramientas/gen-libro.py herramientas/libros/<slug>.json
```

El manifiesto declara el título, la ficha, las rutas a los textos del autor (contratapa, fragmentos, *con voz y voto*), la galería y los campos `seo_titulo` y `seo_desc`. El generador arma la página completa con sus datos estructurados (`Book` y `BreadcrumbList`), omite los bloques sin material y hereda todas las mejoras de SEO. Después hay que añadir la URL nueva a `sitemap.xml` y al índice `/libros/`.

## Reglas de contenido

Decisiones del autor y del estudio que deben respetarse en cualquier cambio futuro:

- **Los textos literarios se publican siempre en su idioma original, el español**, aunque el sitio crezca a otros idiomas.
- **Primera persona**: en la casa habla siempre el autor, salvo donde se declare otra voz.
- **Sin raya larga** en ningún texto público.
- **Mayúscula inicial** en nombres propios, premios y editoriales.
- Las **obras inéditas** se presentan solo con sinopsis y fragmentos, nunca íntegras.
- Las sinopsis marcadas como provisionales se sustituirán por el texto oficial del autor.

## SEO y AEO

27 páginas indexables con títulos y descripciones únicos y en rango, Twitter Cards, 53 bloques JSON-LD válidos (`Person` con premios y `sameAs`, `WebSite`, 14 `Book`, `CollectionPage`/`ProfilePage`/`ContactPage` y `BreadcrumbList`), `llms.txt` con los datos citables del autor para motores de respuesta, `robots.txt` con permiso explícito a los bots de IA e IndexNow configurado.

Al publicar páginas nuevas: actualizar `sitemap.xml`, subir el número de versión de los assets (`?v=N` en `styles.css`, `fonts.css` y `app.js`) y relanzar el ping de IndexNow.

## Créditos

Obra literaria y textos: © Antonio López Sánchez. Cubiertas: Rainel Cabarroi, Juan Carlos García, Ramón Eduardo Haití, Alain R. Cuba, Iván Batista, Tomás Egea Ascona y Michele Millares Hollands, según cada ficha. Fotografía del mar: Wikimedia Commons (CC0).

Desarrollo: [Index01](https://index01.net), Miami. Representación editorial fuera de Cuba: [Ernesto Cisneros](https://ernestocisneros.art/es/representacion-literaria.html).
