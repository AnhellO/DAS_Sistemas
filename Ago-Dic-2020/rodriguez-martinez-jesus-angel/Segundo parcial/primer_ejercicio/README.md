# Primer ejercicio

Lista de comandos: 
- sudo docker run -d -p 4000:3306 --name mysql_db -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 -e MYSQL_DATABASE=baz -e MYSQL_ROOT_PASSWORD=bar123 mysql/mysql-server:8.0
- sudo docker ps
- sudo docker exec -it mysql_db sh -c "mysql --user=foo --password=bar123"
- SHOW DATABASES;

## Evidencias

![Primera evidencia](primera_evidencia.png)