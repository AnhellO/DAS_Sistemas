import json

class Report:

    def getTitle(self):
        return 'Title!'

    def getDate(self):
        return '2018-05-23'

   # def getContents(self):
    #    return {
     #   	'title': self.getTitle(),
      #  	'date': self.getDate()
       # } 
class Contents:

    def formatJson(self):
        return json.dumps(report.getDate() + report.getTitle())
    
report = Report()
conts = Contents()
print(conts.formatJson())

#Realice estos cambios por lo siguiente: A lo que entendi sobre lo que leí del proposito del Single Responsibility Principle es que,
#Una clase no puede tener mas de una responsabilidad, la clase Report, contenia su titulo y una fecha, ademas de que se encargaba de mostrar 
#su información.
#Asi que considere que seria más optimo si lo separaba en dos clases donde una contenga la información del reporte, y otra adicional
#que muestre la información.
#No pude hacer que se imprimiera mas bonito. 