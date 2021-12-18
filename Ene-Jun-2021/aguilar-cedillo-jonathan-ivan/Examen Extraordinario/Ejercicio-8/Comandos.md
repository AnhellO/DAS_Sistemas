#comando
docker run --name database_mysql -d -p 4444:4444 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_USER=extra -e MYSQL_PASSWORD=ordinario123! -e MYSQL_DATABASE=pruebas mysql:8

#comandos para entrar al container
docker exec -it database_mysql bash
mysql -u root -p

#segunda parte 
# entrar a la carpeta en donde está el docker-compose.yml y correr
docker compose up -d 