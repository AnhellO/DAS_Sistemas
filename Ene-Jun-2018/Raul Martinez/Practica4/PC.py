class UnidadDeProceso:
  
    def Proceso(self):
            print("Procesando...")
 
class MostrarUnidad:

    def Mostrar(self):
            print("Mostrando...")
 
class Memoria:
  
    def Operacion(self):
            print("Escribiendo y leyendo memoria...")
 
class Computadora:
    '''Facade'''
    def __init__(self):
        self.unidadDeProceso = UnidadDeProceso()
        self.mostrarUnidad = MostrarUnidad()
        self.memoria = Memoria()
 
    def EncenderPc(self):
        self.unidadDeProceso.Proceso()
        self.memoria.Operacion()
        self.mostrarUnidad.Mostrar()
 
computadora = Computadora()
computadora.EncenderPc()
