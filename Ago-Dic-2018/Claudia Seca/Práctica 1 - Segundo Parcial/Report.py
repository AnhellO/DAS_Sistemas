import json


#Siguiendo el principio de Single Responsability Principle, pasé la Función que devuelve el contenido del reporte a otra clase, dejando
#en esta clase solo las funciones que devuelven el titulo y la fecha

class Report():

#Función que regresa el titulo
    def getTitle(self):
        return 'Title!'

#Función que regresa la fecha
    def getDate(self):
        return '2018-05-03'


class Content(Report):
#Función que regresa el contenido del reporte
    def getContent(self):
        return {
        	'title': self.getTitle(),
        	'date': self.getDate()
        }

    #Función que regresa el contenido y lo convierte a un json con el método 'dumps'
    def formatJson(self):
    	return json.dumps(self.getContent())


#Se asigna un reporte
content = Content()
print(content.formatJson())
