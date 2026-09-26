# Cómo se trabaja en este repositorio

Nota de operación para cualquier persona o agente que abra `tony-site`. Léela antes de tocar nada. Escrita el 8 de septiembre de 2026.

## Quién trabaja aquí

El proyecto lo lleva Ernesto Cisneros (Index01) con tres participantes que nunca están en la misma sesión:

| Participante | Dónde | Qué hace |
|---|---|---|
| **Máquina 1** | Casa de Ernesto | Construye. Es la única con acceso al material original de Tony en OneDrive. |
| **Máquina 2** | Trabajo de Ernesto en UnlimitedWraps | Construye. No alcanza el OneDrive de la Máquina 1. |
| **Instancia evaluadora** | ChatGPT, por turnos | No construye. Audita estructura, contenido, fugas y seguridad. |

Las dos primeras son instancias de Claude Code que construyen; la tercera evalúa lo construido. Entre unas y otra se va mejorando el sitio. Ninguna ve la conversación de las otras.

## La regla que sostiene todo lo demás

**El repositorio es el único medio común. No hay otro.**

La memoria del asistente vive en el perfil local de cada máquina y **no se sincroniza**. Lo que una instancia guarda ahí es invisible para las demás. Las conversaciones tampoco cruzan.

De ahí la regla operativa, que no es una recomendación:

> Si algo tiene que sobrevivir al cambio de máquina o de instancia, **va en un archivo del repositorio**. Nunca solo en la memoria del asistente ni en el hilo de la conversación.

Un hallazgo que se queda en una sesión está perdido. Un hallazgo escrito en `PENDIENTES.md` y empujado lo tienen todos.

## Antes de empezar y al terminar

**Antes:**

1. `git pull`. Puede haber commits de la otra máquina, y los hay a menudo.
2. Lee `PRODUCT.md`. La jerarquía de la obra depende del idioma y no es intuitiva.
3. Lee `PENDIENTES.md`: es la lista de lo que queda por hacer, y nada más.

**Al terminar:**

1. **Pasa el comprobador.** `python herramientas/comprobar.py`. No se cierra una tanda con fallos abiertos.
2. **Borra de `PENDIENTES.md` lo que quedó hecho** y añade lo que quedó abierto, con datos verificables (rutas, cifras, comandos), no con impresiones. Lo hecho no se apunta ahí: vive en el historial de git, y por eso el mensaje del commit explica el porqué. Si lo hecho dejó una decisión que no hay que deshacer, va a la sección de decisiones de este archivo.
3. Commit con mensaje que explique **por qué**, no solo qué.
4. Empuja. Un commit local no existe para las demás instancias.

Si dejas trabajo a medias, dilo en `PENDIENTES.md` con el punto exacto donde parar y cómo verificar. La siguiente instancia no tiene tu contexto.

## El trabajo va en ciclos

Se construye, una instancia evaluadora audita, se corrige, y vuelta a empezar. No es una fase del proyecto: es como se trabaja aquí siempre.

De ahí sale `herramientas/comprobar.py`. Cada regla suya nació de un fallo real que encontró una auditoría, y está anotado cuál. La idea es sencilla: **lo que una máquina puede comprobar sola no debe gastar la atención de nadie**. La auditoría humana o de otra instancia queda libre para lo que sí necesita criterio, que es el sitio, no la sintaxis.

Comprueba hoy enlaces rotos, sitemap contra páginas indexables y **sitemap al día**, JSON-LD válido, con tipos que existan de verdad y, en las páginas de perfil, con la persona dentro (`mainEntity`, que Google exige), títulos y descripciones únicos y en rango, una sola versión de CSS y JS, rutas absolutas de una máquina concreta, raya larga en texto público, imágenes sin `alt` y **con medidas que no son las del archivo**, `target="_blank"` sin `noopener`, el menú y su script, la navegación alineada, que `_config.yml` deje fuera de la publicación los documentos y las herramientas, que cada enlace con `#` apunte a un ancla que existe, y que los generadores sigan reproduciendo su HTML y su `llms.txt`. Sale con código 1 si algo falla, y **corre solo en cada push** con GitHub Actions (`.github/workflows/comprobar.yml`): si la marca sale en rojo, alguien dejó una regla rota.

**Cuando la auditoría encuentre algo que el comprobador podría haber cazado, se arregla el fallo y se añade la regla en el mismo commit.** Ese es el modo en que el ciclo se hace más barato cada vuelta.

## Quién manda sobre qué

Cuando dos documentos se contradigan, este es el orden:

1. **La voluntad del autor**, Antonio López Sánchez, por encima de cualquier criterio técnico o de diseño.
2. **`PRODUCT.md`**: para quién es el sitio y qué tiene que conseguir. Se lee antes de decidir nada de producto.
3. **`DESIGN.md`**: cómo se ve y por qué. Los tokens y las reglas nombradas son vinculantes.
4. **`PENDIENTES.md`**: qué falta y en qué orden.
5. **`README.md`**: reglas de contenido y cómo añadir un libro.

Si encuentras una contradicción entre un documento y el código, **el código gana y el documento se corrige en el mismo commit**. Este repositorio ya tuvo un `DESIGN.md` que describía con total autoridad un diseño abandonado, y estuvo a punto de hacer que un agente devolviera el sitio a un mundo visual que nadie quería. No vuelva a pasar.

## Para la instancia evaluadora

Tu valor está en encontrar lo que las instancias constructoras no vieron. Hay una trampa concreta que lo anula:

**Si evalúas leyendo `PENDIENTES.md`, no estás verificando: estás devolviendo el examen ya resuelto.** Ese archivo lo escriben las instancias que construyen. Coincidir con él no confirma nada.

