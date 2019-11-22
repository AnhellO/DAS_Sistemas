class artist():
    def __init__(self, id_artista='', nombre='', tags='', area='', score='', tipo='group'):
        self._id = id_artista
        self._name = nombre
        self._tags = 'rock or metal'
        self._area = area
        self._extScore = score
        self._type = tipo

    def __str__(self):
        return 'id: {}\nNombre: {}\nTags: {}\nArea: {}\nGenero: {}\nTipo: {}'.format(self._id, self._name, self._tags, self._area, self._extScore, self._type)