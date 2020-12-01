# Parcial 2 - Práctica 1

#### Importante
_Para evitar conflictos con las carpetas, es necesario que todos los
comandos del CLI sean ejecutados estando dentro de la carpeta
de la práctica 1 (Es decir, aquí mismo)._

#### Explicación

En esta práctica se crean 3 contenedores:
1. Con la base de datos de **Mongo**.
2. Con el **phpmoadmin**, que se conecta al primer contenedor.
3. El último con los scripts que llenan la BD y muestran la información ([populate.py](/scripts/populate.py) y [find.py](/scripts/find.py)), este último también se conecta con el primer contenedor.

#### Comandos
Los comandos en orden a ejecutar son los siguientes:

```
docker build -t practica-1 .
docker run -d --name="mongo-co" mongo
docker run --name moadmin -d --link mongo-co:db -p 8080:80 thinkcube/phpmoadmin
docker run -it --link mongo-co practica-1
```

**Orden de ejecución:**
1. Primero creo la imagen del [dockerfile](Dockerfile).
2. Inicio el contenedor de mongo.
3. Inicio el contenedor de phpmoadmin, haciendo _linking_ hacia el contenedor de mongo.
4. Inicio el contenedor para poblar la BD y mostrar la información (En modo interactivo), haciendo _linking_ hacia el contenedor de mongo.