Cómo evaluar de verdad:

- **Mide contra el código y contra el sitio en vivo**, no contra la documentación.
- Si quieres usar los documentos, úsalos para lo contrario: **buscar dónde mienten**. Un documento que no coincide con el código es un hallazgo, y de los buenos.
- Da resultados **falsables**: rutas, cifras, comandos. "El contraste se ve flojo" no se puede contradecir; "`--text-dim` da 2,89:1 en `styles.css:21`" sí.
- Di en qué commit evaluaste. Sin eso no se sabe si tu informe sigue vigente.

Y al revés, para las instancias que construyen: **si dais un hallazgo sin número, ruta o comando con el que otro modelo pueda contradeciros, no habéis dado un hallazgo, habéis dado una opinión.**

## Innegociables

- **Sin raya larga** en ningún texto público del sitio. Se usa guion.
- **La literatura no se traduce.** Poemas, cuentos y fragmentos se publican siempre en su español original, en todos los idiomas del sitio. En las páginas de libro no hace falta recordarlo: las capas de idioma no tienen campo donde poner un fragmento traducido. Lo que se traduce es el aparato: contratapas, notas del autor, fichas, pies de foto y metadatos.
- **El sitio en otro idioma no promete nada que no se pueda mandar esa misma tarde.** Hoy eso son manuscritos completos y sinopsis. Ni muestras traducidas ni informes de lectura mientras no existan.
- **Hay material del autor que existe y que, por decisión suya y de Ernesto, no se publica.** La lista **no vive en este repositorio**: es público en GitHub, y cualquier título que se escriba aquí se lee desde fuera, con motivos o sin ellos. La conocen el autor y Ernesto. La regla operativa, que sí es para todos: **ningún texto nuevo del autor se sube sin que Ernesto lo haya confirmado en esa misma sesión**, y cualquier material de tema político, militar o religioso se para y se consulta antes de tocarlo. Ante la duda, no se sube. Y que el autor mande un material no levanta por sí solo la reserva: el 22 de septiembre de 2026 llegaron tres trabajos suyos dentro de un zip, se quedaron fuera y se consultó, porque comprimir una carpeta entera no es lo mismo que pedir que algo salga.
- **Las obras inéditas de Tony no entran en este repositorio, que es público.** Solo sinopsis y fragmentos que él elija. Publicarlas les quitaría la condición de inéditas ante concursos y editoriales.
- **El mecanismo de cobro, la custodia de fondos y cualquier detalle fiscal o contractual de la representación no se documentan aquí.** Van en la documentación privada del estudio.
- **Las páginas de libro no se maquetan a mano**: se generan con `herramientas/gen-libro.py` desde su manifiesto.
- **Toda gestión de derechos fuera de Cuba va a dos destinos y ningún otro**, en cualquier idioma: la página de representación de Ernesto Cisneros y `derechos@antoniolopezsanchez.art`. El correo vive en `DERECHOS_EMAIL`, en `gen-libro.py`; la página de representación, en el idioma de quien lee, en `herramientas/idiomas.json`.
- **Los colores de texto son sólidos, sin alfa.** Es lo que rompió el contraste una vez. Ver `DESIGN.md`.
- **El dominio solo sirve el sitio.** `_config.yml` deja fuera de la publicación los documentos de trabajo (todos los `.md` de la raíz), `herramientas/` y `fonts/originales/`. El repositorio es público en GitHub, pero lo que no es el sitio no tiene por qué estar además en antoniolopezsanchez.art, bajo el nombre del autor y abierto a los rastreadores de IA que invita `robots.txt`. Hasta el 21 de septiembre de 2026 el dominio servía este archivo, PENDIENTES.md, los textos de `herramientas/textos/` y hasta `/DESIGN.html`, que Jekyll renderizaba por su cuenta. Un documento o una carpeta nueva que no sea parte del sitio se añade a esa lista, y el comprobador falla si falta.
- **El sitemap tampoco se edita a mano**: lo escribe `herramientas/gen-sitemap.py` desde las páginas y la historia de git, y el comprobador falla si no está al día.
- Al cambiar `styles.css`, `fonts.css` o `app.js`, se sube su `?v=N` con `python herramientas/version.py <recurso> <número>`, que lo cambia a la vez en todas las páginas y en todos los generadores.
- **Las cifras de rendimiento se pueden publicar.** Del 12 al 23 de septiembre de 2026 hubo un embargo, decidido por Ernesto: no se publicaban mientras el sitio siguiera en construcción, ni en el README ni en ningún otro documento. **Lo levantó él el 23**, con los cinco idiomas terminados y El periodista cerrado, que eran las dos condiciones que se habían escrito (cada documento llevaba una, y esa contradicción fue lo que obligó a resolverlo). Queda dicho aquí para que nadie reponga el embargo por prudencia. La regla que sí sigue viva es la de siempre: **una cifra se publica con la fecha y las condiciones en que se midió, o no se publica**.

## Decisiones que no se deshacen

No son tareas, así que no viven en `PENDIENTES.md`. Son decisiones tomadas, casi todas con Tony o con Ernesto, que alguien podría "arreglar" de buena fe dentro de un mes. Si una te parece un error, pregunta antes de tocarla.

