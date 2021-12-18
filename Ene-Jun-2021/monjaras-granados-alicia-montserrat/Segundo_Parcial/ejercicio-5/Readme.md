# Ejercicio 5
Toma cualquiera de los 3 primeros ejercicios y trasládalo a que funcione por medio de Docker Compose, tú eliges cual.

Asegúrate de probar que funciona correctamente y no te olvides de adjuntar el archivo docker-compose.yml en la carpeta de tu solución.

- sudo docker-compose up (Inica los contenedores)


- Desde mongo express  cree una base de datos llamada baz
-Igualmente se cree una colección en la base de datos de baz llamada qux
-Por ultimo cree ahi mismo el registro 

- sudo docker stop $(sudo docker ps -q -a) (Detiene los contenedores)