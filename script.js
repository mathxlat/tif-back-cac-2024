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
    fetchAndDisplayMovie(URL);
    function fetchAndDisplayMovie(URL){  
        fetch(URL)
            .then(function (response){
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Error al obtener las peliculas.');
                }
            })
            .then (function (data){ 
                let tablaPeliculas = document.getElementById('peliculasTable');
                console.log(data)
                for (let pelicula of data) {
                    let fila = document.createElement('tr');
                    fila.innerHTML= '<td>' + pelicula.id + '</td>' +
                        '<td>' + pelicula.titulo + '</td>' +
                        '<td align="right">' + pelicula.sinopsis + '</td>' +
                        '<td align="right">' + pelicula.fecha_de_estreno + '</td>' +
                        '<td align="right">' + pelicula.actores + '</td>' +
                        '<td align="right">' + pelicula.genero + '</td>' +
                        '<td align="right">' + pelicula.director + '</td>' +
                        '<td align="right">' + pelicula.pais + '</td>' +
                        '<td align="right">' + pelicula.duracion + '</td>' +
                        '<td><img src=' + URL + "/posters/" + pelicula.poster.split("/")[6] + ' alt="Poster" style="width: 100px;"></td>' +
                        '<td align="right">' + pelicula.trailer + '</td>';

                    tablaPeliculas.appendChild(fila);
                }
            })
    }
}); 
   







