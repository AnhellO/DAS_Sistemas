docker volume create redis_volume

docker network create part3

docker run -d -p 6379:6379 --network=part3 --name redis -v redis_volume redis --protected-mode no

docker inspect part3