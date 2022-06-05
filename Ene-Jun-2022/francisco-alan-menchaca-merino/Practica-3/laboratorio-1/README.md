# Guía

Esta guía pretende mostrar paso por paso como ejecutar un par de contenedores de `MySQL` y de `PHPMyAdmin` que estén conectados entre si.

1. Inicia container de MySQL: `docker run --name=db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret-pw -d mysql:8`
   ![img1](https://user-images.githubusercontent.com/71090472/172030305-b4a72f63-7ed1-4925-997e-e992b7113696.png)
   
 1. Puedes revisar los logs del contenedor con `docker logs db`
   ![img2](https://user-images.githubusercontent.com/71090472/172030343-52358707-da0b-4408-a86d-47d26128297b.png)

 2. Puedes conectarte al contenedor con `docker exec -it db bash` y luego conectarte a MySQL por medio del comando `mysql -u root -p`
   ![img3](https://user-images.githubusercontent.com/71090472/172030446-57b64ed5-340a-48e3-8ad6-298613d988ae.png)

 3. Para salir de la terminal interactiva del contenedor, primero hay que salir de `MySQL` por medio de `exit`, y una vez fuera podemos tecler la combinación `Ctrl+P` y `Ctrl+Q` para salir. Esto no detendrá nuestro contenedor
   ![img4](https://user-images.githubusercontent.com/71090472/172030519-3d042a30-06ac-4b83-a763-f1a2921aaa42.png)

2. Inicia container de `PHPMyAdmin`: `docker run --name=my-admin -p 82:80 --link db:db -d phpmyadmin`
   ![img5](https://user-images.githubusercontent.com/71090472/172030580-98fad621-12b9-49f6-b4ae-c4a78c1c369e.png)

   1. Podrás ver tu contenedor de `PHPMyAdmin` corriendo desde <http://localhost:82/>
      ![img6](https://user-images.githubusercontent.com/71090472/172030602-a22fe088-2e87-4c5b-a817-f5a6f9380f44.png)
   
   2. Una vez ahí introduce las credenciales correctas para acceder y comenzar a jugar con tus contenedores
      ![img7](https://user-images.githubusercontent.com/71090472/172030621-d58af324-2f8e-4505-90d5-f398ebeefbe3.png)

3. Una vez que hayas jugado un poco con los contenedores, asegúrate de detenerlos y borrarlos utilizando `docker stop` para detenerlos, y `docker rm` para removerlos
      ![img8](https://user-images.githubusercontent.com/71090472/172030735-1fc70f24-87eb-4aee-a5ef-2c1039e73ba0.png)
      ![img9](https://user-images.githubusercontent.com/71090472/172030784-bd65c8ab-db9a-4e59-8d5a-3fe14000dcdd.png)
      ![img10](https://user-images.githubusercontent.com/71090472/172030803-54af8277-d974-4ccc-af41-f90b1560333e.png)