**Derechos**
- **Solo se ofrece la obra de Antonio.** En los cinco volúmenes colectivos, la frase de la ficha cambia sola, porque se detecta por el campo `autoría`, y la lista de colectivos de `/derechos/` se lee de ese mismo campo: catálogo y aviso legal no pueden contradecirse. Decisión de Ernesto, 9 de septiembre de 2026.
- **Cada zona enlaza la página de representación en su idioma**: el mismo destino, en la lengua de quien lee. Solo existe la inglesa en `ernestocisneros-site`, así que el francés, el italiano y el portugués apuntan de momento a ella: está apuntado en `PENDIENTES.md`.
- **El dossier de derechos no se duplica aquí.** El sitio de Tony es la casa y el catálogo; el de Ernesto, el negocio.
- **El aviso de derechos es una declaración clara, no asesoría legal.** Antes de firmar una cesión, abogado.

**Contenido**
- **Las tres fechas de *Proclama Real* no son una errata**: escrita en 2009, concurso El Dinosaurio 2013, fallo dado a conocer en 2014. Ya se "corrigió" una vez por error y hubo que revertirlo.
- **La fecha de la entrada 8 de *Mis diarios de cama* es el 18 de septiembre de 2004**, no el 20 que dice el nombre del archivo del autor. Confirmado con Tony el 22 de septiembre de 2026. Está publicada con 18 y no se «corrige» al 20.
- **En la décima *Penitente* dice «Tu lengua», y en *Beso (I)*, «y un cauce».** Los originales traían «legua» y «una cauce»; Ernesto confirmó las dos el 22 de septiembre de 2026. Son la excepción a la regla de no tocar el verso, y por eso van escritas aquí: sin esto, alguien las «devuelve» al original dentro de un mes creyendo que respeta al autor.
- **En la décima *Rabia y pez* dice «y el sueño que cada vez».** El original trae «sue;o»; Ernesto lo resolvió el 25 de septiembre de 2026. Va aquí por lo mismo que las dos de arriba.
- **Las erratas obvias se corrigen sin preguntar, y se informa después.** Decisión de Ernesto, 22 de septiembre de 2026, después de resolver tres a mano. Obvia es la que no admite lectura alternativa: un artículo que falta («la noticia **de que** su mamá murió»), una palabra repetida, un signo pegado a la palabra anterior, un nombre propio mal escrito, «porqué» por «por qué». Se corrige y se cuenta en un informe con la línea exacta, para que el autor pueda revocar cualquiera.

  Lo que **no** es obvio y sigue esperando a Tony: cualquier cosa que cambie el sentido, una fecha que se contradice con otra fuente, y **todo lo que esté en verso**. Ahí sigue mandando el innegociable de que en verso no se normaliza nada: un fallo de concordancia puede ser licencia, y la métrica no se toca a ciegas.

  **Pero un fallo de tecla no es verso, ni en verso.** «un error es un error y nosotros lo arreglamos», Ernesto, 25 de septiembre de 2026, sobre `sue;o` en la décima *Rabia y pez*: el punto y coma sale de teclear al lado de la eñe, no admite lectura, y el mismo documento escribe «sueño» bien dos veces. Se corrige y se informa. La frontera es la misma de siempre: si se puede leer de otra manera, espera a Tony; si solo se puede leer como un dedazo, se arregla.
- **Los nombres de archivo de Tony son dato, y sus erratas también se corrigen.** En los nombres va la fecha, el lugar y quién estaba, así que salen enteros a `NOMBRES ORIGINALES.json` junto a los cortos. El 25 de septiembre de 2026 llegaron «GALERÏA» y «CANCIÖN» con diéresis, y dos nombres propios sin mayúscula; se corrigieron los diecinueve nombres afectados y queda anotado en el propio archivo. **Es GALERÍA y CANCIÓN siempre.** Lo que no se toca de un nombre es el dato: una fecha rara o un lugar inesperado se comprueban, no se enmiendan.
- **Los espacios múltiples del verso son puntuación del autor.** Tony escribe «Y que traigas   mensajera» y el hueco hace de coma; la sangría de la izquierda marca dónde abre cada décima. `styles.css` pinta el verso con `white-space: pre-wrap` justamente para que se vean. Nadie los «limpia»: ni el conversor, ni quien transcriba a mano, ni un corrector automático.

  Se perdieron dos veces sin que nadie lo notara, porque el texto se lee bien sin ellos: `a-texto.py` colapsaba las rachas al convertir, y al transcribir se «mejoraron» a comas. Lo recordó Ernesto el 25 de septiembre de 2026 y se restituyeron 152 versos en 22 textos, en dos pasadas: 133 primero y 19 más al aparecer el original que faltaba. Para volver a comprobarlo, `python herramientas/espacios.py` compara el verso publicado contra los originales del autor y dice qué falta; con `--aplicar` trasplanta los huecos sin tocar las palabras, y después `git diff -w` tiene que salir vacío. No toca la prosa, donde las rachas son descuido de mecanografía, ni el título, que los generadores buscan por texto exacto, ni el epígrafe: los versos de Martí y de Lezama llevan su puntuación canónica, no el tecleo de Tony en el RTF.

  **La herramienta solo ve los originales que están sueltos en disco, no los que siguen dentro de un zip.** Ahí estuvo el punto ciego: las trece décimas de la segunda tanda daban «limpio» porque su documento, `DE CIMITAS   TEXTOS NUMERADOS.rtf`, nunca se había extraído de `De Cimitas  2 TEXTO Y FOTOS.zip`, y sin original no hay con qué comparar. Se extrajo el 25 de septiembre de 2026 y aparecieron diecinueve versos más que restituir. Cuando llegue un zip, **el documento se extrae aunque solo se vayan a usar las fotos**: si no, la auditoría miente sin saberlo y dice que no hay nada donde no ha mirado.
