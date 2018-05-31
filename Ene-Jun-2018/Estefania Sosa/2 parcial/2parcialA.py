import json

class Report:
#1 sola responsabilidad . solo maneja geters
    def getTitle(self):
        return 'Title!'

    def getDate(self):
        return '2018-05-23'
class Cont(Report):
#1 sola responsabilidad regresa
    def getContents(self):
        return {
        	'title': self.getTitle(),
        	'date': self.getDate()
        }
class Imprime:
    #1 responsabilidad imprime
    def formatJson(self):
        contenido=Cont()
        return json.dumps(contenido.getContents())

#resultado
Im = Imprime()
print(Im.formatJson())
