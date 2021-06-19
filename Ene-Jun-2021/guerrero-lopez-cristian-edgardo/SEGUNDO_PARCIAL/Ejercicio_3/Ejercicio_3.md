Ejercicio 3

Comandos ejecutados:

1.- docker network create p2e3
2.- docker volume create redis_volume
3.- docker run -d -p 6379:6379 -v redis_volume --network p2e3 --name redis_db1 redis --protected-mode no
4.- docker build -t kryz73/redis_json .
5.- docker push kryz73/redis_json
6.- docker run -d --network p2e3 --name ejercicio_3 kryz73/redis_json