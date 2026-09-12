# Pendientes · Ala del Mar

**Estado al 12 de septiembre de 2026.** Qué está hecho, qué falta, qué espera la palabra de alguien y qué se decidió y no hay que deshacer. Se lee después de `AGENTS.md` y `PRODUCT.md`.

Este archivo se reescribió entero el 12 de septiembre: había crecido a 500 líneas mezclando el estado vivo con la crónica de cada día, y varias frases ya no decían la verdad. La crónica está en la historia de git; aquí queda lo vigente.

## Dónde estamos

- **El sitio está en vivo** en [antoniolopezsanchez.art](https://antoniolopezsanchez.art): 63 páginas, 60 de ellas indexables, dominio propio, HTTPS, correo operativo e indexación enviada a Google y Bing.
- **El español está completo.** Catorce libros con su página, poesía, cuentos, trova, grabaciones, premios, trayectoria, contacto y aviso de derechos.
- **La zona inglesa tiene** portada, `trova/`, `poetry/`, `fiction/`, `author/`, `rights/`, el catálogo `books/` y las catorce páginas de libro. Falta lo que se lista más abajo para darla por completa.
- **El 404 es bilingüe**: español por defecto, inglés en cualquier ruta que empiece por `/en/`.
- **`comprobar.py` da 0 fallos y corre solo en cada push**, con GitHub Actions.
- **No se publican cifras de rendimiento** mientras el sitio siga en construcción. Decisión de Ernesto, 12 de septiembre de 2026: se mide y se publica cuando esté terminado el inglés y hechas algunas correcciones más.

## Lo que falta para dar el inglés por completo

Hoy hay salas que solo existen en español. En todas, la literatura se queda en español y lo que se traduce es el aparato:

1. **Contarte**: entradilla y línea de cada cuento en inglés; los cuentos, en español.
2. **Tinta-ciones por dentro**: la entradilla de Poemas sueltos, De-Cimitas, Sonata de la lluvia y En mi voz. Hoy `/en/poetry/` explica la poesía y enlaza a las salas españolas.
3. **Laureles**: hoy los premios en inglés viven dentro de `/en/author/`. Valorar si merecen página propia, con las dos obras del Farraluque.
4. **Plano abierto**: las grabaciones con su ficha en inglés.
5. **Entre lectores, Directorio e Inéditos.**
6. **Menú inglés**: decidir si entra "Books". Hoy al catálogo se llega desde la portada, desde las secciones y desde cada libro.

Cuando esto esté, se mide el rendimiento y se publican los resultados.

## Lo que espera la palabra de Tony

1. **El título del poema del Farraluque.** Su mensaje decía *Tres desnudos y un delirio*; su manuscrito dice *Tres delirios y un desnudo*, y así está publicado.
2. **`Revelaciones` es un solo párrafo** de 15.400 caracteres, tal como está en el .docx. No se le inventaron puntos y aparte: si los quiere, los pone él.
3. **"Estación La Gaveta".** Lo dijo con un "quizá", así que es el título de la sala dentro de `/ineditos/`; la sección y su URL siguen siendo Inéditos. Renombrarla toca menú, pie y sitemap en todo el sitio: se hace en cuanto lo confirme.
4. **Erratas en sus textos publicados.** Aparecieron al traducir al inglés y no se han tocado, porque son suyos. En inglés se tradujo lo que quiso decir.

   | Archivo, en `herramientas/textos/libros/` | Dice | Debería decir |
   |---|---|---|
   | `trovadoras/voz-y-voto.txt` | "en mi voy voto" | "en mi voz y voto" |
   | `trovadoras/voz-y-voto.txt` | "las entrevistan dejan" | "las entrevistas dejan" |
   | `trovadoras/voz-y-voto.txt` | "esos matices el retrato escrito" | "esos matices en el retrato escrito" |
   | `convertida-en-cancion/voz-y-voto.txt` | "El otro, sigue todavía espera." | "El otro sigue todavía en espera." |
   | `el-escudo-de-valnuss/voz-y-voto.txt` | "El Escudo de Valnús", "Rainel Caborroi" | "Valnúss", "Cabarroi" |
   | `grimorium/voz-y-voto.txt` | "Howard Philiphs Lovecraft", "en buena medida manera" | "Phillips", "en buena medida" |
   | `de-la-extrana-aventura-de-don-quijote/contratapa.txt` | "Rescribir", "por primera en la Isla", "en al año" | "Reescribir", "por primera vez", "en el año" |
   | `en-un-lugar-de-cuba/voz-y-voto.txt` | "que. muchos años" | "que, muchos años" |
   | `perdidos-en-un-librero/voz-y-voto.txt` y `cuentos-de-munecas/voz-y-voto.txt` | "Magalys" | "Magaly", como en la ficha y en el crédito del libro |

5. **Dos cuentos retenidos**, *Cantar el cuento III* y *La urna del tío*: el autor los marcó como parte de libros en proceso editorial.
6. **El corte de *Aviso***, del concierto de Rita del Prado: pidió dejar solo desde donde él dice «esto se llama aviso». Hay dos cortes candidatos esperando que los escuche.
7. **Extensión y edad recomendada de cada título**, que es lo primero que pregunta una editorial extranjera y no se puede inventar.
8. **Ojos de bruja**: relato por entregas publicado en Cubaliteraria en julio de 2020, siete partes vivas (`/ojos-de-bruja-i/` a `/ojos-de-bruja-vi/` y `/ojos-de-bruja-vii-y-final/`). Si él lo quiere, Contarte es su sitio y este sería el único lugar donde se lee seguido.
9. **Más material cuando haya corriente en Alamar**: cuatro cuentos más para Contarte, más De-Cimitas (dijo tener «cientos» y llegaron ocho fotos), sinopsis oficiales de los libros que aún tienen texto provisional, prensa de los diez libros que no la tienen, fotos de presentaciones y la foto de escritor oficial si hace la sesión.
10. **Inéditos**: hay cinco poemarios y tres libros de cuentos terminados, pero solo se publican las sinopsis y los fragmentos que él elija.

## Lo que espera la decisión de Ernesto

- **`--gold-dim` en los bordes de los botones** da 2,80:1 contra el fondo, bajo el 3:1 que pide la WCAG 1.4.11 a los límites de un control. Subir su alfa de 0,5 a 0,55 lo lleva a 3,14:1 con un cambio casi imperceptible. Toca el peso visual de los botones, así que es decisión de diseño.
- **"Books" en el menú inglés** (ver arriba).
- **Tarjetas sociales de los libros**: las catorce páginas usan `summary_large_image` con la cubierta, que es vertical, y las redes la recortan por el centro. O se pasan a `summary`, o se genera una tarjeta horizontal por libro.
- **`noindex` en `/ineditos/`** mientras no tenga ni una sinopsis.
- **Search Console**: en el informe de Página de perfil, pulsar *Validar corrección* por el aviso de `mainEntity` que se arregló el 11 de septiembre.
- **Las dos obras del Farraluque viven en Laureles** y no en Tinta-ciones ni en Contarte, porque son literatura erótica adulta y Contarte tiene cuentos infantiles en una rejilla que se baraja cada día. Si Tony las quiere además en sus salas naturales, se mueven.
- Opcionales: **Formspree** para las consultas de derechos, y **verificar el dominio en la cuenta de GitHub** con un registro TXT, para que nadie pueda reclamarlo si el repositorio se despublica.

## Revisión del 12 de septiembre de 2026

Evaluada en `388a033`, midiendo contra el código y el sitio en vivo. Todo lo encontrado quedó arreglado el mismo día:

| Hallazgo | Qué se hizo |
|---|---|
| El enlace "Index01" del pie se distinguía solo por el color: único suspenso de accesibilidad de Lighthouse | Subrayado, en `styles.css`, y regla escrita en `DESIGN.md` |
| Diez imágenes del catálogo español con medidas de otra imagen; seis se deformaban de forma visible | Medidas reales. **Regla nueva en el comprobador**: la proporción declarada tiene que ser la del archivo |
| La cubierta de *Las guerreras de la luz* era la única de catorce a 900 de ancho | Recomprimida a 640, como las demás |
| La cubierta de cada libro se pedía con prioridad media | `fetchpriority="high"` desde `gen-libro.py` |
| `app.js` medía cada bloque a mano mientras añadía clases, y obligaba a remaquetar la página entera en la carga | La altura se lee ahora de la entrada del `IntersectionObserver` |
| El `lastmod` del sitemap estaba atrasado en 41 de 60 URLs | El sitemap lo escribe `gen-sitemap.py` desde git. **Regla nueva**: el comprobador falla si no está al día |
| El sitemap solo declaraba los alternates de la portada | Ahora los saca de cada página: los de las 40 que tienen pareja de idioma |
| El 404 de las rutas inglesas salía en español | 404 bilingüe, generado por `gen-404.py` |
| `.claude/launch.json` estaba en el repositorio público | Fuera, y `.claude/` en `.gitignore` |
| La Person de la portada no recogía la mención en cuento del Farraluque; La Rosa Blanca y El Dinosaurio llevaban años distintos en Laureles y en `/en/author/` | Completado y alineado con Laureles: año de entrega o de fallo |
| Sin integración continua | `.github/workflows/comprobar.yml` pasa el comprobador en cada push |
| El README, este archivo, `AGENTS.md` y `DESIGN.md` decían cosas que ya no eran ciertas, incluidas cifras de rendimiento sin medir | Reescritos o corregidos, y sin cifras de rendimiento |

Lo que no se controla desde aquí: GitHub Pages sirve con `max-age=600` y sin HSTS.

## Decisiones que no hay que deshacer

**Derechos**
- Toda gestión de derechos fuera de Cuba va a **dos destinos y ningún otro**, en cualquier idioma: la página de representación de Ernesto Cisneros y `derechos@antoniolopezsanchez.art`. Decisión del autor, 8 de septiembre de 2026. Ninguna página declara derechos sin decir a dónde escribir, en el idioma de quien lee.
- **Solo se ofrece la obra de Antonio.** En los cinco volúmenes colectivos, la frase de la ficha cambia sola, porque se detecta por el campo `autoría`; y la lista de colectivos de `/derechos/` se lee de ese mismo campo, así que catálogo y aviso legal no pueden contradecirse. Decisión de Ernesto, 9 de septiembre.
- La zona inglesa enlaza la página **inglesa** de representación: el mismo destino en el idioma de quien lee.
- **El dossier de derechos no se duplica aquí.** El sitio de Tony es la casa y el catálogo; el de Ernesto, el negocio.
- El aviso es una declaración clara, no asesoría legal: antes de firmar una cesión, abogado.

**Contenido**
- **La atribución es lo primero.** Los versos de Martí, Lezama, Silvio Rodríguez, Polito Ibáñez, Fito Páez, Noel Nicola y Santiago Feliú salen en bloque aparte y con su firma. La lista de versos ajenos del `LICENSE` y de `/derechos/` se revisa cada vez que entra un texto con epígrafe.
- **En verso no se normaliza nada**: espacios múltiples y sangrías son del autor.
- **Los títulos de poema van escritos a mano en el manifiesto**, porque bajarlos de mayúsculas por programa rompe los nombres propios.
- **Un texto vive una sola vez**: ver `AGENTS.md`.
- ***Proclama Real* no se publica.** En Laureles queda la mención del premio. **Sus tres fechas no son una errata**: escrita en 2009, concurso El Dinosaurio 2013, fallo dado a conocer en 2014. Ya se "corrigió" una vez por error y hubo que revertirlo.
- **Inéditos vacía está bien.** No se llena con relleno.
- **Dos reseñas descartadas**, el 8 de septiembre: un vídeo de booktuber sobre *Las guerreras de la luz* que el autor considera flojo, y una reseña de *Grimorium* en un blog que ya no existe. El bloque de Prensa es de piezas firmadas en medios identificables.
- **Habana Radio está caída entera.** Sus reseñas y programas se enlazan en la copia del Internet Archive: este sitio también es rescate.
- **Los diplomas del Farraluque no se publican como imagen**: eran fotos de folios. Sus datos están como texto en Laureles.

**Inglés y demás idiomas**
- **La literatura no se traduce, nunca.** Se traduce el aparato.
- **El orden inglés es otro**: trova, poesía, narrativa. Decisión de Ernesto, 9 de septiembre, razonada en `PRODUCT.md` y en la cabecera de `navegacion.py`.
- **La autoridad se demuestra, no se declara.** Hechos comprobables en lugar de superlativos.
- **La décima y la glosa se explican**, porque un editor anglófono no sabe qué son.
- **El coste de traducir se dice en voz alta.**
- **No se promete nada que no se pueda mandar esa misma tarde.** Hoy: manuscritos completos y sinopsis. Ni muestras traducidas ni informes de lectura mientras no existan.
- **Los títulos no se traducen**: se glosan entre paréntesis en la ficha y en el catálogo.
- **Los titulares de prensa no se traducen**: son del medio.
- **"Mi hermano"**, hablando de Haití o de Alain Gutiérrez, es figurado: en inglés se matiza para que no parezca parentesco.
- **Leonardo Padura estaba en el jurado** que premió el Quijote de Tony en 2005. Sale de su propio texto y figura en el catálogo y en `/en/fiction/`.
- **"Ala del Mar" y "bene scriptus" no se traducen.**
- **Ruso descartado**: Cinzel y Space Mono no tienen cirílico. Francés, italiano y portugués caben en las fuentes actuales.

**Diseño y accesibilidad**
- **El texto cumple AAA**: el peor contraste de cualquier texto es 7,76:1. Una web casi toda navy dispara el atenuado automático de muchos monitores, y con AA el aparato se volvía negro sobre negro.
- **Los colores de texto son sólidos, sin alfa.** La transparencia fue lo que rompió el contraste una vez. Si un texto tiene que ser más discreto, baja de escalón.
- **Los enlaces dentro de texto van subrayados**, no solo en oro.

## Cómo está montado

**Generadores**, en `herramientas/`. Casi nada se edita a mano:

| Generador | Qué escribe |
|---|---|
| `gen-libro.py` | las fichas de libro en cada idioma y los catálogos que no son el español |
| `gen-cuento.py` | Contarte y cada cuento |
| `gen-poemas.py` | Poemas sueltos |
| `gen-decimitas.py` | De-Cimitas |
| `gen-sonata.py` | Sonata de la lluvia |
| `gen-farraluque.py` | las dos obras del Farraluque |
| `gen-audios.py` | las grabaciones, en las salas que las reclaman |
| `gen-ingles.py` | las páginas de sección inglesas |
| `gen-legal.py` | `/derechos/` y `/en/rights/` |
| `gen-404.py` | el 404 bilingüe |
| `gen-sitemap.py` | `sitemap.xml`, con fechas de git y alternates |

**Escritas a mano**: la portada, el catálogo español `/libros/`, Inéditos, la portada de Tinta-ciones, Trova, Plano abierto y En mi voz (salvo la región de grabaciones, que escribe `gen-audios.py`), Laureles, El periodista, Directorio, Entre lectores y las dos redirecciones blandas. Su menú y su pie los mantiene `unificar-nav.py` desde `navegacion.py`.

**Idiomas.** Las páginas de libro salen de un solo generador para todos los idiomas. Lo de interfaz está en `idiomas.json`; lo traducido de cada libro, en `libros/<idioma>/<slug>.json`, con los textos largos junto al original (`contratapa.en.txt`, `voz-y-voto.en.txt`). Si a una capa le falta algo, el generador se para. Para añadir un idioma: su bloque en `idiomas.json`, catorce capas, su menú en `navegacion.py` y su entrada en `_POR_IDIOMA`.

**La Person del autor vive en la portada.** `/en/author/` la lee de ahí. `/periodista/` lleva una copia escrita a mano: **si cambia la Person de la portada, se actualiza también `/periodista/`**. El comprobador falla si una `ProfilePage` no trae la persona con nombre dentro.

**Ritual al terminar cualquier tanda:**

```bash
python herramientas/<el generador que toque>.py
python herramientas/gen-sitemap.py
python herramientas/comprobar.py      # tiene que decir: 0 fallos
```

El comprobador vuelve a correr los generadores y falla si alguno ya no reproduce su página. Si se tocó `styles.css`, `fonts.css` o `app.js`: `python herramientas/version.py <recurso> <número>`. Después de publicar, el ping de IndexNow.

**Otras cosas que conviene saber:**

- `a-texto.py` usa striprtf. Hubo un parser propio y se comía texto: para textos del autor no se improvisa un conversor, y el resultado se compara con el original antes de publicar.
- `/novelas/` y `/poeta/` son redirecciones blandas, con `meta refresh`, `noindex` y canonical: GitHub Pages no permite un 301 real.
- El meta `msvalidate.01` de la portada no se quita: Bing revalida la propiedad periódicamente.
- La clase `.nota-demo` ya no marca contenido de demo, lleva notas reales. Conviene renombrarla a `.nota` antes de clonar la plantilla para otro artista.

## Fuera de este repositorio

- **`ernestocisneros-site`**: `es/representacion-literaria.html` declara dos `hreflang="en"` en conflicto, uno a `literary-representation.html` y otro a `books.html`. Revisar si el patrón se repite en las siete lenguas. Y en la página inglesa de representación, poner la trova delante del orden de géneros.
- **El documento de representación firmado** entre Tony y Ernesto está en marcha, en la documentación privada del estudio.
- **Backlinks de autoridad**, que es lo que más moverá el posicionamiento: que EcuRed enlace el sitio, que Tony lo publique en su Facebook y que aparezca en las páginas de sus editoriales.
