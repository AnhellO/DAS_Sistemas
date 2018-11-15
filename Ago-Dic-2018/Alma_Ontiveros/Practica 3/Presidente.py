class Presidente(Singleton):
	nombre = " "
		
a = Presidente()
b = Presidente()
 
a.nombre = "Enrique Peña Nieto"
b.nombre = "AMLO"
print (a.nombre, b.nombre) # AMLO AMLO