class episodios():
    
    def __init__(self,Id,Nombre,Al_Aire,Episodio,Personaje,Id_Personaje,Url):
        self._Id = Id
        self._Nombre = Nombre
        self._Al_Aire = Al_Aire
        self._Episodio = Episodio
        self._Personaje = Personaje
        self._Id_Personaje = Id_Personaje
        self._Url = Url

    def __str__(self):
        return 'Id: {}\nNombre: {}\nFecha de Transmicion: {}\nEpisodio: {}\nPersonajes: {}\nId Personaje: {}\nUrl: {}'.format(self._Id,self._Nombre,self._Al_Aire,self._Episodio,self._Personaje,self._Id_Personaje,self._Url).strip() 