from Guitarra import Guitarra
from Bateria import Bateria

class Factoria(object): 
		#Esta clase es nuestra factoria, se define un constructor sin argumentos por default para cada clase, por eso no hace falta escribir uno""" 
	
	def get_instrumentoMusical(self, tipo, color, marca, precioAproximado, tamaño, numeroElementos): 
		#Metodo que retorna objetos intrumento segun el tipo""" 	
		#tipo es el parametro usado por la factoria 
		#para elegir el obj a crear 
		if (tipo == 'Percusión'):
			 return Bateria(tipo, color, marca, precioAproximado, tamaño, numeroElementos) 
		elif (tipo == 'Cuerdas'): 
			 return Guitarra(tipo, color, marca, precioAproximado, tamaño, numeroElementos)
