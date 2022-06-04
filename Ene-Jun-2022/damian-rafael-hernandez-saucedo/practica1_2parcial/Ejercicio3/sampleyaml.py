import yaml


class LeerArchivoYML:
	def __init__(self,client):
		self.client = client

	def Leer_Archivo(self):
		print("id: " + self.client["id"])
		print("first_name: " + self.client["first_name"])
		print("last_name: " + self.client["last_name"])
		print("company: " + self.client["company"])
		print("email: " + self.client["email"])
		print("ip_address: " + self.client["ip_address"])
		print("phone_number: " + self.client["phone_number"])
		print('')


class MostrarMultiploTres:
	def __init__(self,data):
		self.data = data

	def Leer_Multiplo_Tres(self):
		for client in self.data["person"]:
			if int(client["id"])%3 == 0:
				yml = LeerArchivoYML(client)
				yml.Leer_Archivo()


class MostrarLongitudNombreApellido:
	def __init__(self,data):
		self.data = data

	def Leer_Nombre_Apellido(self):
		for client in self.data["person"]:
			if len(client["first_name"]) == 5 or  5 == len(client["last_name"]):
				yml = LeerArchivoYML(client)
				yml.Leer_Archivo()


class UpdatedYML:
	def __init__(self,data):
		self.data = data

	def Updated_yml(self):
		count = 0 
		for client in self.data['people']["person"]:
			self.data['people']['person'][count]['email'] = "---"
			count += 1

		for client in self.data['people']['person']:
			yml = LeerArchivoYML(client)
			yml.Leer_Archivo()

		return self.data


if __name__ == "__main__":

	with open('sample.yml','r') as file:
		data  = yaml.load(file)
		data2 = data['people']


	# creamos ciclo para elegir la opcion que queremos usar
	flag = True
	while flag == True:
		print('\n1.- Imprimir lista de ID que sean multiplos de 3.')
		print('2.- Imprimir tamano de letras del nombre o apellido 5.')
		print('3.- Modificar el Archivo "email".')
		op = int(input('opcion: '))

		print('')
		if   op == 1:
			id_MT = MostrarMultiploTres(data2)
			id_MT.Leer_Multiplo_Tres()
		elif op == 2:
			longitud_NA = MostrarLongitudNombreApellido(data2)
			longitud_NA.Leer_Nombre_Apellido()
		elif op == 3:
			updated_yml = UpdatedYML(data)
			updated_data = updated_yml.Updated_yml()

			with open('updated.yml', 'w') as file:
				yaml.dump(updated_data, file)
		else:
			print('Opcion Invalida')
