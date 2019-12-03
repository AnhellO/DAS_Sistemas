from Vehiculo import vehiculo

class automovil(vehiculo):

    def __init__(self, tipo, modelo, **atributos):
        super().__init__(tipo, modelo)
        self._marca = atributos.get('marca')
        self._color = atributos.get('color')
    

    def traslado(self):
        print("El carro se mueve a 40 km/hr")

    def detener(self):
        print('el auto se detuvo')

    def get_marca(self):
        return self._marca
    
    def set_marca(self,marca):
        self._marca = marca

    def get_modelo(self):
        return self._marca
    
    def set_modelo(self, modelo):
        self._modelo = modelo
    
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color
        

    def __str__(self):
        return 'Tipo: {} \nMarca: {} \nModelo: {} \nColor: {}'.format(self._tipo, self._marca, self._modelo, self._color).strip()
    