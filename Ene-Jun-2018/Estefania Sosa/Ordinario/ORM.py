from peewee import *
#import sqlite3

baseD = SqliteDatabase('LIBRERIA.db')

class AUTOR(Model):
    ID_AUTOR = PrimaryKeyField(null=False)
    NOMBRE = TextField(null=False)
    APELLIDO = TextField(null=False)


    class Meta:
        database = baseD # This model uses the "LIBRERIA.db" database.


    def __str__(self):
        return "ID_AUTOR:{}\nNOMBRE:{}\nAPELLIDO:{}\n".format(self.ID_AUTOR,self.NOMBRE,self.APELLIDO)



class EDITORIAL(Model):
    ID_EDITORIAL =PrimaryKeyField(null=False)
    NOMBRE_EDITORIAL = TextField()
    PAIS = TextField()

    class Meta:
        database = baseD # This model uses the "LIBRERIA.db" database.

    def __str__(self):
        return "ID_EDITORIAL:{}\nNOMBRE_EDITORIAL{}\nPAIS:{}\n".format(self.ID_EDITORIAL,self.NOMBRE_EDITORIAL,self.PAIS)


class LIBRO(Model):
    ID_LIBRO =PrimaryKeyField(null=False)
    TITULO = TextField()
    AUTOR_LIBRO = ForeignKeyField(AUTOR,related_name="NOMBRE")
    EDITORIAL_LIBRO = ForeignKeyField(EDITORIAL,related_name="NOMBRE_EDITORIAL")

    class Meta:
        database = baseD # This model uses the "LIBRERIA.db" database.'

    def __str__(self):
        return "ID_LIBRO{}/nTITULO:{}\nAUTOR:{}\nEDITORIAL{}\n".format(self.ID_LIBRO,self.TITULO,self.AUTOR_LIBRO,self.EDITORIAL_LIBRO)

class CRUDManager:

	@staticmethod
	def store(model, **data):

		model = model.lower()
		print(model)
		print(data)

		if model == 'autor':
			return AUTOR.create(**data)
		elif model == 'editorial':
			return EDITORIAL.create(**data)
		elif model == 'libro':
			return LIBRO.create(**data)
		else:
			return 'Modelo no existe'
'''
	@staticmethod
	def select(model, *ids):
		model = model.lower()
		if model == 'autor':
			if ids:
				return [str(autor) for autor in AUTOR.select().where(AUTOR.id << ids)]

				return [str(autor) for autor in AUTOR.select()]
		if model == 'editorial':
			if ids:
				return [str(editorial) for editorial in EDITORIAL.select().where(EDITORIAL.id << ids)]

				return [str(editorial) for editorial in EDITORIAL.select()]

		if model == 'libro':

			if ids:
				return [str(libro) for libro in LIBRO.select().where(LIBRO.id << ids)]

				return [str(libro) for libro in LIBRO.select()]
		else:
			return 'Modelo no existe'

	@staticmethod
	def update(model, *condicion, **data):
		model = model.lower()

		if model == 'autor':
			return AUTOR.update(**data).where(*condicion).execute()
		else:
			return 'Modelo no existe'
		if model == 'editorial':
			return EDITORIAL.update(**data).where(*condicion).execute()
		else:
			return 'Modelo no existe'
		if model == 'libro':
			return LIBRO.update(**data).where(*condicion).execute()
		else:
			return 'Modelo no existe'
'''
#CY = AUTOR.create('AUTOR','NOMBRE'='Infinity War','APELLIDO'='HYU')
print(CRUDManager.store('AUTOR',ID_AUTOR=9,NOMBRE = 'esa',APELLIDO = 'quienHGHHHHsoy'))
#print(AUTOR.select().where(AUTOR.ID_AUTOR==1).get())

#print(CRUDManager.store('EDITORIAL',ID_EDITORIAL=7,NOMBRE_EDITORIAL= 'MEX',PAIS = 'CHULULA'))

#print(CRUDManager.store('LIBRO',ID_LIBRO=1,TITULO = 'GERRA',AUTOR_LIBRO = 'ana',EDITORIAL_LIBRO='MEX'))
#l = LIBRO.select().where(LIBRO.TITULO == 'GERRA').get()


