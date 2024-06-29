```sql 
#Crear tabla si no existe
CREATE TABLE IF NOT EXISTS `peliculas` (
  id INT auto_increment PRIMARY KEY NOT NULL,
  titulo VARCHAR(45) NOT NULL,
  sinopsis VARCHAR(255) DEFAULT NULL,
  fecha_de_estreno date NOT NULL,
  actores VARCHAR(45) DEFAULT NULL,
  genero VARCHAR(45) DEFAULT NULL,
  director VARCHAR(45) NOT NULL,
  pais VARCHAR(45) NOT NULL,
  duracion INT NOT NULL,
  poster VARCHAR(255) DEFAULT NULL,
  trailer VARCHAR(255) DEFAULT NULL,
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
