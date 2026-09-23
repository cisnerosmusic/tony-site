# Pendientes · Ala del Mar

Lo que queda por hacer, y nada más.

- **Lo hecho no se apunta aquí**: está en el historial de git, y el mensaje de cada commit explica el porqué.
- **Las decisiones que no hay que deshacer** están en `AGENTS.md`.
- **Cuando algo se termina, se borra de esta lista en el mismo commit que lo cierra.**

## 1. Terminar los cinco idiomas

De las 257 páginas indexables, 234 tienen pareja de idioma. Las 23 que no la tienen son el archivo de prensa (22) y el Directorio, las dos por decisión y no por olvido:

1. **Directorio.** Fuera del español sería redundante: cada concentrador (`/en/author/` y sus tres hermanos) tiene su bloque de contacto, y el aviso de derechos de cada idioma cubre lo demás. Propuesta pendiente de Ernesto: no hacerla.
2. **El archivo de prensa.** Los veintidós trabajos solo tienen página española, y ahí seguirán mientras los textos no se traduzcan. Lo que sí está traducido es su aparato: los cuatro concentradores listan los veintidós con su medio, su fecha y una línea que dice de qué va cada uno, y enlazan la página española marcada como tal. Las capas son `herramientas/periodismo.<idioma>.json`, así que el día que se quieran veintidós páginas en otro idioma el texto ya está escrito.

Se mide el rendimiento y se publican las cifras cuando cierre la lista de cambios de Tony para El periodista. Antes no: ver `AGENTS.md`.

## 2. Espera la palabra de Tony

1. **El título del poema del Farraluque.** Su mensaje decía *Tres desnudos y un delirio*; su manuscrito dice *Tres delirios y un desnudo*, y así está publicado.
2. **`Revelaciones` es un solo párrafo** de 15.400 caracteres, tal como está en el .docx. Si quiere puntos y aparte, los pone él.
3. **"Estación La Gaveta"**: si es el nombre de toda la sección o solo de la sala. Hoy es la sala, dentro de `/ineditos/`. Renombrar la sección toca menú, pie y sitemap en todo el sitio.
4. **Las dos obras del Farraluque**: si las quiere también en Tinta-ciones y en Contarte, además de en Laureles.
5. **Tres libros suyos en proceso editorial, nombrados en el sitio y sin sitio propio**: *Oleaje de pianos* y *El color de las decisiones*, que salen en la procedencia de dos cuentos de Contarte, y *Son de la trova*, ensayos y entrevistas con Letras Cubanas, que sale al pie de un trabajo de prensa. No son inéditos, porque ya tienen editorial, ni libros publicados. Hace falta saber si quiere que se anuncien, y dónde: una sala nueva, una línea en Mis libros o nada hasta que salgan.
6. **Dónde salieron nueve trabajos de prensa.** El nombre del archivo trae el medio en trece de los veintidós; en estos nueve no, y se publican solo con su fecha: *Locuras de pincel* (jun 2014), *¿El verde de la desesperanza?* (ago 2014), *Para sonar en buen cubano*, *A velo descubierto las palabras* (jun 2014), *Una historia de un siglo* (mar 2014), *Una isla de crimen y enigma* (jun 2014), *¡Salud, maestro H. Zumbado!* (may 2013), *Sonando la lira y el bongó* (may 2013) y *De historias, nombres y apellidos*. Ocho son reseñas de libros de 2013 y 2014, a dos o tres por mes, que es el ritmo de una columna mensual, y eso los pone cerca de una publicación que él dejó fuera de lista. **La que sea de ahí se retira.** Ver la regla de material no publicable en `AGENTS.md`.
7. **El corte de *Aviso***, del concierto de Rita del Prado: pidió dejar solo desde donde él dice «esto se llama aviso». Hay dos cortes candidatos esperando que los escuche.
8. **Extensión y edad recomendada de cada título.** Es lo primero que pregunta una editorial extranjera, y no se puede inventar.
9. **Ojos de bruja**: relato por entregas publicado en Cubaliteraria en julio de 2020, con siete partes vivas (`/ojos-de-bruja-i/` a `/ojos-de-bruja-vi/` y `/ojos-de-bruja-vii-y-final/`). Si él lo quiere, Contarte es su sitio.
10. **Material nuevo, cuando haya corriente en Alamar**:
   - más cuentos para Contarte, que ya son once;
   - más De-Cimitas: dijo tener «cientos», van veinte;
   - prensa de los nueve libros que no la tienen: *La canción de la Nueva Trova*, *Trovadoras*, *Trampas retratos y un 17 rojo*, *De la extraña aventura de Don Quijote*, *Perdidos en un librero*, *En un lugar de Cuba*, *Nota de prensa y otros minicuentos*, *Vamos a cantar y a soñar* y *Cuentos de muñecas*;
   - fotos de presentaciones;
   - la foto de escritor oficial, si hace la sesión.
