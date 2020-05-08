import redis

client = redis.Redis(host='localhost', port=6379)
client.set('digimon-2', 'garurumon') # SET {llave/key} {valor/value}

digimon_1 = client.get('digimon-1')
digimon_2 = client.get('digimon-2')

print(digimon_1)
print(digimon_2)