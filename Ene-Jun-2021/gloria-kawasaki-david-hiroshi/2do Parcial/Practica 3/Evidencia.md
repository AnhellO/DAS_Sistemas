Para construir la imagen:
    - sudo docker build -t hiroshigk/static_flask .
    (site.py utiliza el puerto 8000 por lo que dentro del dockerfile se expone el mismo puerto)

Para correr la imagen:
    - sudo docker run -d -p 5000:8000 --name prueba hiroshigk/static_flask
    (Se expone el puerto 8000 del contenedor en el puerto 5000 de la maquina host)

Para revisar que el contenedor se executa correctamente:
    - sudo docker ps

Para subir una imagen a Docker Hub:
    -  sudo docker push hiroshigk/static_flask:latest

Y para ver si efectivamente se ejecuta:
    - Abrir navegador
    - entrar en localhost:5000 o http://0.0.0.0:8000/

Link a la imagen alojada en mi perfil de Docker Hub:
    - https://hub.docker.com/r/hiroshigk/static_flask