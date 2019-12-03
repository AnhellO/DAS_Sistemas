from Vehiculo import vehiculo

class barco(vehiculo):
    
    def __init__(self, tipo, modelo, **atributos):
        super().__init__(tipo, modelo)
        self._nombre = atributos.get('nombre')
        self._color = atributos.get('color')
        self._capacidad = atributos.get('capacidad')

    def traslado(self):
        print('el barco se mueve')

    def detener(self):
        print('el barco se detuvo')

    def __str__(self):
        return 'Tipo: {} \nModelo: {} \nNombre {} \nColor: {} \nCapacidad {}'.format(self._tipo, self._modelo, self._nombre, self._color, self._capacidad).strip()

