from peewee import *

db = SqliteDatabase('Libreria_db.db')

class Libros(Model):
	id_libro = PrimaryKeyField(null=False)
	nombre_libro = TextField()
	autor_libro = ForeignKeyField(Autores, related_name="autor_detalle")
	editorial_libro = ForeignKeyField(Editoriales, related_name="editorial_detalle")

	class Meta:
		database = db

	def __str__(self):
		return "Libro: {} {}\nAutor: {} {}\nEditorial: {}".format(self.id_libro, self.nombre_libro, self.autor_libro.nombre_autor, self.editorial_libro.editorial)

class Autores(Model):
	id_autor = PrimaryKeyField(null=False)
	nombre_autor = TextField()
	apellidos_autor = TextField()

	class Meta:
		database = db

	def __str__(self):
		return "ID:{}\nAutor:{} {}\nApellido:{}".format(self.id_autor, self.nombre_autor, self.apellidos_autor )

class Consultas(Model):
	id_editorial =PrimaryKeyField(null=False)
	editorial = TextField()
	pais_editorial =TextField()

	class Meta:
		database = db

	def __str__(self):
		return "ID: {}\neDitorial: {} {}\nPais: {}".format(self.id_editorial, self.editorial,self.pais_editorial)


class CRUDPanel:
	@staticmethod
	def insert_row(model, **datos):
		model = model.lower()

		if model == 'libros':
			return Doctores.create(**datos)

		if model == 'autores':
			return Pacientes.create(**datos)

		if model == 'editoriales':
			return Consultas.create(**datos)

		else:
			return 'Modelo no existe. Intenta de nuevo.'


	@staticmethod
	def select_row(model, *ids):
		model = model.lower()
		
		if model == 'libros':
			if ids:
				return [str(lib) for lib in Libros.select().where(*ids)]
			return [str(lib) for lib in Libros.select()]

		if model == 'autores':
			if ids:
				return [str(aut) for aut in Autores.select().where(*ids)]
			return [str(aut) for aut in Autores.select()]

		if model == 'editoriales':
			if ids:
				return [str(ed) for ed in Editoriales.select().where(*ids)]
			return [str(ed) for ed in Editoriales.select()]

		else:
			return 'Modelo no existe. Intenta de nuevo.'


	@staticmethod
	def update_row(model, *condicion, **datos):
		model = model.lower()

		if model == 'libros':
			return Libros.update(**datos).where(*condicion).execute()

		if model == 'autores':
			return Autores.update(**datos).where(*condicion).execute()

		if model == 'editoriales':
			return Editoriales.update(**datos).where(*condicion).execute()

		else:
			return 'Modelo no existe. Intenta de nuevo.'


#------------------------------ INSERTAR REGISTRO(S) A libros -------------------------------------#
#print(CRUDPanel.insert_row('Libros', nombre_libro='Cien años de soledad', autor_libro='Gabriel', editorial_libro='Harper, Jonathan Cape'))
#------------------------------ INSERTAR REGISTRO(S) A autores ------------------------------------#
#print(CRUDPanel.insert_row('Autores', nombre_autor='Gabriel', apellidos_autor='García Márquez'))
#------------------------------- INSERTAR REGISTRO(S) A Editoriales -----------------------------------#
#print(CRUDPanel.insert_row('Editoriales', editorial='Harper, Jonathan Cape', pais_editorial='Reino Unido'))

#-------------------- SELECT A TABLA LIBROS CON id_LIBRO COMO CONDICIONAL ------------------------#
print(Libros.select().where(Libros.id_libro == 1).get())
print(CRUDPanel.select_row('Libros', Libros.id_doctor == 1))
#------------------- SELECT A TABLA Autores CON id_autor COMO CONDICIONAL ----------------------#
print(Autores.select().where(Autores.id_autor == 30).get())
print(CRUDPanel.select_row('Autores', Autores.id_autor == 1))
#------------------- SELECT A TABLA EDITORIALES CON id_editorial COMO CONDICIONAL ----------------------#
print(Editoriales.select().where(editoriales.id_consulta == 1).get())
print(CRUDPanel.select_row('Editoriales', Editoriales.id_editorial == 1))

# --------------------- ACTUALIZAR A UN Libro DE LA CON id_libro COMO CONDICIONAL -------------------- -------- #
# up_lib = {'editorial': 'Oceano'}
# print (CRUDPanel.update_row ('Libros', Libros.id_libro == 1, ** up_lib))
# print (Libros.select (). where (Libros.id_libro == 1) .get ())
# -------------------- ACTUALIZA UN UN Autor CON id_autor COMO CONDICIONAL --------------------- ---- #
# up_aut = {'nombre_autor': 'Aldous', 'apellidos_autor': 'Huxley'}
# print (CRUDPanel.update_row ('Autores', Autores.id_autor == 1, ** up_aut))
# print (Autores.select (). where (Autor.id_autor == 1) .get ())
# ----------------------- ACTUALIZAR UNA EDITORIALES CON id_editorial COMO CONDICIONAL ------------------ --- #
# up_ed = {'pais_editorial': 'china'}
# print (CRUDPanel.update_row ('Editoriales', Editoriales.id_editorial == 1, ** up_ed))
# print (Editoriales.select (). where (Editorial.id_editorial == 1) .get ())

# ------------------------- BORRAR UN Libros con id_libro COMO CONDICIONAL ---------------- -------- #
# print (CRUDPanel.delete_row ('Libros', Libros.id_libro == 1))
# print (CRUDPanel.select_row ('Libros', Libros.id_libro == 1))
# ------------------------ BORRAR UN UN Editoriales CON id_editorial COMO CONDICIONAL ----------------- ---- #
# print (CRUDPanel.delete_row ('Editoriales', Editoriales.id_editorial == 1))
# print (CRUDPanel.select_row ('Editoriales', Editoriales.id_editorial == 1))
# ------------------------ ELIMINAR UNA Autores CON id_autor COMO CONDICIONAL ----------------- --- #
# print (CRUDPanel.delete_row ('Autores', Consultas.id_autor == 1))
# print (CRUDPanel.select_row ('Autores', Consultas.id_autor == 1))