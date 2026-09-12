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
  if (!('IntersectionObserver' in window)) {
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
// las páginas tienen una sola; el 404 tiene dos, la española y la inglesa, y
// solo se ve la del idioma de la ruta.
(function () {
  document.querySelectorAll('.nav-hamburger').forEach(function (boton) {
    var menu = document.getElementById(boton.getAttribute('aria-controls'));
    if (!menu) return;

    function estado(abierto) {
      menu.classList.toggle('open', abierto);
      boton.setAttribute('aria-expanded', abierto ? 'true' : 'false');
      var ingles = document.documentElement.lang === 'en';
      boton.setAttribute('aria-label',
        abierto ? (ingles ? 'Close menu' : 'Cerrar menú')
                : (ingles ? 'Open menu' : 'Abrir menú'));
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
