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

Comprueba hoy enlaces rotos, sitemap contra páginas indexables y **sitemap al día**, JSON-LD válido, con tipos que existan de verdad y, en las páginas de perfil, con la persona dentro (`mainEntity`, que Google exige), títulos y descripciones únicos y en rango, una sola versión de CSS y JS, rutas absolutas de una máquina concreta, raya larga en texto público, imágenes sin `alt` y **con medidas que no son las del archivo**, `target="_blank"` sin `noopener`, el menú y su script, la navegación alineada, y que los generadores sigan reproduciendo su HTML. Sale con código 1 si algo falla, y **corre solo en cada push** con GitHub Actions (`.github/workflows/comprobar.yml`): si la marca sale en rojo, alguien dejó una regla rota.

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
- **Hay material del autor que existe y que, por decisión suya y de Ernesto, no se publica.** Esta lista se respeta y no se revisa sin preguntarles a ellos dos. Hoy son dos entradas y puede crecer:
  - Su columna en **Palabra Nueva**. No se menciona en el sitio.
  - El minicuento **Proclama Real**. En Laureles se queda la mención del premio, que ya está en su currículo público; el texto no entra en este repositorio.

  **Este archivo es público**, así que aquí va la lista y no los motivos. El porqué de cada caso se habla con Ernesto; escribirlo aquí sería publicar por la puerta de atrás justo lo que se decidió no publicar.

  La regla general: **si un material toca lo político, lo militar o lo religioso, se para y se pregunta antes de subirlo.** Ni el asistente ni Ernesto, desde Miami, pueden medir lo que arriesga el autor allí. Ante la duda, se retira y se consulta.
- **Las obras inéditas de Tony no entran en este repositorio, que es público.** Solo sinopsis y fragmentos que él elija. Publicarlas les quitaría la condición de inéditas ante concursos y editoriales.
- **El mecanismo de cobro, la custodia de fondos y cualquier detalle fiscal o contractual de la representación no se documentan aquí.** Van en la documentación privada del estudio.
- **Las páginas de libro no se maquetan a mano**: se generan con `herramientas/gen-libro.py` desde su manifiesto.
- **Toda gestión de derechos fuera de Cuba va a dos destinos y ningún otro**, en cualquier idioma: la página de representación de Ernesto Cisneros y `derechos@antoniolopezsanchez.art`. El correo vive en `DERECHOS_EMAIL`, en `gen-libro.py`; la página de representación, en el idioma de quien lee, en `herramientas/idiomas.json`.
- **Los colores de texto son sólidos, sin alfa.** Es lo que rompió el contraste una vez. Ver `DESIGN.md`.
- **El sitemap tampoco se edita a mano**: lo escribe `herramientas/gen-sitemap.py` desde las páginas y la historia de git, y el comprobador falla si no está al día.
- Al cambiar `styles.css`, `fonts.css` o `app.js`, se sube su `?v=N` con `python herramientas/version.py <recurso> <número>`, que lo cambia a la vez en todas las páginas y en todos los generadores.
- **Sin cifras de rendimiento publicadas mientras el sitio siga en construcción.** Decisión de Ernesto, 12 de septiembre de 2026: se mide y se publica al terminar la versión inglesa, no antes. Ni en el README ni en ningún otro documento.

## Decisiones que no se deshacen

No son tareas, así que no viven en `PENDIENTES.md`. Son decisiones tomadas, casi todas con Tony o con Ernesto, que alguien podría "arreglar" de buena fe dentro de un mes. Si una te parece un error, pregunta antes de tocarla.

**Derechos**
- **Solo se ofrece la obra de Antonio.** En los cinco volúmenes colectivos, la frase de la ficha cambia sola, porque se detecta por el campo `autoría`, y la lista de colectivos de `/derechos/` se lee de ese mismo campo: catálogo y aviso legal no pueden contradecirse. Decisión de Ernesto, 9 de septiembre de 2026.
- **La zona inglesa enlaza la página inglesa de representación**: el mismo destino, en el idioma de quien lee.
- **El dossier de derechos no se duplica aquí.** El sitio de Tony es la casa y el catálogo; el de Ernesto, el negocio.
- **El aviso de derechos es una declaración clara, no asesoría legal.** Antes de firmar una cesión, abogado.

