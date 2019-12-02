class episodio():
    def __init__(self, FechaLanzamiento, Personajes, FechaCreacion, CodEpisodio, Id_Episodio, Nombre, URL):
        self._FechaLanzamiento = FechaLanzamiento
        self._Personajes = Personajes
        self._FechaCreacion = FechaCreacion
        self._CodEpisodio = CodEpisodio
        self._Id_Episodio = Id_Episodio
        self._Nombre = Nombre
        self._URL = URL

    def __str__(self):
        return """
        Fecha de Lanzamiento: {}
        Personajes: {}
        Fecha de Creacion: {}
        Episodio: {}
        Id_Episodio: {}
        Nombre: {}
        Url: {}
        """.format(self._FechaLanzamiento, self._Personajes, self._FechaCreacion, self._CodEpisodio, self._Id_Episodio, self._Nombre, self._URL)
