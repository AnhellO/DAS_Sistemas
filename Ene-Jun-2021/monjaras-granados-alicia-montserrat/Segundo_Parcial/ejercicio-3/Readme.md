# Ejercicio 3

 Crea un volumen que se llame redis_volume y que utilice el driver por default para los Docker volumes.
 - sudo docker volume create redis_volume (crear volumen)
 - sudo docker volume inspect redis_volume  (inspecciona volumen)
- docker network create redis_network2 (crear network)

Ejecuta un contenedor de Redis similar a los del ejercicio anterior pero ahora montándole el volúmen que acabas de crear en el paso anterior.

 - sudo docker run -d -p 6376:6379  --network=redis_network2  -v redis_volume:/data   --name redis_ej3 redis --protected-mode no 

Construye una imágen basada en el Dockerfile que acabas de crear y llámala {mi-user}/redis_json, donde {mi-user} equivale a tu usuario de DockerHub. Una vez que hayas creado la imagen envíala a tu cuenta de DockerHub. Debe de estar accesible similar a como lo está en este ejemplo. Asegúrate de adjuntar el link a ella en tus resultados del ejercicio.

- sudo docker build -t aliciapruebas/redis_json .
- sudo docker login inicia sesión con tu cuenta Dockerhub)
- sudo docker push aliciapruebas/redis_json (subir la imagen)

Para finalizar, ejecuta un nuevo contenedor basado en la imágen recién creada que se llame redis_json_py que sirva como muestra de que tu script y tu imagen funcionan correctamente.
- sudo docker run -d --network redis_network2 --name redis_json_py  aliciapruebas/redis_json (crea contenedor nuevo con la imágen de python)
- sudo docker logs redis_json_py 
- docker exec -it redis_ej3 sh (cli de redis desde docker)
- redis-cli
- KEYS * (muestra llaves)
-  SET 1-Adelice-Castillon (agregar llave, valor)
-  GET  1-Adelice-Castillon  (devuelve el valor anterior almacenado en la clave, o nulo cuando la clave no existía.)
-  exit (salir de la consola)
-  sudo docker stop $(sudo docker stop ps -q -a)( detener contenedores)
-  

Dockerhub:
<https://hub.docker.com/r/aliciapruebas/redis_json>