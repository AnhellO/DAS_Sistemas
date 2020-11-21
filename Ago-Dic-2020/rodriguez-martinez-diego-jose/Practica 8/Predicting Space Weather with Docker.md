# Práctica 8 | Dockercon2020  | 17284052

## Predicting Space Weather with Docker
----
  - [Por que eligieron Docker?](#por-que-eligieron-docker-?)
  - [Nuevos artifacts de deployment](#Nuevos-artifacts-de-deployment)
  - [Deployment steps](#deployment-steps)

----

### Por que eligieron Docker?
* El software científico tiene muchas dependencias y requisitos complicados
* Necesitaban tener deployment mas sencillo
* Como era un proyecto del gobierno, no podian usar la nube, por motivos de seguriad
* la arquitectura de los proyectos eran "un enorme desastre monolítico"

La arquitectura ctual de sus proyectos estaba profundamente acoplada, habia hardcode, y muchas malas practicas,  resulto ser mas facil aprender nuevas tecnologias, cambiar el modelo, que seguir trabajando con el modelo antiguo

Docker les permitio hacer portable software cientifico que antes no lo era, por dentro el contenedor se puede ver complicado, pero por fuera es el mismo proceso, trabajar con ellos.

### Nuevos artifacts de deployment
1. docker-compose.yml: define las relaciones entre los servicios, y con el host
2. .env: aísla las diferencias entre los hosts
3. service-name.env: un config para cada servicio
4. docker images: hosteados en su registry interno

### Deployment steps
1. Hacer cuenta en el host objetivo
2. Configurar docker-compose.yml, .env, y service*.env
3. Añade una cuenta de bot en el puerto. El Docker entra en el registro interno con esa cuenta
4. docker-componer -d; docker-copular registros -f

Listo, un proceso que antes les podria haber tomado una semana, ahora le tomaba al equipo menos de un dia. con Docker y Docker compose, pudieron altamente simplificar el proceso de predecir el clima del espacio.