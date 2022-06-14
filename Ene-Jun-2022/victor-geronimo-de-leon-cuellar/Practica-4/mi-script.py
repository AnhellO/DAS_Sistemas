from faker import Faker
import faker

fake = Faker()

lectura = open("practica4/README.MD") 

for i in lectura.readlines():
    print(i.lower().replace("python", fake.name())) 