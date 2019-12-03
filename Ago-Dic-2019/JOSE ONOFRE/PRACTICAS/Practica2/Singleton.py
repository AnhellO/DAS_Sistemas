class Singleton(object):

    __instancia = None  ## Private para que no sea modificado
    nombre = None #Para mostrar los diferentes nombres sobre el mismo objeto

    def __str__(self):
        string= self.nombre
        return string

    def __new__(cls):
        if Singleton.__instancia is None:
            Singleton.__instancia = object.__new__(cls)
        return Singleton.__instancia


ObjetoA = Singleton()  ##Creamos el ObjetoA del tipo Singleton
ObjetoA.nombre = "Objeto A" ##Asignamos el nombre del objeto A
print(ObjetoA) ##Imprimimos el objeto A para ver su direccion

ObjetoB = Singleton()  ##Creamos el ObjetoB del tipo Singleton
ObjetoB.nombre = "Objeto B" ##Asignamos el nombre del objeto B
print(ObjetoB) ##Imprimos el objeto para ver su direccion

ObjetoC = Singleton()  ##Creamos el ObjetoC del tipo Singleton
ObjetoC.nombre = "Objeto C" ##Asignamos el nombre del objeto B
print(ObjetoC) ##Imprimos el objeto para ver su direccion


