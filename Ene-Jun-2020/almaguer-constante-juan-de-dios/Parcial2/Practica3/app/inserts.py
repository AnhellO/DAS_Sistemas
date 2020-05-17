import redis
from faker import Faker

client = redis.Redis(host='redis', port=6379)

fake = Faker()

lista_emails = []
lista_keys = []

for email in range(100):
    email = fake.email()
    lista_emails.append(email)

for key in range(100):
    key = fake.md5()
    lista_keys.append(key)

str_keys = str(lista_keys).strip("[]")
str_emails = str(lista_emails).strip("[]")

dic = dict(zip(lista_keys,lista_emails))

for k,v in dic.items():
    client.set(k,v)
