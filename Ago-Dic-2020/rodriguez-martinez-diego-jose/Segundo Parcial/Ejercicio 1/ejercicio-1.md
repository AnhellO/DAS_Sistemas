### Comandos

docker run -d --name mysql_db -p 4000:3306 -e MYSQL_ROOT_PASSWORD=1 -e MYSQL_DATABASE=baz -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 mysql:8

docker exec -it mysql_db mysql -u foo -p