- **La línea en blanco entre dos párrafos de prosa también es del autor.** En *Cantar el cuento (III)* separa la narración de la voz que le habla a Olga en segunda persona, y sin ella las dos se leen como una sola. `a-texto.py` las descartaba en prosa, con un `for l in lineas if l`, y ocho cuentos perdieron sus pausas; lo dijo Ernesto el 25 de septiembre de 2026. Ahora se conserva una donde el autor puso una o varias, en prosa y en verso.

  En la página la pinta `gen-cuento.py`, que marca `class="tras-pausa"` el párrafo que viene después: `styles.css` le abre una línea entera de aire y le quita la sangría, que es lo que pide la tipografía cuando un bloque empieza tras un blanco. Se restituyeron veintinueve pausas, de las cuales veintiuna se ven en la página: las otras caían antes del título, del epígrafe o del colofón, que el generador ya trataba aparte. `python herramientas/espacios.py` las comprueba contra los originales igual que las rachas, y con `--aplicar` las repone insertando solo blancos, sin tocar ninguna línea con texto.
- **Ningún texto del autor lleva fecha ni sello al final.** Ni los poemas, ni los cuentos, ni los fragmentos de Inéditos. Tony cierra algunos con la fecha y con «Hallado en Ala del Mar… bene scriptus», que es de donde sale el nombre de la casa, y pidió el 22 de septiembre de 2026 que no salieran a la página. En los cuentos las líneas exactas se declaran en el campo `colofon` del manifiesto y se comprueban, en vez de recortar por parecido: un cuento puede acabar de verdad con una frase corta que lleve un mes dentro. Y si aparece un colofón sin declarar, el generador se para, para que una reimportación del original no lo devuelva a la página en silencio. `leer-poema.parece_colofon()` es quien lo reconoce, y lo usan los tres.
- **Los poemas no llevan fecha.** Los originales de Tony la traen al pie, y `herramientas/leer-poema.py` la sigue separando del cuerpo, precisamente para que ninguna se cuele entre los versos; pero no sale a la página. Decisión de Ernesto, 20 de septiembre de 2026. Si alguna vez se quiere volver a enseñar, el dato está entero en `colofon` y solo hay que imprimirlo.
- **Los tres libros de la trova cuelgan de `/trova/`, no del catálogo.** Viven en `/libros/<slug>/` porque son libros, pero se presentan en La trova, y el menú, el camino de miga y el botón del final devuelven allí. Lo dice el campo `seccion` de su manifiesto, y en inglés el grupo del catálogo de `idiomas.json`. Por eso `unificar-nav.py` deja fuera las páginas de libro: ahí la sección no se deduce de la dirección. Lo pidió Tony el 20 de septiembre de 2026, y tenía razón: se entraba desde La trova y se salía a Mis libros.
- **Una obra en varios tomos lleva una sala por tomo**: portada, sinopsis y fragmento, detrás de la sinopsis general y de Con voz y voto. Estructura pedida por Tony el 20 de septiembre de 2026 para *El Escudo de Valnúss*. Antes eran las cinco portadas juntas en una rejilla y, mucho más abajo, todos los fragmentos seguidos; él lo llamó «la longaniza». Un fragmento por tomo, no dos: el segundo de cada uno está en el material de Tony, sin publicar.
- **Las grabaciones de voz entran a 96 kbps y en mono.** Tony las manda a 320 kbps, que para voz recitada es peso muerto: las siete de septiembre de 2026 pasaron de 16,5 MB a 5. El original no se toca y sigue en su carpeta. Si alguna vez entra música, y no voz, esto se vuelve a pensar.
- **Un poema sin título se anuncia por su primer verso, en cursiva y con puntos suspensivos.** Lo marca el campo `sin_titulo` de `herramientas/grabaciones.json`. Lo pidió Tony para *No vamos a olvidar…* y *Yo soy…*, y la razón es que no se lean como títulos que no existen.
- **Las páginas de libro tampoco llevan frase bajo el título**: título y a la sinopsis. Lo pidió Tony el 20 de septiembre de 2026, por redundante con lo que ya dice la sala de fuera y con Con voz y voto. El campo `tira_sub` se borró de los 28 manifiestos, no solo se dejó de pintar.
- **Cada libro tiene su postal**, la imagen que sale al compartir su página: cubierta pequeña a la izquierda y título centrado a la derecha, con el nombre del autor debajo. Diseño fijado por Ernesto el 21 de septiembre de 2026. La genera `herramientas/gen-tarjetas.py` en `img/tarjetas/` (1200 x 630, JPEG, porque con WebP algunas redes devuelven la tarjeta vacia). En los volúmenes colectivos dice «Con textos de Antonio López Sánchez», nunca que el libro es suyo. Un libro nuevo necesita correrlo: el comprobador falla si una página apunta a una postal que no existe.
- **Las fuentes servidas están recortadas.** Las de Google llegan con el bloque latino entero y con funciones OpenType que el sitio no pide: eran 52 KB de los 217 que pesaban las de la portada, donde las fuentes son el 68% del peso. Los originales viven en `fonts/originales/`, no se sirven, y de ahí sale todo con `python herramientas/subset-fuentes.py`. Añadir un carácter o una función es volver a correrlo. El comprobador verifica que cada carácter que sale en el sitio existe en cada fuente servida, así que un texto nuevo con un signo raro se caza antes de publicarse.
- **Laureles se genera** desde `herramientas/laureles.json`, y en inglés (`/en/awards/`) desde su capa. Estaba a mano; pasó a generarse el 21 de septiembre de 2026, cuando los premios iban a vivir en tres sitios. La página inglesa del autor ya no repite la lista: la resume y enlaza. El generador se para si la capa no trae los mismos premios, en el mismo orden y con los mismos años. En inglés los premios cuelgan de The author en el menú.
- **Inéditos se genera** con `herramientas/gen-ineditos.py` desde `herramientas/ineditos.json`, y en inglés (`/en/unpublished/`) desde la capa `herramientas/ineditos.en.json`, que trae solo el aparato: títulos y fragmentos se quedan en español. En inglés no tiene entrada en el menú: se llega desde el catálogo `/en/books/`, y es Books lo que se enciende. Todo, con la maqueta de las páginas de libro. De cada novela entra solo lo que Tony eligió: sinopsis, Con voz y voto y fragmentos. La línea de cada tarjeta es la primera frase de su sinopsis, tal cual. El campo `lugar` marca las novelas cuyos fragmentos abren con el lugar y el tiempo de la escena, que se pintan juntos y no como párrafos; no se deduce solo porque en los diarios la línea sin sangría es «Querido Diario:».
- **La portada lleva el Índice de la casa.** Pedido por Ernesto el 22 de septiembre de 2026. La portada explicaba de dónde viene el nombre y no decía qué hay dentro, y seis de las diez puertas del menú no dicen lo que guardan: nadie que llegue por primera vez sabe que Tinta-ciones es la poesía ni que Laureles son los premios. La salida **no** es un texto que explique cómo leer la web, que en la portada de un escritor se lee como una disculpa, sino un índice que sea la propia navegación: cada sala con su nombre y una línea que dice qué es.
- **El índice dice qué es cada sala, nunca cuánto hay dentro.** Llevó una cifra por sala durante unas horas del mismo día y Ernesto la quitó: una cantidad cambia rápido y envejece a la vista. No se vuelve a proponer. Lo escribe `herramientas/gen-portada.py` entre los marcadores `<!-- indice -->`, y lo único que comprueba, que es la razón de que sea un generador y no HTML a mano, es que **el índice y el menú digan las mismas salas en el mismo orden**: si divergieran, el visitante tendría que aprenderse dos.
- **Cada idioma de fuera tiene su concentrador de toda la obra**: `/en/author/`, `/fr/auteur/`, `/it/autore/` y `/pt/autor/`. Quién es el autor, su hoja de servicios completa y, por géneros, las catorce obras publicadas, los veintitrés trabajos de prensa, los once cuentos, los veinte poemas, las treinta y una décimas y las cuatro novelas inéditas, cada uno enlazado. Estructura pedida por Ernesto el 22 de septiembre de 2026. **Las listas no se escriben en la zona**: las arma `gen-idioma.py` desde los mismos manifiestos que el sitio, con el tipo de sección `obras`. Escribirlas a mano sería tener el dato dos veces, y el segundo envejecería sin que nadie lo notara.
- **En cada idioma se dice que la obra no está traducida.** Ninguna obra de Tony existe en otra lengua y no hay muestra traducida: lo que se ofrece es el original. Va dicho en `/en/author/`, con la frase de que se aceptan ofertas para traducir cualquier zona de la obra, y repetido en `llms.txt`. **La oferta es solo sobre la obra de Antonio**, nunca sobre los textos ajenos de los volúmenes colectivos: es la misma regla del catálogo y del aviso de derechos.
- **`llms.txt` se genera.** Lo escribe `herramientas/gen-llms.py` desde `llms.json` (la prosa que no sale de ningún otro sitio, con `{n}` donde va un número) y desde todos los manifiestos. Estuvo escrito a mano hasta el 22 de septiembre de 2026 y llevaba doce días diciendo que Contarte tenía siete cuentos cuando ya eran once, que De-Cimitas tenía siete décimas cuando eran veinte, y sin enterarse del archivo de prensa. Nadie lo vio porque ese archivo no lo miran las personas: lo leen los motores de respuesta. Ahora el comprobador falla si se queda atrás.
- **Las anclas se comprueban.** Los enlaces a un poema o a una décima dentro de su sala (`/en/poetry/poems/#el-poeta`) no dan 404 si el ancla desaparece: simplemente no llevan a ninguna parte. El ancla la calcula `pagina.ancla()`, una sola vez para el que escribe el `id` y el que escribe el enlace, y el comprobador verifica que cada `#` apunta a un `id` que existe.
- **El archivo de prensa vive dentro de `/periodista/`, agrupado por género**: Entrevistas, Reseñas, Crónicas y ensayos. Decisión de Ernesto, 22 de septiembre de 2026, frente a agruparlos por publicación o por año: un lector busca por lo que quiere leer, no por dónde salió. La sección va entre la ficha de redacción y la Trayectoria, y la escribe `herramientas/gen-periodismo.py` entre los marcadores `<!-- trabajos -->`, igual que las grabaciones. El resto de la página se sigue editando a mano.
- **Los intertítulos y las preguntas de un trabajo periodístico van declarados en `herramientas/periodismo.json`**, línea por línea, y el generador se para si no las encuentra. Se probó a deducirlos por el largo de la línea y no sirve: en los trabajos de trova los intertítulos son versos de canciones, y una cita corta y un titular se parecen demasiado.
- **De nueve trabajos no consta dónde salieron y se publican igual, callando el medio.** Decisión de Ernesto, 22 de septiembre de 2026, tomada sabiendo de dónde podían venir y asumiendo ese riesgo. La lista de los nueve está en `PENDIENTES.md`, a la espera de que Tony diga de dónde son; el que resulte ser de material reservado se retira. **El razonamiento que llevaba a un medio concreto se quitó de aquí el 23 de septiembre**: este repositorio es público, y escribir la deducción era tan revelador como escribir el nombre. Lo saben el autor y Ernesto.
- **La entrevista a Carlos Varela de 1994 entra**, aunque toca lo político y nunca llegó a publicarse. Decisión de Ernesto, 22 de septiembre de 2026. Sale con la entradilla que el propio Tony escribió para explicar por qué se publica ahora.
- **Los cuentos de Contarte entran sin línea de presentación**: título y al texto. La línea sigue viva en el índice de Contarte, que es donde sirve para escoger.
- **El aviso para adultos de un cuento es de dos clases, no de una.** *Cantar el cuento (III)* y *La urna del tío* llevan el de literatura erótica; *Hipo-Tálamo* no es erótico y lleva el suyo. Lo elige el campo `adultos` del manifiesto. Publicarlo lo decidió Ernesto el 22 de septiembre de 2026.
- **Un aviso avisa, no cuenta.** El de *Hipo-Tálamo* enumeraba de qué trata, y Ernesto lo acortó el mismo día a «Cuento para lectores adultos.»: en ese cuento lo que se enumeraba era el final. Vale para cualquier aviso que se escriba en adelante. Y la frase vive en el generador, no en el HTML: una corrección hecha sobre la página generada la borra la siguiente pasada.
- **El logotipo de De-Cimitas no se usa.** Tony mandó dos versiones el 22 de septiembre de 2026, en cian y en blanco, y Ernesto decidió ese mismo día que no van al sitio. No se vuelve a proponer, ni en JPEG ni redibujado. Los archivos siguen en su material, no en este repositorio.
- **De-Cimitas lleva aviso visible y `rating: adult` en toda la sala**, desde la segunda tanda: cuatro de las trece nuevas son poesía erótica sin rodeos y todas las décimas viven en la misma página, así que no se puede avisar una a una.
- **La dedicatoria y el epígrafe de un texto van declarados en el manifiesto**, nunca adivinados: una dedicatoria de cuatro líneas y un primer párrafo corto se parecen demasiado. El generador se para si el texto no trae exactamente lo declarado.
- **Tres libros se quedan sin Sinopsis, y está bien así.** *En un lugar de Cuba*, *Trampas retratos y un 17 rojo* y *Vamos a cantar y a soñar* no tienen contratapa del autor, así que su página va de la cubierta a Con voz y voto, sin ese bloque y sin rellenarlo con un resumen del estudio. Decisión de Ernesto, 22 de septiembre de 2026, después de comprobar que los otros once sí llevan la de Tony. No se pide, no se inventa y no se vuelve a plantear.
- **El bloque de cada libro se llama *Sinopsis***, en español, y *Synopsis* en inglés. El rótulo vive en `herramientas/idiomas.json`; la clave interna sigue siendo `contratapa`, porque es el nombre del archivo de texto en cada manifiesto. La única excepción es *Cuentos de muñecas*: es un volumen colectivo y su nota no resume un libro de Tony, sino que explica la compilación, así que mantiene **Sobre el libro**.
- **Los títulos de poema van escritos a mano en el manifiesto.** En los originales vienen en mayúsculas, y bajarlos por programa rompe los nombres propios y confunde el nombre de la serie con el del poema.
- **La lista de versos ajenos** del `LICENSE` y de `/derechos/` se revisa cada vez que entra un texto con epígrafe.
- **Las dos obras del Farraluque viven en Laureles**, no en Tinta-ciones ni en Contarte: son literatura erótica adulta, y Contarte tiene cuentos infantiles en una rejilla que se baraja cada día. Llevan `<meta name="rating" content="adult">`, `isFamilyFriendly: false` y un aviso visible antes del texto.
- **Inéditos vacía está bien.** No se rellena con relleno.
- **El bloque de Prensa es de piezas firmadas en medios identificables.** Por eso se descartaron el 8 de septiembre un vídeo de booktuber sobre *Las guerreras de la luz* y una reseña de *Grimorium* en un blog que ya no existe.
- **Habana Radio está caída entera**: sus reseñas y programas se enlazan en la copia del Internet Archive.
- **Los diplomas del Farraluque no se publican como imagen**, porque eran fotos de folios. Sus datos están como texto en Laureles.

