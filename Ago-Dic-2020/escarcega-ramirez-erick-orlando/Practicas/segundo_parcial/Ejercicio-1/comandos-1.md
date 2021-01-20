# docker run --name=mysql_db -d -p 4000:3306 -e MYSQL_ROOT_PASSWORD=mypass -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar123 -e MYSQL_DATABASE=baz -t mysql:8


# docker exec -it mysql_db mysql -u foo -p
