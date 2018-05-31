from peewee import *

db = SqliteDatabase('consultas_db.db')

class Doctores(Model):
	id_doctor = PrimaryKeyField(null=False)
	nombre_doctor = TextField()
	apellidos_doctor = TextField()
	especialidad = TextField()

	class Meta:
		database = db

	def __str__(self):
		return "ID: {}\nDoctor: {} {}\nEspecialidad: {}\n".format(self.id_doctor, self.nombre_doctor, self.apellidos_doctor, self.especialidad)

class Pacientes(Model):
	id_paciente = PrimaryKeyField(null=False)
	nombre_paciente = TextField()
	apellidos_paciente = TextField()
	edad = IntegerField()

	class Meta:
		database = db

	def __str__(self):
		return "ID: {}\nPaciente: {} {}\nEdad: {}\n".format(self.id_paciente, self.nombre_paciente, self.apellidos_paciente, self.edad)

class Consultas(Model):
	id_consulta = PrimaryKeyField(null=False)
	doctor = ForeignKeyField(Doctores, related_name="doctor_detalle")
	paciente = ForeignKeyField(Pacientes, related_name="paciente_detalle")
	fecha_consulta = DateField()
	diagnostico = TextField()
	medicamento = TextField()

	class Meta:
		database = db

	def __str__(self):
		return "No. consulta: {}\nDoctor: {} {}\nPaciente: {} {}\nFecha: {}\nDiagnóstico: {}\nMedicamento: {}\n".format(self.id_consulta, self.doctor.nombre_doctor, self.doctor.apellidos_doctor, self.paciente.nombre_paciente, self.paciente.apellidos_paciente, self.fecha_consulta, self.diagnostico, self.medicamento)
		#return "No. consulta: {}\nDoctor: {}\nPaciente: {}\nFecha: {}\nDiagnóstico: {}\nMedicamento: {}\n".format(self.id_consulta, self.doctor, self.self.paciente, self.fecha_consulta, self.diagnostico, self.medicamento)


class CRUDPanel:
	@staticmethod
	def insert_row(model, **datos):
		model = model.lower()

		if model == 'doctores':
			return Doctores.create(**datos)

		if model == 'pacientes':
			return Pacientes.create(**datos)

		if model == 'consultas':
			return Consultas.create(**datos)

		else:
			return '¡ERROR!'


	@staticmethod
	def select_row(model, *ids):
		model = model.lower()
		
		if model == 'doctores':
			if ids:
				return [str(doc) for doc in Doctores.select().where(*ids)]
			return [str(doc) for doc in Doctores.select()]

		if model == 'pacientes':
			if ids:
				return [str(pcte) for pcte in Pacientes.select().where(*ids)]
			return [str(pcte) for pcte in Pacientes.select()]

		if model == 'consultas':
			if ids:
				return [str(con) for con in Consultas.select().where(*ids)]
			return [str(con) for con in Consultas.select()]

		else:
			return '¡ERROR!'


	@staticmethod
	def update_row(model, *condicion, **datos):
		model = model.lower()

		if model == 'doctores':
			return Doctores.update(**datos).where(*condicion).execute()

		if model == 'pacientes':
			return Pacientes.update(**datos).where(*condicion).execute()

		if model == 'consultas':
			return Consultas.update(**datos).where(*condicion).execute()

		else:
			return '¡ERROR!'

	@staticmethod
	def delete_row(model, *condicion):
		model = model.lower()

		if model == 'doctores':
			return Doctores.delete().where(*condicion).execute()

		if model == 'pacientes':
			return Pacientes.delete().where(*condicion).execute()

		if model == 'consultas':
			return Consultas.delete().where(*condicion).execute()

		else:
			return '¡ERROR!'


#-------------------- SELECT A TABLA DOCTORES CON id_doctor COMO CONDICIONAL ------------------------#
print(Doctores.select().where(Doctores.id_doctor == 30).get())
print(CRUDPanel.select_row('Doctores', Doctores.id_doctor == 30))
#------------------- SELECT A TABLA PACIENTES CON id_paciente COMO CONDICIONAL ----------------------#
print(Pacientes.select().where(Pacientes.id_paciente == 30).get())
print(CRUDPanel.select_row('Pacientes', Pacientes.id_paciente == 30))
#------------------- SELECT A TABLA PACIENTES CON id_consulta COMO CONDICIONAL ----------------------#
print(Consultas.select().where(Consultas.id_consulta == 20).get())
print(CRUDPanel.select_row('Consultas', Consultas.id_consulta == 20))