**Inglés y demás idiomas**
- **Ningún generador sabe cuál es el segundo idioma.** Hasta el 22 de septiembre de 2026, el inglés estaba escrito dentro del código: dos parejas de funciones de navegación casi iguales con el enlace al otro idioma clavado dentro, un `if es else "/en/poetry/"` en cuatro generadores, y `gen-ingles.py` leyendo `ingles.json` con trece rutas `/en/` a mano. Con cinco idiomas eso se habría escrito cuatro veces. Ahora:
  - `navegacion.IDIOMAS` declara cada idioma entero (menú, pie, portada, etiqueta) y **el enlace entre idiomas se arma solo**: cada menú enlaza a todos los demás del registro.
  - La sección de menú que enciende cada sala es un dato de su capa (`seccion`), no un `if`.
  - `gen-idioma.py` (antes `gen-ingles.py`) escribe **una zona por idioma**, desde `herramientas/zona.<idioma>.json`, y de ahí salen las parejas de `hreflang`, el orden de los grupos del catálogo, los rótulos y el alt de la banda de mar.

  **Añadir un idioma es, casi todo, escribir datos.** El francés se construyó entero el 23 de septiembre de 2026 y salió con su menú, su `hreflang`, su JSON-LD y el selector, desde 1047 cadenas y sin tocar ninguno de los generadores de sala. Pero cuatro sitios seguían atados a dos idiomas, y eso solo se ve cuando nace el tercero: el `hreflang` de `gen-idioma.py` emparejaba cada página solo con la española, así que la francesa y la inglesa se declaraban inexistentes entre sí; `unificar-nav.py` excluía `"en/"` escrito a mano y le plantó el menú español a las veintitantas páginas de `/fr/`; `gen-404.py`, su CSS y `app.js` conocían dos idiomas; y `gen-llms.py` tenía la zona inglesa clavada. Ya están hechos lista. **La lección, escrita cuando el francés era el tercero: lo que se probó con dos no está probado.** El italiano y el portugués llegaron el mismo día, ya con esas cuatro cosas hechas lista, y entraron sin tocar ni un generador: los cuatro idiomas de fuera dan exactamente 1048 cadenas cada uno. Un idioma nuevo son cinco cosas: su bloque en `idiomas.json`, su menú en `navegacion.py`, su `zona.<idioma>.json`, sus capas de sala y de libro, y su bloque en `gen-404.py` con sus dos líneas de `styles.css` y su pareja de etiquetas en `app.js`.
