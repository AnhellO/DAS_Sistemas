class personaje():

    def __init__(self, FechaDeCreacion, EpisodiosDondeAparece, NumeroEpisodiosDondeAparece, Genero, Id_Personaje, Imagen, Location_Name, Location_URL, Nombre, Origen_Name, Origen_URL, Especie, Status, Tipo, URL):
        self._FechaDeCreacion = FechaDeCreacion
        self._EpisodiosDondeAparece = EpisodiosDondeAparece
        self._NumeroEpisodiosDondeAparece = NumeroEpisodiosDondeAparece
        self._Genero = Genero
        self._Id_Personaje = Id_Personaje
        self._Imagen = Imagen
        self._Location_Name = Location_Name
        self._Location_URL = Location_URL
        self._Nombre = Nombre
        self._Origen_Name = Origen_Name
        self._Origen_URL = Origen_URL
        self._Especie = Especie
        self._Status = Status
        self._Tipo = Tipo
        self._URL = URL

    
    def __str__(self):
        return """
        Fecha de Creacion: {}
        Episodios Donde Aparece: {}
        Numero de Episodios Donde Aparece: {}
        Genero: {}
        Id_Personaje: {}
        Link de Imagen: {}
        Nombre de Locacion: {}
        Url de Locacion: {}
        Nombre: {}
        Nombre de Origen: {}
        Url de Origen: {}
        Especie: {}
        Status: {}
        Tipo: {}
        Url: {}
        """.format(self._FechaDeCreacion, self._EpisodiosDondeAparece, self._NumeroEpisodiosDondeAparece, self._Genero, self._Id_Personaje, self._Imagen, self._Location_Name, self._Location_URL, self._Nombre, self._Origen_Name, self._Origen_URL, self._Especie, self._Status, self._Tipo, self._URL)


"""
Resultados:
    FechaDeCreacion
    EpisodioDondeAparece
    Genero
    Id
    Image
    Location
        Name
        url
    Name
    Origin
        Name
        url
    especie
    status
    type
    url
"""