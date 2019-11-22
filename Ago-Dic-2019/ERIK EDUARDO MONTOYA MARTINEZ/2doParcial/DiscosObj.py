class Discos():
    def __init__(self, id, NameArt, Title, Status, Type):
        self._id = id
        self._NameArt = NameArt
        self._Title = Title
        self._Status = Status
        self._Type = Type

    def __str__(self):
        return 'ID: {}\nArtista: {}\nTitle: {}\nStatus: {}\nTipo: {}'\
            .format(self._id,
                    self._NameArt,
                    self._Title,
                    self._Status,
                    self._Type)
