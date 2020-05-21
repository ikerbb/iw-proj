let boton = document.getElementById("btnSubmit");

boton.addEventListener("click", (event) => {
  loadData();
});

function loadData() {
  fetch('preguntasListView')
    .then((response) => response.json())
    .then((json) => {
        let bloque = document.getElementById("div_js");
        bloque.removeChild("formulario");
        var parrafo = document.createElement('p');
        bloque.append("parrafo")
        parrafo.textContent = `"${json.pregunta}"`
    });
}

loadData();