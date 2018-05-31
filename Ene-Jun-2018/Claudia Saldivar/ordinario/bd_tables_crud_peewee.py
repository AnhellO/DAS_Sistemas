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
			return 'Modelo no existe. Intenta de nuevo.'


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
			return 'Modelo no existe. Intenta de nuevo.'


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
			return 'Modelo no existe. Intenta de nuevo.'

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
			return 'Modelo no existe. Intenta de nuevo.'


#------------------------------ INSERTAR REGISTRO(S) A DOCTORES -------------------------------------#
#print(CRUDPanel.insert_row('Doctores', nombre_doctor='Steve', apellidos_doctor='Young', especialidad='General'))
#------------------------------ INSERTAR REGISTRO(S) A PACIENTES ------------------------------------#
#print(CRUDPanel.insert_row('Pacientes', nombre_paciente='Karina', apellidos_paciente='Montes', edad=49))
#------------------------------- INSERTAR REGISTRO(S) A CONSULTAS -----------------------------------#
#print(CRUDPanel.insert_row('Consultas', doctor=3, paciente=23, fecha_consulta='2018-05-30', diagnostico='Cortadura en mano', medicamento='Paracetamol'))

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
#print(CRUDPanel.select_row('Consultas', Consultas.id_consulta == 35)
