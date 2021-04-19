Parte 1
docker run --name mysql_db -p 4000:4000 -e MYSQL_ROOT_USER=foo -e MYSQL_ROOT_PASSWORD=bar123 -e MYSQL_DATABASE=baz -d mysql:8

docker exec -it mysql_db bash
mysql -u root -p

Parte 2
docker network create net1
docker run -d -p 27017:27017 --name=m1 --network net1 mongo

docker run -d --name=mexpress --network net1 -e ME_CONFIG_MONGODB_SERVER=m1 -e ME_CONFIG_BASICAUTH_USERNAME=DAS -e ME_CONFIG_BASICAUTH_PASSWORD=abcde123?! -p 8081:8081 mongo-express

docker run -d --name=redis -p 6379:6379 redis