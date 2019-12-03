class artista(object):


    def __init__(self, **args):
        self._id = args.get('id')
        self._area = args.get('area')
        self._typeC = args.get('typeC')
        self._nombre = args.get('nombre')
        self._sort = args.get('sort')
        self._idd = args.get('idd')
        self._extScore = args.get('extScore')

    def __str__(self):
        return f'''Id -> {self._idd}\nNombre -> {self._nombre}\n
        Otro Nombre -> {self._sort}\nTipo Ciudad -> {self._typeC}\n
        Ext:Score -> {self._extScore}'''