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
Saleccionar datos de la tabla
SELECT * FROM cacmovies.peliculas;
```
```sql
Añadir datos a la tabla
INSERT INTO peliculas (id, titulo, sinopsis, fecha_de_estreno, actores, genero, director, pais, duracion, poster, trailer) VALUES ();
```
```sql 
Actualizar datos de la tabla
UPDATE peliculas SET id=1;
```

```sql 
Eliminar datos de la tabla
DELETE FROM peliculas WHERE id = '1';
```
