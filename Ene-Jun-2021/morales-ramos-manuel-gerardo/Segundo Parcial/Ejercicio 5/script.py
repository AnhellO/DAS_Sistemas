import json, redis

try:
    with open('mock_data.json') as mock_data:
     
        data = json.load(mock_data)

        redis_client = redis.Redis(host='redis', port='6379')

        for e in data:
            id = "{}-{}-{}".format(e['id'], e['first_name'], e['last_name'])

            redis_client.set(id, str(e))
            print(e)

except FileNotFoundError:
    print('The file does not exists.')