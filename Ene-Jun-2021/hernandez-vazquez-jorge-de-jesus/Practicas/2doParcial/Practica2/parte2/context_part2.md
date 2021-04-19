Comandos de docker:

    docker network create mynetwork 

    docker run -d -p 27017:27017 --name m1 --network mynetwork mongo 

    docker run -d --name mexpress --network mynetwork -e ME_CONFIG_MONGODB_SERVER=m1 -e ME_CONFIG_BASICAUTH_USERNAME=DAS -e ME_CONFIG_BASICAUTH_PASSWORD=abcde123?! -p 8081:8081 mongo-express