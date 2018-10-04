import Factoria 

if __name__ == '__main__': 
	mi_factoria = Factoria.Factoria() 	

	#Factoria, crea a un instrumento! 
	instrumentoMusical1 = mi_factoria.get_instrumentoMusical('Percusión', 'Plata', 'DrumWorkShop', '2500	Dlls', '2m','8') 
	#se ha creado un instrumentoMusical tipo Batería 
	print (instrumentoMusical1) 	
	# print instrumentoMusical.get_tipo() 
	# print instrumentoMusical.get_marca()

	#Factoria, crea a un instrumento! 
	instrumentoMusical2 = mi_factoria.get_instrumentoMusical('Cuerdas', 'Café', 'Fender', '1500 Dlls', '135cm','6') 
	#se ha creado un instrumentoMusical tipo Guitarra
	print (instrumentoMusical2) 	

	#Factoria, crea a un instrumento! 
	instrumentoMusical3 = mi_factoria.get_instrumentoMusical('Cuerdas', 'Negro con Blanco', 'Gibson', '1350 Dlls','129cm','6') 
	#se ha creado un instrumentoMusical tipo Guitarra
	print (instrumentoMusical3) 

	#Factoria, crea a un instrumento! 
	instrumentoMusical4 = mi_factoria.get_instrumentoMusical('Cuerdas', 'Rojo con Blanco', 'Fender', '1800 Dlls', '142cm','6') 
	#se ha creado un instrumentoMusical tipo Guitarra
	print (instrumentoMusical4) 

	#Factoria, crea a un instrumento! 
	instrumentoMusical5 = mi_factoria.get_instrumentoMusical('Percusión', 'Azul', 'Ludwig', '2335 Dlls', '145cm','12') 
	#se ha creado un instrumentoMusical tipo Batería 
	print (instrumentoMusical5)

	instrumentoMusical1.afinarB()
	instrumentoMusical1.tocarB()

	instrumentoMusical2.afinarP()
	instrumentoMusical2.tocarP()

	instrumentoMusical3.afinarP()
	instrumentoMusical3.tocarP()

	instrumentoMusical4.afinarP()
	instrumentoMusical4.tocarP()

	instrumentoMusical5.afinarB()
	instrumentoMusical5.tocarB()