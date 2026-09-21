# Pendientes · Ala del Mar

Lo que queda por hacer, y nada más.

- **Lo hecho no se apunta aquí**: está en el historial de git, y el mensaje de cada commit explica el porqué.
- **Las decisiones que no hay que deshacer** están en `AGENTS.md`.
- **Cuando algo se termina, se borra de esta lista en el mismo commit que lo cierra.**

## 1. Terminar el inglés

Todas las salas tienen ya su versión inglesa salvo dos, por decisión y no por olvido:

1. **Directorio.** En inglés sería redundante: `/en/author/` tiene su bloque de contacto y `/en/rights/` cubre los derechos. Propuesta pendiente de Ernesto: no hacerla.
2. **El periodista.** Su pareja inglesa es `/en/author/`, que resume la trayectoria y enlaza la ficha española completa. Se revisa cuando llegue la lista de cambios de Tony para esa página.

Cuando esté, se mide el rendimiento y se publican las cifras. Antes no: ver `AGENTS.md`.

## 2. Espera la palabra de Tony

1. **El título del poema del Farraluque.** Su mensaje decía *Tres desnudos y un delirio*; su manuscrito dice *Tres delirios y un desnudo*, y así está publicado.
2. **`Revelaciones` es un solo párrafo** de 15.400 caracteres, tal como está en el .docx. Si quiere puntos y aparte, los pone él.
3. **"Estación La Gaveta"**: si es el nombre de toda la sección o solo de la sala. Hoy es la sala, dentro de `/ineditos/`. Renombrar la sección toca menú, pie y sitemap en todo el sitio.
4. **Las dos obras del Farraluque**: si las quiere también en Tinta-ciones y en Contarte, además de en Laureles.
5. **Dos cuentos retenidos**, *Cantar el cuento III* y *La urna del tío*: los marcó como parte de libros en proceso editorial.
6. **El corte de *Aviso***, del concierto de Rita del Prado: pidió dejar solo desde donde él dice «esto se llama aviso». Hay dos cortes candidatos esperando que los escuche.
7. **Extensión y edad recomendada de cada título.** Es lo primero que pregunta una editorial extranjera, y no se puede inventar.
8. **Ojos de bruja**: relato por entregas publicado en Cubaliteraria en julio de 2020, con siete partes vivas (`/ojos-de-bruja-i/` a `/ojos-de-bruja-vi/` y `/ojos-de-bruja-vii-y-final/`). Si él lo quiere, Contarte es su sitio.
9. **Material nuevo, cuando haya corriente en Alamar**:
   - cuatro cuentos más para Contarte;
   - más De-Cimitas: dijo tener «cientos» y llegaron ocho fotos;
   - las sinopsis oficiales de los libros que aún tienen texto provisional;
   - prensa de los diez libros que no la tienen;
   - fotos de presentaciones;
   - la foto de escritor oficial, si hace la sesión.
10. **Inéditos**: entraron las cuatro novelas que mandó. Si quiere enseñar también algo de sus poemarios y libros de cuentos inéditos, falta que lo mande.
12. **El periodista**: anunció una lista de cambios («hay que hacerle mil cosas») y los trabajos periodísticos que quiere enseñar. Se espera la lista antes de tocar la página.
13. **Los segundos fragmentos de Valnúss**: cada tomo lleva uno, como pidió. El segundo de cada tomo está en su material (`OneDrive/Imágenes/tony/x/(2015) El Escudo de Valnúss/`, archivos 016, 026, 039, 042 y 059) por si los quiere.
11. **Erratas dudosas en los Inéditos**, que no se tocaron por si son a propósito: en *Mis diarios de cama*, el archivo de la entrada 8 dice «20 de septiembre de 2004» y el texto «18» (se publicó el 18), y «María con la mala noticia de su mamá al final murió», donde parece faltar un «de que»; en *Preguntas*, «un tangente homenaje» y «desde las páginas de novela»; en *Palabras*, «A esas respuestas [...] se intentó responder», donde quizá quiso decir «preguntas».

## 3. Espera la decisión de Ernesto

- ***Cuentos de muñecas*** es el único libro cuyo primer bloque no se llama Sinopsis sino «Sobre el libro», porque es un volumen colectivo y su nota explica la compilación. Si se prefiere uniformidad total, se cambia.

