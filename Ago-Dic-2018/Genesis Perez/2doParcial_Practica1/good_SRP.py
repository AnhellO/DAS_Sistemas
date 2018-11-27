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

class Formato(Report):

    def formatJson(self):
        return json.dumps(self.getContents())

reportf = Formato()
print(reportf.formatJson())


# EXPLICACION:
# Los cambios que hice fueron para que no se mezclaran muy diferentes responsabilidades
# Cree una clase exclusiva para darle formato al reporte, de forma que si se quisiera
# presentar en otro formato solo se modifique esa clase unicamente sin afectar a todo lo existente
# Esta nueva clase creada hereda de la clase Report para que así se puedan usar sus
# distintas funciones sin alterarlas, dejando a cada clase con una sola responsabilidad como lo dice el SRP.
