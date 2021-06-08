# Gonzalo Garcia

# SE CREA LA NETWORK
docker network create P2E3

# Iniciamos el volumen
docker volume create --name redis_volume --driver local

# Corremos el contenedor de redis
docker run -d -p 6379:6379 -v redis_volume --network P2E3 --name redis_db_1 redis 

# SACAMOS LA IP del contenedor de redis desde la networ para ponerla en el script de python
Docker network inspect P2E3   
"IPv4Address": "192.168.144.2" Como en el ejercicio anterior las ip puede que cambien 

# Ejecutamos el Dockerfile que construye la imagen
docker build -t gonchologon/redis_json .

# Corremos el contenedor de la imagen respecto al DOCKERFILE 
docker run -d --name redis_json_py --network P2E3 gonchologon/redis_json:latest

# SUBIMOS TODO A DOCKER HUB
docker push gonchologon/redis_jsonz
