import redis
from time import perf_counter

cliente = redis.Redis(host="0.0.0.0", port=6379)
inicio = perf_counter()
for i in range(0,100):
    cliente.get(str(i))
fin = perf_counter()
print(f"tiempo: {fin-inicio}")