11. **El periodista**: los trabajos ya llegaron y están publicados. Falta la lista de cambios que anunció para la ficha de redacción («hay que hacerle mil cosas»). Y **tres trabajos del mismo zip se quedaron fuera**, porque son de la publicación que está fuera de lista: si quiere que salgan, que lo diga él.
12. **Los segundos fragmentos de Valnúss**: cada tomo lleva uno, como pidió. El segundo de cada tomo está en su material (`OneDrive/Imágenes/tony/x/(2015) El Escudo de Valnúss/`, archivos 016, 026, 039, 042 y 059) por si los quiere.

## 3. Espera la decisión de Ernesto

- ***Cuentos de muñecas*** es el único libro cuyo primer bloque no se llama Sinopsis sino «Sobre el libro», porque es un volumen colectivo y su nota explica la compilación. Si se prefiere uniformidad total, se cambia.
- **El largo de los concentradores.** Medido en el navegador el 23 de septiembre de 2026: `/en/author/` mide 13.911 píxeles, con 109 piezas listadas una a una más la hoja de servicios, y los otros tres son iguales. Como índice funciona. **Cuidado con el atajo que parecía obvio**: dejar los veinte poemas y las veinte décimas como un enlace a su sala solo quita 2.184 píxeles, un 16%, no la mitad; el bloque más alto es el periodismo, con 3.030, y le siguen los libros (1.956), la hoja de servicios (1.813) y los cuentos (1.539). Cualquier recorte se decide contra esas cifras. Se cambiaría quitando secciones `obras` de cada `zona.<idioma>.json`, sin tocar `gen-idioma.py`, y hay que hacerlo en los cuatro idiomas o divergen.
- **Dos campos más en la ficha de cada libro**, que pide un editor extranjero: derechos ya vendidos, además de los disponibles, y si existe muestra traducida.
- **DMARC: puesto el 21 de septiembre de 2026, falta la revisión.** `_dmarc.antoniolopezsanchez.art` ya existe con `v=DMARC1; p=none; rua=mailto:ernestocisnerosmusic@gmail.com`, comprobado en los resolutores 8.8.8.8 y 1.1.1.1. Pendiente: a las 3 o 4 semanas, revisar los informes (llegan como zip al correo de `rua`) y decidir si sube de nivel. **No subir a `quarantine` ni a `reject`** sin esa revisión: el correo del dominio pasa por el reenvío de ImprovMX y el SPF solo autoriza a ImprovMX, así que un envío desde Gmail con la dirección del dominio fallaría. Referencia: ernestocisneros.art pasó a `p=quarantine` el mismo día, tras cinco semanas de informes sin un fallo.
- **Validar en Search Console la corrección de `mainEntity`**, si no se hizo. El arreglo está en vivo desde el 11 de septiembre de 2026 (los dos `ProfilePage` llevan la persona dentro); falta pulsar *Validar corrección* en el informe de Página de perfil para que Google lo dé por cerrado.
- **CAA, opcional.** Un registro CAA que solo autorice a `letsencrypt.org`, que es quien emite el certificado de GitHub Pages, impide que otra autoridad emita uno para el dominio. A cambio, si GitHub cambia de autoridad, la renovación falla hasta que se actualice el registro. Ganancia pequeña: se puede dejar.
- **El historial público de git sigue nombrando el material que no se publica.** El 21 de septiembre de 2026 la lista salió de `AGENTS.md` y de `.impeccable/design.json`, y el dominio dejó de servir los documentos, pero el historial la conserva, y al menos un mensaje de commit del 8 de septiembre la nombra en el propio título, visible en GitHub para cualquiera. Quitarla del presente no la quita del pasado. Dos salidas: **repositorio privado y publicar con Cloudflare Pages**, como Index01 desde el 25 de agosto (lo más limpio; hay que decidir con qué cuenta de Cloudflare y dar acceso a la instancia evaluadora), o **reescribir el historial y forzar el push**, que es irreversible, obliga a reclonar en las dos máquinas y no borra las copias que otros ya tengan. Recomendación: la primera. **Dos trampas si se hace**: el orden (primero Cloudflare sirviendo y el DNS apuntando allí, y solo después el repositorio privado, o la web se cae), y que `_config.yml` solo lo entiende GitHub: en Cloudflare hay que publicar solo el sitio por otra vía, o volverían a servirse los documentos y `herramientas/`.
- **Formulario de consultas de derechos con Formspree**, en lugar del correo: daría historial de consultas y filtro de spam, a cambio de un servicio de terceros, que el sitio hoy no tiene. Recomendación: no, mientras el correo `derechos@` baste.

