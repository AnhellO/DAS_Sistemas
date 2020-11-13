from peewee import *

# Mappea con la DB
db = PostgresqlDatabase('random_cats',
                        user='admin',
                        password='secret123',
                        host='localhost',
                        port=5432)

# ORM con una tabla
class MyCats(Model):
	nombre = CharField()
	imagen = CharField()

	class Meta:
		database = db
		table_name = 'my_cats'

# Conectate a la DB
db.connect()

# Obtén solo un registro
cat = MyCats.get()
print(f"ID: {cat.id}\nNombre: {cat.nombre}\nImagen: {cat.imagen}")

# Añade un nuevo registro
charizardo = MyCats.get_or_create(nombre='Charizardo', imagen='https://purr.objects-us-east-1.dream.io/i/G4Iu1.jpg')
print(charizardo)

# Obtén múltiples registros
cat = MyCats.select()
for _cat in cat:
	print(f"ID: {_cat.id}\nNombre: {_cat.nombre}\nImagen: {_cat.imagen}\n")

listita = [_cat.nombre for _cat in cat]
print(listita)

# *Siempre* cierra la conexión
db.close()