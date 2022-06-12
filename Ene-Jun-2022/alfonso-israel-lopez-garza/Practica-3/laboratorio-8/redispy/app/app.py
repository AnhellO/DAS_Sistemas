import redis
from faker import Faker

redis_client = redis.Redis(host='redis', port=6379)
faker = Faker()

_keys = [faker.md5() for i in range(0, 500)]

for _key in _keys:
	redis_client.set(_key, faker.email())

print(redis_client.get(_keys[0]))
print(redis_client.get(_keys[1]))
print(redis_client.get(_keys[2]))
print(redis_client.keys())