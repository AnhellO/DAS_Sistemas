class Agencia:
    # Definicion de __init__ y atributos de la clase Agencia
    def __init__(self, nombre, direccion):
        # Se inician atributos
        self.nombre = nombre
        self.direccion = direccion

    # Metodo getNombre
    def getNombre(self):
        return self.nombre

    # Metodo getDireccion
    def getDireccion(self):
        return self.direccion

    # ventaVehiculo regesa un string donde se muestran los datos de los
    # participantes en la venta de un Vehiculo
    def ventaVehiculo(self, Cli, Vehi, Vend):
        return "Cliente: {0}\nVehiculo: {1}\nVendedor: {2}".format(Cli, Vehi, Vend)

    # compraVehiculo regresa un string donde se muestran la cantidad y el Vehiculo
    # que la Agencia vendió
    def compraVehiculo(self, n, Vehi):
        return "Cantidad: {0}\nVehiculo: {1}".format(n, Vehi)
