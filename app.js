// La única pieza de motion del mundo: el oficio se mecanografía solo al cargar,
// con retorno de carro invisible y cursor de bloque. Con reduced-motion, texto directo.

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const oficio = document.getElementById("oficio");

if (oficio && !reduceMotion) {
  const texto = oficio.textContent;
  oficio.textContent = "";
  const cursor = document.createElement("span");
  cursor.className = "cursor-maquina";
  cursor.setAttribute("aria-hidden", "true");
  oficio.setAttribute("aria-label", texto);
  oficio.appendChild(cursor);

  let i = 0;
  const tecla = () => {
    if (i < texto.length) {
      cursor.before(document.createTextNode(texto[i]));
      i += 1;
      const pausa = texto[i - 1] === "," ? 220 : 34 + Math.random() * 40;
      setTimeout(tecla, pausa);
    } else {
      setTimeout(() => cursor.remove(), 2600);
    }
  };
  setTimeout(tecla, 500);
}
