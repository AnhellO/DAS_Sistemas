import json

class Report:

    def getTitle(self):
        return 'Title!'

    def getDate(self):
        return '2018-05-23'

class Contents(Report):
    def Title(self):
        return {'title':self.getTitle()}
    def Date(self):
        return {'date':self.getDate()}

    def formatJson(self):
    	return json.dumps(self.getContents())

class print:
    contents = Contents()
    print(contents.Title(),contents.Date())

#Cree una clase para las difrentes tareas que realiza el codigo, la clase Report se encarga de dar los datos.
#La clase Contents se encarga de obtener los datos.
#La clase print se encarga de mostrar los datos
#Todo esto es por que el principio de Responsabilidad Única nos dice que un objeto debe realizar una única cosa
