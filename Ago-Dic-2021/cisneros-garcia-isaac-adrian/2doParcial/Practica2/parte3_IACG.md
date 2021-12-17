  # Parte 3 (Docker-compose)
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

>
    import redis
    import json
    print("SE EJECUTO CORRECTAMENTE LA APP")

    r = redis.Redis(host='redis_db', port=6379, decode_responses=True) #Docker
    file = open('mock_data.json')
    data = json.load(file)

    for i in range(0, 99):
        r.set('id{}'.format(data[i]['id']), 'first_name{}'.format(data[i]['first_name']), 'last_name{}'.format(data[i]['last_name']), 'email{}'.format(data[i]['gender']), 'ip_address{}'.format(data[i]['ip_address']), 'school_numer{}'.format(data[i]['school_number']))            

>
    redis
>
    FROM python:3.8
    WORKDIR ./app
    COPY requirements.txt .

    RUN pip install -r requirements.txt

    COPY . .

    RUN python ./app.py
    CMD ["python", "./app.py"]
