var formulario= document.getElementById('formulario_alta') //tomar referncia del html
var usuario = formulario['usuario'].value
var titulo = formulario['titulo'].value;
var mensaje = formulario['mensaje'].value

form.addEventListener('submit',function(e){
    e.preventDefault() //no se envia el formulario predefinido sino como queremos nosotros
        formulario.usuario = usuario;
        formulario.titulo =  titulo;
        formulario.mensaje = mensaje;
        fetch('../../myApp/preguntas/',{method:'POST',body:formulario})//manda los datos del formulario al servidor
        .then(function (response) {
        if (response.ok) {
          return response.text();
        } else {
          throw "Error en la llamada Ajax";
        }
      })
      .then(function (texto) {

        alert('¡Registrado correctamente!')

      })
      .catch(function (err) {
        alert("error inesperado");
      });

    })