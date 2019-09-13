import json

class Report:
    def __init__(self,title, date):
        self._title = 'title'
        self._date = 'date'

    def getTitle(self):
        return self._title()

    def getDate(self):
        return self._date()


class ReportPrinter(object):
    def __init__(self,Report):
        self._Report = report

    def getContents(self):
        return {
    'title': self._report.getTitle(),
    'date': self._report.getDate()
    }
    def formatJson(self):
        return json.dumps(self.getContents())

    def print(self):
        return print(self.getContents)

#El primer principio nos viene a decir que una clase debe ser especificamente para un solo proposito
#dicho esto separe en dos clases, una por asi decirlo de logica donde se establecen los valores y
#otra en la cua solo sirve para imprimir con un formato duchos valores, ademas de agregarles un constructor init el cual
#hace que asi se vualva mas eficiente en ves de estar modificando la clase Repor los valores de date y title, con ese constructor hace
#que aunque se cambien los valores que se le asignen  a date o title no se tien que modificar dicha clas cada vez
