#Ejercicio 2
#Solución
**Crear 3 contenedores redis y asignarles su nombre**

>   redis:
        container_name: redis1
        ports:
            - "5000:6379"
        image: redis

>   redis2:
        container_name: redis2
        ports:
            - "27027:6379"
        image: redis

>    redis3:
        container_name: redis3
        ports:
            - "6379:6379"
        image: redis

**Crear un cuarto contenedor de redist-commander**
>redis-commander:
        container_name: redis_dbms
        image: rediscommander/redis-commander:latest
        environment:
            - HTTP_USER=DASistemas
            - HTTP_PASSWORD=Ya-Casi-Se-Acaba-El-Semestre!
            - REDIS_HOSTS=redis1,redis2,redis3
        ports:
            - "8081:8081"

**Acceder a http://localhost:8081/ para entrar a Redis Commander**
>Al entrar nos pedira un usuario y contraseña, que serán los que establecimos arriba en nuestro archivo .yml con Docker Compose.

>Podremos ver los 3 contenedores de redis.            