#--------------------- UPDATE A UN DOCTOR CON id_doctor COMO CONDICIONAL ----------------------------#
#up_doc = {'especialidad': 'Oncología'}
#print(CRUDPanel.update_row('Doctores', Doctores.id_doctor == 30, **up_doc))
#print(Doctores.select().where(Doctores.id_doctor == 30).get())
#-------------------- UPDATE A UN PACIENTE CON id_paciente COMO CONDICIONAL -------------------------#
#up_pcte = {'nombre_paciente': 'Návila', 'apellidos_paciente': 'Peña'}
#print(CRUDPanel.update_row('Pacientes', Pacientes.id_paciente == 30, **up_pcte))
#print(Pacientes.select().where(Pacientes.id_paciente == 30).get())
#----------------------- UPDATE A UNA CONSULTA CON id_consulta COMO CONDICIONAL ---------------------#
#up_cns = {'diagnostico': 'Ciática'}
#print(CRUDPanel.update_row('Consultas', Consultas.id_consulta == 20, **up_cns))
#print(Consultas.select().where(Consultas.id_consulta == 20).get())

#------------------------- DELETE A UN DOCTOR CON id_doctor COMO CONDICIONAL ------------------------#
#print(CRUDPanel.delete_row('Doctores', Doctores.id_doctor == 34))
#print(CRUDPanel.select_row('Doctores', Doctores.id_doctor == 34))
#------------------------ DELETE A UN PACIENTE CON id_paciente COMO CONDICIONAL ---------------------#
#print(CRUDPanel.delete_row('Pacientes', Pacientes.id_paciente == 34))
#print(CRUDPanel.select_row('Pacientes', Pacientes.id_paciente == 34))
#------------------------ DELETE A UNA CONSULTA CON id_consulta COMO CONDICIONAL --------------------#
#print(CRUDPanel.delete_row('Consultas', Consultas.id_consulta == 35))
#print(CRUDPanel.select_row('Consultas', Consultas.id_consulta == 35))




