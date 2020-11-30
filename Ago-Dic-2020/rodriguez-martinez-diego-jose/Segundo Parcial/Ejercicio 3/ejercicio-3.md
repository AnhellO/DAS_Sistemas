### Comandos

docker volume create mongo_volume
docker run --name mongo -d -p 27017:27017 --mount source=mongo_volume,destination=/data/db/ mongo:latest
python3 populate.py
python3 find.py
docker stop mongo
docker rm mongo
docker run --name mongo2 -d -p 27017:27017 --mount source=mongo_volume,destination=/data/db/ mongo
python3 find.py

#### ¿Cuál fue nuestra salida en está ocasión?
> La salida debe de ser la misma, ya que le montamos el mismo volumen. Con los volumenes los datos persisten, aun si el contenedor no.