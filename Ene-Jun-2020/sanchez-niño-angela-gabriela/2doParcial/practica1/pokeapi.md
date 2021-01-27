Link:
https://hub.docker.com/r/gabysanchez/pokeapi
=============================================================================
Pasos:
Comencemos descargando la imagen de docker con el comando:
    $sudo docker pull gabysanchez/pokeapi:1.0
=============================================================================
Despues abriremos nuestra CLI y ejecutaremos lo siguiente:
    $sudo docker images <---- nos mostrara las imágenes del contenedor 
=============================================================================
Para finalizar escribiremos el siguiente comando para correrlo:
    $sudo docker run –it –p 5000:5000 gabysanchez/pokeapi:1.0 
=============================================================================
Notas:
Para poder visualizarla debes de ingresar a la siguiente url en tu navegador:
    http://0.0.0.0:5000
