from peewee import *
import sqlite3

baseD = SqliteDatabase('LIBRERIA.db')

class cAutor(Model):
    id = PrimaryKeyField(null=False)
    NOM = TextField()
    AP = TextField()


    class Meta:
        BD = baseD # This model uses the "LIBRERIA.db" database.


    def __str__(self):
        return "ID_AUTOR:{}\nNOMBRE:{}\nAPELLIDO:{}\n".format(self.id,self.NOM,self.AP)



class cEditorial(Model):
    id =PrimaryKeyField(null=False)
    NOMBRE_EDITORIAL = TextField()
    PAIS = TextField()

    class Meta:
        BD = baseD # This model uses the "LIBRERIA.db" database.

    def __str__(self):
        return "NOM:{}\nPAIS:{}\n".format(self.NOMBRE_EDITORIAL,self.PAIS)


class cLibro(Model):
    id =PrimaryKeyField(null=False)
    TITULO = TextField()
    AUTOR_LIBRO = ForeignKeyField(cAutor,related_name="NOM")
    EDITORIAL_LIBRO = ForeignKeyField(cEditorial,related_name="NOMBRE_EDITORIAL")

    class Meta:
        BD = baseD # This model uses the "LIBRERIA.db" database.'

    def __str__(self):
        return "ID_LIBRO:{}\nTITULO:{}\nAUTOR:{}\nEDITORIAL{}\n".format(self.id,self.TITULO,self.AUTOR_LIBRO,self.EDITORIAL_LIBRO)

class CRUDManager:

	@staticmethod
	def store(model, **data):

		model = model.lower()

		if model == 'AUTOR':
			return cAutor.create(**data)
		if model == 'EDITORIAL':
			return cEditorial.create(**data)
		elif model == 'LIBRO':
			return cLibro.create(**data)
		else:
			return 'Modelo no existe'

	@staticmethod
	def select(model, *ids):
		model = model.lower()
		if model == 'AUTOR':
			
			if ids:
				return [str(AUTOR) for AUTOR in cAutor.select().where(cAutor.id << ids)]
			
			return [str(AUTOR) for AUTOR in cAutor.select()]
		else:
			return 'Modelo no existe'

		if model == 'EDITORIAL':
			
			if ids:
				return [str(EDITORIAL) for EDITORIAL in cEditorial.select().where(cEditorial.id << ids)]
			
			return [str(EDITORIAL) for EDITORIAL in cEditorial.select()]
		else:
			return 'Modelo no existe'

		if model == 'LIBRO':
			
			if ids:
				return [str(LIBRO) for LIBRO in cLibro.select().where(cLibro.id << ids)]

				return [str(LIBRO) for LIBRO in cLibro.select()]
		else:
			return 'Modelo no existe'

	@staticmethod
	def update(model, *condicion, **data):
		model = model.lower()

		if model == 'AUTOR':
			return cAutor.update(**data).where(*condicion).execute()
		else:
			return 'Modelo no existe'

		if model == 'EDITORIAL':
			return cEditorial.update(**data).where(*condicion).execute()
		if model == 'LIBRO':
			return cLibro.update(**data).where(*condicion).execute()
		else:
			return 'Modelo no existe'


print(CRUDManager.store('cAutor',NOM = 'Infinity Was',AP = 'super heroes'))
#A = cAutor.select()#.where(cAutor.NOMBRE == 'Infinity Was').get()'''
