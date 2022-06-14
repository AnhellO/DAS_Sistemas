# Guía

Esta guía pretende dar una breve introducción al concepto de "_docker networks_".

1. Docker se encarga de los aspectos de red para que los contenedores puedan comunicarse con otros contenedores y también con el Docker Host. Los contenedores podrán comunicarse con cada uno de los hosts y su configuración de red puede ser altamente personalizable gracias a las Docker networks. Este networking también se puede integrar con "orquestadores" como Docker Compose y Docker Swarm.
2. Puedes ver las redes de Docker disponibles con el comando `docker network ls`

  ![image](https://user-images.githubusercontent.com/71090472/172037577-ca60ada2-d41f-4d0e-96b4-083b1bb88595.png)

3. Puedes inspeccionar la configuración de una red con el comando `docker network inspect networkname`

  ![image](https://user-images.githubusercontent.com/71090472/172037615-338fb7f1-3a46-4d0e-8bc3-b4920db7555d.png)

4. Podemos echar a andar un contenedor de Ubuntu con el siguiente comando `docker run -it -d ubuntu:latest`, y verificar la red default de docker con `docker network inspect bridge`. Esto nos mostrará el contenedor conectado a la red default de Docker

  ![image](https://user-images.githubusercontent.com/71090472/172037962-b52395e8-2262-43dc-a208-277d14bd271b.png)
  
  ![image](https://user-images.githubusercontent.com/71090472/172038052-5e93717d-2b08-4047-9bc7-6faa80465f2f.png)

5. Podemos crear nuestras propias redes más customizables con el comando `docker network create --driver drivername networkname`. El driver default es `bridge`. Intentemos crear una con el siguiente comando: `docker network create --driver bridge my_new_network`

  ![image](https://user-images.githubusercontent.com/71090472/172038137-0a8a3101-a663-4c60-867e-21ad2b24db23.png)

6. Ahora podemos volver a instanciar un nuevo contenedor de Ubuntu pero conectándolo a nuestra propia red: `docker run -it --network my_new_network -d ubuntu:latest`. Y de igual manera, podemos inspeccionar nuestra red utilizando el comando `docker network inspect my_new_network`

  ![image](https://user-images.githubusercontent.com/71090472/172038290-b2ec0a6d-7538-4052-a6f6-77bcd86df119.png)

  ![image](https://user-images.githubusercontent.com/71090472/172038305-bd69aec0-5ff9-4b56-bbf1-d67365fba962.png)  

## Recursos

- <https://docs.docker.com/network/>
