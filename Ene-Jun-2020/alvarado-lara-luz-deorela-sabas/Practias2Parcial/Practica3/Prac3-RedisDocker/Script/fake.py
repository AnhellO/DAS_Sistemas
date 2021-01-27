from faker import Faker
import redis

client = redis.Redis(host='localhost', port=6379)

#Funcion para generar 100 emails 
def getData():
    fake = Faker()
    for i in range(100):
        keys = fake.md5()
        email = fake.email()
        client.set(keys, email)
        value1 = client.get(keys)
        #print(keys)
        #print(email)
        print('----------------------------------')
        print(value1)
        print(keys)
        print(email)
        print('----------------------------------')


getData()