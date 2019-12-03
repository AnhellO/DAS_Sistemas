class ubicaciones():
    
    def __init__(self,Id,Nombre,Tipo,Dimension,Residentes,Id_Residente,Url):
        self._Id = Id
        self._Nombre = Nombre
        self._Tipo = Tipo
        self._Dimension = Dimension
        self._Residentes = Residentes
        self._Id_Residente = Id_Residente
        self._Url = Url

    def __str__(self):
        return 'Id: {}\nNombre: {}\nTipo: {}\nDimension: {}\nResidentes: {}\nId Residente: {}\nUrl: {}'.format(self._Id,self._Nombre,self._Tipo,self._Dimension,self._Residentes,self._Id_Residente,self._Url).strip() 