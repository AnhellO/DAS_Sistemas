class Ave(Singleton):
	nombre = u""
		
a = Ave()
b = Ave()
 
a.nombre = u"Cuervo"
b.nombre = u"Gorrión"
print (a.nombre, b.nombre) # Gorrion Gorrion