- **El orden inglés es otro: trova, poesía, narrativa.** Decisión de Ernesto, 9 de septiembre de 2026, razonada en `PRODUCT.md` y en la cabecera de `navegacion.py`.
- **La autoridad se demuestra con hechos comprobables**, no se declara con superlativos.
- **La décima y la glosa se explican**, porque un editor anglófono no sabe qué son.
- **El coste de traducir se dice en voz alta** a quien hace números.
- **Los títulos no se traducen**: se glosan entre paréntesis en la ficha y en el catálogo.
- **Los titulares de prensa no se traducen**: son del medio.
- **"Mi hermano"**, cuando Tony habla de Ramón Eduardo Haití o de Alain Gutiérrez, es figurado: en inglés se matiza para que no parezca parentesco.
- **Leonardo Padura estaba en el jurado** que premió el Quijote de Tony en 2005. Sale de su propio texto y es el dato más citable del sitio inglés.
- **"Ala del Mar" y "bene scriptus" no se traducen.**
- **Ruso descartado**: Cinzel y Space Mono no tienen cirílico. Francés, italiano y portugués caben en las fuentes actuales, con un límite: los originales que bajamos de Google son el subconjunto `latin` y **no traen Latin Extended-A**, así que no hay `č`, `ž` ni `Ÿ`. Se vio el 23 de septiembre de 2026 al escribir «Solženicyn» en la sinopsis italiana de *Preguntas*; se dejó «Solzhenitsyn», que es la transliteración internacional y se lee igual. Ampliar el rango del recorte no sirve: hay que volver a bajar las siete fuentes con `latin-ext`. El comprobador lo caza siempre, así que no puede colarse.

