# Guía

La intención de esta guía es involucrarse con el uso de Dockerfiles y la construcción de imágenes en `Docker`.

1. Clona el repositorio de <https://github.com/AnhellO/pokepy> en esta ubicación
2. Muévete al directorio a través de la CLI y ejecuta el comando `docker build` para construir una nueva imágen de Docker en base al Dockerfile existente en el repositorio, por ejemplo `docker build -t fulanito-hub/pokepy-ejemplo:1.0 .`, donde `fulanito-hub` es el nombre de usuario en `DockerHub`, `pokepy-ejemplo` es el nombre que le vas a poner a tu imagen (puede ser cualquiera, el que tu gustes), y `1.0` la versión de tu imagen (puedes utilizar cualquier versión para este ejemplo)
  
  ![image](https://user-images.githubusercontent.com/71090472/172033965-ff22c74b-5f13-4aa4-8668-7d515caec9ca.png)  

3. Utiliza el comando `docker images` para que puedas listar todas las imágenes existentes en tu computadora o máquina host. Si te das cuenta, la nueva imagen que acabas de construir debería estar listada ahí

  ![image](https://user-images.githubusercontent.com/71090472/172033984-ba8bf2ca-c6b6-429d-81f0-501abc0da97b.png)

4. Instancia un contenedor en base a esa nueva imagen utilizando `docker run`
  
  ![image](https://user-images.githubusercontent.com/71090472/172034008-30ec159b-ced9-4e1b-9ceb-9553fa0d6a70.png)

5. Verifica que tu contenedor está corriendo correctamente por medio de <http://localhost:5000/>
  
  ![image](https://user-images.githubusercontent.com/71090472/172034039-6cb1c807-3421-4f57-abe6-49016057515d.png)

6. Esta imágen existe solamente en tu máquina host, puedes proceder a subirla a tu cuenta de docker hub utilizando el comando [`docker push`](https://docs.docker.com/engine/reference/commandline/push/) o bien, borrarla de tu máquina local con `docker rmi <image-name>`

  ![image](https://user-images.githubusercontent.com/71090472/172034125-8a39727d-7523-41be-88ef-0260bebf1c27.png)
