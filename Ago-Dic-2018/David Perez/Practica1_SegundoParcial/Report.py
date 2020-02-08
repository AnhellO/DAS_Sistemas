import json
#Principio de Single responsability,
#se pasa el formato del reporte a otra clase
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
class formato(Report):
    def formatJson(self):
    	return json.dumps(self.getContents())

report = Report()
print(report.getContents())
