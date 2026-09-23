# Pendientes · Ala del Mar

Lo que queda por hacer, y nada más.

- **Lo hecho no se apunta aquí**: está en el historial de git, y el mensaje de cada commit explica el porqué.
- **Las decisiones que no hay que deshacer** están en `AGENTS.md`.
- **Cuando algo se termina, se borra de esta lista en el mismo commit que lo cierra.**

## 1. Terminar los cinco idiomas

De las 257 páginas indexables, 234 tienen pareja de idioma. Las 23 que no la tienen son el archivo de prensa (22) y el Directorio, las dos por decisión y no por olvido:

1. **Directorio.** Fuera del español sería redundante: cada concentrador (`/en/author/` y sus tres hermanos) tiene su bloque de contacto, y el aviso de derechos de cada idioma cubre lo demás. Propuesta pendiente de Ernesto: no hacerla.
2. **El archivo de prensa.** Los veintidós trabajos solo tienen página española, y ahí seguirán mientras los textos no se traduzcan. Lo que sí está traducido es su aparato: los cuatro concentradores listan los veintidós con su medio, su fecha y una línea que dice de qué va cada uno, y enlazan la página española marcada como tal. Las capas son `herramientas/periodismo.<idioma>.json`, así que el día que se quieran veintidós páginas en otro idioma el texto ya está escrito.

## 2. Espera la palabra de Tony

1. **El título del poema del Farraluque.** Su mensaje decía *Tres desnudos y un delirio*; su manuscrito dice *Tres delirios y un desnudo*, y así está publicado.
2. **`Revelaciones` es un solo párrafo** de 15.400 caracteres, tal como está en el .docx. Si quiere puntos y aparte, los pone él.
3. **"Estación La Gaveta"**: si es el nombre de toda la sección o solo de la sala. Hoy es la sala, dentro de `/ineditos/`. Renombrar la sección toca menú, pie y sitemap en todo el sitio.
4. **Las dos obras del Farraluque**: si las quiere también en Tinta-ciones y en Contarte, además de en Laureles.
5. **Tres libros suyos en proceso editorial, nombrados en el sitio y sin sitio propio**: *Oleaje de pianos* y *El color de las decisiones*, que salen en la procedencia de dos cuentos de Contarte, y *Son de la trova*, ensayos y entrevistas con Letras Cubanas, que sale al pie de un trabajo de prensa. No son inéditos, porque ya tienen editorial, ni libros publicados. Hace falta saber si quiere que se anuncien, y dónde: una sala nueva, una línea en Mis libros o nada hasta que salgan.
6. **Dónde salieron nueve trabajos de prensa.** El nombre del archivo trae el medio en trece de los veintidós; en estos nueve no, y se publican solo con su fecha: *Locuras de pincel* (jun 2014), *¿El verde de la desesperanza?* (ago 2014), *Para sonar en buen cubano*, *A velo descubierto las palabras* (jun 2014), *Una historia de un siglo* (mar 2014), *Una isla de crimen y enigma* (jun 2014), *¡Salud, maestro H. Zumbado!* (may 2013), *Sonando la lira y el bongó* (may 2013) y *De historias, nombres y apellidos*. Hace falta que Tony diga de dónde son. **El que resulte ser de material reservado se retira**: ver la regla en `AGENTS.md`.
7. **El corte de *Aviso***, del concierto de Rita del Prado: pidió dejar solo desde donde él dice «esto se llama aviso». Hay dos cortes candidatos esperando que los escuche.
8. **Extensión y edad recomendada de cada título.** Es lo primero que pregunta una editorial extranjera, y no se puede inventar.
9. **Ojos de bruja**: relato por entregas publicado en Cubaliteraria en julio de 2020, con siete partes vivas (`/ojos-de-bruja-i/` a `/ojos-de-bruja-vi/` y `/ojos-de-bruja-vii-y-final/`). Si él lo quiere, Contarte es su sitio.
10. **Material nuevo, cuando haya corriente en Alamar**:
   - más cuentos para Contarte, que ya son once;
   - más De-Cimitas: dijo tener «cientos», van veinte;
   - prensa de los nueve libros que no la tienen: *La canción de la Nueva Trova*, *Trovadoras*, *Trampas retratos y un 17 rojo*, *De la extraña aventura de Don Quijote*, *Perdidos en un librero*, *En un lugar de Cuba*, *Nota de prensa y otros minicuentos*, *Vamos a cantar y a soñar* y *Cuentos de muñecas*;
   - fotos de presentaciones;
   - la foto de escritor oficial, si hace la sesión.