## 4. Técnico

- **El selector de idiomas, con los cinco ya puestos.** El menú español lleva cuatro siglas detrás de la línea vertical, y cada menú extranjero, otras cuatro. Medido en el navegador el 23 de septiembre de 2026: la barra española pide 1123px y a 1441 deja 85px de margen sobre el logotipo; a 1600 deja 244, y entre 1081 y 1440 se aprieta a 874. **Cabe, pero un sexto idioma ya no cabría a 1441.** Queda decidir si se convierte en un desplegable y en qué orden van las siglas. Y el pie español sigue sin enlazar idiomas mientras los cuatro de fuera sí: hay que decidir si se igualan.
- **Solo existe la página inglesa de representación literaria** en `ernestocisneros-site`. El francés, el italiano y el portugués apuntan de momento a ella desde `idiomas.json`. Es un enlace correcto, pero no está en el idioma de quien lee.
- **Las fuentes originales son el subconjunto `latin` de Google y no traen Latin Extended-A.** Faltan `č`, `ž` y `Ÿ`. Se vio con «Solženicyn» en la sinopsis italiana de *Preguntas*, que quedó como «Solzhenitsyn», la transliteración internacional. **Ampliar el rango de `subset-fuentes.py` no basta**, porque el glifo no está en el original: hay que volver a bajar las siete fuentes desde Google con `latin-ext` y volver a recortar. Coste medido ese día: el rango entero de Latin Extended-A añade unos 250 bytes al total de las siete. El comprobador falla siempre que un carácter del sitio no exista en una fuente servida, así que nada puede colarse mientras tanto.
- **La cola de las fuentes es lo único que no está en verde.** PageSpeed móvil del 23 de septiembre de 2026 sobre la portada en vivo: rendimiento 98, accesibilidad 100, recomendaciones 100, SEO 100, navegación con agentes 3/3, FCP 1,2 s, LCP 1,7 s, TBT 0 ms, CLS 0 y **Speed Index 3,9 s**, el único naranja. Rastreado ese mismo día en frío con Chrome a 412x823, red Slow 4G y CPU al 25%, que es la receta de Lighthouse móvil, sale el porqué:

  - Nada se pide antes de los **640 ms**, que es cuando termina de llegar el HTML (13,5 KB, con 152 ms de primer byte). Ahí arrancan a la vez el retrato, `fonts.css` y `styles.css`.
  - El LCP es el retrato, a 1.851 ms: 152 de primer byte, 488 de espera, 1.193 de descarga y 18 de pintado. Concuerda con el 1,7 s del informe.
  - La cadena crítica mide **2.529 ms** y tiene tres niveles: `/` → `fonts.css?v=6` → `cormorant-garamond-400.woff2`. Las tres fuentes precargadas llegan a 1.588, 1.849 y 1.864 ms; las dos que **no** se precargan llegan a **2.340** (`space-mono-400`) y **2.523** (`cormorant-garamond-400`), porque no se pueden ni pedir hasta que `fonts.css` se descarga y se lee.
  - `cormorant-garamond-400` **sí se usa en la primera pantalla del móvil** (comprobado elemento a elemento); `space-mono-400` no. Con `font-display: swap`, cada fuente que llega repinta el texto, y eso es exactamente lo que castiga el Speed Index: la última cae 670 ms después del LCP.

  Dos arreglos, y el segundo es el de fondo:

  1. **Precargar `cormorant-garamond-400.woff2`**, que es una línea en las páginas y en los generadores que escriben la cabecera. Le quita un viaje de ida y vuelta y debería bajarla de 2.523 ms al entorno de las otras tres.
  2. **Fundir `fonts.css` dentro de `styles.css`.** Hoy son dos hojas que bloquean el pintado en todas las páginas, y ninguna fuente no precargada se descubre hasta que llega la primera: `fonts.css` sola tarda 1.266 ms. Fundirlas quita una petición bloqueante por página y deja la cadena en dos niveles en vez de tres. A cambio toca los nueve generadores que escriben la cabecera y las páginas escritas a mano.

  **Contra qué se compara.** Medido el 20 de septiembre de 2026, después de recortar las fuentes: FCP 1.057 ms y LCP 1.507 ms de mediana en tres pasadas de Lighthouse móvil sobre el sitio vivo. Cualquier cambio se compara contra esas cifras y contra el Speed Index de 3,9 s, y hace falta que mejore más que el ruido entre pasadas, que es de unos 50 ms. **Ojo con una explicación que no se sostiene**: el comentario de `index.html` dice que poner la precarga del retrato la primera le ahorró 485 ms. En el rastreo de hoy el retrato se pide a los 640 ms, a la vez que las dos hojas de estilo, porque en esta red el documento entero llega de golpe: reordenar precargas dentro del `<head>` no compra nada aquí. Lo que cuesta es el salto de más.

