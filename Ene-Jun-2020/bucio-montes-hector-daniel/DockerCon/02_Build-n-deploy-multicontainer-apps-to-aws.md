### Build & Deploy Multi-Container Applications to AWS

En esta charla el ingeniero en software Lukonde Mwila nos habló sobre cómo compilar e implementar 
una aplicación de contenedores múltiples en AWS (Amazon Web Services, es una colección de servicios 
de computación en la nube).
Luke menciona que lo que lo inspiró a dar esta plática fue la fantástica portabilidad y consistencia que 
obtenemos con Docker, luego nos comienza a hablar sobre Docker compose diciendo que Docker compose 
es una herramienta CLI separada que es realmente útil cuando se trata de correr múltiples contenedores 
al mismo tiempo, pero que de igual manera lo podemos utilizar para un solo contenedor si así lo deseamos 
y que realmente nos ayuda a eliminar el que tengamos que correr muchos de los comandos repetitivos que 
tendríamos que ejecutar cuando usemos Docker CLI, además de que lo hace de una manera más eficiente.

Después nos muestra que dentro de su Docker compose los contenedores que ejecuta, no tienen ninguna 
comunicación automática ya que son básicamente procesos aislados, cuenta con 4 contenedores los cuales
se van a construir y nos vuelve a recalcar que cada uno de ellos es un proceso por separado pero que si
queremos que se comuniquen, su contenedor de Nginx(contenedor 1) va a hacer solicitudes de proxying a través 
del cliente que es React (contenedor 2) y al backend que es NodeJS (contenedor 3) y no solo eso, el contenedor de
NodeJS también necesita comunicarse con la base de datos que es MongoDB (contenedor 4), igual menciona que 
todo eso lo podría resolver configurando la infraestructura de red y que para eso tendría que usar Docker CLI 
porque tiene funciones de red pero que todo eso puede llegar a ser un proceso muy laborioso por lo que decide 
utilizar Docker compose ya que se encargará de realizar todo eso por nosotros automáticamente.
Por último lo que hace es configurar su archivo buildspec.yml para la etapa de construcción y luego configura un
archivo Dockerrun.aws.json que es un archivo específico para Elastic Beanstalk (EB es un servicio de AWS que permite
crear aplicaciones y desplegarlas a un conjunto definido de servicios de AWS que incluye Amazon EC2, Amazon S3, etc.)
que especificará cómo quiere desplegar los contenedores y eso se transmitirá a ECS (Elastic Container Service) 
y después configura una variable de entorno en Elastic Beanstalk (que lo utiliza como el servicio o plataforma 
para ejecutar su aplicación).

Lo aprendido en esta charla fue:

	- Obtuve más información acerca de como funciona Docker compose, además de ver lo útil que es ésta
	  herramienta para todos aquellos desarrolladores que ya tienen tiempo en esto, ya que les facilita más 
	  su trabajo y fue bueno dar un repaso al ver un poquito más a detalle el archivo, ya que Luke fue explicando 
	  cosa por cosa aunque igual de una manera rápida ya que las charlas son cortas y no cuenta con mucho 
	  tiempo como para ser muy específico en todo, aunque el tema es muy interesante, considero que haría falta 
	  dedicarle un muy buen tiempo a todo esto para comprenderlo completamente.