- **Dos campos más en la ficha de cada libro**, que pide un editor extranjero: derechos ya vendidos, además de los disponibles, y si existe muestra traducida.
- **DMARC para el correo del dominio.** `derechos@` es la dirección a la que escriben los editores, y el dominio no tiene DMARC (`_dmarc.antoniolopezsanchez.art` no existe, comprobado el 21 de septiembre de 2026). Sin él es más fácil falsificar un correo que parezca salir de `derechos@`. En get.art, un TXT en `_dmarc` con `v=DMARC1; p=none;` para empezar a vigilar sin romper nada. **No subir a `quarantine` ni a `reject`** hasta confirmar desde qué servicio se envía de verdad con esas direcciones: el SPF actual solo autoriza a ImprovMX, así que un envío desde Gmail con la dirección del dominio fallaría y acabaría en spam.
- **CAA, opcional.** Un registro CAA que solo autorice a `letsencrypt.org`, que es quien emite el certificado de GitHub Pages, impide que otra autoridad emita uno para el dominio. A cambio, si GitHub cambia de autoridad, la renovación falla hasta que se actualice el registro. Ganancia pequeña: se puede dejar.
- **El historial público de git sigue nombrando el material que no se publica.** El 21 de septiembre de 2026 la lista salió de `AGENTS.md` y de `.impeccable/design.json`, y el dominio dejó de servir los documentos, pero el historial la conserva, y al menos un mensaje de commit del 8 de septiembre la nombra en el propio título, visible en GitHub para cualquiera. Quitarla del presente no la quita del pasado. Dos salidas: **repositorio privado y publicar con Cloudflare Pages**, como Index01 desde el 25 de agosto (lo más limpio; hay que decidir con qué cuenta de Cloudflare y dar acceso a la instancia evaluadora), o **reescribir el historial y forzar el push**, que es irreversible, obliga a reclonar en las dos máquinas y no borra las copias que otros ya tengan. Recomendación: la primera.
- **Formulario de consultas de derechos con Formspree**, en lugar del correo: daría historial de consultas y filtro de spam, a cambio de un servicio de terceros, que el sitio hoy no tiene. Recomendación: no, mientras el correo `derechos@` baste.

## 4. Técnico

- **Francés, italiano y portugués**, después del inglés. El procedimiento está en el README, sección Idiomas.
- **Fundir `fonts.css` dentro de `styles.css`.** Hoy son dos hojas que bloquean el pintado en todas las páginas, y las fuentes no se descubren hasta que llega la primera. Es una hoja menos por página para siempre; a cambio toca los once generadores y las páginas escritas a mano. Medido el 20 de septiembre de 2026, después de recortar las fuentes: FCP 1.057 ms y LCP 1.507 ms de mediana en tres pasadas de Lighthouse móvil sobre el sitio vivo. Cualquier cambio se compara contra esas cifras, y hace falta que mejore más que el ruido entre pasadas, que es de unos 50 ms.

- **La prensa de Juventud Rebelde es frágil.** Las tres entrevistas enlazadas (2012, 2016 y 2019) respondieron de forma intermitente el 21 de septiembre de 2026: dos no cargaban, la portada del diario tampoco, y la tercera sí. Solo la de 2016 tiene copia en el Internet Archive. Si el diario cae como cayó Habana Radio, se pierden dos de las tres. Hay que guardarlas en el Archive (`web.archive.org/save/`) en cuanto respondan y, si caen, enlazar la copia. Es mandar URLs públicas a un servicio de terceros: lo decide Ernesto.
- **`.impeccable/design.json` describe el diseño abandonado**: mesa y papel, añil, Bonum y Courier Prime. Es el registro que hizo la herramienta `impeccable` sobre el DESIGN.md viejo el 6 de septiembre, y nadie lo regeneró cuando se reescribió. Si alguien vuelve a usar esa herramienta, hará cumplir el mundo que se descartó, igual que casi pasó con el DESIGN.md. Regenerarlo desde el DESIGN.md actual, o borrarlo si la herramienta ya no se usa.

## 5. Fuera de este repositorio

- **`ernestocisneros-site`**: en la página inglesa de representación, poner la trova delante en la frase de géneros, que hoy abre con la fantasía.
- **Backlinks de autoridad**, que es lo que más moverá el posicionamiento: que EcuRed enlace el sitio, que Tony lo publique en su Facebook y que aparezca en las páginas de sus editoriales.
