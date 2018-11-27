import json

class Report:

	def getTitle(self):

		return 'title'

	def getDate(self):
		return '2018-05-23'

class Contents(Report):

	def Contenido(self):
		return {
		'title': self.getTitle(),
		'date': self.getDate()
        }

	def formatJson(self):
		return json.dumps(self.Contenido())


class print:
	contenido = Contents()
	print(contenido.Contenido())

#Principio de Responsabilidad Unica 
#Este principio nos dice que cada clase debe de tener una sola responsabilidad
#lo que se debe hacer es crear diferentes clases que solo tengan 
#una responsabilida,en este caso la clase report da los datos necesarios
#la clase contents obtiene los datos y le da un formato
#la clase prit nos muestra en pantalla los datos 