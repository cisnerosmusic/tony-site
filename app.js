// Ala del Mar · aparición lateral de bloques (patrón del template Index01)
// threshold 0: un bloque muy alto (capítulos completos en Fragmentos) nunca
// alcanza un porcentaje visible, así que disparamos en cuanto asoma su borde.
// Y a prueba de balas: lo que mide más que la pantalla se muestra directo,
// porque el contenido largo jamás debe poder quedar invisible.
(function () {
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.classList.add('visible'); });
    return;
  }
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0, rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) {
    if (el.getBoundingClientRect().height > window.innerHeight * 1.2) {
      el.classList.add('visible');
    } else {
      observer.observe(el);
    }
  });
})();
