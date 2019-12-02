class locacion():
    def __init__(self, FechaCreacion, Dimension, Id_Locacion, Nombre, Residentes, Tipo, URL):
        self._FechaCreacion = FechaCreacion
        self._Dimension = Dimension
        self._Id_Locacion = Id_Locacion
        self._Nombre = Nombre
        self._Residentes = Residentes
        self._Tipo = Tipo
        self._URL = URL

    def __str__(self):
        return """
        Fecha de Creacion: {}
        Dimension: {}
        Id Locacion: {}
        Nombre: {}
        Residentes: {}

        Tipo: {}
        Url: {}
        --------------------------------------------""".format(self._FechaCreacion, self._Dimension, self._Id_Locacion, self._Nombre, self._Residentes, self._Tipo, self._URL)