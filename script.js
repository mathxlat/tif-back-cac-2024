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
                mostrarPeliculas(URL);  //actualizar la tabla de peliculas con los datos actuales
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
    mostrarPeliculas(URL); //al cargar la pagina cargue la tabla por primera vez
    
}); 

function borrarPelicula(id){
    const URL = "https://mathxlat.pythonanywhere.com/peliculas";
    fetch(URL + '/' + id, {
        method: 'DELETE',
    })
    .then(function (response) {
    if (response.ok) {
            alert('Pelicula eliminada correctamente.');
            mostrarPeliculas(URL);
        } else {
            throw new Error('Error al eliminar la película.');
        }
    })
}

function mostrarPeliculas(PAGINA){
    let URL = PAGINA; //URL recibe "PAGINA" que es la base de datos cuando la llama  
    fetch(URL)
            .then(function (response){
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Error al obtener las peliculas.');
                }
            })
        .then(function (data){
            let tablaPeliculas = document.getElementById('peliculasTable');
            tablaPeliculas.innerHTML = '';
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
                        '<td align="right">' + pelicula.trailer + '</td>' +
                        '<td text-align="center"><button onclick="borrarPelicula(' + pelicula.id + ')">Borrar</button><button onclick="modificarPelicula(' + pelicula.id + ')">Modificar</button></td>';
                    tablaPeliculas.appendChild(fila);
            }
        })
}

function modificarPelicula(id){
    const URL = "https://mathxlat.pythonanywhere.com/peliculas";
    const formPelicula = document.getElementById("peliculaForm");
    const formData = new FormData(formPelicula);
    fetch(URL + '/' + id, {
        method: 'PUT',
        body: formData,
    })
    .then(function (response) {
        if (response.ok) {
            alert('Película modificada correctamente.');
            mostrarPeliculas(URL);
        } else {
            alert("Complete todos los campos para modificar la pelicula.")
            throw new Error('Error al modificar la película.'); //Error en consola
            
        }
    })
    //finalmente limpia todos los campos
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
}



