import json

class Report:

    def getTitle(self):
        return 'Title!'

    def getDate(self):
        return '2018-05-23'

    def getContents(self):
        return {
        	'title': self.getTitle(),
        	'date': self.getDate()
        }

class Fto(Report):

    def formatJson(self):
    	return json.dumps(self.getContents())

reportfto = Fto()
print(reportfto.formatJson())

#Agregue la clase "Fto"  para separar la funcion
#que le da formato, porque aplicar cambios a la clase 
#principal podria afectarnos la funcion del formato
