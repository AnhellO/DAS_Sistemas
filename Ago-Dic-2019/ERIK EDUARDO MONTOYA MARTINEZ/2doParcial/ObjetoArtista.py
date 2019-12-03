class Artista(object):
    def __init__(self, **args):
        self._id = args.get('id')
        self._area = args.get('area')
        self._tipoc = args.get('TipoC')
        self._name= args.get('nombre')
        self._sortname = args.get('nombreBus')
        self._id2 = args.get('id2')
        self._eScore = args.get('extScore')
    def __str__(self):
        return
        '''id: {}\n 
        nombre: {}\n 
        nombreBus: {}\n 
        TipoCd: {}\n 
        ExtScore: {}\n '''.format(self._id2, self._name,self._sortname, self._tipoc, self._eScore)
