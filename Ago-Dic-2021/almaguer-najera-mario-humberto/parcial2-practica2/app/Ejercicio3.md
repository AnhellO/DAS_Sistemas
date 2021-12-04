#Ejercicio 3
*Ejecuta un contenedor de Redis similar a los del ejercicio anterior pero ahora montándole el volúmen que acabas de crear en el paso anterior.

**Crea un Dockerfile que cumpla con los siguientes requisitos:**

    Que extienda de la imágen base de Python3
    Que utilice el directorio /app como el directorio de trabajo
    Que instale todas las dependencias necesarias para este ejercicio por medio de pip
    Que monte el volumen de redis_volume creado previamente
    Y finalmente que ejecute un script de Python el cual inserte los registros del archivo mock_data.json en el servidor de Redis uno por uno de la siguiente forma
        {id}-{first_name}-{last_name} como llave
        json_record como valor
        Por ejemplo, si insertáramos el 1er registro del archivo JSON en el server de Redis de acuerdo al criterio anterior entonces esto luciría así a través de una simple instrucción en Redis: SET 1-Adelice-Castillon '{"id":1,"first_name":"Adelice","last_name":"Castillon","email":"acastillon0@intel.com","gender":"Male","ip_address":"110.188.66.73","school_number":"ca2bae7e-c200-4c5b-97ba-f14407cb19c5"}'
    Es completamente opcional crear un contenedor con Redis Commander para revisar los resultados en el contenedor de Redis

#Solucion
**Crear mi docker-compose.yml**
>
    version: '3.3'

    services:
        redis:
            container_name: redis_db
            ports:
                - "5000:6379"
            image: redis
            volumes:
                - redis_volume:/app

    redis-commander:
            container_name: redis_dbms
            image: rediscommander/redis-commander:latest
            environment:
                - HTTP_USER=admin
                - HTTP_PASSWORD=admin
                - REDIS_HOSTS=redis_db
            ports:
                - "8081:8081"            

    volumes:
        redis_volume:
            external: false

**Crear mi app.py**
>
    import redis
    import json

    print("SE EJECUTO CORRECTAMENTE LA APP")

    r = redis.Redis(host='redis_db', port=6379, decode_responses=True) #Docker
    file = open('mock_data.json')
    data = json.load(file)

    for i in range(0, 99):
        r.set('id{}'.format(data[i]['id']), 'first_name{}'.format(data[i]['first_name']), 'last_name{}'.format(data[i]['last_name']), 'email{}'.format(data[i]['gender']), 'ip_address{}'.format(data[i]['ip_address']), 'school_numer{}'.format(data[i]['school_number']))            

**Crear requirements.txt**
>
    redis

**Crear mi Dockerfile**
>
    FROM python:3.8
    WORKDIR ./app

    COPY requirements.txt .

    RUN pip install -r requirements.txt

    COPY . .

    RUN python ./app.py
    CMD ["python", "./app.py"]

**Finalmente**
Verificar resultados desde Redis Commander    