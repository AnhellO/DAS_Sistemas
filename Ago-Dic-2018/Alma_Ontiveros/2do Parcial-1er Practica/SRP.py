import json

class Report:
    def getTitle(self):
        return "Title!"
    def getDate(self):
        return "2018-05-23"

class Contents(Report):
    def getContents(self, report):
        return {
        	"title": report.getTitle(),
        	"date": report.getDate()
        }

    def formatJson(self, report):
        return json.dumps(self.getContents(report))

report = Report()
contents = Contents()
print(contents.formatJson(report))

#EXPLICACIÓN
#Igual que el programa OCP.py busqué por Internet en tutoriales como hacerlo
#y guiarme, y lo que entendí fue que siguiendo el tema Single Responsability Principle
#las funciones que se encuentran dentro de la clase Report van a ser regresadas a la
#clase Contents donde devuelve el titulo y la fecha. Esta clase la cree para darle
#otra vista y también para no afectar la clase Reporte si despues se desea agregar mas
#formato a la clase creada y sea mas sencillo y seguro.
#Cuando la funcion regresa el contenido del reporte del titulo y la fecha, esto lo
#convierte en un "json" gracias al método "dumps".
#Al ultimo el print solo muestra los datos solicitados.