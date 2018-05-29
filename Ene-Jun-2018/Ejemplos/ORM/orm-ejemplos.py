from peewee import *

db = SqliteDatabase('DAS.db')

class Usuario(Model):
    id = IntegerField()
    nombre = TextField()
    edad = IntegerField()

    class Meta:
        database = db # This model uses the "DAS.db" database.

    def __str__(self):
        return "Nombre:{}\nEdad:{}\n".format(self.nombre, self.edad)

class Pelicula(Model):
    id = IntegerField()
    nombre = TextField()
    genero = TextField()

    class Meta:
        database = db # This model uses the "DAS.db" database.

    def __str__(self):
        return "Nombre:{}\nGenero:{}\n".format(self.nombre, self.genero)

class CRUDManager:

	@staticmethod
	def store(model, **data):
		model = model.lower()

		if model == 'usuario':
			return Usuario.create(**data)
		if model == 'pelicula':
			return Pelicula.create(**data)
		else:
			return 'Modelo no existe'

	@staticmethod
	def select(model, *ids):
		model = model.lower()
		if model == 'usuario':
			
			if ids:
				return [str(usuario) for usuario in Usuario.select().where(Usuario.id << ids)]
			
			return [str(usuario) for usuario in Usuario.select()]
		else:
			return 'Modelo no existe'

	@staticmethod
	def update(model, *condicion, **data):
		model = model.lower()

		if model == 'pelicula':
			return Pelicula.update(**data).where(*condicion).execute()
		else:
			return 'Modelo no existe'


# print(CRUDManager.store('Pelicula', nombre='Infinity Was', genero='super heroes'))
# pelicula = Pelicula.select().where(Pelicula.nombre == 'Infinity Was').get()
# print(pelicula)
data = {'id':666, 'nombre':'Infinity War'}
print(CRUDManager.update('peliculA', Pelicula.nombre == 'Infinity Was', Pelicula.genero == 'super heroes', **data))

# sujeto2 = Usuario.create(id=9818, nombre='Claudia', edad=18)

# sujeto = Usuario.get(Usuario.id == 666)
# print(sujeto)

# sujeto.edad = 18
# sujeto.save()
# print(sujeto)


# for usuario in Usuario.select():
#     print(usuario)
