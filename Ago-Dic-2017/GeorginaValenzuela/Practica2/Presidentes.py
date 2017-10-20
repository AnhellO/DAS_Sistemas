class Singleton(object):
	_instance = None
	
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = object.__new__(cls, *args, **kwargs)
		
		return cls._instance

class Presidente(Singleton):
	nombre= ""
		
a = Presidente()
b = Presidente()
 
a.nombre = "Felipe Calderon"
b.nombre = "EPN"
print (a.nombre,b.nombre) #EPN EPN