- **La prensa de Juventud Rebelde es frágil.** Las tres entrevistas enlazadas (2012, 2016 y 2019) respondieron de forma intermitente el 21 de septiembre de 2026: dos no cargaban, la portada del diario tampoco, y la tercera sí. Solo la de 2016 tiene copia en el Internet Archive. Si el diario cae como cayó Habana Radio, se pierden dos de las tres. Hay que guardarlas en el Archive (`web.archive.org/save/`) en cuanto respondan y, si caen, enlazar la copia. Es mandar URLs públicas a un servicio de terceros: lo decide Ernesto.
- **`.impeccable/design.json` describe el diseño abandonado**: mesa y papel, añil, Bonum y Courier Prime. Es el registro que hizo la herramienta `impeccable` sobre el DESIGN.md viejo el 6 de septiembre, y nadie lo regeneró cuando se reescribió. Si alguien vuelve a usar esa herramienta, hará cumplir el mundo que se descartó, igual que casi pasó con el DESIGN.md. Regenerarlo desde el DESIGN.md actual, o borrarlo si la herramienta ya no se usa.

## 5. Fuera de este repositorio

- **`ernestocisneros-site`**: en la página inglesa de representación, poner la trova delante en la frase de géneros, que hoy abre con la fantasía.
- **Backlinks de autoridad**, que es lo que más moverá el posicionamiento: que EcuRed enlace el sitio, que Tony lo publique en su Facebook y que aparezca en las páginas de sus editoriales.
