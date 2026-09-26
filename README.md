# Ala del Mar · Antonio López Sánchez

[![Comprobar el sitio](https://github.com/cisnerosmusic/tony-site/actions/workflows/comprobar.yml/badge.svg)](https://github.com/cisnerosmusic/tony-site/actions/workflows/comprobar.yml)

Sitio oficial del escritor cubano **Antonio López Sánchez** (La Habana, 1973): novelista, poeta y periodista cultural. En vivo en **[antoniolopezsanchez.art](https://antoniolopezsanchez.art)**.

La casa se llama *Ala del Mar* por la fórmula con que el autor cierra sus libros desde Alamar, el barrio habanero frente al mar donde vive y escribe: *"Hallado en Ala del Mar, [fecha]. bene scriptus"*.

## Cómo está hecho

Sitio estático: HTML, CSS y JS propios, sin frameworks, sin dependencias en tiempo de ejecución y **sin una sola petición a terceros** (tipografías, imágenes y audio autohospedados). Alojado en GitHub Pages con dominio propio y HTTPS forzado.

**Medido el 23 de septiembre de 2026 con PageSpeed Insights sobre la portada en vivo**, no estimado:

| | móvil | escritorio |
|---|---|---|
| Rendimiento | **100** | **100** |
| Accesibilidad | **100** | **100** |
| Recomendaciones | **100** | **100** |
| SEO | **100** | **100** |
| Navegación con agentes | 3/3 | 3/3 |

En móvil, con un Moto G Power emulado y 4G lenta: FCP 1,2 s, LCP 1,5 s, TBT 0 ms, CLS 0 y Speed Index 2,4 s. En escritorio, FCP y LCP 0,3 s y Speed Index 0,5 s. Las cifras se dan con la fecha y las condiciones en que se midieron, que es la única forma en que significan algo.

## Qué publica el dominio

El repositorio es público en GitHub, pero **antoniolopezsanchez.art solo sirve el sitio**. `_config.yml` deja fuera de la publicación los documentos de trabajo (este README, `AGENTS.md`, `PENDIENTES.md`, `PRODUCT.md` y `DESIGN.md`), la carpeta `herramientas/` y `fonts/originales/`. El comprobador falla si un documento nuevo de la raíz se queda fuera de esa lista. Se sirven, a propósito, `LICENSE`, `robots.txt`, `llms.txt`, `sitemap.xml` y la clave de IndexNow.

## Mundo visual

Base heredada del template propio de Index01 ([impulses-art-site](https://github.com/cisnerosmusic/impulses-art-site)), adaptado a esta casa: fondos azul noche en varias tonalidades (`#0a0c1f` a `#252860`), acento en oro (`#d4a030`), Cinzel para los nombres y títulos, Cormorant Garamond para la lectura y Space Mono para el aparato. Navegación fija con desenfoque, aparición lateral de bloques, retrato del autor a sangre en la portada y una banda de mar entre secciones. El sistema completo, con sus tokens y sus reglas, está en [DESIGN.md](DESIGN.md).

## Estructura

| Ruta | Contenido |
|------|-----------|
| `/` | Portada: la casa, el autor y su bienvenida |
| `/libros/` | Los 14 libros publicados, cada uno con su propia página |
| `/ineditos/` | Obras que esperan editorial: cuatro novelas, cada una con su sinopsis, su Con voz y voto y los fragmentos que eligió el autor, nunca íntegras |
| `/tinta-ciones/` | Poesía: `poemas-sueltos/` (12 poemas y 8 glosas), `de-cimitas/` (20 piezas de foto y décima, con aviso para lectores adultos), `sonata-de-la-lluvia/`, `en-mi-voz/` |
| `/contarte/` | Los 11 cuentos, uno por página, con orden rotatorio diario |
| `/trova/` | Su obra documental sobre la Nueva Trova |
| `/plano-abierto/` | Radio, televisión y grabaciones |
| `/laureles/` | Los premios, y las dos obras premiadas en el Farraluque 2026, para lectores adultos: `tres-delirios-y-un-desnudo/` y `revelaciones/` |
| `/periodista/` | Ficha, trayectoria y el archivo de prensa: 23 trabajos firmados, cada uno con su página |
| `/entre-lectores/` | Álbum de ferias y firmas; se llega solo desde Mis libros |
| `/directorio/` | Contacto del autor y consultas de derechos |
| `/derechos/` | Aviso de derechos |
| `/en/` | La zona inglesa, en otro orden que el español a propósito (ver [PRODUCT.md](PRODUCT.md)): portada, `trova/`, `poetry/` (con `poems/`, `decimitas/`, `sonata-de-la-lluvia/` e `in-my-voice/`), `books/` (los catorce libros y `among-readers/`), `stories/` (los once cuentos), `unpublished/` (las cuatro novelas), `awards/` (con las dos obras del Farraluque), `author/` (el concentrador de toda la obra, con `on-record/`, que es Plano abierto), `fiction/` y `rights/` |
| `/fr/` | La zona francesa, con el mismo orden que la inglesa y las mismas piezas: portada, `trova/`, `poesie/` (con `poemes/`, `decimitas/`, `sonata-de-la-lluvia/` y `de-ma-voix/`), `livres/` (los catorce libros y `parmi-les-lecteurs/`), `recits/`, `inedits/`, `prix/`, `auteur/` (el concentrador, con `plan-large/`, que es Plano abierto), `fiction/` y `droits/` |
| `/it/` | La zona italiana, con las mismas piezas: portada, `trova/`, `poesia/` (con `poesie/`, `decimitas/`, `sonata-de-la-lluvia/` y `la-mia-voce/`), `libri/` (los catorce libros y `tra-i-lettori/`), `racconti/`, `inediti/`, `premi/`, `autore/` (el concentrador, con `campo-lungo/`, que es Plano abierto), `narrativa/` y `diritti/` |
| `/pt/` | La zona portuguesa, con las mismas piezas: portada, `trova/`, `poesia/` (con `poemas/`, `decimitas/`, `sonata-de-la-lluvia/` y `na-minha-voz/`), `livros/` (los catorce libros y `entre-leitores/`), `contos/`, `ineditos/`, `premios/`, `autor/` (el concentrador, con `plano-aberto/`, que es Plano abierto), `ficcao/` y `direitos/` |

Archivos de raíz: `index.html`, `styles.css`, `app.js`, `fonts.css`, `robots.txt`, `sitemap.xml`, `llms.txt`, `404.html` (uno solo para todo el sitio, en el idioma de la zona de donde viene el error), `CNAME`, el favicon en archivos reales (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`) y la clave de IndexNow. Recursos en `fonts/`, `img/`, `audio/` y `video/`.

**260 páginas; 257 URLs en el sitemap.** No entran el 404 ni las dos redirecciones blandas, `/novelas/` y `/poeta/`.

## Idiomas

- **Los textos literarios se publican siempre en su español original**, en todos los idiomas del sitio. Se traduce el aparato: navegación, contratapas, notas del autor, fichas, pies de foto y metadatos.
- **Son los cinco del plan: español, inglés, francés, italiano y portugués.** El portugués se escribe pensando en Brasil, que es el mercado grande, pero se declara `pt` y no `pt-BR`: un `hreflang` regional dejaría fuera a Portugal.
- **Las zonas extranjeras no son la española traducida.** En español abre la fantasía heroica; en los cuatro idiomas de fuera, la investigación sobre la Nueva Trova, luego la poesía y luego la narrativa. Cada idioma puede tener su propio orden: lo declara su zona.
- **Las páginas de libro son el mismo generador para todos los idiomas.** Los textos de interfaz de cada idioma están en `herramientas/idiomas.json`, y lo traducido de cada libro, en una capa: `herramientas/libros/<idioma>/<slug>.json`. Esas capas no tienen campo para los fragmentos, así que un fragmento traducido no puede colarse.
- **Añadir un idioma es, casi todo, escribir datos.** Hacen falta cinco cosas: su bloque en `idiomas.json`, su menú en `herramientas/navegacion.py`, su zona `herramientas/zona.<idioma>.json` (la portada y las páginas de sección propias, que no salen de ninguna sala española), y las capas: catorce de libro en `herramientas/libros/<idioma>/` y una por sala (`cuentos`, `poemas`, `decimitas`, `sonata`, `farraluque`, `ineditos`, `laureles`, `grabaciones` y `periodismo`), con el nombre `herramientas/<sala>.<idioma>.json`. Cada generador publica la sala en los idiomas que tengan capa y se salta los que no, y el enlace entre idiomas del menú se arma solo. Y su bloque en `gen-404.py` con sus dos líneas de `styles.css`, más su pareja en `app.js`. El francés obligó además a desatar de dos idiomas el `hreflang`, `unificar-nav.py`, el 404 y `llms.txt`: está contado en `AGENTS.md`. El italiano y el portugués entraron ya sin tocar ni un generador.
- **Son 1048 cadenas por idioma**, de las cuales 382 son las ocho páginas propias de la zona y 245 las capas de libro. El resto es aparato corto. Los cuatro idiomas dan exactamente la misma cifra, que es la forma barata de ver que no falta nada.

## Añadir contenido

Casi nada se escribe a mano: cada sala tiene su generador y su manifiesto en `herramientas/`.

| Generador | Escribe | Lee |
|---|---|---|
| `gen-libro.py` | las 14 fichas de libro en cada idioma, y los catálogos que no son el español | `libros/<slug>.json`, `libros/<idioma>/<slug>.json`, `idiomas.json` |
| `gen-cuento.py` | Contarte y la página de cada cuento, en cada idioma | `cuentos.json`, `cuentos.<idioma>.json` |
| `gen-ineditos.py` | Inéditos y la página de cada novela inédita, en cada idioma | `ineditos.json`, `ineditos.<idioma>.json` |
| `gen-poemas.py` | Poemas sueltos, en cada idioma | `poemas.json`, `poemas.<idioma>.json` |
| `gen-decimitas.py` | De-Cimitas, en cada idioma | `decimitas.json`, `decimitas.<idioma>.json` |
| `gen-sonata.py` | Sonata de la lluvia, en cada idioma | su `.txt`, `sonata.<idioma>.json` |
| `gen-laureles.py` | Laureles, los premios, en cada idioma | `laureles.json`, `laureles.<idioma>.json` |
| `gen-farraluque.py` | las dos obras del Farraluque, en Laureles, en cada idioma | sus `.txt` en `textos/laureles/`, `farraluque.<idioma>.json` |
| `gen-periodismo.py` | la página de cada trabajo de prensa y el archivo dentro de `/periodista/` | `periodismo.json`, sus `.txt` en `textos/periodismo/` |
| `gen-audios.py` | las grabaciones, repartidas a las salas que las reclaman | `grabaciones.json` |
| `gen-idioma.py` | las páginas propias de cada idioma extranjero: su portada, sus secciones y su concentrador | `zona.<idioma>.json` y todos los manifiestos |
| `gen-legal.py` | el aviso de derechos en cada idioma, del español al portugués | `legal.json` |
| `gen-404.py` | el 404, en todos los idiomas a la vez | `navegacion.py` |
| `gen-tarjetas.py` | la postal de cada libro para redes, 1200 x 630: cubierta a la izquierda, título a la derecha | `libros/<slug>.json` y las cubiertas |
| `gen-portada.py` | el Índice de la casa, dentro de la portada | `portada.json` y `navegacion.py` |
| `gen-llms.py` | `llms.txt`, el mapa del sitio para los modelos de lenguaje | `llms.json` y todos los manifiestos |
| `gen-sitemap.py` | `sitemap.xml`, con la fecha real de cada página según git y sus alternates por idioma | las propias páginas |

Auxiliares: `pagina.py`, el marco común de una página en cualquier idioma (cabecera, menú, pie y camino de miga), que usan diez de los generadores y `unificar-nav.py`, y donde vive además el cálculo del ancla de un poema o de una décima, para que el que escribe el `id` y el que escribe el enlace no puedan discrepar; `subset-fuentes.py`, que recorta las fuentes servidas desde `fonts/originales/` a lo que el sitio escribe de verdad; `navegacion.py`, que es la **única** definición del menú y del pie en cada idioma; `unificar-nav.py`, que la aplica a las páginas escritas a mano; `comprobar.py`, que verifica el sitio entero; `version.py`, que sube el `?v=N` de un recurso en todas las páginas a la vez; `a-texto.py`, que convierte los RTF y DOCX del autor a texto plano (con `--verso` para conservar las estrofas); y `leer-poema.py`, que separa título, epígrafe, cuerpo y colofón.

Siguen escritas a mano la portada (salvo el Índice de la casa, que escribe `gen-portada.py`), el catálogo español `/libros/`, la portada de Tinta-ciones, Trova, Plano abierto y En mi voz (salvo la región de grabaciones, que escribe `gen-audios.py`), El periodista (salvo la región del archivo de prensa, que escribe `gen-periodismo.py`), Directorio, Entre lectores y las dos redirecciones blandas. Su menú y su pie no se tocan a mano: los mantiene `unificar-nav.py`.

**Una obra nueva aparece sola en seis sitios**: en su sala, en los cuatro concentradores (`/en/author/`, `/fr/auteur/`, `/it/autore/`, `/pt/autor/`) y en `llms.txt`. Todos leen el mismo manifiesto. No hay que acordarse de nada, y el comprobador falla si alguno se queda atrás. El Índice de la casa de la portada no cuenta obras, solo salas, y se para si deja de coincidir con el menú.

Requisitos: Python 3 y `pip install Pillow fonttools brotli`, las mismas dependencias que instala GitHub Actions.

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
- **La atribución es sagrada.** Varios textos glosan o citan a otros autores (José Martí, Lezama Lima, Jorge Luis Borges, Silvio Rodríguez, Polito Ibáñez, Fito Páez, Noel Nicola, Santiago Feliú, Carlos Varela). Esos versos salen siempre en bloque aparte y con la firma de quien los escribió, nunca corridos con los del autor.
- **En verso no se normaliza nada.** Los espacios múltiples dentro del verso son puntuación del autor y las sangrías marcan dónde abre cada décima. Se conservan tal cual, con `white-space: pre-wrap`.
- **Un texto vive una sola vez.** Si una pieza pertenece a dos salas, se repite el enlace o el reproductor, nunca el texto ni el marcado de datos.
- **Hay material que existe y no se publica**, por decisión del autor y de Ernesto. La lista no está en este repositorio, que es público: la conocen el autor y Ernesto. Ver los innegociables de `AGENTS.md`.
- **Mayúscula inicial** en nombres propios, premios y editoriales.
- Las **obras inéditas** se presentan solo con sinopsis y fragmentos, nunca íntegras.
- **La Sinopsis de un libro es su contratapa, escrita por el autor, o no está.** Once libros la tienen; tres no llegaron a mandarla (*En un lugar de Cuba*, *Trampas retratos y un 17 rojo* y *Vamos a cantar y a soñar*) y su página va de la cubierta a Con voz y voto, sin inventar nada. La línea corta que cada libro enseña en el catálogo, en español y en los cuatro idiomas de fuera, sí la escribe el estudio en primera persona del autor: sirve para escoger, no para citar como contratapa.

## SEO y AEO

257 URLs indexables, con títulos y descripciones únicos y en rango, canónicas propias y Twitter Cards. JSON-LD válido en todas: `Person` con premios y `sameAs`, `WebSite`, `Book` por cada libro y en cada idioma, con `sameAs` a EcuRed y `subjectOf` a la prensa, `ShortStory` por cuento, `CreativeWork` para los poemas, las décimas, la Sonata y las obras del Farraluque, `NewsArticle` para cada pieza de prensa, `ItemList`, `AudioObject`, `CollectionPage`, `ProfilePage` con la persona dentro, `ContactPage` y `BreadcrumbList`.

`hreflang` recíproco en las 234 páginas que tienen pareja de idioma, con `x-default` al español, y los mismos alternates en `sitemap.xml`. Cada una enlaza a todas sus hermanas, no solo a la española; las cuatro páginas de narrativa, que no tienen equivalente español, se enlazan entre ellas y sin `x-default`. Las 23 que no tienen pareja son el archivo de prensa, que solo existe en español, y el Directorio.

`llms.txt` es el mapa para los motores de respuesta: datos citables del autor, la declaración de que nada está traducido y la lista entera de libros, premios, poemas, décimas, cuentos, trabajos de prensa y novelas inéditas, con su dirección. **No se escribe a mano**: lo genera `herramientas/gen-llms.py` desde los mismos manifiestos que el sitio, y el comprobador falla si se queda atrás. `robots.txt` da permiso explícito a los bots de IA, e IndexNow está configurado.

En los cuatro idiomas de fuera, `/en/author/`, `/fr/auteur/`, `/it/autore/` y `/pt/autor/` son el concentrador: la biografía, la hoja de servicios completa y toda la obra en una sola página, por géneros y con cada pieza enlazada. Las listas salen de los manifiestos, así que una obra nueva aparece ahí sola.

## Cómo se trabaja aquí

El proyecto se construye desde dos máquinas con instancias distintas, más una tercera instancia que audita por turnos, y ninguna ve la conversación de las otras. El repositorio es el único medio común. El sistema de trabajo, el protocolo de entrega y los innegociables están en [AGENTS.md](AGENTS.md): **léelo antes de tocar nada**.

Orden de autoridad cuando dos documentos se contradigan: la voluntad del autor, luego [PRODUCT.md](PRODUCT.md), [DESIGN.md](DESIGN.md), [PENDIENTES.md](PENDIENTES.md) y este README. Si un documento contradice al código, gana el código y el documento se corrige en el mismo commit.

## Pendientes

Lo que queda por hacer, y lo que espera la palabra de Tony o la decisión de Ernesto, está en [PENDIENTES.md](PENDIENTES.md). Las decisiones que no hay que deshacer están en [AGENTS.md](AGENTS.md), y lo ya hecho, en el historial de git.

## Créditos

Obra literaria y textos: © Antonio López Sánchez. Cubiertas: Rainel Cabarroi, Juan Carlos García, Ramón Eduardo Haití, Alain R. Cuba, Iván Batista, Tomás Egea Ascona y Michele Millares Hollands, según cada ficha. Fotografía del mar: Wikimedia Commons (CC0). Qué es de quién, con detalle: [LICENSE](LICENSE) y [/derechos/](https://antoniolopezsanchez.art/derechos/).

Desarrollo: [Index01](https://index01.net), Miami. Representación editorial fuera de Cuba: [Ernesto Cisneros](https://ernestocisneros.art/es/representacion-literaria.html).
