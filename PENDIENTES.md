# Pendientes · Ala del Mar

Lo que queda por hacer, y nada más.

- **Lo hecho no se apunta aquí**: está en el historial de git, y el mensaje de cada commit explica el porqué.
- **Las decisiones que no hay que deshacer** están en `AGENTS.md`.
- **Cuando algo se termina, se borra de esta lista en el mismo commit que lo cierra.**

## 1. Terminar el inglés

Hay salas que solo existen en español. En todas, la literatura se queda en español y lo que se traduce es el aparato:

1. **Contarte**: la entradilla y la línea de presentación de cada cuento.
2. **Tinta-ciones por dentro**: Poemas sueltos, De-Cimitas, Sonata de la lluvia y En mi voz. Hoy `/en/poetry/` explica la poesía y enlaza a las salas españolas.
3. **Laureles**: hoy los premios en inglés viven dentro de `/en/author/`. Decidir si merecen página propia, con las dos obras del Farraluque.
4. **Plano abierto**: las grabaciones, con su ficha en inglés.
5. **Entre lectores, Directorio e Inéditos.**
6. **"Books" en el menú inglés**, sí o no. Hoy al catálogo se llega desde la portada, desde las secciones y desde cada libro. Decide Ernesto.

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
11. **Erratas dudosas en los Inéditos**, que no se tocaron por si son a propósito: en *Mis diarios de cama*, el archivo de la entrada 8 dice «20 de septiembre de 2004» y el texto «18» (se publicó el 18), y «María con la mala noticia de su mamá al final murió», donde parece faltar un «de que»; en *Preguntas*, «un tangente homenaje» y «desde las páginas de novela»; en *Palabras*, «A esas respuestas [...] se intentó responder», donde quizá quiso decir «preguntas».

## 3. Espera la decisión de Ernesto

- **Tarjetas sociales de los libros**: las catorce páginas usan `summary_large_image` con la cubierta, que es vertical, y las redes la recortan por el centro. O se pasan a `summary`, o se genera una tarjeta horizontal por libro.
- **Dos campos más en la ficha de cada libro**, que pide un editor extranjero: derechos ya vendidos, además de los disponibles, y si existe muestra traducida.
- **Verificar el dominio en la cuenta de GitHub.** Lo tiene que hacer Ernesto; son unos minutos. En la configuración de Pages de la cuenta `cisnerosmusic` se añade `antoniolopezsanchez.art`, GitHub da un registro TXT, se pega en el DNS del dominio y se pulsa verificar. Protege contra que otra cuenta de GitHub se quede con el dominio si algún día el sitio se despublica mientras el DNS sigue apuntando a GitHub.
- **Formulario de consultas de derechos con Formspree**, en lugar del correo: daría historial de consultas y filtro de spam, a cambio de un servicio de terceros, que el sitio hoy no tiene. Recomendación: no, mientras el correo `derechos@` baste.

## 4. Técnico

- **Francés, italiano y portugués**, después del inglés. El procedimiento está en el README, sección Idiomas.

## 5. Fuera de este repositorio

- **`ernestocisneros-site`**: `es/representacion-literaria.html` declara dos `hreflang="en"` en conflicto, uno a `literary-representation.html` y otro a `books.html`. Revisar si el patrón se repite en las siete lenguas. Y en la página inglesa de representación, poner la trova delante del orden de géneros.
- **El documento de representación entre Tony y Ernesto**: pendiente de decisión y de revisión legal, en la documentación privada del estudio.
- **Backlinks de autoridad**, que es lo que más moverá el posicionamiento: que EcuRed enlace el sitio, que Tony lo publique en su Facebook y que aparezca en las páginas de sus editoriales.
