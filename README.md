# Ala del Mar · Antonio López Sánchez

Sitio oficial del escritor cubano **Antonio López Sánchez** (La Habana, 1973): novelista, poeta y periodista cultural. En vivo en **[antoniolopezsanchez.art](https://antoniolopezsanchez.art)**.

La casa se llama *Ala del Mar* por la fórmula con que el autor cierra sus libros desde Alamar, el barrio habanero frente al mar donde vive y escribe: *"Hallado en Ala del Mar, [fecha]. bene scriptus"*.

## Cómo está hecho

Sitio estático: HTML, CSS y JS propios, sin frameworks, sin dependencias en tiempo de ejecución y **sin una sola petición a terceros** (tipografías, imágenes y audio autohospedados). Alojado en GitHub Pages con dominio propio y HTTPS forzado.

El sitio sigue en construcción. Las mediciones de rendimiento se harán y se publicarán cuando esté terminada la versión inglesa.

## Mundo visual

Base heredada del template propio de Index01 ([impulses-art-site](https://github.com/cisnerosmusic/impulses-art-site)), adaptado a esta casa: fondos azul noche en varias tonalidades (`#0a0c1f` a `#252860`), acento en oro (`#d4a030`), Cinzel para los nombres y títulos, Cormorant Garamond para la lectura y Space Mono para el aparato. Navegación fija con desenfoque, aparición lateral de bloques, retrato del autor a sangre en la portada y una banda de mar entre secciones. El sistema completo, con sus tokens y sus reglas, está en [DESIGN.md](DESIGN.md).

## Estructura

| Ruta | Contenido |
|------|-----------|
| `/` | Portada: la casa, el autor y su bienvenida |
| `/libros/` | Los 14 libros publicados, cada uno con su propia página |
| `/ineditos/` | Obras que esperan editorial |
| `/tinta-ciones/` | Poesía: `poemas-sueltos/` (20 poemas), `de-cimitas/` (7 piezas de foto y décima), `sonata-de-la-lluvia/`, `en-mi-voz/` |
| `/contarte/` | Los cuentos, uno por página, con orden rotatorio diario |
| `/trova/` | Su obra documental sobre la Nueva Trova |
| `/plano-abierto/` | Radio, televisión y grabaciones |
| `/laureles/` | Los premios, y las dos obras premiadas en el Farraluque 2026, para lectores adultos: `tres-delirios-y-un-desnudo/` y `revelaciones/` |
| `/periodista/` | Ficha y trayectoria en la prensa cultural cubana |
| `/entre-lectores/` | Álbum de ferias y firmas; se llega solo desde Mis libros |
| `/directorio/` | Contacto del autor y consultas de derechos |
| `/derechos/` | Aviso de derechos |
| `/en/` | La zona inglesa: portada, `trova/`, `poetry/`, `fiction/`, `author/`, `rights/` y `books/`, con los catorce libros. En otro orden que el español, a propósito: ver [PRODUCT.md](PRODUCT.md) |

Archivos de raíz: `index.html`, `styles.css`, `app.js`, `fonts.css`, `robots.txt`, `sitemap.xml`, `llms.txt`, `404.html` (uno solo para todo el sitio, en español o en inglés según la ruta), `CNAME`, el favicon en archivos reales (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`) y la clave de IndexNow. Recursos en `fonts/`, `img/`, `audio/` y `video/`.

**63 páginas; 60 URLs en el sitemap.** No entran el 404 ni las dos redirecciones blandas, `/novelas/` y `/poeta/`.

## Idiomas

- **Los textos literarios se publican siempre en su español original**, en todos los idiomas del sitio. Se traduce el aparato: navegación, contratapas, notas del autor, fichas, pies de foto y metadatos.
- **La zona inglesa no es la española traducida.** En español abre la fantasía heroica; en inglés, la investigación sobre la Nueva Trova, luego la poesía y luego la narrativa.
- **Las páginas de libro son el mismo generador para todos los idiomas.** Los textos de interfaz de cada idioma están en `herramientas/idiomas.json`, y lo traducido de cada libro, en una capa: `herramientas/libros/<idioma>/<slug>.json`. Esas capas no tienen campo para los fragmentos, así que un fragmento traducido no puede colarse.
- **Añadir un idioma**: su bloque en `idiomas.json`, catorce capas y su menú en `herramientas/navegacion.py`. No hace falta tocar el generador.

## Añadir contenido

Casi nada se escribe a mano: cada sala tiene su generador y su manifiesto en `herramientas/`.

| Generador | Escribe | Lee |
|---|---|---|
| `gen-libro.py` | las 14 fichas de libro en cada idioma, y los catálogos que no son el español | `libros/<slug>.json`, `libros/<idioma>/<slug>.json`, `idiomas.json` |
| `gen-cuento.py` | Contarte y la página de cada cuento | `cuentos.json` |
| `gen-poemas.py` | Poemas sueltos | `poemas.json` |
| `gen-decimitas.py` | De-Cimitas | `decimitas.json` |
| `gen-sonata.py` | Sonata de la lluvia | su `.txt` |
| `gen-farraluque.py` | las dos obras del Farraluque, en Laureles | sus `.txt` en `textos/laureles/` |
| `gen-audios.py` | las grabaciones, repartidas a las salas que las reclaman | `grabaciones.json` |
| `gen-ingles.py` | las páginas de sección inglesas | `ingles.json` |
| `gen-legal.py` | `/derechos/` y `/en/rights/` | `legal.json` |
| `gen-404.py` | el 404, en los dos idiomas | `navegacion.py` |
| `gen-sitemap.py` | `sitemap.xml`, con la fecha real de cada página según git y sus alternates por idioma | las propias páginas |

Auxiliares: `navegacion.py`, que es la **única** definición del menú y del pie en cada idioma; `unificar-nav.py`, que la aplica a las páginas escritas a mano; `comprobar.py`, que verifica el sitio entero; `version.py`, que sube el `?v=N` de un recurso en todas las páginas a la vez; `a-texto.py`, que convierte los RTF y DOCX del autor a texto plano (con `--verso` para conservar las estrofas); y `leer-poema.py`, que separa título, epígrafe, cuerpo y colofón.

Al terminar cualquier cambio:

```bash
python herramientas/gen-libro.py herramientas/libros/<slug>.json   # o el generador que toque
python herramientas/gen-sitemap.py                                 # las fechas y los alternates
python herramientas/comprobar.py                                   # tiene que decir: 0 fallos
```

Si se cambia `styles.css`, `fonts.css` o `app.js`, su versión se sube con `python herramientas/version.py styles.css <número>`. Después de publicar, se relanza el ping de IndexNow.

**El comprobador corre solo en cada push**, con GitHub Actions (`.github/workflows/comprobar.yml`). Cada regla suya nació de un fallo real que encontró una auditoría.

## Reglas de contenido

Decisiones del autor y del estudio que deben respetarse en cualquier cambio futuro:

- **Los textos literarios se publican siempre en su idioma original, el español**, aunque el sitio crezca a otros idiomas.
- **Primera persona**: en la casa habla siempre el autor, salvo donde se declare otra voz.
- **Sin raya larga** en ningún texto público.
- **La atribución es sagrada.** Varios poemas glosan o citan a otros autores (José Martí, Lezama Lima, Silvio Rodríguez, Polito Ibáñez, Fito Páez, Noel Nicola, Santiago Feliú). Esos versos salen siempre en bloque aparte y con la firma de quien los escribió, nunca corridos con los del autor.
- **En verso no se normaliza nada.** Los espacios múltiples dentro del verso son puntuación del autor y las sangrías marcan dónde abre cada décima. Se conservan tal cual, con `white-space: pre-wrap`.
- **Un texto vive una sola vez.** Si una pieza pertenece a dos salas, se repite el enlace o el reproductor, nunca el texto ni el marcado de datos.
- **Hay material que existe y no se publica**, por decisión del autor y de Ernesto. La lista está en los innegociables de `AGENTS.md` y no se revisa sin preguntarles.
- **Mayúscula inicial** en nombres propios, premios y editoriales.
- Las **obras inéditas** se presentan solo con sinopsis y fragmentos, nunca íntegras.
- Las sinopsis marcadas como provisionales se sustituirán por el texto oficial del autor.

## SEO y AEO

60 URLs indexables, con títulos y descripciones únicos y en rango, canónicas propias y Twitter Cards. JSON-LD válido en todas: `Person` con premios y `sameAs`, `WebSite`, `Book` por cada libro y en cada idioma, con `sameAs` a EcuRed y `subjectOf` a la prensa, `ShortStory` por cuento, `ItemList`, `AudioObject`, `CollectionPage`, `ProfilePage` con la persona dentro, `ContactPage` y `BreadcrumbList`.

`hreflang` recíproco en las 40 páginas que tienen pareja de idioma, con `x-default` al español, y los mismos alternates en `sitemap.xml`. `llms.txt` con los datos citables del autor para motores de respuesta, `robots.txt` con permiso explícito a los bots de IA e IndexNow configurado.

## Cómo se trabaja aquí

El proyecto se construye desde dos máquinas con instancias distintas, más una tercera instancia que audita por turnos, y ninguna ve la conversación de las otras. El repositorio es el único medio común. El sistema de trabajo, el protocolo de entrega y los innegociables están en [AGENTS.md](AGENTS.md): **léelo antes de tocar nada**.

Orden de autoridad cuando dos documentos se contradigan: la voluntad del autor, luego [PRODUCT.md](PRODUCT.md), [DESIGN.md](DESIGN.md), [PENDIENTES.md](PENDIENTES.md) y este README. Si un documento contradice al código, gana el código y el documento se corrige en el mismo commit.

## Pendientes

El trabajo por delante, las decisiones tomadas y lo que espera la palabra del autor están en [PENDIENTES.md](PENDIENTES.md).

## Créditos

Obra literaria y textos: © Antonio López Sánchez. Cubiertas: Rainel Cabarroi, Juan Carlos García, Ramón Eduardo Haití, Alain R. Cuba, Iván Batista, Tomás Egea Ascona y Michele Millares Hollands, según cada ficha. Fotografía del mar: Wikimedia Commons (CC0). Qué es de quién, con detalle: [LICENSE](LICENSE) y [/derechos/](https://antoniolopezsanchez.art/derechos/).

Desarrollo: [Index01](https://index01.net), Miami. Representación editorial fuera de Cuba: [Ernesto Cisneros](https://ernestocisneros.art/es/representacion-literaria.html).
