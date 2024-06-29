```sql 
CREATE TABLE `peliculas` (
  `id` int unsigned NOT NULL,
  `titulo` varchar(45) NOT NULL,
  `sinopsis` varchar(45) DEFAULT NULL,
  `fecha_de_estreno` date NOT NULL,
  `actores` varchar(45) DEFAULT NULL,
  `genero` varchar(45) DEFAULT NULL,
  `director` varchar(45) NOT NULL,
  `pais` varchar(45) NOT NULL,
  `duracion` time NOT NULL,
  `poster` varchar(45) DEFAULT NULL,
  `trailer` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idpeliculas_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```



```sql 
Saleccionar datos de la tabla
SELECT * FROM cacmovies.peliculas;
```
```sql
Añadir datos a la tabla
INSERT INTO peliculas (
id, titulo, sinopsis, fecha_de_estreno, actores, genero, director, pais, duracion, poster, trailer
) VALUES ();
```
```sql 
Actualizar datos de la tabla
UPDATE peliculas SET id=1;
```

```sql 
Eliminar datos de la tabla
DELETE FROM peliculas WHERE id = '1';
```
