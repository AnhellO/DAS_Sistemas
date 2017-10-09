class Electrodomestico:

    def __init__(self, marca, modelo, color, potencia, frecuencia):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.potencia = potencia
        self.frecuencia = frecuencia

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_potencia(self):
        return self.potencia

    def set_potencia(self, potencia):
        self.potencia = potencia

    def get_frecuencia(self):
        return self.frecuencia

    def set_frecuencia(self, potencia):
        self.frecuencia = frecuencia

    def encender(self):
        info = "{} {} ha sido encendido.".format(self.marca, self.modelo)
        return(info)

    def usar(self):
        info = "{} {} está en uso.".format(self.marca, self.modelo)
        return info

    def apagar(self):
        info = "{} {} ha sido apagado.".format(self.marca, self.modelo)
        return info




# mi_electro = Electrodomestico('A', '1', 'Azul',
# '100', '60')
# print(mi_electro.encender())
