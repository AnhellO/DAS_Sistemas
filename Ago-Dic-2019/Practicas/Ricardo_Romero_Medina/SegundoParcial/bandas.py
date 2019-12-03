class bandas():
    
    def __init__(self,Id,Banda,Tipo,Tag,Area):
        self._Id = Id
        self._Banda = Banda
        self._Tipo = Tipo
        self._Tag = 'Rock and Metal'
        self._Area = Area

    def __str__(self):
        return 'Id: {}\nNombre: {}\nTipo: {}\nTag: {}\nArea: {}'.format(self._Id,self._Banda,self._Tipo,self._Tag,self._Area).strip() 