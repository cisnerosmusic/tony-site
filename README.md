# Ala del Mar · Antonio López Sánchez

Sitio oficial del escritor cubano **Antonio López Sánchez** (La Habana, 1973): novelista, poeta y periodista cultural. En vivo en **[antoniolopezsanchez.art](https://antoniolopezsanchez.art)**.

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
| `/tinta-ciones/` | Poesía: `poemas-sueltos/` (20 poemas), `de-cimitas/` (7 piezas de foto y décima), `sonata-de-la-lluvia/`, `en-mi-voz/` |
| `/contarte/` | Los cuentos, uno por página, con orden rotatorio diario |
| `/trova/` | Su obra documental sobre la Nueva Trova |
| `/plano-abierto/` | Radio, televisión y grabaciones |
| `/laureles/` | Los premios |
| `/periodista/` | Ficha y trayectoria en la prensa cultural cubana |
| `/entre-lectores/` | Álbum de ferias y firmas; se llega solo desde Mis libros |
| `/directorio/` | Contacto del autor y consultas de derechos |

Archivos de raíz: `index.html`, `styles.css`, `app.js`, `fonts.css`, `robots.txt`, `sitemap.xml`, `llms.txt`, `404.html`, `CNAME`, el favicon en archivos reales (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`) y la clave de IndexNow. Recursos en `fonts/`, `img/`, `audio/` y `video/`.

**40 páginas, 37 URLs en el sitemap.**

## Añadir contenido

Casi nada se escribe a mano: cada sala tiene su generador y su manifiesto en `herramientas/`.

| Generador | Escribe | Manifiesto |
|---|---|---|
| `gen-libro.py` | las 14 fichas de libro | `libros/<slug>.json` |
| `gen-cuento.py` | Contarte y la página de cada cuento | `cuentos.json` |
| `gen-poemas.py` | Poemas sueltos | `poemas.json` |
| `gen-decimitas.py` | De-Cimitas | `decimitas.json` |
| `gen-sonata.py` | Sonata de la lluvia | el propio `.txt` |
| `gen-audios.py` | las grabaciones, repartidas a las salas que las reclaman | `grabaciones.json` |

Y cuatro auxiliares: `navegacion.py`, que es la **única** definición del menú y del pie; `unificar-nav.py`, que la aplica a las páginas escritas a mano y tiene un `--comprobar` que falla si algo se desalinea; `a-texto.py`, que convierte los RTF y DOCX del autor a texto plano (con `--verso` para conservar las estrofas); y `leer-poema.py`, que separa título, epígrafe, cuerpo y colofón.

```bash
python herramientas/gen-libro.py herramientas/libros/<slug>.json
python herramientas/unificar-nav.py --comprobar   # debe decir: desalineadas: 0
```

Después de publicar algo nuevo: añadir la URL a `sitemap.xml`, subir el `?v=N` de `styles.css` en **todas** las páginas y en los generadores, y relanzar el ping de IndexNow.

## Reglas de contenido

Decisiones del autor y del estudio que deben respetarse en cualquier cambio futuro:

- **Los textos literarios se publican siempre en su idioma original, el español**, aunque el sitio crezca a otros idiomas.
- **Primera persona**: en la casa habla siempre el autor, salvo donde se declare otra voz.
- **Sin raya larga** en ningún texto público.
- **La atribución es sagrada.** Varios poemas glosan o citan a otros autores (José Martí, Lezama Lima, Polito Ibáñez, Fito Páez, Noel Nicola, Santiago Feliú). Esos versos salen siempre en bloque aparte y con la firma de quien los escribió, nunca corridos con los del autor.
- **En verso no se normaliza nada.** Los espacios múltiples dentro del verso son puntuación del autor y las sangrías marcan dónde abre cada décima. Se conservan tal cual, con `white-space: pre-wrap`.
- **Un texto vive una sola vez.** Si una pieza pertenece a dos salas, se repite el enlace o el reproductor, nunca el texto ni el marcado de datos.
- **Hay material que existe y no se publica**, por decisión del autor y de Ernesto. La lista está en los innegociables de `AGENTS.md` y no se revisa sin preguntarles.
- **Mayúscula inicial** en nombres propios, premios y editoriales.
- Las **obras inéditas** se presentan solo con sinopsis y fragmentos, nunca íntegras.
- Las sinopsis marcadas como provisionales se sustituirán por el texto oficial del autor.

## SEO y AEO

37 páginas indexables con títulos y descripciones únicos y en rango, Twitter Cards, JSON-LD válido en todas ellas (`Person` con premios y `sameAs`, `WebSite`, 14 `Book` con `sameAs` a EcuRed y `subjectOf` a la prensa, `ShortStory` por cuento, `ItemList`, `AudioObject`, `CollectionPage`/`ProfilePage`/`ContactPage` y `BreadcrumbList`), `llms.txt` con los datos citables del autor para motores de respuesta, `robots.txt` con permiso explícito a los bots de IA e IndexNow configurado.

Al publicar páginas nuevas: actualizar `sitemap.xml`, subir el número de versión de los assets (`?v=N` en `styles.css`, `fonts.css` y `app.js`) y relanzar el ping de IndexNow.

## Cómo se trabaja aquí

El proyecto se construye desde dos máquinas con instancias distintas, más una tercera instancia que audita por turnos, y ninguna ve la conversación de las otras. El repositorio es el único medio común. El sistema de trabajo, el protocolo de entrega y los innegociables están en [AGENTS.md](AGENTS.md): **léelo antes de tocar nada**.

Orden de autoridad cuando dos documentos se contradigan: la voluntad del autor, luego [PRODUCT.md](PRODUCT.md), [DESIGN.md](DESIGN.md), [PENDIENTES.md](PENDIENTES.md) y este README. Si un documento contradice al código, gana el código y el documento se corrige en el mismo commit.

## Pendientes

El trabajo por delante (traducciones a inglés, francés, italiano y portugués, y el material que falta de Tony) está en [PENDIENTES.md](PENDIENTES.md).

## Créditos

Obra literaria y textos: © Antonio López Sánchez. Cubiertas: Rainel Cabarroi, Juan Carlos García, Ramón Eduardo Haití, Alain R. Cuba, Iván Batista, Tomás Egea Ascona y Michele Millares Hollands, según cada ficha. Fotografía del mar: Wikimedia Commons (CC0).

Desarrollo: [Index01](https://index01.net), Miami. Representación editorial fuera de Cuba: [Ernesto Cisneros](https://ernestocisneros.art/es/representacion-literaria.html).
