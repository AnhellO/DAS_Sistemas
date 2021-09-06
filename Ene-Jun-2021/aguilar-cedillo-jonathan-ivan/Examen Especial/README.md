### Nombre: Jonathan Ivan Aguilar Cedillo
#### Matricula: 12021818
---------------------------

### Instrucciones:

1. Clona el repositorio.
2. Ingrese a la carpeta del repositorio.
3. En caso de tener contenedores en funcionamiento, asegúrese de que todos los contenedores estén detenidos. 
` $ sudo docker stop $(sudo docker ps -q -a) `
4. Asegúrese de que todos los puertos necesarios para ejecutar los contenedores estén disponibles.
5. Como paso opcional puedes borrar todas las imágenes y contenedores para que no provoquen ningún tipo de conflicto. 
` $ docker system prune --all `
6. Ejecute el comando $ sudo docker-compose up 

### Contenedores:
#### DB
El servicio MongoDB se ejecuta en el puerto 27017.
```
MONGO_HOST='db'
MONGO_PORT='27017'
MONGO_USER='das-sistemas'
MONGO_PASS='eespecial-2021!'
MONGO_URI= "mongodb://das-sistemas:eespecial-2021!@db:27017"
```

#### DBMS
El servicio web MongoExpress se ejecuta en 
```
http://localhost:8081/
```

#### Scraper
```
Contiene un scraper creado en Python, que extrae datos de personas de un archivo llamado person.xml y los inserta en la base de datos de mongo con la libreria pymongo. 
```

#### API
```
Contiene una imagen de Flask, que se utilizará para establecer la comunicación y el manejo de solicitudes.
```

#### requirements.txt
```
flask==2.0.1
pymongo==3.12.0
```

#### Imagenes
```
Se encuentran en la carpeta llamada Pruebas
```