import Agencia, Automovil, Camion, Cliente, Motocicleta, Vendedor

auto = []
moto = []
camion = []



def menu():

	auto1 = Automovil.Automovil('Nissan', 'Tsuru 99', 'Amarillo', 'Estándar', 'A1NT99', 'Sedán', '10 km/L')
	auto.append(auto1)

	auto1 = Automovil.Automovil('Ford', 'Topaz 85', 'Rojo', 'Automático', 'A2fT85', 'Sedán', '9 km/L')
	auto.append(auto1)

	auto1 = Automovil.Automovil('VW', 'Jetta 09', 'Celeste', 'Estándar', 'A3VJ09', 'Hatchback', '19 km/L')
	auto.append(auto1)


	camion1 = Camion.Camion('International', 'Prostar 90', 'Azul', 'Eaton Fuller', 'C1IP90', '6 ejes', '900 hp')
	camion.append(camion1)

	camion1 = Camion.Camion('Freightliner', 'Cascadia 10', 'Gris', 'Eaton Fuller', 'C2FC18', '5 ejes', '500 hp')
	camion.append(camion1)

	camion1 = Camion.Camion('Kenworth', 'T6680 15', 'Blanco', 'Eaton Fuller', 'C3TB15', '8 ejes', '1000 hp')
	camion.append(camion1)


	moto1 = Motocicleta.Motocicleta('Italika', 'GSC175 17', 'Naranja', 'Automático', 'M1IG17', 'Motoneta', '175 cc')
	moto.append(moto1)

	moto1 = Motocicleta.Motocicleta('Honda', 'CRF230 18', 'Rojo', 'Estándar', 'M2HC18', 'Motocross', '500 cc')
	moto.append(moto1)

	moto1 = Motocicleta.Motocicleta('Kawasaki', 'Ninja 15', 'Verde', 'Estándar', 'M3KN15', 'Deportiva', '1043 cc')
	moto.append(moto1)

	print ("Selecciona una opción")
	print ("\t1 - Comprar Vehículo")
	print ("\t2 - Vender Vehiculo")
	print ("\t3 - Salir")


while True:

	menu()


	opcionMenu = input("Selecciona una opción >> ")

	if opcionMenu=="1":
		print ("Tipos de Vehículos disponibles:")
		print ("\t1 - Automóviles")
		print ("\t2 - Camiones")
		print ("\t3 - Motocicletas")
		subopc2 = input("Selecciona el tipo de vehículo >> ")

		if subopc2 == '1':
			print ("Autos Disponibles: ")
			print('==========================================')
			print("")
			for item in auto:
				print(item.atribAuto())
				print('==========================================')
			print ("¿Qué auto desea comprar?")
			print ("1 - " + auto[0].getMarca() + ' ' + auto[0].getModelo())
			print ("2 - " + auto[1].getMarca() + ' ' + auto[1].getModelo())
			print ("3 - " + auto[2].getMarca() + ' ' + auto[2].getModelo())
			subop3 = input("Seleccione el auto a comprar >> ")
			if subop3 == '1':
				print("\n¡¡Felicidades!! Usted ha comprado un: \n" + auto[0].atribAuto())
			elif subop3 == '2':
				print("\n¡¡Felicidades!! Usted ha comprado un: \n" + auto[1].atribAuto())
			elif subop3 == '2':
				print("\n¡¡Felicidades!! Usted ha comprado un: \n" + auto[2].atribAuto())

		elif subopc2 == '2':
			print ("Camiones Disponibles: ")
			print('==========================================')
			print("")
			for item in camion:
				print(item.atribCamion())
				print('==========================================')
			print ("¿Qué camion desea comprar?")
			print ("1 - " + camion[0].getMarca() + ' ' + camion[0].getModelo())
			print ("2 - " + camion[1].getMarca() + ' ' + camion[1].getModelo())
			print ("3 - " + camion[2].getMarca() + ' ' + camion[2].getModelo())
			subop4 = input("Seleccione el camion a comprar >> ")
			if subop4 == '1':
				print("\n¡¡Felicidades!! Usted ha comprado un: \n" + camion[0].atribCamion())
			elif subop4 == '2':
				print("\n¡¡Felicidades!! Usted ha comprado un: \n" + camion[1].atribCamion())
			elif subop4 == '3':
				print("\n¡¡Felicidades!! Usted ha comprado un: \n" + camion[2].atribCamion())

		elif subopc2 == '3':
			print ("Motocicletas Disponibles: ")
			print('==========================================')
			print("")
			for item in moto:
				print(item.atribMoto())
				print('==========================================')
			print ("¿Qué motocicleta desea comprar?")
			print ("1 - " + moto[0].getMarca() + ' ' + moto[0].getModelo())
			print ("2 - " + moto[1].getMarca() + ' ' + moto[1].getModelo())
			print ("3 - " + moto[2].getMarca() + ' ' + moto[2].getModelo())
			subop5 = input("Seleccione la motocicleta a comprar >> ")
			if subop5 == '1':
				print("\n¡¡Felicidades!! Usted ha comprado un: \n" + moto[0].atribMoto())
			elif subop5 == '2':
				print("\n¡¡Felicidades!! Usted ha comprado un: \n" + moto[1].atribMoto())
			elif subop5 == '3':
				print("\n¡¡Felicidades!! Usted ha comprado un: \n" + moto[2].atribMoto())
		input("\npulsa una tecla para continuar\n")

	elif opcionMenu=="2":
		print("¿Qué tipo de Vehículo deseas vender?")
		print ("\t1 - Automóviles")
		print ("\t2 - Camiones")
		print ("\t3 - Motocicletas")
		subopc3 = input("Selecciona el tipo de vehículo >> ")
		if subopc3 == '1':
			print("Gracias por vendernos tu Auto.")
		if subopc3 == '2':
			print("Gracias por vendernos tu Camión.")
		if subopc3 == '3':
			print("Gracias por vendernos tu Motocicleta.")
		input("\npulsa una tecla para continuar\n")

	elif opcionMenu=="3":
		break

	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
