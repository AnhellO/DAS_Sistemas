import json

class Report:

    def getTitle(self):
        return 'Title!'

    def getDate(self):
        return '2018-05-23'

class Content():
    def getContents(self, report):
        return {
        	'title': report.getTitle(),
        	'date': report.getDate()
        }

    def formatJson(self, report):
    	return json.dumps(self.getContents(report))

report = Report()
content = Content()
#print(report.formatJson())
print(content.formatJson(report))

'''
Para aplicar el Singe Responsability Principle moví los metodos que modifican el contenido a otra clase,
por si se necesita despues que el contenido del reporte sea en otro formato, poder codificar sin alterar
losmetodos de la clase Report ya existente.
'''