#------------------------------ INSERTAR REGISTRO(S) A DOCTORES -------------------------------------#
#print(CRUDPanel.insert_row('Doctores', nombre_doctor='Steve', apellidos_doctor='Young', especialidad='General'))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Marisol",apellidos_doctor="García",especialidad="General"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Lucero",apellidos_doctor="Valdez",especialidad="Pediatra"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Lucio",apellidos_doctor="Lopez",especialidad="Alergologo"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Oliver",apellidos_doctor="Perez",especialidad="Anestesiologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Lucas",apellidos_doctor="Gonzalez",especialidad="Cardiologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Fabio",apellidos_doctor="Sanchez",especialidad="Gastroenterologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Bosco",apellidos_doctor="Martinez",especialidad="Endocrinologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Nahuel",apellidos_doctor="Rodriguez",especialidad="Geriatria"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Helio",apellidos_doctor="Fernandez",especialidad="Ginecologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Leonel",apellidos_doctor="Gomez",especialidad="Hematologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Jacinto",apellidos_doctor="Martin",especialidad="Infectologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Narciso",apellidos_doctor="Hernandez",especialidad="Medicina aeroespacial"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Manuel",apellidos_doctor="Ruiz",especialidad="Medicina del deporte"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Angel",apellidos_doctor="Diaz",especialidad="Medicina del trabajo"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Jasper",apellidos_doctor="Alvarez",especialidad="Medicina de urgencias"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Vernon",apellidos_doctor="Jimenez",especialidad="Medicina familiar y comunitaria"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Silvano",apellidos_doctor="Moreno",especialidad="Medicina fisica y rehabilitacion"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Luciano",apellidos_doctor="Munoz",especialidad="Medicina intensiva"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Delfin",apellidos_doctor="Alonso",especialidad="Medicina Interna"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Simon",apellidos_doctor="Gutierrez",especialidad="Medicina legal y forense"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Nil",apellidos_doctor="Romero",especialidad="Medicina preventiva y salud publica"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Moises",apellidos_doctor="Sanz",especialidad="Medicina veterinaria"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Eos",apellidos_doctor="Suarez",especialidad="Nefrologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Banyan",apellidos_doctor="Ramirez",especialidad="Neumologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Leon",apellidos_doctor="Vazquez",especialidad="Urologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Bryce",apellidos_doctor="Navarro",especialidad="Nutriologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Eden",apellidos_doctor="Dominguez",especialidad="Oftamologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Adrian",apellidos_doctor="Ramos",especialidad="Oncologia medica"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Silvestre",apellidos_doctor="Castro",especialidad="Oncologia redioterapia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Florencio",apellidos_doctor="Gil",especialidad="Psiquiatria"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Lorenzo",apellidos_doctor="Flores",especialidad="Toxicologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Bryn",apellidos_doctor="Morales",especialidad="Reumatologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Rafael",apellidos_doctor="Zuzunaga",especialidad="Cirujano general y del aparato digestivo"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Jonathan",apellidos_doctor="Sorni",especialidad="Cirujano cuello, torax y cardiovascular"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Esteban",apellidos_doctor="Garza",especialidad="Cirujano oido, nariz y cavidad oral"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Juan Manuel",apellidos_doctor="Sandemetrio",especialidad="Cirujano maxilofacial"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Julian",apellidos_doctor="Urriaga",especialidad="Cirujano ortopedia y traumatologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Mauricio",apellidos_doctor="Bonachera",especialidad="Cirujano pediatra"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Oscar",apellidos_doctor="Vital",especialidad="Cirujano plastico, estetico y reconstructivo"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Santino",apellidos_doctor="Pregonas",especialidad="Neurologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Axel",apellidos_doctor="Sazon",especialidad="Proctologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Sergio",apellidos_doctor="Enamorado",especialidad="Angiologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Guillermo",apellidos_doctor="Cacharro",especialidad="Anestesiologia y reanimacion"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Matthew",apellidos_doctor="Vibora",especialidad="Cardiologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Valentin",apellidos_doctor="Cama",especialidad="Gastroenterologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Bautista",apellidos_doctor="Pieldelobo",especialidad="Endocrinologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Alvaro",apellidos_doctor="Piesplanos",especialidad="Geriatria"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Dylan",apellidos_doctor="Tenedor",especialidad="Ginecologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Marcos",apellidos_doctor="Delfin",especialidad="Hematologia y hemoterapia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Kimberly",apellidos_doctor="Pechoabierto",especialidad="Infectologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Luciano",apellidos_doctor="Alcoholado",especialidad="Medicina aeroespacial"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Mario",apellidos_doctor="Verdugo",especialidad="Medicina del deporte"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Cesar",apellidos_doctor="Feo",especialidad="Medicina del trabajo"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Cristobal",apellidos_doctor="Llagaria",especialidad="Medicina de urgencias"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Luca",apellidos_doctor="Cidoncha",especialidad="Medicina familiar y comunitaria"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Iker",apellidos_doctor="Parraverde",especialidad="Medicina fisica y rehabilitacion"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Juan Andres",apellidos_doctor="Nuero",especialidad="Medicina intensiva"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Gonzalo",apellidos_doctor="Nomdedeu",especialidad="Medicina Interna"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Roberto",apellidos_doctor="Pernavieja",especialidad="Medicina legal y forense"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Valentino",apellidos_doctor="Perfume",especialidad="Medicina preventiva y salud publica"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Facundo",apellidos_doctor="Ariztimuño",especialidad="Nefrologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Patricio",apellidos_doctor="Arrubal",especialidad="Neumologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Diego",apellidos_doctor="Barato",especialidad="Neurologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Alejandro",apellidos_doctor="Viejobueno",especialidad="Nutriologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Josue",apellidos_doctor="Cayado",especialidad="Oftamologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Franco",apellidos_doctor="Callado",especialidad="Oncologia medica"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Alessandro",apellidos_doctor="Cazador",especialidad="Oncologia radioterapica"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Alonzo",apellidos_doctor="Caimanes",especialidad="Pediatria"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Amadeo",apellidos_doctor="Sin",especialidad="Psiquiatria"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Amando",apellidos_doctor="Zas",especialidad="Rehabilitacion"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Andrea",apellidos_doctor="Rajado",especialidad="Reumatologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Angelo",apellidos_doctor="Chinchurreta",especialidad="Toxicologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Baldassare",apellidos_doctor="Cosio",especialidad="Urologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Bartolomeo",apellidos_doctor="Fermonsel",especialidad="Cirujano pediatra"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Basilio",apellidos_doctor="Gandul",especialidad="Cirujano toracico"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Aurelio",apellidos_doctor="Piernabierta",especialidad="Neurocirugia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Arnaldo",apellidos_doctor="Guarnido",especialidad="Angiologia y cirugia vascular"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Antonello",apellidos_doctor="Fisica",especialidad="Estomatologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Battista",apellidos_doctor="Sacamoco",especialidad="Ginecologia y obstetricia o tocologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Benedetto",apellidos_doctor="Dios",especialidad="Oftamologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Bernardino",apellidos_doctor="Parahoy",especialidad="Otorrinolaringologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Calvino",apellidos_doctor="Triunfo",especialidad="Urologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Camilo",apellidos_doctor="De la Polla",especialidad="Analisis clinicos"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Carlo",apellidos_doctor="Hergueta",especialidad="Anatomia patologica"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Celestino",apellidos_doctor="Bru",especialidad="Bioquimica clinica"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Dante",apellidos_doctor="Raga",especialidad="Farmacologia clinica"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Domenico",apellidos_doctor="Cuñat",especialidad="Genetica medica"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Donato",apellidos_doctor="Pruñonosa",especialidad="Inmunologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Enrico",apellidos_doctor="Fonollar",especialidad="Medicina nuclear"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Eusebio",apellidos_doctor="Lujan",especialidad="Microbiologia y parasitologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Fabrizio",apellidos_doctor="Fajardo",especialidad="Neurofisiologia clinica"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Felippo",apellidos_doctor="Coscojuela",especialidad="Radiologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Fiorenzo",apellidos_doctor="Funes",especialidad="Alergologo"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Florentino",apellidos_doctor="Mantilla",especialidad="Anestesiologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Francesco",apellidos_doctor="Gallur",especialidad="Cardiologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Giovanni",apellidos_doctor="Melgar",especialidad="Endocrinologia"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Guido",apellidos_doctor="Longan",especialidad="Geriatria"))
# print(CRUDPanel.insert_row('Doctores', nombre_doctor="Leandro",apellidos_doctor="Cedeño",especialidad="Infectologia"))