'''
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	899	,	NOMBRE=	   '  	Nikolai	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	4	,	NOMBRE=	   '  	Lev	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	5	,	NOMBRE=	   '  	Toni	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	6	,	NOMBRE=	   '  	Alfred	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	7	,	NOMBRE=	   '  	Saadi	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	8	,	NOMBRE=	   '  	Henrik	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	9	,	NOMBRE=	   '  	Gabriel	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	10	,	NOMBRE=	   '  	Fiódor	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	11	,	NOMBRE=	   '  	Edgar	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	12	,	NOMBRE=	   '  	Hans	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	13	,	NOMBRE=	   '  	Emily	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	14	,	NOMBRE=	   '  	Giovanni	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	15	,	NOMBRE=	   '  	Lu	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	16	,	NOMBRE=	   '  	Dante	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	17	,	NOMBRE=	   '  	Miguel	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	18	,	NOMBRE=	   '  	Sófocles	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	19	,	NOMBRE=	   '  	Franz	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	20	,	NOMBRE=	   '  	Doris	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	21	,	NOMBRE=	   '  	Albert	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	22	,	NOMBRE=	   '  	Ralph	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	23	,	NOMBRE=	   '  	Robert	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	24	,	NOMBRE=	   '  	William	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	26	,	NOMBRE=	   '  	Yasunari	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	27	,	NOMBRE=	   '  	Günter	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	28	,	NOMBRE=	   '  	Ernest	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	29	,	NOMBRE=	   '  	Marcel	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	30	,	NOMBRE=	   '  	Virgilio	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	31	,	NOMBRE=	   '  	José	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	32	,	NOMBRE=	   '  	Michel	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	33	,	NOMBRE=	   '  	Johann	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	34	,	NOMBRE=	   '  	Jorge	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	35	,	NOMBRE=	   '  	François	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	36	,	NOMBRE=	   '  	Murasaki	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	37	,	NOMBRE=	   '  	Halldór	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	38	,	NOMBRE=	   '  	João	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	39	,	NOMBRE=	   '  	Charles	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	40	,	NOMBRE=	   '  	Knut	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	41	,	NOMBRE=	   '  	Salman	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	42	,	NOMBRE=	   '  	Naguib	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	43	,	NOMBRE=	   '  	D.	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	44	,	NOMBRE=	   '  	Walt	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	45	,	NOMBRE=	   '  	Homero	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	46	,	NOMBRE=	   '  	Denis	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	47	,	NOMBRE=	   '  	Italo	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	48	,	NOMBRE=	   '  	Gustave	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	49	,	NOMBRE=	   '  	Elsa	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	50	,	NOMBRE=	   '  	Thomas	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	51	,	NOMBRE=	   '  	Mark	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	52	,	NOMBRE=	   '  	Ovidio	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	53	,	NOMBRE=	   '  	Anónimo	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	54	,	NOMBRE=	   '  	Fernando	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	55	,	NOMBRE=	   '  	Vladimir	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	56	,	NOMBRE=	   '  	Geoffrey	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	57	,	NOMBRE=	   '  	Jonathan	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	58	,	NOMBRE=	   '  	Viasa	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	59	,	NOMBRE=	   '  	Rumi	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	60	,	NOMBRE=	   '  	Eurípides	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	61	,	NOMBRE=	   '  	Marguerite	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	63	,	NOMBRE=	   '  	Herman	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	64	,	NOMBRE=	   '  	Samuel	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	65	,	NOMBRE=	   '  	Joseph	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	66	,	NOMBRE=	   '  	Jane	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	67	,	NOMBRE=	   '  	Honoré	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	68	,	NOMBRE=	   '  	Juan	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	69	,	NOMBRE=	   '  	Astrid	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	70	,	NOMBRE=	   '  	Paul	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	71	,	NOMBRE=	   '  	Giacomo	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	72	,	NOMBRE=	   '  	Valmiki	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	73	,	NOMBRE=	   '  	Antón	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	74	,	NOMBRE=	   '  	Stendhal	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	75	,	NOMBRE=	   '  	Federico	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	76	,	NOMBRE=	   '  	Kālidāsa	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	77	,	NOMBRE=	   '  	Tayeb	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	78	,	NOMBRE=	   '  	Chinua	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	79	,	NOMBRE=	   '  	James	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	80	,	NOMBRE=	   '  	Louis-Ferdinand	     '	,APELLIDO='ANONIMO'))
print(CRUDManager.store(	'AUTOR',ID_AUTOR=	81	,	NOMBRE=	   '  	Laurence	     '	,APELLIDO='ANONIMO'))'''

#print(CRUDManager.store('AUTOR',NOMBRE='Infinity Was',APELLIDO='super heroes'))
#A = AUTOR.select()#.where(AUTOR.NOMBRE == 'Infinity Was').get()
