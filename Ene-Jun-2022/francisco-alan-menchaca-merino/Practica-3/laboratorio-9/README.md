# Guía

Esta guía muestra un ejemplo de un contenedor con `PostgreSQL`, el cual podremos visualizar por medio de `pgAdmin`, todo orquestado por medio de `Docker Compose`.

1. Ejecuta el comando `docker-compose up -d --build` y espera a que ambos contenedores estén listos

   ![image](https://user-images.githubusercontent.com/71090472/172155707-5b01f295-5d7e-40f6-8ed2-821f54642844.png)
   
   ![image](https://user-images.githubusercontent.com/71090472/172155785-854fc5f4-2c6b-4657-aa2f-c0ccd751d37f.png)

2. Visita `pgAdmin` por medio de la URL <http://localhost:8080> y haz login con las credenciales que vienen en el [docker-compose.yml](docker-compose.yml)   
   1. `PGADMIN_DEFAULT_EMAIL: admin@example.com`      
   2. `PGADMIN_DEFAULT_PASSWORD: secret123`

      ![image](https://user-images.githubusercontent.com/71090472/172156718-43f6a919-b94e-44e9-9836-0ee0367be461.png)

3. Crea un nuevo server por medio de la interfaz de `pgAdmin` siguiendo los pasos descritos en las imágenes que se adjuntan a continuación. Recuerda que las credenciales que tienes que usar son las que también vienen en el archivo [docker-compose.yml](docker-compose.yml), pero en esta ocasión para el servicio de `db` (`POSTGRES_USER: admin` y `POSTGRES_PASSWORD: secret123`)
   1. [paso-1.png](paso-1.png)
   2. [paso-2.png](paso-2.png)
   3. [paso-3.png](paso-3.png)

   ![image](https://user-images.githubusercontent.com/71090472/172157103-844d02c2-59b1-45d7-81ce-6ddbff9b607c.png)

4. Una vez establecida la conexión con el servidor de `PostgreSQL` correctamente, y en caso de que desees jugar y aprender un poco con la interfaz de `pgAdmin`, puedes referirte a la siguiente documentación para crear una tabla por medio del panel de `pgAdmin`, y después de eso comenzar a insertar registros en ella
   1. <https://www.digitalocean.com/community/tutorials/how-to-install-configure-pgadmin4-server-mode-es#paso-6-crear-una-tabla-en-el-panel-de-pgadmin>
5. Ya que hayas terminado de utilizar los contenedores puedes proceder a removerlos utilizando el comando `docker-compose down -v --rmi all`, esto detendrá y removerá los contenedores en ejecución, juntos a los volúmenes que también se crearon para cada servicio y de paso las imágenes que se descargaron del registro de `Docker`
   
   ![image](https://user-images.githubusercontent.com/71090472/172157769-9758a21b-b281-4491-b6d8-a2088d213b35.png)

## Recursos

- <https://docs.docker.com/compose/>
- <https://www.postgresql.org/>
- <https://hub.docker.com/_/postgres>
- <https://www.pgadmin.org/>
- <https://hub.docker.com/r/dpage/pgadmin4/>
- [Curso de PGAdmin 4 | Tutorial Gratis en Español desde Cero | Parte #1](https://www.youtube.com/watch?v=6q9BXkzAeOM)
- [Curso de PGAdmin 4 | Tutorial Gratis en Español desde Cero | Parte #2](https://www.youtube.com/watch?v=18RWX9qRBPU)
