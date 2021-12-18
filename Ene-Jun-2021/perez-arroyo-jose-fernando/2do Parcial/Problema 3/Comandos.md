docker network create Ejercicio3

docker volume create --name redis_volume --driver local

docker run -d -p 6379:6379 -v redis_volume --network Ejercicio3 --name redis_db_1 redis 

docker build -t dividing69/redis_json .

docker run -d --name redis_json_py --network Ejercicio3 dividing69/redis_json:latest

docker push dividing69/redis_json
