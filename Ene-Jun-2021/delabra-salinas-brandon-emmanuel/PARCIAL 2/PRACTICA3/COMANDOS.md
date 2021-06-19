COMANDOS UTILIZADOS:

1.- ACCEDER A LA DIRECCIÓN 
    CD C:\Users\brand\OneDrive\Escritorio\BREND ESCUELA 2\7 semestre\DISEÑO Y ARQUITECTURA\DAS_Sistemas\Ene-Jun-2021\delabra-salinas-brandon-emmanuel\PARCIAL 2\PRACTICA3

2.- CREAR LA IMAGEN BASADO EN DOCKERFILE
    docker build -t brend303/static_flask . 

3.- VERIFICAR LAS IMAGENES CREADAS    
    docker images

4.- CONECTAR CON D0CKER HUB
    docker login 

5.- PUSH DE LA IMAGEN
    docker push brend303/static_flask 

6.-ASIGNANDO PUERTO 5000
    docker run --name= flask -p 5000:8000  brend303/static_flask   


DOCKERHUB
https://hub.docker.com/r/brend303/static_flask