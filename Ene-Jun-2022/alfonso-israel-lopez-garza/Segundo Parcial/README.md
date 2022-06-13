# Pasos a seguir
1.- Tener docker instalado
2.- Tener este repositorio clonado
3.- Abrir una terminal
4.- Moverse a la ubicación donde se encuentra el docker-compose.yml
5.- escribir en la terminal docker-compose up -d --build
## En caso de querer detenerlo
6.- En la misma ubicación del docker-compose.yml
7.- Escribir en la terminal docker-compose down

## Nota
Para ver los datos de la base de datos se puede dirigir a localhost:8081 para observarlos por medio del DBMS de mongo, o si prefiere verlos de una manera diferente, ingresar al localhost:5000.
En esa ubicacion se encontrara con 2 link uno que se llama abierto y otro cerrado, segun el que seleccione se mostraran los Issues, la unica diferencia es que ese link determina si su estado es abierto o cerrado. En esta practica solo se recorren 59 paginas de los que se encuentran cerrados, puesto que como no se estaba verificado, teniamos un numero de peticiones contadas, una ves autorizados solo se cambia un parametro en el documento Issues.py de la carpeta processor, para que recorra todas las paginas.

# URLs
1.- Api Github: https://docs.github.com/es/rest
2.- Repositorio de Flask: https://github.com/pallets/flask/
3.- Imagen de mongoDB: https://hub.docker.com/_/mongo
4.- Imagen de DBMS mongo: https://hub.docker.com/_/mongo-express
5.- Documentacion Flask: https://flask.palletsprojects.com/en/2.1.x/tutorial/templates/