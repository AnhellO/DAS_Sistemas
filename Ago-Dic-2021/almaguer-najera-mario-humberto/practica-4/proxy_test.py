import unittest
from proxy import *


class tests(unittest.TestCase):

    def test_cantidad_mil(self):
        # Crear una cuenta de banco.
        cuenta_banco = CuentaBanco()
        # Crear nuestra tarjeta de credito o proxy
        proxy = TarjetaCreditoProxy(cuenta_banco)
        # Solicitar un pago de x cantidad
        cantidad_solicitada = 1000
        proxy.solicitar(cantidad_solicitada)
        # Comprobar que el saldo de la cuenta sea igual a la cantidad solicitada
        resultado = proxy.cuenta_banco.get_dinero()
        self.assertEqual("El saldo de la persona es: {}".format(
            cantidad_solicitada), resultado)

    def test_cantidad_cero(self):
        # Crear una cuenta de banco.
        cuenta_banco = CuentaBanco()
        # Crear nuestra tarjeta de credito o proxy
        proxy = TarjetaCreditoProxy(cuenta_banco)
        # Solicitar un pago de x cantidad
        cantidad_solicitada = 0
        proxy.solicitar(cantidad_solicitada)
        # Comprobar que el saldo de la cuenta sea igual a la cantidad solicitada
        resultado = proxy.cuenta_banco.get_dinero()
        self.assertEqual("El saldo de la persona es: {}".format(
            cantidad_solicitada), resultado)

    def test_cantidad_cambio(self):
        # Crear una cuenta de banco.
        cuenta_banco = CuentaBanco()
        # Crear nuestra tarjeta de credito o proxy
        proxy = TarjetaCreditoProxy(cuenta_banco)
        # Solicitar un pago de x cantidad
        cantidad_solicitada = 6500
        proxy.solicitar(cantidad_solicitada)
        cantidad_solicitada = 8500
        proxy.solicitar(cantidad_solicitada)
        # Comprobar que el saldo de la cuenta sea igual a la cantidad solicitada
        resultado = proxy.cuenta_banco.get_dinero()
        self.assertEqual("El saldo de la persona es: {}".format(
            cantidad_solicitada), resultado)


if __name__ == '__main__':
    unittest.main()
