class discos():
    
    def __init__(self,Id,Banda,Titulo,Pais,Status):
        self._Id = Id
        self._Banda = Banda
        self._Titulo = Titulo
        self._Pais = Pais
        self._Status = Status

    def __str__(self):
        return 'Id: {}\nNombre: {}\nTitulo: {}\nPais: {}\nStatus: {}'.format(self._Id,self._Banda,self._Titulo,self._Pais,self._Status).strip()