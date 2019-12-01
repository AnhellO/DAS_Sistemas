class usuarios():
    
    def __init__(self,Id,Nombre,NombreUsuario,Email,calle,suite,ciudad,codigozip,latitud,longitud,telefono,website,compañiaNonmbre,catchPhrase,bs):
        self._Id = Id
        self._Nombre = Nombre
        self._NombreUsuario = NombreUsuario
        self._Email = Email
        self._Calle = calle
        self._Suite = suite
        self._Ciudad = ciudad
        self._CodigoZip = codigozip
        self._Latitud = latitud
        self._Longitud = longitud
        self._Telefono = telefono
        self._WebSite = website
        self._CompañiaNombre = compañiaNonmbre
        self._CatchPhrase = catchPhrase
        self._Bs = bs

    def __str__(self):
        return "Id: {}\nNombre: {}\nNombre Usuario: {}\nE-mail: {}\nCalle: {}\nSuite: {}\nCiudad: {}\nCodigo Zip: {}\nLatitud: {}\nLongitud: {}\nTelefono: {}\nWeb Site: {}\nCompañia: {}\nCatch Phrase: {}\nBs: {}".format(self._Id,self._Nombre,self._NombreUsuario,self._Email,self._Calle,self._Suite,self._Ciudad,self._CodigoZip,self._Latitud,self._Longitud,self._Telefono,self._WebSite,self._CompañiaNombre,self._CatchPhrase,self._Bs).strip() 