11. **Tres trabajos del zip de prensa se quedaron fuera**, por la regla de material reservado de `AGENTS.md`: si quiere que salgan, que lo diga él. (La lista de cambios que anunció para la ficha de redacción de El periodista la dio Ernesto por cerrada el 23 de septiembre de 2026.)
13. **El casete del programa de Radio Ciudad.** Tony lo tiene y puede digitalizarlo, pero se grabó en una grabadora de pilas y va ligeramente fuera de revoluciones, así que el archivo saldrá desafinado y lento o rápido. **Se puede arreglar después**: corregir la velocidad sin cambiar el tono es cosa de un minuto en el estudio, y si hace falta se limpia el ruido de cinta. Que lo pase cuando tenga corriente y luz; no corre prisa y la página sale igual sin él.
12. **Los segundos fragmentos de Valnúss**: cada tomo lleva uno, como pidió. El segundo de cada tomo está en su material (`OneDrive/Imágenes/tony/x/(2015) El Escudo de Valnúss/`, archivos 016, 026, 039, 042 y 059) por si los quiere.

## 3. Espera la decisión de Ernesto

- ***Cuentos de muñecas*** es el único libro cuyo primer bloque no se llama Sinopsis sino «Sobre el libro», porque es un volumen colectivo y su nota explica la compilación. Si se prefiere uniformidad total, se cambia.
- **El largo de los concentradores.** Medido en el navegador el 23 de septiembre de 2026: `/en/author/` mide 13.911 píxeles, con 109 piezas listadas una a una más la hoja de servicios, y los otros tres son iguales. Como índice funciona. **Cuidado con el atajo que parecía obvio**: dejar los veinte poemas y las veinte décimas como un enlace a su sala solo quita 2.184 píxeles, un 16%, no la mitad; el bloque más alto es el periodismo, con 3.030, y le siguen los libros (1.956), la hoja de servicios (1.813) y los cuentos (1.539). Cualquier recorte se decide contra esas cifras. Se cambiaría quitando secciones `obras` de cada `zona.<idioma>.json`, sin tocar `gen-idioma.py`, y hay que hacerlo en los cuatro idiomas o divergen.
- **El botón de Mis libros, solo, en la portada.** A Tony le hace «un poco de ruido» verlo suelto en el móvil, aunque entiende la intención, y lo dijo como comentario, no como petición. Son dos botones, *Mis libros* y *Escribir al autor*, que en pantalla ancha van uno al lado del otro y en el móvil se parten en dos líneas. Tres salidas: dejarlo, poner los dos del mismo ancho para que se lean como pareja, o dejar solo el primero. Decide Ernesto.
- **Dos campos más en la ficha de cada libro**, que pide un editor extranjero: derechos ya vendidos, además de los disponibles, y si existe muestra traducida.
- **DMARC: puesto el 21 de septiembre de 2026, falta la revisión.** `_dmarc.antoniolopezsanchez.art` ya existe con `v=DMARC1; p=none; rua=mailto:ernestocisnerosmusic@gmail.com`, comprobado en los resolutores 8.8.8.8 y 1.1.1.1. Pendiente: a las 3 o 4 semanas, revisar los informes (llegan como zip al correo de `rua`) y decidir si sube de nivel. **No subir a `quarantine` ni a `reject`** sin esa revisión: el correo del dominio pasa por el reenvío de ImprovMX y el SPF solo autoriza a ImprovMX, así que un envío desde Gmail con la dirección del dominio fallaría. Referencia: ernestocisneros.art pasó a `p=quarantine` el mismo día, tras cinco semanas de informes sin un fallo.
- **Validar en Search Console la corrección de `mainEntity`**, si no se hizo. El arreglo está en vivo desde el 11 de septiembre de 2026 (los dos `ProfilePage` llevan la persona dentro); falta pulsar *Validar corrección* en el informe de Página de perfil para que Google lo dé por cerrado.
- **CAA, opcional.** Un registro CAA que solo autorice a `letsencrypt.org`, que es quien emite el certificado de GitHub Pages, impide que otra autoridad emita uno para el dominio. A cambio, si GitHub cambia de autoridad, la renovación falla hasta que se actualice el registro. Ganancia pequeña: se puede dejar.
- **Formulario de consultas de derechos con Formspree**, en lugar del correo: daría historial de consultas y filtro de spam, a cambio de un servicio de terceros, que el sitio hoy no tiene. Recomendación: no, mientras el correo `derechos@` baste.