#------------------------------ INSERTAR REGISTRO(S) A PACIENTES ------------------------------------#
#print(CRUDPanel.insert_row('Pacientes', nombre_paciente='Karina', apellidos_paciente='Montes', edad=49))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente='Karina', apellidos_paciente='Montes', edad=49))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Claudia", apellidos_paciente="Saldivar", edad=23))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Raúl", apellidos_paciente="Martínez", edad=20))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="David", apellidos_paciente="Savala", edad=7))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Manila", apellidos_paciente="Jaramillo", edad=10))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Ainara", apellidos_paciente="Blanco", edad=24))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Alana", apellidos_paciente="Serrano", edad=43))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Carola", apellidos_paciente="Molina", edad=15))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Mia", apellidos_paciente="Ortiz", edad=61))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Amelia", apellidos_paciente="Santos", edad=70))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Malva", apellidos_paciente="Ortega", edad=35))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Maite", apellidos_paciente="Morrell", edad=29))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Adelaida", apellidos_paciente="Delgado", edad=20))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Dafne", apellidos_paciente="Mendez", edad=18))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Olga", apellidos_paciente="Castillo", edad=47))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Haley", apellidos_paciente="Marquez", edad=68))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Olivia", apellidos_paciente="Cruz", edad=22))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Wara", apellidos_paciente="Pascual", edad=43))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Meritxel", apellidos_paciente="Medina", edad=47))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Maia", apellidos_paciente="Herrera", edad=27))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Dana", apellidos_paciente="Marin", edad=18))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Ambar", apellidos_paciente="Nunez", edad=22))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Erika", apellidos_paciente="Vega", edad=21))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Ada", apellidos_paciente="Iglesias", edad=9))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Magali", apellidos_paciente="Rojas", edad=12))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Adelma", apellidos_paciente="Reyes", edad=34))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Maitena", apellidos_paciente="Luna", edad=41))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Mariel", apellidos_paciente="Campos", edad=5))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Naiara", apellidos_paciente="Rubio", edad=55))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Navila", apellidos_paciente="Pena", edad=78))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Gaia", apellidos_paciente="Ferrer", edad=80))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Petra", apellidos_paciente="Lozano", edad=17))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Yaima", apellidos_paciente="Aguilar", edad=32))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Santiago", apellidos_paciente="Garcia", edad=13))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Sebastian", apellidos_paciente="Gonzalez", edad=24))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Diego", apellidos_paciente="Rodriguez", edad=45))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Nicolas", apellidos_paciente="Fernandez", edad=51))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Samuel", apellidos_paciente="Lopez", edad=33))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Alejandro", apellidos_paciente="Martinez", edad=12))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Daniel", apellidos_paciente="Sanchez", edad=22))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Mateo", apellidos_paciente="Perez", edad=12))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Angel", apellidos_paciente="Gomez", edad=5))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Matias", apellidos_paciente="Martin", edad=1))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Gabriel", apellidos_paciente="Jimenez", edad=3))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Tomas", apellidos_paciente="Ruiz", edad=15))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="David", apellidos_paciente="Hernandez", edad=10))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Emiliano", apellidos_paciente="Diaz", edad=20))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Andres", apellidos_paciente="Moreno", edad=36))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Joaquin", apellidos_paciente="Muñoz", edad=26))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Carlos", apellidos_paciente="Alvarez", edad=22))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Alexander", apellidos_paciente="Romero", edad=23))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Adrian", apellidos_paciente="Alonso", edad=43))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Lucas", apellidos_paciente="Gutierrez", edad=40))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Benjamin", apellidos_paciente="Navarro", edad=10))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Leonardo", apellidos_paciente="Torres", edad=52))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Rodrigo", apellidos_paciente="Dominguez", edad=66))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Felipe", apellidos_paciente="Vazquez", edad=75))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Francisco", apellidos_paciente="Ramos", edad=53))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Pablo", apellidos_paciente="Gil", edad=12))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Martin", apellidos_paciente="Ramirez", edad=54))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Fernando", apellidos_paciente="Serrano", edad=33))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Isaac", apellidos_paciente="Blanco", edad=12))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Manuel", apellidos_paciente="Molina", edad=31))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Juan Pablo", apellidos_paciente="Suarez", edad=45))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Emmanuel", apellidos_paciente="Ortega", edad=14))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Emilio", apellidos_paciente="Ligas", edad=19))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Vicente", apellidos_paciente="Delgado", edad=22))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Eduardo", apellidos_paciente="Castro", edad=20))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Juan", apellidos_paciente="Ortiz", edad=17))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Javier", apellidos_paciente="Rubio", edad=29))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Jorge", apellidos_paciente="Marin", edad=63))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Aaron", apellidos_paciente="Saenz", edad=60))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Jose", apellidos_paciente="Nuñes", edad=39))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Erick", apellidos_paciente="Iglesias", edad=27))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Luis", apellidos_paciente="Medina", edad=52))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Cristian", apellidos_paciente="Garrido", edad=7))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Ignacio", apellidos_paciente="Cortes", edad=32))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Christopher", apellidos_paciente="Castillo", edad=35))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Jesus", apellidos_paciente="Santos", edad=12))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Kevin", apellidos_paciente="Lozano", edad=15))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Juan jose", apellidos_paciente="Guerrero", edad=23))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Agustin", apellidos_paciente="Cano", edad=28))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Juan david", apellidos_paciente="Prieto", edad=9))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Simon", apellidos_paciente="Mendez", edad=59))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Joshua", apellidos_paciente="Cruz", edad=13))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Maximiliano", apellidos_paciente="Calvo", edad=74))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Miguel Angel", apellidos_paciente="Gallego", edad=26))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Juan sebastian", apellidos_paciente="Vidal", edad=9))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Bruno", apellidos_paciente="Leon", edad=62))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Ivan", apellidos_paciente="Marquez", edad=19))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Gael", apellidos_paciente="Herrera", edad=50))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Miguel", apellidos_paciente="Fierro", edad=41))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Thiago", apellidos_paciente="Peña", edad=16))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Jeronimo", apellidos_paciente="Flores", edad=36))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Hugo", apellidos_paciente="Cabrera", edad=12))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Ricardo", apellidos_paciente="Campos", edad=5))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Antonio", apellidos_paciente="Vega", edad=24))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Ian", apellidos_paciente="Fuentes", edad=38))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Anthony", apellidos_paciente="Carrasco", edad=41))
# print(CRUDPanel.insert_row('Pacientes', nombre_paciente="Pedro", apellidos_paciente="Diez", edad=23))

