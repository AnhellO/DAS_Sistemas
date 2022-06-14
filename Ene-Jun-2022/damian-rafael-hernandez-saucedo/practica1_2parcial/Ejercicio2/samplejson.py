import json


class LeerArchivoJSON:
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


class MostrarIdImpar:
	def __init__(self,data):
		self.data = data

	def Leer_Impar(self):
		for client in self.data["person"]:
			if int(client["id"])%2 != 0:
				json = LeerArchivoJSON(client)
				json.Leer_Archivo()


class MostrarLongitudCompania:
	def __init__(self,data):
		self.data = data

	def Leer_Compania(self):
		for client in self.data["person"]:
			if len(client["company"]) >= 4 and  6 >= len(client["company"]):
				json = LeerArchivoJSON(client)
				json.Leer_Archivo()


class UpdatedJSON:
	def __init__(self,data):
		self.data = data

	def Updated_Json(self):
		count = 0 
		for client in self.data['people']["person"]:
			self.data['people']['person'][count]['phone_number'] = "XX-XX-XXX"
			count += 1

		for client in self.data['people']['person']:
			json = LeerArchivoJSON(client)
			json.Leer_Archivo()

		return self.data		


if __name__ == "__main__":
	with open('sample.json') as file:
		data = json.load(file)
		data2 = data["people"]

	# creamos ciclo para elegir la opcion que queremos usar
	flag = True
	while flag == True:
		print('\n1.- Imprimir lista de ID que sean impar.')
		print('2.- Imprimir tamano de letras de la compania entre 4 y 6.')
		print('3.- Modificar el Archivo "phone_number".')
		op = int(input('opcion: '))

		print('')
		if   op == 1:
			id_impar = MostrarIdImpar(data2)
			id_impar.Leer_Impar()
		elif op == 2:
			compania = MostrarLongitudCompania(data2)
			compania.Leer_Compania()
		elif op == 3:
			updated_json = UpdatedJSON(data)
			updated_data = updated_json.Updated_Json()

			with open('updated.json', 'w') as file:
				json.dump(updated_data, file)
		else:
			print('Opcion Invalida')
