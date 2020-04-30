from peewee import *

# Mappea con la DB
db = SqliteDatabase('pokemon.db')

# ORM con una tabla
class Pokemon(Model):
	nombre = CharField()
	tipos = CharField()
	imagen = CharField()

	class Meta:
		database = db

# Conectate a la DB
db.connect()

# Obtén solo un registro
pokemon = Pokemon.get()
print(f"ID: {pokemon.id}\nNombre: {pokemon.nombre}\nTipos: {pokemon.tipos}\nimagen: {pokemon.imagen}\n")

# Añade un nuevo registro
charizard = Pokemon.get_or_create(nombre='Charizard', tipos='Fuego,Volador', imagen='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png')
print(charizard)

# Obtén múltiples registros
pokemon = Pokemon.select()
for _pokemon in pokemon:
	print(f"ID: {_pokemon.id}\nNombre: {_pokemon.nombre}\nTipos: {_pokemon.tipos}\nimagen: {_pokemon.imagen}\n")

listita = [_pokemon.nombre for _pokemon in pokemon]
print(listita)

# *Siempre* cierra la conexión
db.close()