#------------------------------- INSERTAR REGISTRO(S) A CONSULTAS -----------------------------------#
#print(CRUDPanel.insert_row('Consultas', doctor=3, paciente=23, fecha_consulta='2018-05-30', diagnostico='Cortadura en mano', medicamento='Paracetamol'))
# print(CRUDPanel.insert_row('Consultas', doctor=3, paciente=23, fecha_consulta='2018-05-30', diagnostico='Cortadura en mano', medicamento='Paracetamol'))
# print(CRUDPanel.insert_row('Consultas', doctor=2, paciente=2, fecha_consulta="2018-03-02", diagnostico="Gripa", medicamento="Paracetamol"))
# print(CRUDPanel.insert_row('Consultas', doctor=3, paciente=4, fecha_consulta="2018-05-15", diagnostico="Resfriado", medicamento="Mejoralito"))
# print(CRUDPanel.insert_row('Consultas', doctor=1, paciente=1, fecha_consulta="2018-05-19", diagnostico="Tos", medicamento="Ambroxol"))
# print(CRUDPanel.insert_row('Consultas', doctor=5, paciente=6, fecha_consulta="2018-01-10", diagnostico="Absceso dental", medicamento="Zidovudina"))
# print(CRUDPanel.insert_row('Consultas', doctor=31, paciente=18, fecha_consulta="2018-01-30", diagnostico="Alcoholismo", medicamento="Emtricitabina"))
# print(CRUDPanel.insert_row('Consultas', doctor=6, paciente=5, fecha_consulta="2018-02-15", diagnostico="Anemia", medicamento="Efavirenz"))
# print(CRUDPanel.insert_row('Consultas', doctor=7, paciente=8, fecha_consulta="2018-02-28", diagnostico="Anorexia", medicamento="Nevirapina"))
# print(CRUDPanel.insert_row('Consultas', doctor=9, paciente=10, fecha_consulta="2018-03-09", diagnostico="Apnea del sueño", medicamento="Ranitidina"))
# print(CRUDPanel.insert_row('Consultas', doctor=10, paciente=15, fecha_consulta="2018-03-17", diagnostico="Asma", medicamento="Omeprazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=20, paciente=19, fecha_consulta="2018-03-28", diagnostico="Aterosclerosis", medicamento="Loperamida"))
# print(CRUDPanel.insert_row('Consultas', doctor=11, paciente=21, fecha_consulta="2018-04-05", diagnostico="Bronquiectasias", medicamento="Metoclopramida"))
# print(CRUDPanel.insert_row('Consultas', doctor=19, paciente=23, fecha_consulta="2018-04-19", diagnostico="Bronquitis", medicamento="Ondansetron"))
# print(CRUDPanel.insert_row('Consultas', doctor=12, paciente=25, fecha_consulta="2018-04-30", diagnostico="Brucelosis", medicamento="Tinidazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=18, paciente=27, fecha_consulta="2018-05-08", diagnostico="Bulimia", medicamento="Metronidazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=13, paciente=29, fecha_consulta="2018-05-26", diagnostico="Calambres musculares", medicamento="Diloxanida"))
# print(CRUDPanel.insert_row('Consultas', doctor=17, paciente=31, fecha_consulta="2018-06-03", diagnostico="Calculos de riñon", medicamento="Benznidazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=14, paciente=33, fecha_consulta="2018-06-13", diagnostico="Callos y callosidades", medicamento="Nifurtimox"))
# print(CRUDPanel.insert_row('Consultas', doctor=16, paciente=7, fecha_consulta="2018-06-21", diagnostico="Cefaleas", medicamento="Albendazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=15, paciente=12, fecha_consulta="2018-06-30", diagnostico="Ciatica", medicamento="Mebendazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=20, paciente=13, fecha_consulta="2018-07-10", diagnostico="Colitis Ulcerosa", medicamento="Praziquantel"))
# print(CRUDPanel.insert_row('Consultas', doctor=30, paciente=14, fecha_consulta="2018-07-23", diagnostico="Colon irritable", medicamento="Salbutamol"))
# print(CRUDPanel.insert_row('Consultas', doctor=21, paciente=17, fecha_consulta="2018-07-28", diagnostico="Coma etilico", medicamento="Aminofilina"))
# print(CRUDPanel.insert_row('Consultas', doctor=29, paciente=32, fecha_consulta="2018-08-04", diagnostico="Degeneracion macular del ojo", medicamento="Teofilina"))
# print(CRUDPanel.insert_row('Consultas', doctor=22, paciente=30, fecha_consulta="2018-08-18", diagnostico="Hipocondria", medicamento="Codeina"))
# print(CRUDPanel.insert_row('Consultas', doctor=28, paciente=28, fecha_consulta="2018-08-23", diagnostico="Hipotension", medicamento="Beclometasona"))
# print(CRUDPanel.insert_row('Consultas', doctor=23, paciente=26, fecha_consulta="2018-09-05", diagnostico="Hongos", medicamento="Cromoglicato disodico"))
# print(CRUDPanel.insert_row('Consultas', doctor=27, paciente=24, fecha_consulta="2018-09-11", diagnostico="Juanetes", medicamento="Beractante"))
# print(CRUDPanel.insert_row('Consultas', doctor=24, paciente=22, fecha_consulta="2018-09-20", diagnostico="Laringitis", medicamento="Digoxina"))
# print(CRUDPanel.insert_row('Consultas', doctor=26, paciente=20, fecha_consulta="2018-09-29", diagnostico="Mareo", medicamento="Enalapril"))
# print(CRUDPanel.insert_row('Consultas', doctor=25, paciente=16, fecha_consulta="2018-10-02", diagnostico="Mastoiditis", medicamento="Amiodarona"))
# print(CRUDPanel.insert_row('Consultas', doctor=32, paciente=11, fecha_consulta="2018-11-16", diagnostico="Obesidad", medicamento="Verapamilo clorhidrato"))
# print(CRUDPanel.insert_row('Consultas', doctor=33, paciente=9, fecha_consulta="2018-12-01", diagnostico="Piel seca", medicamento="Adenosina"))
# print(CRUDPanel.insert_row('Consultas', doctor=30, paciente=6, fecha_consulta="2018-12-22", diagnostico="Reflujo gastroesofagico", medicamento="Fenilefrina"))
# print(CRUDPanel.insert_row('Consultas', doctor=35, paciente=35, fecha_consulta="2018-12-23", diagnostico="Diabetes", medicamento="Insulina"))
# print(CRUDPanel.insert_row('Consultas', doctor=36, paciente=36, fecha_consulta="2018-12-24", diagnostico="Anemia", medicamento="Eritropoyena"))
# print(CRUDPanel.insert_row('Consultas', doctor=37, paciente=37, fecha_consulta="2018-12-25", diagnostico="VIH", medicamento="Aptivus"))
# print(CRUDPanel.insert_row('Consultas', doctor=38, paciente=38, fecha_consulta="2018-12-26", diagnostico="Lupus Eritematozo", medicamento="antiflamatorio"))
# print(CRUDPanel.insert_row('Consultas', doctor=39, paciente=39, fecha_consulta="2018-12-27", diagnostico="Denge", medicamento="Vacuna contra el denge"))
# print(CRUDPanel.insert_row('Consultas', doctor=40, paciente=40, fecha_consulta="2018-12-28", diagnostico="Cancer", medicamento="Tylenol"))
# print(CRUDPanel.insert_row('Consultas', doctor=41, paciente=41, fecha_consulta="2018-12-29", diagnostico="Malaria", medicamento="Artemer"))
# print(CRUDPanel.insert_row('Consultas', doctor=42, paciente=42, fecha_consulta="2018-12-30", diagnostico="Rubeola", medicamento="Paracetamol"))
# print(CRUDPanel.insert_row('Consultas', doctor=43, paciente=43, fecha_consulta="2018-12-31", diagnostico="Candidiasis", medicamento="Clotrimazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=44, paciente=44, fecha_consulta="2019-01-01", diagnostico="Tetanos", medicamento="Antibioticos"))
# print(CRUDPanel.insert_row('Consultas', doctor=45, paciente=45, fecha_consulta="2019-01-02", diagnostico="Hepatitis", medicamento="Segun el medico"))
# print(CRUDPanel.insert_row('Consultas', doctor=46, paciente=46, fecha_consulta="2019-01-03", diagnostico="Sarampion", medicamento="Tylenol"))
# print(CRUDPanel.insert_row('Consultas', doctor=47, paciente=47, fecha_consulta="2019-01-04", diagnostico="Tuberculosis", medicamento="Rifampicina"))
# print(CRUDPanel.insert_row('Consultas', doctor=48, paciente=48, fecha_consulta="2019-01-05", diagnostico="Salmonela", medicamento="ciprofloxacin"))
# print(CRUDPanel.insert_row('Consultas', doctor=49, paciente=49, fecha_consulta="2019-01-06", diagnostico="Varicela", medicamento="analgesicos"))
# print(CRUDPanel.insert_row('Consultas', doctor=50, paciente=50, fecha_consulta="2019-01-07", diagnostico="Gripe", medicamento="descongestionantes"))
# print(CRUDPanel.insert_row('Consultas', doctor=51, paciente=51, fecha_consulta="2019-01-08", diagnostico="Viruela", medicamento="Vacuna contra la Viruela"))
# print(CRUDPanel.insert_row('Consultas', doctor=52, paciente=52, fecha_consulta="2019-01-09", diagnostico="Gastroenteritis", medicamento="Antiacidos"))
# print(CRUDPanel.insert_row('Consultas', doctor=53, paciente=53, fecha_consulta="2019-01-10", diagnostico="Conjuntivitis", medicamento="Artemer"))
# print(CRUDPanel.insert_row('Consultas', doctor=54, paciente=54, fecha_consulta="2019-01-11", diagnostico="Anguna de pecho", medicamento="Teofilina"))
# print(CRUDPanel.insert_row('Consultas', doctor=55, paciente=55, fecha_consulta="2019-01-12", diagnostico="Aerofagia", medicamento="Tylenol"))
# print(CRUDPanel.insert_row('Consultas', doctor=56, paciente=56, fecha_consulta="2019-01-13", diagnostico="Amigdalitis aguda", medicamento="Benznidazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=57, paciente=57, fecha_consulta="2019-01-14", diagnostico="Angina", medicamento="Aminofilina"))
# print(CRUDPanel.insert_row('Consultas', doctor=58, paciente=58, fecha_consulta="2019-01-15", diagnostico="Anorexia", medicamento="Teofilina"))
# print(CRUDPanel.insert_row('Consultas', doctor=59, paciente=59, fecha_consulta="2019-01-16", diagnostico="Apendicitis", medicamento="Codeina"))
# print(CRUDPanel.insert_row('Consultas', doctor=60, paciente=60, fecha_consulta="2019-01-17", diagnostico="Apert", medicamento="Beclometasona"))
# print(CRUDPanel.insert_row('Consultas', doctor=61, paciente=61, fecha_consulta="2019-01-18", diagnostico="Asma", medicamento="Cromoglicato disodico"))
# print(CRUDPanel.insert_row('Consultas', doctor=62, paciente=62, fecha_consulta="2019-01-19", diagnostico="Alergias", medicamento="Beractante"))
# print(CRUDPanel.insert_row('Consultas', doctor=63, paciente=63, fecha_consulta="2019-01-20", diagnostico="Balanitis", medicamento="Digoxina"))
# print(CRUDPanel.insert_row('Consultas', doctor=64, paciente=64, fecha_consulta="2019-01-21", diagnostico="Blefaritis", medicamento="Enalapril"))
# print(CRUDPanel.insert_row('Consultas', doctor=65, paciente=65, fecha_consulta="2019-01-22", diagnostico="Bronquiolitis", medicamento="Amiodarona"))
# print(CRUDPanel.insert_row('Consultas', doctor=66, paciente=66, fecha_consulta="2019-01-23", diagnostico="Bronquitis", medicamento="Verapamilo clorhidrato"))
# print(CRUDPanel.insert_row('Consultas', doctor=67, paciente=67, fecha_consulta="2019-01-24", diagnostico="Catarro", medicamento="Adenosina"))
# print(CRUDPanel.insert_row('Consultas', doctor=68, paciente=68, fecha_consulta="2019-01-25", diagnostico="Cianosis", medicamento="Fenilefrina"))
# print(CRUDPanel.insert_row('Consultas', doctor=69, paciente=69, fecha_consulta="2019-01-26", diagnostico="Convulsiones febriales", medicamento="Iboprufeno"))
# print(CRUDPanel.insert_row('Consultas', doctor=70, paciente=70, fecha_consulta="2019-01-27", diagnostico="Colicos del lactante", medicamento="Paracetamol"))
# print(CRUDPanel.insert_row('Consultas', doctor=71, paciente=71, fecha_consulta="2019-01-28", diagnostico="Coqueluche", medicamento="Mejoralito"))
# print(CRUDPanel.insert_row('Consultas', doctor=72, paciente=72, fecha_consulta="2019-01-29", diagnostico="Deshidratacion", medicamento="Ambroxol"))
# print(CRUDPanel.insert_row('Consultas', doctor=73, paciente=73, fecha_consulta="2019-01-30", diagnostico="Dermatitis atopica", medicamento="Zidovudina"))
# print(CRUDPanel.insert_row('Consultas', doctor=74, paciente=74, fecha_consulta="2019-01-31", diagnostico="Dermatitis del pañal", medicamento="Emtricitabina"))
# print(CRUDPanel.insert_row('Consultas', doctor=75, paciente=75, fecha_consulta="2019-02-01", diagnostico="Dermatitis seborreica", medicamento="Efavirenz"))
# print(CRUDPanel.insert_row('Consultas', doctor=76, paciente=76, fecha_consulta="2019-02-02", diagnostico="Diarrea aguda", medicamento="Nevirapina"))
# print(CRUDPanel.insert_row('Consultas', doctor=77, paciente=77, fecha_consulta="2019-02-03", diagnostico="Dolor abdominal agudo", medicamento="Ranitidina"))
# print(CRUDPanel.insert_row('Consultas', doctor=78, paciente=78, fecha_consulta="2019-02-04", diagnostico="Dolor de cabeza", medicamento="Omeprazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=79, paciente=79, fecha_consulta="2019-02-05", diagnostico="Enuresis", medicamento="Loperamida"))
# print(CRUDPanel.insert_row('Consultas', doctor=80, paciente=80, fecha_consulta="2019-02-06", diagnostico="Epligotitis aguda", medicamento="Metoclopramida"))
# print(CRUDPanel.insert_row('Consultas', doctor=81, paciente=81, fecha_consulta="2019-02-07", diagnostico="Epilepsia", medicamento="Ondansetron"))
# print(CRUDPanel.insert_row('Consultas', doctor=82, paciente=82, fecha_consulta="2019-02-08", diagnostico="Escarlatina", medicamento="Tinidazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=83, paciente=83, fecha_consulta="2019-02-09", diagnostico="Espasmos del sollozo", medicamento="Metronidazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=84, paciente=84, fecha_consulta="2019-02-10", diagnostico="Espina bifida", medicamento="Diloxanida"))
# print(CRUDPanel.insert_row('Consultas', doctor=85, paciente=85, fecha_consulta="2019-02-11", diagnostico="Estenosis hipertrofica del piloro", medicamento="Benznidazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=86, paciente=86, fecha_consulta="2019-02-12", diagnostico="Estrabismo", medicamento="Nifurtimox"))
# print(CRUDPanel.insert_row('Consultas', doctor=87, paciente=87, fecha_consulta="2019-02-13", diagnostico="Estreñimiento", medicamento="Albendazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=88, paciente=88, fecha_consulta="2019-02-14", diagnostico="Gastroneteritis", medicamento="Mebendazol"))
# print(CRUDPanel.insert_row('Consultas', doctor=89, paciente=89, fecha_consulta="2019-02-15", diagnostico="Hernia inguinal", medicamento="Praziquantel"))
# print(CRUDPanel.insert_row('Consultas', doctor=90, paciente=90, fecha_consulta="2019-02-16", diagnostico="Hernia umbilical", medicamento="Salbutamol"))
# print(CRUDPanel.insert_row('Consultas', doctor=91, paciente=91, fecha_consulta="2019-02-17", diagnostico="Herpangina", medicamento="Aminofilina"))
# print(CRUDPanel.insert_row('Consultas', doctor=92, paciente=92, fecha_consulta="2019-02-18", diagnostico="Herpes", medicamento="Teofilina"))
# print(CRUDPanel.insert_row('Consultas', doctor=93, paciente=93, fecha_consulta="2019-02-19", diagnostico="Ictericia", medicamento="Codeina"))
# print(CRUDPanel.insert_row('Consultas', doctor=94, paciente=94, fecha_consulta="2019-02-20", diagnostico="Infeccion Urinaria", medicamento="Beclometasona"))
# print(CRUDPanel.insert_row('Consultas', doctor=95, paciente=95, fecha_consulta="2019-02-21", diagnostico="Meningitis", medicamento="Cromoglicato disodico"))
# print(CRUDPanel.insert_row('Consultas', doctor=96, paciente=96, fecha_consulta="2019-02-22", diagnostico="Neumococo", medicamento="Beractante"))
# print(CRUDPanel.insert_row('Consultas', doctor=97, paciente=97, fecha_consulta="2019-02-23", diagnostico="Neumonia", medicamento="Digoxina"))
# print(CRUDPanel.insert_row('Consultas', doctor=98, paciente=98, fecha_consulta="2019-02-24", diagnostico="Obesidad exogena", medicamento="Enalapril"))
# print(CRUDPanel.insert_row('Consultas', doctor=99, paciente=99, fecha_consulta="2019-02-25", diagnostico="Otitis media aguda", medicamento="Amiodarona"))
# print(CRUDPanel.insert_row('Consultas', doctor=100, paciente=100, fecha_consulta="2019-02-26", diagnostico="Oxiuriasis", medicamento="Verapamilo clorhidrato"))