**Diseño**
- **El Índice de la casa lleva un cuadradito de oro delante de cada sala.** Lo pidió Tony el 23 de septiembre de 2026, con su razón: nueve puertas seguidas y el ojo necesita ver dónde empieza cada una sin leer. Es `.indice-casa` en `styles.css`, y va solo en la portada: en los concentradores de fuera la misma lista tiene más de cien entradas, y un cuadrado por línea sería ruido.
- **El texto cumple AAA**, no solo AA. Una web casi toda navy dispara el atenuado automático de muchos monitores, y con AA el aparato se volvía negro sobre negro.
- **Los enlaces dentro de un texto van subrayados**, no solo en oro. Ver `DESIGN.md`.
- **Animaciones solo en escritorio.** En teléfono y tablet, hasta 1080 px o en cualquier pantalla sin ratón, no hay ni una: todo aparece directo. Decisión de Ernesto, 14 de septiembre de 2026: el teléfono se agiliza siempre. La consulta está en `styles.css` y en `app.js`, y tiene que ser la misma en los dos.
- **El borde de los botones (`--gold-dim`) se queda como está.** Da 2,80:1 contra el fondo, bajo el 3:1 que la WCAG 1.4.11 pide a los límites de un control, pero el texto del botón va a 12:1 y el botón se reconoce y se usa sin problema. Decisión de Ernesto, 14 de septiembre de 2026: no se vuelve a proponer.

**Mantenimiento**
- **La Person del autor vive en la portada.** `/en/author/` la lee de ahí, pero `/periodista/` lleva una copia escrita a mano: si cambia la de la portada, se actualiza también la de `/periodista/`.
- **El TXT `_github-pages-challenge-cisnerosmusic` del DNS no se borra.** Es la verificación del dominio en la cuenta `cisnerosmusic` de GitHub, hecha el 21 de septiembre de 2026: impide que otra cuenta se quede con el dominio si el sitio se despublica mientras el DNS sigue apuntando a GitHub. El DNS está en get.art. Si el sitio se muda a otro alojamiento, se puede quitar después de mover el DNS, nunca antes.
- **El meta `msvalidate.01` de la portada no se quita**: Bing revalida la propiedad periódicamente.
- **`a-texto.py` usa striprtf.** Hubo un parser propio y se comía texto. Para textos del autor no se improvisa un conversor, y el resultado se compara con el original antes de publicar.
- **Y repara los acentos que salen en griego.** Algunos RTF declaran cp1252 pero traen tipografías con juego de caracteres griego, y los escapes se resuelven por ahí: en el trabajo de la Orquesta Aragón, «cumpleaños» salía «cumpleaρos». El byte es correcto y solo está leído con la tabla equivocada, así que `sin_griego()` lo vuelve a codificar en cp1253 y lo lee en cp1252. Si el texto no trae letras griegas, esa función no toca nada.
- **`/novelas/` y `/poeta/` son redirecciones blandas**, con `meta refresh`, `noindex` y canonical, porque GitHub Pages no permite un 301 real.

