class Vehiculo:
    # Clase para representar un vehículo.

    def __init__(self, modelo, color, transmision, motor, cilindros, sku):
        # Inicializa atributos para describir cada vehículo.
        self.modelo = modelo
        self.color = color
        self.transmision = transmision
        self.motor = motor
        self.cilindros = cilindros
        self.sku = sku
        self.existencia = 1

    def get_modelo(self):
        # Regresa el modelo.
        return self.modelo

    def set_modelo(self, modelo):
        # Asigna un modelo.
        self.modelo = modelo

    def get_color(self):
        # Regresa el color.
        return self.color

    def set_color(self, color):
        # Asigna un color.
        self.color = color

    def get_transmision(self):
        # Regresa el tipo de transmisión.
        return self.transmision

    def set_transmision(self, transmision):
        # Asigna un tipo de transmisión.
        self.transmision = transmision

    def get_motor(self):
        # Regresa el tipo de motor.
        return self.motor

    def set_motor(self, motor):
        # Asigna un motor.
        self.motor = motor

    def get_cilindros(self):
        # Regresa la cantidad de cilindros que posee.
        return self.cilindros

    def set_cilindros(self, cilindros):
        # Asigna una cantidad de cilindros.
        self.cilindros = cilindros

    def get_sku(self):
        # Regresa el SKU.
        return self.sku

    def set_sku(self, sku):
        # Asigna un SKU.
        self.sku = sku

    def get_existencia(self):
        # Regresa el número de existencia.
        return self.existencia

    def incrementa_existencia(self):
        # Incrementa la existencia del vehículo por 1.
        self.existencia += 1

    def decrementa_existencia(self):
        # Decrementa la existencia del vehículo por 1.
        if self.existencia > 0:
            self.existencia -= 1
        else:
            print("No puedes tener un número de existencias negativo.")

    def get_info_vehiculo(self):
        # Regresa un resumen del vehículo.
        info = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.modelo, self.color,
        self.transmision, self.motor, self.cilindros, self.sku, self.existencia)
        return info

'''
mi_vehiculo = Vehiculo('Ford Focus S 2017', 'Plata', 'Automático', '2.0L', 3, 'F-FocS-2017')
mi_vehiculo.color = 'Rojo'
mi_vehiculo.decrementa_existencia()
mi_vehiculo.decrementa_existencia()
print(mi_vehiculo.get_info_vehiculo())
'''
