# Predicting Space Weather with Docker | Chris Lauer

1. Como empezamos a usar Docker
2. Como empezamos a usar docker de verdad
3. como empezamos a ensenar docker a nuestros cientificos

### EL GRAN CENTOR DE PREDICCION DEL CLIMA ESPACIAL
forman parte del gobierno federal, tienen su propio software para el clima, tienen un sistema FISMA y tienen una mision muy cool Bl

### Space Weather
Todo lo que sucede entre la tierra y el sol como:
- Radiacion electromagnetica
- Particulas energeticamente cargadas
- Campos magneticos

### Metodologias
Utilizan la metodologia SCRUM para entrenar a sus desarrolladores pero desde 2012 han empezado el cambio a la agil

### Why Docker?
Debido a que el software cientifico utilizado tiene demasiadas dependencias y requisitos, necesitaban despegar de manera mas rapida y sencilla. Entonces Docker de una manera garantizo arreglar todos estos problemas ya qque garantiza que el software funcione en produccion y este resuelve la configuracion y persistencia de datos para cada uno de sus proyectos.

### Replacing the old way
utilizando docker con un patron Strangles pudieron
- Construir un servicio
- El servicio construido tiene que entender y resolver
    1. La naturaleza de los datos
    2. La forma en la que la aplicacion utiliza los datos
- Agregar los datos antiguos
- Portear el legado de las aplicaciones
- Agregar los nuevos datos y Empezar.

### 4 Deployment artifacts
1. **docker-compose.yml**: define las relaciones entre los servicios y con el host
2. **.env**: aisla las diferencias entre los hosts
3. **service-name.env**: un configuracion para cada servicio
4. **docker images**: alojados en su registro interno