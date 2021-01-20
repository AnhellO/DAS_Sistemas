# Soluciones

A continuación se presentan las soluciones propuestas para los ejercicios del examen extraordinario.

## Ejercicio 1

- Solución disponible en el archivo [`figuras.py`](ejercicio-1/figuras.py)

## Ejercicio 2

- Solución disponible en el archivo [`factory_method.py`](ejercicio-2/factory_method.py)

## Ejercicio 3

- Creamos una network para que los contenedores puedan comunicarse: `docker network create mongo`
- Contenedor de `MongoDB`: `docker run --network mongo -d -p 27017:27017 --name m1 mongo`
- Contenedor de `Mongo Express`: `docker run --network mongo -d -p 8081:8081 -e ME_CONFIG_MONGODB_SERVER=m1 -e ME_CONFIG_BASICAUTH_USERNAME=DAS -e ME_CONFIG_BASICAUTH_PASSWORD=extra123 --name mexpress mongo-express`

## Ejercicio 4

- El Dockerfile debe de quedar algo como [esto](ejercicio-4/Dockerfile)
- Para crear la imagen con la versión correcta se utiliza el siguiente comando: `docker build -t "anhellojz/hello_flask:extraordinario" --no-cache .`
- Instanciamos el contenedor basado en la imágen con el comando `docker run -d -p 9999:8000 --name hflask anhellojz/hello_flask`
- Finalmente hacemos push a nuestro registro de `Docker` con el comando `docker push anhellojz/hello_flask:extraordinario`
  - Si no estamos loggeados, basta con utilizar el comando `docker login -u anhellojz -p`

## Ejercicio 5

- El archivo `docker-compose` debe de quedar similar a [este](ejercicio-5/docker-compose.yml)
- Por otro lado, el Dockerfile para el 3er contenedor debería de lucir similar a [este ejemplo](ejercicio-5/app/Dockerfile)
  - Tenemos que asegurarnos de instalar todas las dependencias necesarias en el mismo
- Lo demás bastaría con ejecutar el comando `docker-compose -d --build`
  - Deberíamos de poder ver que el proceso para guardar los países en la DB se ejecutó con éxito utilizando `docker logs nombre-del-3er-contenedor`
  - También deberíamos de poder revisar los registros a través de la URL del contenedor de `PHPMyAdmin`, por ejemplo <http://localhost:8080/>
