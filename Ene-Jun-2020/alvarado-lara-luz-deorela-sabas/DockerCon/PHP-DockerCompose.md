# How to Create PHP Development Environments with Docker Compose

En esta charla vimos como crear un entorno de desarrollo PHP con docker Compose,
utilizando una aplicacion Laravel6. Observamos como definir e integrar servicios,
como compartir archivos entre contenedores y como administrar su entorno con los comandos
de Docker Compose. 

Gracias a la popularizacion de micoroservicios y sistemas distribuidos, los contenedores se
convirtieron en una opcion popular para crear entornos livianos y desechables que se pueden 
replicar y distribuir facilmente. Docker compose se creo para facilitar la administracion de entornos Docker que requieren multiples conteneodres de servicios. 

## Talk Goals 
- **Part 1:** PHP development environments in the wild, how Docker compose fits in 
- **Part 2:** Building a multi-container environment for Laravel with Docker Compose
- **Part 3:** Demo

## Environment Needs 
### Web Server: Ngnix (pre-built image)
Use Ngnix to serve the application in our development environment
### PHP-FPM (Image based on custom Dockerfile)
PHP-FPM is required to parse the PHP content an return the results to Ngnix
### Database: MySQL (pre-built image)
The application uses a MySQL database to store places an mark them as "visited" or "to go"

### Acquired knowledge
#### Using Docker Compose
**docker-compose [comand]**
#### Controlling the environment
- up | down | stop | start
#### Monitoring & Troubleshooting
- ps | logs | top | kill
#### Executing Commands on containers 
- exec **service_name** *command*
