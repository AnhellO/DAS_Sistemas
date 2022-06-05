# Guía

Esta guía parte del [`laboratorio-7`](../laboratorio-7/), pero ahora utilizando `Docker Compose`.

1. Mismo paso, clona el repositorio de `https://github.com/AnhellO/redispy`

   ![image](https://user-images.githubusercontent.com/71090472/172041787-f55d53f8-6302-4c19-acb3-a82141c9152f.png)

2. En esta ocasión haremos uso del archivo `docker-compose.yml` que se encuentra en el mismo directorio, pero ejecutando un nuevo comando: `docker-compose up`
   
   ![image](https://user-images.githubusercontent.com/71090472/172041928-d60e18c3-046e-48b6-b818-008877583d39.png)
   
   ![image](https://user-images.githubusercontent.com/71090472/172042176-8a782045-3470-40d8-be26-db8682944b4f.png)
   
   1. ¿Te das cuenta como con un solo comando, ahora levantamos toda una aplicación (imágenes, network, contenedores)?. Esto es [orquestación de contenedores](https://www.campusmvp.es/recursos/post/las-10-herramientas-mas-importantes-para-orquestacion-de-contenedores-docker.aspx)
      
   2. Puedes ver tus contenedores utilizando `docker ps -a`. En esta ocasión vale la pena que revises los nombres de los mismos, ¿puedes ver como están basados en nuestra configuración del archivo `docker-compose.yml`?
   
      ![image](https://user-images.githubusercontent.com/71090472/172042954-fe77befa-e772-4d7f-a9de-d442f6b23f8e.png)
   
   3. Sigue los pasos 5 y 6 del `laboratorio-7` en caso de que quieras revisar que los contenedores están funcionando correctamente

3. Ahora procederemos a hacer un cambio en nuestro archivo `app.py`. Cambiemos nuestra lista comprimida de `for i in range(0, 100)` a `for i in range(0, 500)`, y seguido de esto reiniciemos nuestro contenedor de `redispy_app` con `docker restart redispy_app`. ¿Puedes ver cómo ahora insertamos 500 nuevos valores en Redis, pero no tuvimos que recrear imágenes ni contenedores?. Esto es gracias a los [volume-bind-mounts](https://docs.docker.com/storage/bind-mounts/) de Docker :wink:
   
   ![image](https://user-images.githubusercontent.com/71090472/172043368-d83c7342-9599-4a17-85bf-a400efb8acec.png)

4. Procedamos a jugar un poco con nuestro archivo `docker-compose.yml`
   1. Detén tu app de docker compose actual utilizando `Ctrl+C`, y después utiliza el comando `docker-compose down` para detener y remover los contenedores y la network. ¿Viste cómo un solo comando volvió a "orquestar" todo este proceso?
   
   ![image](https://user-images.githubusercontent.com/71090472/172043399-d16edfd7-8224-4e2c-9df5-3e8d05ecd920.png)
   
   2. Dentro de la carpeta del repositorio clonado, crea una nueva carpeta llamada `/redis`, y dentro de esa nueva carpeta incluye el [`Dockerfile` que se encuentra en este mismo directorio](Dockerfile)
   3. Cambia las siguientes líneas en el archivo `docker-compose.yml`:
   ``` yml
   redis:
    image: redis:latest
    container_name: redispy_redis
    ports:
      - 6379:6379
    command: ["redis-server"]
   ```
   por estas otras (¡asegúrate de borrar la línea de `command`!):
   ``` yml
   redis:
    build: ./redis
    container_name: redispy_redis
    ports:
      - 6379:6379
   ```
   1. Guarda los cambios y vuelve a ejecutar tu comando de `docker-compose up`, pero ahora agregando el parámetro `--build` (que reconstruirá las imágenes de docker) y el parámetro `-d` (que ejecutará los contenedores en el "background")
      1. OJO: En caso de que esto no funcione, prueba deteniendo la app, borrando tus imágenes anteriores de redis con `docker rmi redispy_app redispy_redis`, y volviendo a ejecutar el comando `docker-compose up --build -d`
      2. ¿Puedes ver como ahora construimos nuestra propia imágen de Redis a nuestra medida, y la "orquestamos" dentro de nuestro archivo de configuración del `docker-compose.yml` file?
      3. ¡Siéntete libre de seguir jugando con el archivo YAML y agregar/quitar lo que tú quieras!

      ![image](https://user-images.githubusercontent.com/71090472/172043789-2acc824d-f715-4c4b-89b0-6ea2fcd04694.png)

## Recursos

- <https://yaml.org/>
- <https://docs.docker.com/compose/>
