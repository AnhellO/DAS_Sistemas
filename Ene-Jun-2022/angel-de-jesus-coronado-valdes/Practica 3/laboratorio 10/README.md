## LABORATORIO 10

Listamos los contenedores que tenemos con el comando: `sudo docker ps -a`, vemos los contenedores que se encuentra en nuestro equipo.

![](/imagenes/1.png)


1. Construye la imagen con el comando `docker build -t mipostgre .`.
   1. Recuerda que puedes revisar tu imagen recién creada utilizando el comando `docker images`.

![](/imagenes/2.png)
   
   
2. Ahora ejecuta un contenedor en base a la imágen que acabas de crear utilizando el comando `docker run -d --name postgres -p 5432:5432 mipostgre`.

![](/imagenes/3.png)

   1. Utiliza el comando `docker logs postgres` para poder verificar la inicialización del contenedor, ¿puedes ver como nuestro script de `init.sql` se ejecuta en la línea de `running /docker-entrypoint-initdb.d/init.sql`?.

![](/imagenes/4.png)
   
   
3. Después de esto ejecuta el script [`orm.py`](orm.py) utilizando el comando `python orm.py`. En caso de decidirte por `GO`, entonces puedes ejecutar el archivo [`main.go`](main.go) por medio del comando `go run main.go`.
   1. Asegúrate de instalar las librerías necesarias para el lenguaje que elijas antes de continuar.
      1. Para `Python`: `pip install --no-cache-dir -r requirements.txt`.
      2. Para `GO`: `go mod download`.

![](/imagenes/5.png)
 
   2. El script debe de correr sin problema alguno, y deberías de poder ver en el output de tu consola como se imprimen registros de la `DB` y valores de las operaciones `CRUD`.
   3. Puedes revisar la base de datos directamente desde el contenedor de `PostgreSQL`, siguiendo los pasos descritos a continuación:
      1. Ejecuta el comando `docker exec -it postgres bin/bash` para meterte al contenedor de `PostgreSQL`.
      2. Una vez dentro ejecuta el cliente de CLI `psql` con el siguiente comando: `psql -U the_cat -d random_cats`.
      3. Una vez dentro de la DB puedes utilizar el comando `\dt` para ver las tablas existentes en la base de datos, y ahí deberías de ver la tabla de `my_cats`. Teclea el query `SELECT * FROM my_cats;` para poder ver los rows existentes.
      4. Puedes salir del client `psql` utilizando el comando `\q`, y después salir del contenedor de `PostgreSQL` tecleando `exit`.

![](/imagenes/6.png)
      
   4. Siéntete libre de jugar todo lo necesario con los scripts y con el contenedor en ejecución, y una vez que hayas terminado asegúrate de remover el contenedor de `PostgreSQL` por medio del comando `docker stop postgres; docker rm postgres`


Lo que aprendí en este laboratorio fue como jugar con los scripts de python y de go, de operaciones CRUD y de ver nuevas librerias en python.

