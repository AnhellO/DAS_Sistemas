from dataclasses import replace
from faker import Faker
from faker.providers import internet

def cambio(file):
    archivo = open(file, 'r+' )
    archivo.read().replace('python', Faker.name())
    print(archivo.read())

cambio('Ene-Jun-2022\carlos-emilio-leos-alcala\Practica4\README.md')