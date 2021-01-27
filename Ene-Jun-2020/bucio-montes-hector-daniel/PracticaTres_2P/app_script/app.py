from faker import Faker
import redis

client = redis.Redis(host='localhost', port=6379)


def get_information():
    fake = Faker(['es_MX'])
    for i in range(100):
        llaves = fake.sha256()
        email = fake.email('wadek.mx')
        client.set(llaves, email)
        # p = client.get(llaves)

        # print(p)
        print(llaves)
        print(email)
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')


get_information()
