import json
import redis

mock_data = open("mock_data.json", 'r').read().replace("[", "").replace("]", "")

values = [json.loads(i) for i in mock_data.split(",\n")]

#valores = [i for i in mock_data.split(",\n")]

keys = [f'{values[i].get("id")}-{values[i].get("first_name")}-{values[i].get("last_name")}' for i in range(len(values))]

redis_client = redis.Redis(host='redis', port=6379)

for i in range(len(values)):
    redis_client.set(keys[i], str(values[i]))

