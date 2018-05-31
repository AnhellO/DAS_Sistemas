"""
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

    def formatJson(self):
    	return json.dumps(self.getContents())

report = Report()
print(report.getContents())
"""


###################################################################################################
###################################################################################################
###################################################################################################

import json

class Title:
    def getTitle(self):
        return "Title"

    def Json(self):
        return json.dumps(self.getTitle())

class Date:
    def getDate(self):
        return "2018-05-23"

    def Json(self):
        return json.dumps(self.getDate())

class Contents:
    def getContents(self, title="titulo", date="2018-05-23"):
        return "title:{}\ndate:{}".format(title, date)

    def Json(self):
        return json.dumps(self.getContents())

titulo = Title()
print(titulo.getTitle())

fecha = Date()
print(fecha.getDate())

contenido = Contents()
print(contenido.getContents())

"""
Separé las funcionalidades en clases para que las peticiones sean más sencillas de implementar y
si llegase a existir algun crecimiento, que no haya tanto problema para implementar las nuevas
funcionalidades
"""