**Contenido**
- **Las tres fechas de *Proclama Real* no son una errata**: escrita en 2009, concurso El Dinosaurio 2013, fallo dado a conocer en 2014. Ya se "corrigió" una vez por error y hubo que revertirlo.
- **Los títulos de poema van escritos a mano en el manifiesto.** En los originales vienen en mayúsculas, y bajarlos por programa rompe los nombres propios y confunde el nombre de la serie con el del poema.
- **La lista de versos ajenos** del `LICENSE` y de `/derechos/` se revisa cada vez que entra un texto con epígrafe.
- **Las dos obras del Farraluque viven en Laureles**, no en Tinta-ciones ni en Contarte: son literatura erótica adulta, y Contarte tiene cuentos infantiles en una rejilla que se baraja cada día. Llevan `<meta name="rating" content="adult">`, `isFamilyFriendly: false` y un aviso visible antes del texto.
- **Inéditos vacía está bien.** No se rellena con relleno.
- **El bloque de Prensa es de piezas firmadas en medios identificables.** Por eso se descartaron el 8 de septiembre un vídeo de booktuber sobre *Las guerreras de la luz* y una reseña de *Grimorium* en un blog que ya no existe.
- **Habana Radio está caída entera**: sus reseñas y programas se enlazan en la copia del Internet Archive.
- **Los diplomas del Farraluque no se publican como imagen**, porque eran fotos de folios. Sus datos están como texto en Laureles.

**Inglés y demás idiomas**
- **El orden inglés es otro: trova, poesía, narrativa.** Decisión de Ernesto, 9 de septiembre de 2026, razonada en `PRODUCT.md` y en la cabecera de `navegacion.py`.
- **La autoridad se demuestra con hechos comprobables**, no se declara con superlativos.
- **La décima y la glosa se explican**, porque un editor anglófono no sabe qué son.
- **El coste de traducir se dice en voz alta** a quien hace números.
- **Los títulos no se traducen**: se glosan entre paréntesis en la ficha y en el catálogo.
- **Los titulares de prensa no se traducen**: son del medio.
- **"Mi hermano"**, cuando Tony habla de Ramón Eduardo Haití o de Alain Gutiérrez, es figurado: en inglés se matiza para que no parezca parentesco.
- **Leonardo Padura estaba en el jurado** que premió el Quijote de Tony en 2005. Sale de su propio texto y es el dato más citable del sitio inglés.
- **"Ala del Mar" y "bene scriptus" no se traducen.**
- **Ruso descartado**: Cinzel y Space Mono no tienen cirílico. Francés, italiano y portugués caben en las fuentes actuales.

**Diseño**
- **El texto cumple AAA**, no solo AA. Una web casi toda navy dispara el atenuado automático de muchos monitores, y con AA el aparato se volvía negro sobre negro.
- **Los enlaces dentro de un texto van subrayados**, no solo en oro. Ver `DESIGN.md`.
- **Animaciones solo en escritorio.** En teléfono y tablet, hasta 1080 px o en cualquier pantalla sin ratón, no hay ni una: todo aparece directo. Decisión de Ernesto, 14 de septiembre de 2026: el teléfono se agiliza siempre. La consulta está en `styles.css` y en `app.js`, y tiene que ser la misma en los dos.
- **El borde de los botones (`--gold-dim`) se queda como está.** Da 2,80:1 contra el fondo, bajo el 3:1 que la WCAG 1.4.11 pide a los límites de un control, pero el texto del botón va a 12:1 y el botón se reconoce y se usa sin problema. Decisión de Ernesto, 14 de septiembre de 2026: no se vuelve a proponer.

**Mantenimiento**
- **La Person del autor vive en la portada.** `/en/author/` la lee de ahí, pero `/periodista/` lleva una copia escrita a mano: si cambia la de la portada, se actualiza también la de `/periodista/`.
- **El meta `msvalidate.01` de la portada no se quita**: Bing revalida la propiedad periódicamente.
- **`a-texto.py` usa striprtf.** Hubo un parser propio y se comía texto. Para textos del autor no se improvisa un conversor, y el resultado se compara con el original antes de publicar.
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

Y sobre todo, **el dato vive una sola vez**. La fuente es `herramientas/grabaciones.json`: cada grabación con su título, su ficha larga, su frase corta, su sala canónica y la lista de salas donde aparece. `herramientas/gen-audios.py` la reparte.

Cada página marca su región así, y **todo lo que hay dentro lo escribe el script**:

```html
<!-- grabaciones: en-mi-voz -->
  <!-- /grabaciones -->
```

Fuera de los marcadores no se toca nada, así que el resto de la página se sigue editando a mano. Correr el generador dos veces no cambia nada, está comprobado. Si corriges una fecha, se corrige en el JSON y aparece bien en las dos salas a la vez: es justamente lo que evita que deriven.

Cuando toque resolver los cuentos, se hace igual, con su propio manifiesto.

## Git en cada máquina

No hay identidad de git global configurada, y es a propósito: Ernesto mantiene dos identidades separadas, la personal y artística y la de Index01. Una global las mezclaría sin avisar en cualquier repo nuevo.

Así que un clon nuevo falla el primer commit con "Author identity unknown". Es un fallo sano, no una avería. Se configura por repositorio, copiando la que domine el historial:

```bash
git log --format='%an <%ae>' | sort | uniq -c | sort -rn
git config --local user.name "..."
git config --local user.email "..."
```

En este repositorio la identidad del historial es la personal.
