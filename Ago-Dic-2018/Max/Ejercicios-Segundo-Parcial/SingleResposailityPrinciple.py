import json #Formato de intercambio de datos con una respectiva API
from abc import ABCMeta, abstractmethod #Metaclase para la definición de clases base abstractas, Utilice esta metaclase para crear un ABC

#Single Responsibility Principle : Una clase, función y/o objeto
#debe de tener una única responsabilidad, y esta responsabilidad
#debe de ser su única razón para cambiar.

class Report(object): #Al usar clases abstractas quito mas peso al main principal

    __metaclass__ = ABCMeta #Creando una "subclase virtual"

    @abstractmethod
    def getTitle(self, title):
        pass #Operacion nula

    @abstractmethod
    def getDate(self, date):
        pass #Operacion nula

class Contents(Report):

    def __init__(self, title, date): #Constructor del objeto
        self.title = None
        self.date = None

    def getTitle(self, title):
        self.title = title

    def getDate(self, date):
        self.date = date

    def getContents(self):
        return 'title'.self.getTitle(), 'data'.self.getDate()

    def formatJson(self):
    	return json.dumps(self.Contents())


def main():
    report = Contents('La divina comedia','2018-05-23')
    print(Contents.getContents())

main()
#Realize diferentes clases en las cuales dividi diferentes tareas, lo mas reducido que pude
#para asi ovedecer el principio SRD, y ademas quitar tanta carga como fuer aposible
#a una sola clase y/o funcion.
