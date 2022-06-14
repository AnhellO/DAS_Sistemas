# Guía

Esta guía pretende enseñar un breve ejemplo de como llevar a cabo operaciones `CRUD` por medio de un `ORM` tanto `Python` ([`Peewee`](http://docs.peewee-orm.com/en/latest/)) como en `GO` ([`GORM`](https://gorm.io/index.html))

Las operaciones `CRUD` se llevan a cabo en un contenedor de `PostgreSQL`, el cual inicializaremos por medio de un archivo `init.sql` y el entrypoint de Docker `docker-entrypoint-initdb.d`, que permite que todos los scripts dentro de esa ruta sean ejecutados al inicializar un nuevo contenedor. Para ello utilizaremos el [`Dockerfile`](Dockerfile) que se encuentra dentro de la carpeta del ejemplo.

1. Construye la imagen con el comando `docker build -t mipostgre .`
   
   ![image](https://user-images.githubusercontent.com/71090472/172252954-8424a604-62e2-41ae-a2cd-72555a7e91ec.png)
      
   1. Recuerda que puedes revisar tu imagen recién creada utilizando el comando `docker images`

      ![image](https://user-images.githubusercontent.com/71090472/172253517-86752029-0a25-4ff7-bfbb-9336fa10e794.png)

2. Ahora ejecuta un contenedor en base a la imágen que acabas de crear utilizando el comando `docker run -d --name postgres -p 5432:5432 mipostgre`
   
   ![image](https://user-images.githubusercontent.com/71090472/172253958-93d50715-223a-4a2e-bbb7-1e093f3ac8eb.png)
   
   1. Utiliza el comando `docker logs postgres` para poder verificar la inicialización del contenedor, ¿puedes ver como nuestro script de `init.sql` se ejecuta en la línea de `running /docker-entrypoint-initdb.d/init.sql`?

   ![image](https://user-images.githubusercontent.com/71090472/172254076-af48a93a-98f5-4d9b-99cd-3498bf18349e.png)
   
   ![image](https://user-images.githubusercontent.com/71090472/172254332-fac357c6-0add-463c-96c1-91bcfa1a958f.png)

3. Después de esto ejecuta el script [`orm.py`](orm.py) utilizando el comando `python orm.py`. En caso de decidirte por `GO`, entonces puedes ejecutar el archivo [`main.go`](main.go) por medio del comando `go run main.go`
   
   ![image](https://user-images.githubusercontent.com/71090472/172254853-6dfab060-0aeb-4a6d-bfce-236e2d0161d1.png)
   
   1. Asegúrate de instalar las librerías necesarias para el lenguaje que elijas antes de continuar
      1. Para `Python`: `pip install --no-cache-dir -r requirements.txt`
      
      ![image](https://user-images.githubusercontent.com/71090472/172254901-475d8ba7-b12a-447e-ac07-262c2e0f7cdd.png)
      
      2. Para `GO`: `go mod download`

   2. El script debe de correr sin problema alguno, y deberías de poder ver en el output de tu consola como se imprimen registros de la `DB` y valores de las operaciones `CRUD`
   3. Puedes revisar la base de datos directamente desde el contenedor de `PostgreSQL`, siguiendo los pasos descritos a continuación:     
      1. Ejecuta el comando `docker exec -it postgres bin/bash` para meterte al contenedor de `PostgreSQL`
      
         ![image](https://user-images.githubusercontent.com/71090472/172255178-4f5199c9-f3dd-4fb2-9048-dc7a9c7307b9.png)
      
      2. Una vez dentro ejecuta el cliente de CLI `psql` con el siguiente comando: `psql -U the_cat -d random_cats`
   
         ![image](https://user-images.githubusercontent.com/71090472/172255305-2e3b44b2-0b21-4329-8b62-061ddba726ad.png)
      
      3. Una vez dentro de la DB puedes utilizar el comando `\dt` para ver las tablas existentes en la base de datos, y ahí deberías de ver la tabla de `my_cats`. Teclea el query `SELECT * FROM my_cats;` para poder ver los rows existentes
      
         ![image](https://user-images.githubusercontent.com/71090472/172255479-4316b96e-953a-40d2-90e9-d446dae9938f.png)
   
         ![image](https://user-images.githubusercontent.com/71090472/172255527-dee9e042-9dbe-4ca0-a4d0-402eca4b1ecd.png)
      
      4. Puedes salir del client `psql` utilizando el comando `\q`, y después salir del contenedor de `PostgreSQL` tecleando `exit`
         
         ![image](https://user-images.githubusercontent.com/71090472/172255603-602bc31a-7b3a-453b-966b-82b1de29d0ea.png)
   
   4. Siéntete libre de jugar todo lo necesario con los scripts y con el contenedor en ejecución, y una vez que hayas terminado asegúrate de remover el contenedor de `PostgreSQL` por medio del comando `docker stop postgres; docker rm postgres`
   
      ![image](https://user-images.githubusercontent.com/71090472/172256034-81ae1b75-f11e-430f-92c6-896aa8204914.png)
   
## Recursos

- <https://www.docker.com/>
- <https://www.postgresql.org/>
- <https://hub.docker.com/_/postgres>
- <http://docs.peewee-orm.com/en/latest/>
- <https://parzibyte.me/blog/2019/06/17/python-postgresql-ejemplo-conexion-crud/>
- <https://cosasdedevs.com/posts/como-crear-un-crud-en-python-parte-4-conexion-a-postgresql/>
- <https://www.fullstackpython.com/object-relational-mappers-orms.html>
- <https://gorm.io/index.html>
- <https://gorm.io/docs/connecting_to_the_database.html>
- <https://gorm.io/docs/models.html>
- <https://gorm.io/docs/create.html>
- <https://gorm.io/docs/query.html>
- <https://gorm.io/docs/update.html>
- <https://gorm.io/docs/delete.html>
- <https://github.com/brianvoe/gofakeit>
