class characters():
    
    def __init__(self,Id,Nombre,Status,Species,Tipo,Origen,Location,Id_locacion,Episode,Id_episodio,Url):
        self._Id = Id
        self._Nombre = Nombre
        self._Status = Status
        self._Species = Species
        self._Origen = Origen
        self._Tipo = Tipo
        self._Location = Location
        self._Id_Locacion = Id_locacion
        self._Episode = Episode
        self._Id_Episodio = Id_episodio
        self._Url = Url

    def __str__(self):
        return 'Id: {}\nNombre: {}\nStatus: {}\nEspecies: {}\nTipo: {}\nOrigen: {}\nLocacion: {}\nNumero Locacion: {}\nEpisodios: {}\nNumero Episodio: {}\nUrl: {}'.format(self._Id,self._Nombre,self._Status,self._Species,self._Tipo,self._Origen,self._Location,self._Id_Locacion,self._Episode,self._Id_Episodio,self._Url).strip() 