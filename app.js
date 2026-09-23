// Ala del Mar · aparición lateral de bloques (patrón del template Index01)
// threshold 0: un bloque muy alto (capítulos completos en Fragmentos) nunca
// alcanza un porcentaje visible, así que disparamos en cuanto asoma su borde.
// Y a prueba de balas: lo que mide más que la pantalla se muestra directo,
// porque el contenido largo jamás debe poder quedar invisible.
//
// La altura de cada bloque se lee de la propia entrada del
// IntersectionObserver, que la calcula a su tiempo sin forzar nada. Antes se
// medía con getBoundingClientRect() dentro del mismo bucle que iba añadiendo
// clases, y el navegador tenía que volver a maquetar la página entera en cada
// vuelta. Lo cazó la auditoría del 12 de septiembre de 2026 como reflujo
// forzado en la carga.
(function () {
  var els = document.querySelectorAll('.reveal');
  // Las animaciones son solo de escritorio. En telefono y tablet, o si la
  // persona pidio menos movimiento, todo aparece directo y no se observa nada.
  // Es la misma consulta que apaga las transiciones en styles.css, y las dos
  // tienen que decir lo mismo. Decision de Ernesto, 14 de septiembre de 2026.
  var sinAnimacion = window.matchMedia('(max-width: 1080px), (hover: none), (prefers-reduced-motion: reduce)').matches;
  if (sinAnimacion || !('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.classList.add('visible'); });
    return;
  }
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      var muyAlto = entry.boundingClientRect.height > window.innerHeight * 1.2;
      if (entry.isIntersecting || muyAlto) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0, rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) { observer.observe(el); });
})();

// El menú móvil, con teclado y con lector de pantalla. Antes era un onclick en
// línea que solo alternaba una clase: quien navega con teclado no sabía si
// estaba abierto ni podía cerrarlo, y quien usa lector de pantalla no se
// enteraba de nada.
//
// Cada hamburguesa gobierna el menú que nombra en aria-controls. Casi todas
// las páginas tienen una sola; el 404 tiene una por idioma, y solo se ve la de
// la zona de donde viene el error.
//
// La etiqueta del botón se lee con lector de pantalla y tiene que estar en el
// idioma de la página: un idioma nuevo añade aquí su pareja.
(function () {
  var ETIQUETA = {
    es: ['Abrir menú', 'Cerrar menú'],
    en: ['Open menu', 'Close menu'],
    fr: ['Ouvrir le menu', 'Fermer le menu'],
    it: ['Apri il menu', 'Chiudi il menu'],
    pt: ['Abrir o menu', 'Fechar o menu']
  };

  document.querySelectorAll('.nav-hamburger').forEach(function (boton) {
    var menu = document.getElementById(boton.getAttribute('aria-controls'));
    if (!menu) return;

    function estado(abierto) {
      menu.classList.toggle('open', abierto);
      boton.setAttribute('aria-expanded', abierto ? 'true' : 'false');
      var par = ETIQUETA[document.documentElement.lang] || ETIQUETA.es;
      boton.setAttribute('aria-label', abierto ? par[1] : par[0]);
    }

    boton.addEventListener('click', function () {
      estado(!menu.classList.contains('open'));
    });

    // Escape cierra y devuelve el foco al botón, que es donde estaba el usuario.
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) {
        estado(false);
        boton.focus();
      }
    });

    // Al elegir una sección, el menú se aparta.
    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) estado(false);
    });

    // Si la ventana crece hasta que la barra vuelve a caber, se limpia el estado.
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1080 && menu.classList.contains('open')) estado(false);
    });
  });
})();
