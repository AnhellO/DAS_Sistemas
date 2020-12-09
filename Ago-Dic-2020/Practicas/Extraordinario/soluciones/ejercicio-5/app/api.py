import requests
import json
from peewee import *

# Crea conexión con la DB
db = MySQLDatabase(
    'ejercicio_5',
    user='root',
    password='extra-admin123',
    host='mysql',
    port=3306
)

# ORM con la tabla
class Country(Model):
	name = CharField()
	alpha_3_code = CharField()
	capital = CharField()
	region = CharField()
	subregion = CharField()
	population = IntegerField()
	flag = CharField()

	class Meta:
		database = db
		table_name = 'countries'

	def __str__(self):
		return f"ID: {self.id}\nNombre: {self.name}\nBandera: {self.flag}"

# Conectate a la DB
db.connect()
print("¡Conectado!")

r = requests.get('https://restcountries.eu/rest/v2/all')
if r.status_code != 200:
    raise Exception(f'Invalid status code "{r.status_code}" from API.')

for c in r.json():
    # Añade un nuevo registro si es que no existe
    country = Country.get_or_create(
        population=c.get('population', -1),
        name=c.get('name', ''),
        alpha_3_code=c.get('alpha3Code', ''),
        capital=c.get('capital', ''),
        region=c.get('region', ''),
        subregion=c.get('subregion', ''),
        flag=c.get('flag', '')
    )
    print("Registro:")
    print(country)

# Cierra la conexión
db.close()