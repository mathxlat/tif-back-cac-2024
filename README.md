```sql
#Crear tabla si no existe
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

```sql
#Seleccionar datos de la tabla
SELECT * FROM cacmovies.peliculas;
```

```sql
#Añadir datos a la tabla
INSERT INTO peliculas (id, titulo, sinopsis, fecha_de_estreno, actores, genero, director, pais, duracion, poster, trailer) VALUES ();
```

```sql
#Actualizar datos de la tabla
UPDATE peliculas
SET titulo= 'Kong',
 sinopsis= 'Kong vs godzilla',
 fecha_de_estreno= '29/6/2024',
 actores= 'king kong, godzilla',
 genero= 'acciom',
 director= 'alguien',
 pais= 'alguno',
 duracion= '2hs',
 poster= 'poster',
 trailer= 'trailer'
WHERE id= ;


```

```sql
#Eliminar datos de la tabla
DELETE FROM peliculas WHERE id = '1';
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
        "poster": "https://cdn.marvel.com/content/1x/deadpoolandwolverine_lob_crd_02.jpg",
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
    "poster": "https://cdn.marvel.com/content/1x/deadpoolandwolverine_lob_crd_02.jpg",
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
    "poster": "https://cdn.marvel.com/content/1x/deadpoolandwolverine_lob_crd_02.jpg",
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
    "poster": "https://cdn.marvel.com/content/1x/deadpoolandwolverine_lob_crd_02.jpg",
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