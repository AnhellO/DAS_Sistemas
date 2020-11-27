# Comandos utilizados para crear volumen y contenedores:
- Crear volumen: docker volume create mongo_volume
- Contenedor de mongo con el volume : docker run --name mongo -v mongo_volume:/data/db -d -p 27017:27017 mongo:latest
- Ejecutar el archivo populate: python populate.py
- Ejecutar el archivo find: python find.py
- Detener y borrar el contenedor de mongo: 
docker stop mongo
docker rm mongo
- Contenedor de mongo2 con el volume: docker run --name mongo2 -v mongo_volume:/data/db -d -p 27017:27017 mongo:latest
#### ¿Cual fue la salida al ejecutar el find.py por segunda vez con el contenedor mongo2?
La salida fue la misma que se dio la primera vez que se ejecuto el find.py, creo que
esto se debe gracias al volume, como habíamos visto en clase en los contenedores
como tal no existe la persistencia de datos, osea que si hiciste algo en un
contenedor y después lo detienes y borras pierdes la información que tenías dentro,
pero si creas un volumen y montas un contenedor con ese volume cuando pares y borres
tu contenedor los datos van a persisitir, se van a quedar guardados en el volumen en
la ruta que se especifico, así fue como creando un contenedor que también hiciera
uso de el volume que creamos puede acceder a los datos que habíamos ingresado en el
primer contenedor.

### Comando que use para llegar hasta la carpeta del ejercicio
cd desktop\universidad\diseño y arquitectura de software\das_sistemas\ago-dic-2020\salazar-coronado-juan-daniel\segundo parcial\ejercicio3