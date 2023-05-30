const button = document.getElementById("cartoon");
const link = document.getElementById("link");

button.addEventListener("click", (e) => {
  e.preventDefault(); // Evita el comportamiento predeterminado del enlace

  // Realiza una solicitud al servidor utilizando Fetch API o XMLHttpRequest
  fetch("/cartoon")
    .then(function (response) {
      // Maneja la respuesta del servidor
      if (response.ok) {
        window.location.href = "/result";
        // Realiza alguna acción si la solicitud fue exitosa
        console.log("Solicitud exitosa");
        // Puedes actualizar la imagen o realizar otras operaciones aquí
      } else {
        // Maneja el caso de error de la solicitud
        console.error("Error en la solicitud");
      }
    })
    .catch(function (error) {
      // Maneja los errores de red u otras excepciones
      console.error("Error en la solicitud", error);
    });
});
