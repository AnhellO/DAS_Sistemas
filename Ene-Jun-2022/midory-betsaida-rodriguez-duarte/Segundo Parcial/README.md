# Conclusiones
Se crearon 4 contenedores los cuales son, una base de datos de mongo, creada a partir de su image, DBMS de mongo igualmente creado por su imagen
un contenedor el cual extrae informacion por medio del api de github y la guarda en la base de datos, un contenedor final el cual muestra en paginas los datos recolectados, en este se utiliza flask.

se creo un docker compose para no tener que levantar contenedor por contenedor, aplicamos lo aprendido el clase sobre los docker compose para crearlo y que se levanten todos los servicios con la instruccion docker-compose up -d --build y de igualmanera se detengan y borren con docker-compose down.

# Pasos para ejecutar la aplicacion
- tener docker instalado y una session iniciada
- Ingresar con la terminal al directorio principal en el cual se encuentra el docker compose
- ejecutar la instruccion docker-compose up -d --build

Si se quieren detener solo tendremos que correr el comando
- docker-compose down

#  links