## Material que llega del autor

Tony usa el nombre del archivo como contexto: la fecha, el lugar, quién estaba y a veces un recado. **Ese nombre es dato, no ruido**, y a menudo es la única fuente de la fecha o del nombre propio que va en el pie de foto. Léelo antes de renombrar nada.

Eso produce rutas larguísimas, y ahí aparece el problema: **el explorador de Windows corta en 260 caracteres y salta esos archivos sin avisar**. El 8 de septiembre de 2026, un zip de 65 archivos se extrajo con 8 perdidos por esta razón, con rutas de 199 a 253 caracteres, y entre ellos estaba la presentación en la Biblioteca Nacional. Dentro del zip estaban intactos.

Procedimiento fijado con Ernesto: **el zip se entrega sin extraer y lo abre el asistente.** Python no tiene ese límite. Se listan las entradas, se extraen con nombre corto y el nombre largo original se guarda junto a ellas en un `NOMBRES ORIGINALES.json`, para no perder el contexto.

Dos trampas al leer esos zips:

- Si el zip no lleva la marca de UTF-8, Python ya decodifica los nombres con cp437 y **salen bien**. No los "recuperes" reconvirtiéndolos: eso los rompe. Compruébalo mirando si los acentos se ven correctos antes de tocar nada.
- La consola de Windows destroza los acentos al imprimir. Un nombre que se ve mal en pantalla puede estar perfecto en disco. Para comparar contra el disco, normaliza y compara por tamaño, no por cómo se imprime.

Y una regla de contenido que salió de aquí: **en los pies de foto no se atribuyen caras.** Se nombra a quien la nota del autor dice que estaba y se describe el acto, pero no se afirma quién es quién en la imagen si no lo ha dicho él.

## Una pieza que pertenece a dos salas

Pasa a menudo y va a seguir pasando. Un poema leído por el autor pertenece a la vez a **Plano abierto**, por el acto que lo generó, y a **En mi voz**, porque está en su voz. Tony planteó lo mismo para los cuentos: uno que salga en un libro y además en la sección de cuentos.

La regla, decidida con Ernesto el 8 de septiembre de 2026:

> **El reproductor, o el texto, se repite donde haga falta. La ficha larga y el marcado de datos NO se repiten: viven en la sala canónica, y la otra remite a ella con una línea corta.**

No es contenido duplicado: el archivo tiene una sola URL, y la página que lo rodea es distinta en cada sala. Lo que sí haría daño es declarar dos veces el mismo `AudioObject` o repetir la descripción larga, porque parte la señal entre dos URLs.

Y sobre todo, **el dato vive una sola vez**. La fuente es `herramientas/grabaciones.json`: cada grabación con su título, su ficha larga, su frase corta, su sala canónica y la lista de salas donde aparece. `herramientas/gen-audios.py` la reparte en las salas españolas. En los idiomas de fuera las pinta `gen-idioma.py`, leyendo el mismo `grabaciones.json` y su capa `grabaciones.<idioma>.json`, que trae solo los textos: el título, solo cuando es descriptivo, porque el de un poema no se traduce.

Cada página marca su región así, y **todo lo que hay dentro lo escribe el script**:

```html
<!-- grabaciones: en-mi-voz -->
  <!-- /grabaciones -->
```

Fuera de los marcadores no se toca nada, así que el resto de la página se sigue editando a mano. Correr el generador dos veces no cambia nada, está comprobado. Si corriges una fecha, se corrige en el JSON y aparece bien en las dos salas a la vez: es justamente lo que evita que deriven.

Cuando toque resolver los cuentos, se hace igual, con su propio manifiesto.

## Cada máquina

**Dependencias.** Los generadores y el comprobador necesitan Python 3 y `pip install Pillow fonttools brotli`, las mismas que instala GitHub Actions. Sin `fonttools`, el comprobador revienta en la regla de las fuentes: le pasó a la Máquina 2 el 21 de septiembre de 2026.

**Fin de línea.** `.gitattributes` fija LF para todo el texto del repositorio en las dos máquinas. Antes, en la Máquina 2 (Windows, `core.autocrlf=true`), cada regeneración dejaba una veintena de HTML marcados como modificados sin un solo cambio de contenido, y eso engaña a quien verifica con `git status`.

### Git

No hay identidad de git global configurada, y es a propósito: Ernesto mantiene dos identidades separadas, la personal y artística y la de Index01. Una global las mezclaría sin avisar en cualquier repo nuevo.

Así que un clon nuevo falla el primer commit con "Author identity unknown". Es un fallo sano, no una avería. Se configura por repositorio, copiando la que domine el historial:

```bash
git log --format='%an <%ae>' | sort | uniq -c | sort -rn
git config --local user.name "..."
git config --local user.email "..."
```

En este repositorio la identidad del historial es la personal.

**Al empujar con un token, desactiva antes el ayudante de credenciales.** `git -c credential.helper='!f() { ... }; f' push` **añade** el ayudante a los que ya hay, no los sustituye: el Git Credential Manager de Windows se consulta igual y se queda esperando una ventana que en una sesión de agente nadie va a ver. El push no falla, se cuelga, que es peor. Pasó el 25 de septiembre de 2026 subiendo las once décimas nuevas. La forma que sí funciona lleva un valor vacío delante, que vacía la lista:

```bash
git -c credential.helper= -c credential.helper='!f() { echo username=x-access-token; echo "password=$GH_TOKEN"; }; f' push origin main
```

El token sale de `~/.secrets` o de `$GH_TOKEN`, nunca escrito en el comando. Si aun así se queda colgado, el proceso a matar es `git-credential-manager`.
