# Práctica 3

Se usaron los sig comandos:

- sudo docker  ps -a ( muestra los contenedores)
- sudo docker images  (muestra las imagenes)
- sudo docker build -t aliciapruebas/static_flask ( crea la imagen basada en el Dockerfile )
- sudo docker images 
- sudo docker login (inicia sesión  con tu cuenta Dockerhub)
- sudo docker push aliciapruebas/static_flask (subir la imagen)
- sudo docker run --name= flask -p 5000:8000  aliciapruebas/static_flask   ( nuevo contenedor basado en la imágen, asignandose el puerto 5000 de mi máquina )
- sudo docker ps -a
- sudo docker stop $(sudo docker stop ps -q -a)( detener contenedores)

Dockerhub:
<https://hub.docker.com/r/aliciapruebas/static_flask>