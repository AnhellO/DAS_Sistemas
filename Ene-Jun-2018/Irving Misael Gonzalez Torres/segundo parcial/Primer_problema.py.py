class Report:

    def __init__(self, **args):
        self.title = args.get('title')
        self.date = args.get('date')

class Content:
    
    def __init__(self, objeto = None):
        self.objetos = {}

        if objeto:
            self.agregarObjeto(objeto)

    def agregarObjeto(self, objeto):
        self.objetos[objeto.__class__.__name__] = objeto

    def getPropiedades(self, objeto):
        args = [i for i in objeto.__dict__.keys() if not i.startswith('_')]
        values = [i for i in objeto.__dict__.values()]
        return dict(zip(args, values))

    def PrintContent(self, objeto):
        iObjeto = self.objetos.get(objeto.__class__.__name__)
        print(self.getPropiedades(iObjeto) if iObjeto else "No existe el objeto")


reporte = Report(title="Cero Miedo.", date="2018-05-23")
printer = Content()
printer.agregarObjeto(reporte)
printer.PrintContent(reporte)
