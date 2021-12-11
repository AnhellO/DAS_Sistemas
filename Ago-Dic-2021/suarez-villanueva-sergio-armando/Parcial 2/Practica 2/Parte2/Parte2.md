CONTENEDORES
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

CONTENEDOR REDIST COMMANDER
>redis-commander:
        container_name: redis_dbms
        image: rediscommander/redis-commander:latest
        environment:
            - HTTP_USER = DASistemas
            - HTTP_PASSWORD = Ya-Casi-Se-Acaba-El-Semestre!
            - REDIS_HOSTS = redis1,redis2,redis3
        ports:
            - "8081:8081"