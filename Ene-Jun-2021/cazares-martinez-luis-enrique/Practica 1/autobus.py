from vehiculo import vehiculo


class autobus(vehiculo):

    def tarifaAutobus(self):
        return float(vehiculo.tarifa(self)) + ((vehiculo.random * 100) * 0.10)
