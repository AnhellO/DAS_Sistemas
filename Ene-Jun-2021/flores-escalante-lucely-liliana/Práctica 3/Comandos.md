Comandos utilizados:
    cd C:\Users\lulif\Documents\DAS_Sistemas\Ene-Jun-2021\flores-escalante-lucely-liliana\Práctica 3
    docker build -t lucelyflores27/static_flask .
    docker run -d -p 5000:8000 --name prueba lucelyflores27/static_flask
    docker push lucelyflores27/static_flask:latest

Link a la imagen alojada en mi perfil de Docker Hub:
    https://hub.docker.com/r/lucelyflores27/static_flask