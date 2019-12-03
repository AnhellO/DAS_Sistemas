from Vehiculo import vehiculo

class avion(vehiculo):

    def __init__(self, tipo, modelo, **atributos):
        super().__init__(tipo, modelo)
        self._color = atributos.get('color')
        self._nPasajeros = atributos.get('nPasajeros')
    
    def traslado(self):
        print("El avion avanza")

    def detener(self):
        print('el avion se detuvo')

    def __str__(self):
        return 'Tipo: {} \nModelo: {} \nColor: {} \nNumero de Pasajeros {}'.format(self._tipo, self._modelo, self._color, self._nPasajeros).strip()
