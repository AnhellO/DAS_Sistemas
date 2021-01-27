from vehiculo import Vehiculo

class Automovil(Vehiculo):
    
    def __init__(self,tipo,marca,color,modelo,pasajeros):
        self._tipo = "Terrestre"
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._pasajeros = pasajeros

    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_tipo(self):
        return self._tipo

    def set_marca(self, marca):
        self._marca = marca

    def get_marca(self):
        return self._marca

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_modelo(self):
        return self._modelo

    def set_pasajeros(self, pasajeros):
        self._pasajeros = pasajeros

    def get_pasajeros(self):
        return self._pasajeros  

    @staticmethod
    def traslado(**atributos):
        tipo = atributos.get('tipo')
        marca = atributos.get('marca')
        color = atributos.get('color')
        modelo = atributos.get('modelo')
        pasajeros = atributos.get('pasajeros')
        return Automovil(tipo,marca,color,modelo,pasajeros)

    def __str__(self):
        return '''
            Tipo: {}\nMarca: {}\nColor: {}\nModelo: {}\nPasajeros: {}
        '''.format(self._tipo,self._marca,self._color,self._modelo,self._pasajeros)
