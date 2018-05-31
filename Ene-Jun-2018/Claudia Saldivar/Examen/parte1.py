import json

class Report:
    def _init_(self,**args):
              self.Titulo=args.get('Title')
              self.Date=arg.get('2018-05-23')

    def getContents(self,Titulo='A Clockwork Orange',Date='1971'):
        return Titulo,Date

    def formatJson(self):
    	return json.dumps(self.getContents())

report = Report()
print(report.getContents())
