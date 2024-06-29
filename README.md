```sql 
#Crear tabla si no existe
CREATE TABLE IF NOT EXISTS `peliculas` (
  `id` int unsigned NOT NULL,
  `titulo` varchar(45) NOT NULL,
  `sinopsis` varchar(255) DEFAULT NULL,
  `fecha_de_estreno` date NOT NULL,
  `actores` varchar(45) DEFAULT NULL,
  `genero` varchar(45) DEFAULT NULL,
  `director` varchar(45) NOT NULL,
  `pais` varchar(45) NOT NULL,
  `duracion` int NOT NULL,
  `poster` varchar(255) DEFAULT NULL,
  `trailer` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idpeliculas_UNIQUE` (`id`)
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
