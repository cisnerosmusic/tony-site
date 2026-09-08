# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

delegated: HTML/CSS/JS estático, sin frameworks ni plugins, por filosofía técnica de Index01 (sitios rápidos y ligeros, código propio, mobile-first). GitHub Pages con dominio propio y HTTPS forzado, sin una sola petición a terceros. Las páginas de libro no se escriben a mano: se generan con `herramientas/gen-libro.py` desde manifiestos JSON.

## Users

Tres lectores, en este orden de valor:

1. **Editores, agentes, scouts y traductores fuera de Cuba.** Es el lector que decide si esta web cumple su función. Llega buscando un autor, un título o un tema, con frecuencia en inglés, y necesita saber en noventa segundos qué escribió, qué premios tiene, qué derechos están libres y a quién se le escribe. No compra el libro: compra la licencia.
2. **Lectores hispanohablantes de Latinoamérica y España.** Mercado inmediato y sin fricción: no necesitan traducción ni intermediario. Llegan por el nombre del autor, por el género o por la trova, y leen la obra en su idioma original.
3. **Jurados, festivales, prensa cultural y académicos** que necesitan bio y bibliografía verificables para citar, invitar o premiar.

El lector residente en Cuba no es público objetivo. Tony ya tiene allí sus editoriales y su circuito; esta casa se construyó para lo que no tiene, que es el afuera. El sitio carga bien desde la isla y así debe seguir, pero el ancho de banda cubano dejó de ser la restricción que manda sobre las decisiones técnicas.

## Product Purpose

Ventana al mundo de la obra de Antonio López Sánchez. Cumple dos funciones a la vez:

- **Catálogo del autor**: quién es y qué ha escrito, con ficha, contratapa, fragmentos y comentario propio del autor en cada uno de sus libros publicados.
- **Cabecera de un embudo de derechos**: cada página de libro declara el estado de sus derechos y debe conducir a la página de representación literaria de Ernesto Cisneros, que es donde ocurre la conversación comercial.

El sitio no cierra la venta, la entrega. Toda página que declare derechos disponibles y no ofrezca a dónde escribir es una fuga.

## Positioning

Escritor cubano de fantasía heroica premiado (La Rosa Blanca, UNEAC) que a la vez es cronista de la Nueva Trova: fantasía épica escrita desde La Habana, con una segunda vida documental sobre la canción cubana. Esa doble condición, espada y trova, no la puede reclamar otro autor del género.

**Las dos obras no tienen la misma dificultad de venta según el idioma, y el sitio debe reflejarlo:**

- **En español, la fantasía va delante.** Es la puerta de entrada del lector de Latinoamérica y España, y es donde está el volumen.
- **En inglés, la trova va delante.** La fantasía traducida compite contra un mercado anglófono sobreabastecido en su propio género. El ensayo y la entrevista sobre la canción cubana, con *Convertida en canción* y *Trovadoras* al frente, compiten en otro circuito, el de las editoriales universitarias y de música, donde la musicología cubana tiene demanda y no tiene equivalente en inglés. Es la vía corta, y un libro colocado ahí mejora la posición del autor para todo lo demás.

## Operating Context

El visitante llega desde búsqueda, prensa cultural o redes, casi siempre por el nombre del autor o por un título concreto.

Los libros publicados tienen exclusividad editorial solo dentro de Cuba. **Los derechos para el resto del mundo están disponibles y los gestiona personalmente Ernesto Cisneros desde Miami**, como representante del autor. La página de representación vive en `ernestocisneros.art`, en español (`/es/representacion-literaria.html`) y en inglés (`/literary-representation.html`), con la dirección dedicada `derechos@antoniolopezsanchez.art`. Esa separación es deliberada y se mantiene: el sitio de Tony es la casa y el catálogo, el sitio de Ernesto es el negocio. El dossier de derechos no se duplica aquí.

La compra directa de ejemplares no está resuelta y no es el objetivo. La acción primaria es doble según quién llegue: conocer la obra, o escribir por los derechos.

## Capabilities and Constraints

