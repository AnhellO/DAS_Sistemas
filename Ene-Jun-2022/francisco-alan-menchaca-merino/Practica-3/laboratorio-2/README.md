# Guía

Esta guía pretende mostrar paso por paso como ejecutar un contenedor que corre `MongoDB` y con el cual nos conectaremos por medio de `Python`

1. Iniciar el container de `MongoDB` utilizando el comando `docker run -d -p 27017:27017 --name m1 mongo`

   ![image](https://user-images.githubusercontent.com/71090472/172030914-4679abc4-bf10-4d57-8a49-58da0e748a3f.png)

   1. Puedes conectarte al contenedor de Mongo con `docker exec -it m1 /bin/bash` y luego conectarte a `MongoDB` por medio del comando `mongo`

      ![image](https://user-images.githubusercontent.com/71090472/172030955-adb10d9b-eb11-4fe6-b5e3-151c615bf3c1.png)

   2. Para salir de la terminal interactiva del contenedor, primero hay que salir de `MongoDB` tecleando el comando `exit`, y una vez fuera podemos tecler la combinación `Ctrl+P` y `Ctrl+Q` para salir
     
      ![image](https://user-images.githubusercontent.com/71090472/172030966-798bfd7c-339d-4127-b244-ccc7149a3456.png)

2. Utilizaremos los scripts de `Python` existentes en la carpeta para popular la colección de mongo, utilizando la librería <https://api.mongodb.com/python/current/tutorial.html>
   1. Instalar la librería de mongo por medio del comando `pip install pymongo`
      
      ![image](https://user-images.githubusercontent.com/71090472/172031003-f00fb3c4-47f5-45fe-a23d-5bbc90035ad5.png)

   2. Ejecuta los scripts con `python populate.py` y `python find.py`
      
      ![image](https://user-images.githubusercontent.com/71090472/172031391-7761dfc8-9460-4817-b470-ddc64e6bea32.png)      

   3. Revisa los registros por medio del CLI de `mongo` o de tu DBMS favorito

      ![image](https://user-images.githubusercontent.com/71090472/172031449-b02e7015-dbdd-4e00-b330-fcb746af63fb.png)

3. Una vez que hayas terminado de jugar con `MongoDB` y los scripts de `Python`, asegúrate de detener y remover el contenedor de `MongoDB` en ejecución utilizando `docker stop m1; docker rm m1`
   
   ![image](https://user-images.githubusercontent.com/71090472/172031548-2c829647-8abf-443b-af30-a7329d02abbe.png)
   
   ![image](https://user-images.githubusercontent.com/71090472/172031567-1ad1be57-bf6a-4cbb-a478-d551ab716cd2.png)


      

