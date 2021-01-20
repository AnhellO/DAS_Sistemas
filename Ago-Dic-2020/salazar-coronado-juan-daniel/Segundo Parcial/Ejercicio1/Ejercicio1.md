#### Comando para poder levantar el contenedor de docker solicitado:
docker run -d -p 4000:4000 --name mysql_db -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=baz -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 mysql:8
### Comandos para conectarse a la bd:
docker exec -it mysql_db mysql -u foo -pbar123 (Aquí es recomendable no introducir la contraseña en el comando y ponerla después, solo lo hago así para que se vea que accede con esa contraseña.)
Ya dentro del monito de mysql se usan los siguientes comandos:
show databases; para ver que en efecto aparece la bd "baz"
use baz; para entrar a usar esa bd y eso es todo.
### Comando que use para llegar hasta la carpeta del ejercicio
cd desktop\universidad\diseño y arquitectura de software\das_sistemas\ago-dic-2020\salazar-coronado-juan-daniel\segundo parcial\ejercicio1