
docker network create networknet

docker run -d -p 27017:27017 --name mongo --network mynetwork mongo

docker run -d -p 6379:6379 --network=mynetwork --name redis redis --protected-mode no




docker exec -it mongo /bin/bash  (Para entrar al CLI de mongo)