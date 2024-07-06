document.addEventListener('DOMContentLoaded', () => {

    const URL = "https://mathxlat.pythonanywhere.com/peliculas";
    const formPelicula = document.getElementById("peliculaForm");

    formPelicula.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(formPelicula);    

        fetch(URL, {
            method: 'POST',
            body: formData, 
        })
        .then(function (response) {
            if (response.ok) {
                return response.json(); 
            } else {
                throw new Error('Error al agregar la película.');
            }
        })

            .then(function (data) {
                alert('Película agregada correctamente.');
            })
            
            .catch(function (error) {
                alert('Error al agregar la película.');
            })
            
            .finally(function () {
                document.getElementById('peliculaId').value = "";
                document.getElementById('titulo').value = "";
                document.getElementById('sinopsis').value = "";
                document.getElementById('fecha_de_estreno').value = "";
                document.getElementById('actores').value = "";
                document.getElementById('genero').value = "";
                document.getElementById('director').value = "";
                document.getElementById('pais').value = "";
                document.getElementById('duracion').value = "";
                document.getElementById('poster').value = "";
                document.getElementById('trailer').value = "";
            });
    });
}); 








