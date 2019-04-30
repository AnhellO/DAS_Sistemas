class InstrumentoMusical(object):
    """docstring for InstrumentoMusical"""

    def __init__(self, **argumentos):
        self.tipo = argumentos.get('tipo')
        self.marca = argumentos.get('marca')
        self.color = argumentos.get('color')

    def __str__(self):
        return """
        Tipo: {}\nMarca: {}\nColor: {}
        """.format(self.tipo, self.marca, self.color).strip()

class SingleFactory(object):
    """docstring for SingleFactory"""

    @staticmethod
    def makeInstrumento(**arg):
        return InstrumentoMusical(**arg)

mi_guitarra = SingleFactory.makeInstrumento(tipo='guitarra', marca='chibson', color='negro')
print(mi_guitarra)