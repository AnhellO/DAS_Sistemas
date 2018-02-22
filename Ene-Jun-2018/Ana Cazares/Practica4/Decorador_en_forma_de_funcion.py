# El nombre de la funcion es el nombre del decorador y recibe la funcion que decora.
# En este caso logger tiene como funcion registrar los parametros recibidos.
def logger(fn):
 	# Este wrapper lo usas para atrapar los parametros de la funcion decorada
    def wrapper(*args):
         
        # esta es la funcionalidad de la decoracion
        for i, arg in enumerate(args):
            print ("arg %d:%d" % (i, arg))
         
        # no se debe olvidar ejecutar la funcion que se esta decorando o esta seria sobre escrita. 
        return fn(*args)
 
    return wrapper

# Sumador va a sumar todos los argumentos enviandos, sin importar cuantos son.
@logger
def Sumador(*args):
    return sum([i for i in args])
     
# Ejecuto mi funcion decorada.     
Sumador(1,2,3,4)

# Retornara
# arg 0:1
# arg 1:2
# arg 2:3
# arg 3:4
