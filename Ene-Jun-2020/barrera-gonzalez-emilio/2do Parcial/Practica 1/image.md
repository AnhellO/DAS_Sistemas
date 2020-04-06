###LINK
https://hub.docker.com/repository/docker/emiliobg1997/pokepy
##Instrucciones
1. DESCARGA LA IMAGEN:

>sudo docker pull emiliobg1997/pokepy:1.0

2. CORRER LA IMAGEN
    - Verificar que la imagen este descargada:
    > sudo docker images
    - Correr la imagen
    > sudo docker run -it -p 5000:5000 emiliobg1997/pokepy:1.0

3. Enjoy:
    - Abre tu navegador e ingresa a la url http://0.0.0.0:5000 y obten un Pokemon aleatorio
    - Alternativamente, puedes escoger tu mismo un pokemon de la siguiente forma: http://0.0.0.0:5000/POKEMON
    sustituyendo la palabra POKEMON por tu monstruo preferido (ej: http://0.0.0.0:5000/charizard)

