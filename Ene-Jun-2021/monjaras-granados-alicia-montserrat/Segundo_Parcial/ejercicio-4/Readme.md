# Ejercicio 4

El diagrama que hice empieza por la interface de usuario donde el cliente se comunica con la máquina. Para eso primero el primer proceso que usan es la herramienta de Flask (utilizan para crear aplicaciones web), de ahi flask envia y recibe informacion hacia postgress y redis.
Luego para poderse conectar con SQLAlchemy (Libreroa  SQL para Python)  primero debe de conectarse con el servicio de postgress (gestor de base de datos), donde ahi van a recibir o enviar información. 
Flask  envia las peticiones a el servicio de  redis (almacenamiento de datos en memoria)  y lgo  el  servicio de worker (pide las peticiones y las ejecuta manera asincrona) y por ultimo las muestra en flask.