- Sitio estático, ligero, mobile-first, SEO y AEO en cada decisión (regla del estudio).
- **Se traduce el aparato, no la literatura.** Navegación, títulos de sección, presentaciones, fichas, notas de derechos y metadatos SEO se traducen. Poemas, fragmentos de novela y de ensayo y cualquier texto literario quedan siempre en su español original, salvo excepción que decida el propio autor. Un editor extranjero no necesita la novela en inglés: necesita saber que existe, qué es y que puede comprarla.
- Idiomas: español como base, inglés como segunda lengua y prioridad real. Francés, italiano y portugués después. Ruso descartado por tipografía.
- Sin raya larga en ningún texto público de la página (regla innegociable del estudio).
- "Ala del Mar" y "bene scriptus" nunca se traducen.
- Las obras inéditas se presentan solo con sinopsis y fragmentos, nunca íntegras, y su material original no entra en este repositorio, que es público.
- El mecanismo de cobro, la custodia de fondos y cualquier detalle fiscal o contractual de la representación no se documentan aquí. Van en la documentación privada del estudio.

## Evidence on Hand

Verificado en fuentes públicas (EcuRed, El Camagüey, La Jiribilla):

- Antonio López Sánchez, La Habana, 16 de enero de 1973. Licenciado en Comunicación Social (Universidad de La Habana). Egresado del IX curso del Centro de Formación Literaria Onelio Jorge Cardoso (2007).
- Novelas de fantasía y horror: Las guerreras de la luz (Editorial de la Mujer, 2011; Premio La Rosa Blanca 2012, UNEAC), El Escudo de Valnúss (Editorial de la Mujer, 2015), El otro lado del espejo (Gente Nueva, 2017; mención Concurso La Edad de Oro 2014), Grimorium (Editorial Oriente, 2018), Perdidos en un librero (Quisicuaba, 2026).
- Ensayo y entrevista: La canción de la Nueva Trova (Atril, 2001), Trovadoras (Editorial Oriente, 2009), Convertida en canción (Capiro, 2019).
- Poesía colectiva: Trampas, retratos y un 17 rojo (coautor, Editorial de la Mujer, 2005).
- Primer premio "Reescribir El Quijote en Cuba" (2005). Premio Farraluque de Literatura Erótica (2026). Premio Colateral Yasmina Calcines, XXVI Concurso Nacional Ala Décima (2026).
- Periodismo cultural: revistas Mujeres y Muchacha (2001-2011); colaborador de La Jiribilla, La Gaceta de Cuba, El Caimán Barbudo, Juventud Rebelde, Alma Máter.
- Carátulas reales de las ediciones, entregadas por Ernesto y optimizadas en `img/libros/`. Originales en OneDrive/Imágenes/tony.
- Fotos reales del autor, entregadas por Tony vía Ernesto (sept 2026, 715px nativos por las condiciones de envío desde Cuba): retrato junto al cañón de la fortaleza de La Habana (`img/retrato.webp`) y la foto de mar que el autor quiso en su portada por valor simbólico (`img/mar2.webp`).
- Textos literarios reales del autor: contratapas, fragmentos y "con voz y voto" de cada libro, más el poema íntegro "Informe legal sobre la muerte de un poema".
- Dos grabaciones en la voz del autor, en `/tinta-ciones/en-mi-voz/`.

Ausencias que no se deben fabricar: sinopsis oficiales de los títulos aún marcados como provisionales, reseñas y prensa citable de la mayoría de los libros, y cualquier dato de extensión o categoría de edad que no venga del autor o de su editorial.

## Product Principles

- **La obra manda, pero el orden depende del idioma.** En español entra por la fantasía; en inglés, por la trova. Ver Positioning.
- **Todo dato biográfico o bibliográfico publicado debe ser verificable.** Nada sintético sin etiquetar.
- **Ninguna declaración de derechos sin salida.** Si una página dice que los derechos están disponibles, tiene que ofrecer a dónde escribir, en el idioma de quien lee.
- **El inglés no es el español traducido.** Es el mismo catálogo en otro orden, para otro lector, con otra intención.
- **Rápido y ligero siempre**, no por restricción de red sino porque es correcto y porque aquí sale gratis.
- **La voluntad del autor manda sobre cualquier criterio de diseño.**
