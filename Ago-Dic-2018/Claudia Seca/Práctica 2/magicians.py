def show_magicians(lista):
	for nombre in lista:
		#Pone automatico la primer letra de un nombre en mayus
		msg = nombre.title()
		print(msg)

magicians = ["annie", "morgana", "diana"]
show_magicians(magicians)