## 4. Técnico

- **El selector de idiomas, con los cinco ya puestos.** El menú español lleva cuatro siglas detrás de la línea vertical, y cada menú extranjero, otras cuatro. Medido en el navegador el 23 de septiembre de 2026: la barra española pide 1123px y a 1441 deja 85px de margen sobre el logotipo; a 1600 deja 244, y entre 1081 y 1440 se aprieta a 874. **Cabe, pero un sexto idioma ya no cabría a 1441.** Queda decidir si se convierte en un desplegable y en qué orden van las siglas. Y el pie español sigue sin enlazar idiomas mientras los cuatro de fuera sí: hay que decidir si se igualan.
- **Solo existe la página inglesa de representación literaria** en `ernestocisneros-site`. El francés, el italiano y el portugués apuntan de momento a ella desde `idiomas.json`. Es un enlace correcto, pero no está en el idioma de quien lee.
- **Las fuentes originales son el subconjunto `latin` de Google y no traen Latin Extended-A.** Faltan `č`, `ž` y `Ÿ`. Se vio con «Solženicyn» en la sinopsis italiana de *Preguntas*, que quedó como «Solzhenitsyn», la transliteración internacional. **Ampliar el rango de `subset-fuentes.py` no basta**, porque el glifo no está en el original: hay que volver a bajar las siete fuentes desde Google con `latin-ext` y volver a recortar. Coste medido ese día: el rango entero de Latin Extended-A añade unos 250 bytes al total de las siete. El comprobador falla siempre que un carácter del sitio no exista en una fuente servida, así que nada puede colarse mientras tanto.
- **El rendimiento está en 100, y conviene saber por qué para no estropearlo.** PageSpeed móvil sobre la portada en vivo, 23 de septiembre de 2026 a las 8:22: **rendimiento 100, accesibilidad 100, recomendaciones 100, SEO 100** y navegación con agentes 3/3, con FCP 1,2 s, **LCP 1,5 s**, TBT 0 ms, CLS 0 y **Speed Index 2,4 s**. Todo verde. En escritorio, 100 en rendimiento con Speed Index 0,5 s.

  Tres horas antes, en la misma página, era rendimiento 98 y Speed Index 3,9 s. Lo que cambió en medio fue sacar la cursiva completa de la precarga de la portada y poner en su lugar `lema.woff2`, la misma cursiva recortada a los once glifos de *bene scriptus*: de 28,7 KB a 2,8. Está en el historial de git.

  **La lección, porque la predicción falló.** Se dijo aquí que el Speed Index lo causaba el repintado de `cormorant-garamond-400` al llegar a 2.523 ms, y que aliviar la congestión mejoraría el LCP pero apenas el Speed Index. Se equivocó: el Speed Index bajó 1,5 s. En una portada donde el retrato ocupa casi toda la primera pantalla del móvil, **lo que manda en el Speed Index es cuándo se pinta esa imagen**, no los repintados de texto posteriores. Descongestionar el tubo adelantó la imagen y arrastró toda la curva. Medido antes y después con Chrome a 412x823, Slow 4G y CPU al 25%: la descarga del retrato pasó de **1.193 ms a 1.049-1.066 ms** en tres pasadas, y lo que compite con él a los 640 ms, de 94,9 KB a 70,2 KB.

  **Lo que queda abierto, en orden de valor:**

  1. **El retrato con `srcset`.** Sigue sirviéndose el mismo archivo de 1080 px a todos los dispositivos, y el móvil necesita 721 px reales. Medido: a 760 px pesa **15,9 KB en vez de 26,2**, un 39% menos sobre el recurso que es el LCP. Exige pasar el `<div class="split-image">` con imagen de fondo a un `<img>` con `object-fit: cover`, que toca la portada española y `portada_hero()` de `gen-idioma.py`. El `aria-label` del div tendría que volverse el `alt` de la imagen, y el texto ya está listo para eso: vive en `retrato_alt` de cada zona.
  2. **Fundir `fonts.css` dentro de `styles.css`.** Dos hojas bloquean el pintado en todas las páginas, y ninguna fuente sin precargar se descubre hasta que llega la primera: `fonts.css` sola tardaba 1.266 ms. Fundirlas quita una petición bloqueante por página y deja la cadena en dos niveles en vez de tres. A cambio toca los nueve generadores que escriben la cabecera y las páginas escritas a mano.
  3. **Precargar `cormorant-garamond-400.woff2` ya no parece buena idea**, y se deja escrito para que nadie la recupere sin pensarlo: son 27,2 KB, casi exactamente el hueco que se acaba de liberar. Volvería a meter en la carrera del retrato lo que se sacó, a cambio de adelantar un repintado de texto que, según lo que acabamos de aprender, pesa poco en el Speed Index. El hueco se queda libre.

  **Contra qué se compara de ahora en adelante:** rendimiento 100, LCP 1,5 s y Speed Index 2,4 s en móvil. Cualquier cambio tiene que mejorar más que el ruido entre pasadas, que es de unos 50 ms, y no puede bajar de 100 ninguna de las cuatro cifras.

  **Ojo con una explicación que no se sostiene**: el comentario de `index.html` dice que poner la precarga del retrato la primera le ahorró 485 ms. En los rastreos de hoy el retrato se pide a los 611-640 ms, a la vez que las dos hojas de estilo, porque en esta red el documento entero llega de golpe: reordenar precargas dentro del `<head>` no compra nada aquí. Lo que cuesta es el salto de más.

