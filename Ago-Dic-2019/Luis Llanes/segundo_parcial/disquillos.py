class album():
    def __init__(self, id_album, artista, titulo, status, tipo):
        self._id = id_album
        self._artista = artista
        self._titulo = titulo
        self._status = status
        self._type = tipo

    def __str__(self):
        return 'ID: {}\nArtista: {}\nTitulo: {}\nStatus: {}\nTipo: {}'.format(self._id, self._artista, self._titulo, self._status, self._type)