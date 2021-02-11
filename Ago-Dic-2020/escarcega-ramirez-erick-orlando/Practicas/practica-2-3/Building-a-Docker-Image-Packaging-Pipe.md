# Building a Docker Image Packaging Pipeline Using GitHub Actions | @garethr

A veces la vida es simple, tienes un repositorio con tu codigo y un dockerfiles y quieres crear y publicar una Docker Image en un contenedor de registro unico... y a veces estas empaquetando contenido de terceros, creando muchas variantes imagenes y publicando infinidad de tags al mismo tiempo.

## AGENDA
- Dockerfiles Reusables
- Hello build-push-action
- Un ejemplo Real
- Conclusiones

### Dockerfiles reusables
Evitando la trampa del copy-paste
Un docker file como hemos visto cientos de veces es el standar para construir contenedores de imagenes. 
pero que hacen los dockerfiles??
Estos cream un Filesystem, agregando metadata y tenemos un clasico ejemplo de un docker file donde

**FROM: node:current-slim** utiliza la imagen oficial como una imagen padre
**WORKDIR /usr/src/app** Establece el directorio de trabajo
**COPY package.json .** Copia el archivo del host hacia tu ubicacion actual
**RUN npm install** Corre el comando dentro del systema de archivos de la imagen
**EXPOSE 8080** Le informa a Docker que el contenedor esta escuchando un puerto especifico al tiempo de correr
**CMD ["npm", "start"]** Corre el comando especifico dentro del contenedor

Antes, solo se tenia un dockerfile que creaba una imagen, se corria y todo era excelente.
Se utilizaba el Copy-paste pero con el tiempo ha pasado habia muchos duplicados y archivos inecesarios.
pero que podemos hacer para no caer en esta trampa?
- Docker Build Arg: Crea variables limitads con valores default
- Pasar valores en el tiempo de construccion: De igual manera puedes pasar de local ENV
- Sigue agregando ARGS: Posible para construir dockerfiles muy genericos

One Dockerfile to rule them all, en pocas palabras reduce la duplicacion y mantenimiento general
Muchas mas tecnicas y patrones de dockerfiles como:
- Aliases
- Inheritance
- Logic
- *cabe mecionar el* Multi-stage build *el cual fue utilizado en mi primera practica del segundo parcial ;)*
