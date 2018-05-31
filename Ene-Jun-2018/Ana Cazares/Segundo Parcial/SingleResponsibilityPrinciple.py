import json

class Report: #clase que encapsula el concepto y sus funadamentos
    def _init_(self,**args):
              self.Titulo=args.get('Title')
              self.Date=arg.get('2018-05-23')

    def getContents(self,Titulo='A Clockwork Orange',Date='1971'):
        return Titulo,Date 
    def formatJson(self):
        return json.dumps(self.getContents())

report = Report()
print(report.getContents())
#primero separamos la presentacion logica ,una vez identificado las clases
#separamos las responsabilidades e intercambiamos metodos
#sin afectar Report clase