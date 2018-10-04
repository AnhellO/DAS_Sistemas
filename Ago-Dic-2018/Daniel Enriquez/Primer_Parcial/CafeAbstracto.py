def establecer_tipo_decorator(funcion):
    def envoltorio1(instancia, tipo,precio):#este es el decorador
        funcion(instancia, tipo,precio)
    return envoltorio1
#Agrega el costo adicional segun el ripo de cafe 
def obtener_costo_decorator(tipo):
    def envoltorio1(funcion):
        def envoltorio2(instancia):
			if(tipo==1):
				precio=precio+7
            print('cafe con vainilla a '+preico)
			if(tipo==2):
				precio=precio+3
			return print('cafe con leche a '+precio)
	    	if(tipo==3):
				precio=precio+5
		    return print('cafe con canela a '+precio)
			if(tipo==4):
				precio=precio+8
		    return print('cafe con leche con canela a '+precio)
        return envoltorio2
    return envoltorio1

class CafeAbstracto(object):
	precio=25
    @establecer_tipo_decorator
    def establecer_costo(self, tipo,preico):
        self.tipo = tipo
		self.precio=precio


    @obtener_costo_decorator(1)
    @obtener_costo_decorator(2)
    @obtener_costo_decorator(3)
	@obtener_costo_decorator(4)
    def obtener_costo(self):
        return self.tipo