- **La prensa de Juventud Rebelde es frágil.** Las tres entrevistas enlazadas (2012, 2016 y 2019) respondieron de forma intermitente el 21 de septiembre de 2026: dos no cargaban, la portada del diario tampoco, y la tercera sí. Solo la de 2016 tiene copia en el Internet Archive. Si el diario cae como cayó Habana Radio, se pierden dos de las tres. Hay que guardarlas en el Archive (`web.archive.org/save/`) en cuanto respondan y, si caen, enlazar la copia. Es mandar URLs públicas a un servicio de terceros: lo decide Ernesto.

- **Servir desde Cloudflare y hacer privado el repositorio. Decidido por Ernesto el 23 de septiembre de 2026; no es para hoy.** Deja de ser una opción y pasa a ser el próximo paso. Tres cosas distintas se resuelven con la misma mudanza, y por eso vale la pena hacerla entera y una sola vez:

  1. **El historial público de git sigue nombrando el material que no se publica.** El 21 de septiembre la lista salió de `AGENTS.md`, el 23 salió de los documentos la deducción que llevaba a ella, y el dominio no sirve nada de eso (404 comprobado en `/AGENTS.md`, `/PENDIENTES.md`, `/herramientas/` y `/.impeccable/`). Pero el historial lo conserva, y al menos un mensaje de commit del 8 de septiembre lo nombra en el propio título. **Quitarlo del presente no lo quita del pasado**, y ahí no se llega con un commit.
  2. **Cabeceras.** GitHub Pages solo manda `Content-Type` y `Cache-Control: max-age=600`, y no deja añadir ninguna. Detrás de Cloudflare se pueden poner las que pidió la auditoría del 23 de septiembre: `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin` y una caché larga de verdad para `fonts/` e `img/`, que hoy caducan en diez minutos. **Ojo con dos**: la CSP tendrá que admitir el `style` en línea del retrato en la portada y el `script` en línea del 404, o los rompe; y `interest-cohort` no hace falta, es de una función que Google retiró en 2022.
  3. **Compresión.** GitHub Pages no sirve brotli: se pidió `Accept-Encoding: br` el 23 de septiembre y devolvió gzip. `styles.css` viaja en 9,9 KB comprimido; con brotli bajaría sin tocar una línea del código, que es más de lo que daría minificarlo.

  **Dos trampas, en este orden.** Primero Cloudflare sirviendo y el DNS apuntando allí, y **solo después** el repositorio privado, o la web se cae en medio. Y `_config.yml` solo lo entiende GitHub: en Cloudflare hay que acotar la publicación por otra vía, o volverían a servirse los documentos y `herramientas/`. Queda por decidir con qué cuenta de Cloudflare y cómo se le da acceso a la instancia evaluadora.

  La alternativa, reescribir el historial y forzar el push, se descarta: es irreversible, obliga a reclonar en las dos máquinas y no borra las copias que otros ya tengan.

## 5. Fuera de este repositorio

- **`ernestocisneros-site`**: en la página inglesa de representación, poner la trova delante en la frase de géneros, que hoy abre con la fantasía.
- **Backlinks de autoridad**, que es lo que más moverá el posicionamiento: que EcuRed enlace el sitio, que Tony lo publique en su Facebook y que aparezca en las páginas de sus editoriales.
