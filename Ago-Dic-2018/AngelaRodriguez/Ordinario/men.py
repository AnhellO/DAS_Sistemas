import os
import sqlite3
cnxn = sqlite3.connect('Recetas.db')
cursor = cnxn.cursor()
 
def menu():
	cnxn = sqlite3.connect('Recetas.db')
	cursor = cnxn.cursor()
	cant=0
	total=0
	
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Busca Usuario")
	print ("\t2 - Tacos")
	print ("\t3 - Receta 1")
	print ("\t4 - Receta 2")
	print ("\t5 - Receta 3")
	print ("\t6 - Receta 4")
	print ("\t7 - Borrar Receta")
	print ("\t9 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		rows = cursor.execute("select first, last  from USUARIOS where id=1")
		for row in rows:
			print(row)


	elif opcionMenu=="2":
		cant=input("¿Cuantos tacos quieres?")
		total=cant * 15
		print("El total a pagar es:%s" %total)

	elif opcionMenu=="3":
#		n=input("Dame un ID para ver la receta")
		rows=cursor.execute("select contribuidor,descripcion from RECETA where id_taco=1").fetchall()
		for row in rows:
			print(row)	

	elif opcionMenu=="4":
#		n=input("Dame un ID para ver la receta")
		rows=cursor.execute("select contribuidor,descripcion from RECETA where id_taco=2").fetchall()
		for row in rows:
			print(row)

	elif opcionMenu=="5":
#		n=input("Dame un ID para ver la receta")
		rows=cursor.execute("select contribuidor,descripcion from RECETA where id_taco=3").fetchall()
		for row in rows:
			print(row)	
	elif opcionMenu=="6":
#		n=input("Dame un ID para ver la receta")
		rows=cursor.execute("select contribuidor,descripcion from RECETA where id_taco=4").fetchall()
		for row in rows:
			print(row)

	elif opcionMenu=="7":
		cursor.execute("delete from RECETA where id_taco=58")
		cnxn.commit()
		print("la Receta se ha eliminado")

	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")