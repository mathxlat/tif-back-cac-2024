## SQL

### Crear tabla si no existe
```sql
CREATE TABLE IF NOT EXISTS peliculas (
id INT AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(45) NOT NULL,
sinopsis VARCHAR(255) NOT NULL,
fecha_de_estreno date NOT NULL,
actores VARCHAR(45) NOT NULL,
genero VARCHAR(45) NOT NULL,
director VARCHAR(45) NOT NULL,
pais VARCHAR(45) NOT NULL,
duracion INT NOT NULL,
poster VARCHAR(255) NULL,
trailer VARCHAR(255) NOT NULL,
)
```
### Seleccionar datos de la tabla
```sql
SELECT * FROM peliculas;
```
### Añadir datos a la tabla
```sql
INSERT INTO peliculas (id, titulo, sinopsis, fecha_de_estreno, actores, genero, director, pais, duracion, poster, trailer)
VALUES (1, 'Deadpool & Wolverine','Get ready for a rollercoaster ride of action, humor, and unexpected twists as Deadpool and Wolverine embark on an epic adventure that will leave a lasting impact on the MCU and its beloved characters.','2024-07-25','Ryan Reynolds, Hugh Jackman','Action','Shawn Levy','USA',120,'https://cdn.marvel.com/content/1x/deadpoolandwolverine_lob_crd_02.jpg','https://www.youtube.com/watch?v=73_1biulkYk');
```
### Actualizar datos de la tabla
```sql
UPDATE peliculas
SET titulo= 'Godzilla y Kong: El nuevo imperio',
sinopsis= 'Dos enemigos ancestrales se ven obligados a unir sus fuerzas contra un nuevo enemigo En Godzilla x Kong: the new empire, un enemigo ancestral resurge de la oscuridad, decidido a desatar el caos absoluto en el mundo. Ante una amenaza imparable, los legendarios Godzilla y Kong deben dejar de lado su histórica rivalidad y trabajar juntos. Mientras todos se preparan para la batalla, importantes descubrimientos del pasado se revelan, brindando información sobre el origen de la Isla Calavera y la enigmática rivalidad entre especies, que ha perdurado a lo largo de generaciones.',
fecha_de_estreno= '2024-03-27',
actores= 'Dan Stevens, Rebecca Hall, Brian Tyree Henry, Kaylee Hottle, Fala Chen, Alex Ferns, Rachel House',
genero= 'Ciencia Ficción',
director= 'Adam Wingard',
pais= 'Estados Unidos',
duracion= 115,
poster= 'poster',
trailer= 'trailer'
WHERE id= 1;


```
### Eliminar datos de la tabla
```sql
DELETE FROM peliculas WHERE id = 1;
```

## API Endpoints

### GET /peliculas
Respuesta
```json
[
    {
        "actores": "Ryan Reynolds, Hugh Jackman",
        "director": "Shawn Levy",
        "duracion": 120,
        "fecha_de_estreno": "Thu, 25 Jul 2024 00:00:00 GMT",
        "genero": "Action",
        "id": 1,
        "pais": "USA",
        "poster": "./static/posters/2478693ac166460c829df501ad334e23-deadpoolandwolverine.jpg",
        "sinopsis": "Get ready for a rollercoaster ride of action, humor, and unexpected twists as Deadpool and Wolverine embark on an epic adventure that will leave a lasting impact on the MCU and its beloved characters.",
        "titulo": "Deadpool & Wolverine",
        "trailer": "https://www.youtube.com/watch?v=73_1biulkYk"
    }
]
```
### GET /peliculas/:id
Respuesta
```json
{
    "actores": "Ryan Reynolds, Hugh Jackman",
    "director": "Shawn Levy",
    "duracion": 120,
    "fecha_de_estreno": "Thu, 25 Jul 2024 00:00:00 GMT",
    "genero": "Action",
    "id": 1,
    "pais": "USA",
    "poster": "./static/posters/2478693ac166460c829df501ad334e23-deadpoolandwolverine.jpg",
    "sinopsis": "Get ready for a rollercoaster ride of action, humor, and unexpected twists as Deadpool and Wolverine embark on an epic adventure that will leave a lasting impact on the MCU and its beloved characters.",
    "titulo": "Deadpool & Wolverine",
    "trailer": "https://www.youtube.com/watch?v=73_1biulkYk"
}
```

### POST /peliculas
Body
```json
{
    "titulo": "Deadpool & Wolverine",
    "sinopsis": "Get ready for a rollercoaster ride of action, humor, and unexpected twists as Deadpool and Wolverine embark on an epic adventure that will leave a lasting impact on the MCU and its beloved characters.",
    "fecha_de_estreno": "2024-07-25",
    "actores": "Ryan Reynolds, Hugh Jackman",
    "genero": "Action",
    "director": "Shawn Levy",
    "pais": "USA",
    "duracion": 120,
    "poster": "./static/posters/2478693ac166460c829df501ad334e23-deadpoolandwolverine.jpg",
    "trailer": "https://www.youtube.com/watch?v=73_1biulkYk"
}
```
Respuesta
```json
{
    "id": 1,
    "message": "Pelicula agregada exitosamente"
}
```

### PUT /peliculas/:id
Body
```json
{
    "titulo": "Deadpool & Wolverine",
    "sinopsis": "Get ready for a rollercoaster ride of action, humor, and unexpected twists as Deadpool and Wolverine embark on an epic adventure that will leave a lasting impact on the MCU and its beloved characters.",
    "fecha_de_estreno": "2024-07-25",
    "actores": "Ryan Reynolds, Hugh Jackman",
    "genero": "Action",
    "director": "Shawn Levy",
    "pais": "USA",
    "duracion": 128,
    "poster": "./static/posters/2478693ac166460c829df501ad334e23-deadpoolandwolverine.jpg",
    "trailer": "https://www.youtube.com/watch?v=73_1biulkYk"
}
```

Respuesta
```json
{
    "message": "Pelicula modificada exitosamente"
}
```

### DELETE /peliculas/:id
Respuesta
```json
{
    "message": "Pelicula eliminada exitosamente"
}
```
