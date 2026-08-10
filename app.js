// El número se imprime al cargar: pasadas de tinta en orden de imprenta.
// La cabecera responde al scroll con su peso variable (materia viva, no imagen).

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (!reduceMotion) {
  document.body.classList.add("imprimiendo");
  requestAnimationFrame(() => {
    requestAnimationFrame(() => document.body.classList.remove("imprimiendo"));
  });
}

const cabecera = document.getElementById("cabecera");
if (cabecera && !reduceMotion) {
  let ticking = false;
  const pesar = () => {
    const alto = window.innerHeight || 1;
    const avance = Math.min(window.scrollY / alto, 1);
    const peso = Math.round(900 - avance * 250);
    cabecera.style.fontVariationSettings = `"wght" ${peso}`;
    ticking = false;
  };
  window.addEventListener("scroll", () => {
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(pesar);
    }
  }, { passive: true });
}
