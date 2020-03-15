class CuentaHandler:
    """docstring for CuentaHandler"""

    sucesor = None
    monto = None

    def set_sig(self, cuenta):
        self.sucesor = cuenta

    def alc_pagar(self, montoo: int):
        return self.monto >= montoo

    def pagar(self, monto_a_pagar):
        tipo_pago = self.__class__.__name__
        if self.alc_pagar(monto_a_pagar):       # Si alcanza a pagar con x tipo de pago imprime lo siguiente
            print('\n*** Pagaste los $' + str(monto_a_pagar) + ' con ' + tipo_pago + '!!! :v')
        elif self.sucesor:      # Si no completa con un tipo de pago, pasa al siguiente tipo y checa si completa, si no completa, continúa con el que sigue
            print('\n- No completas con ' + tipo_pago + ' compa :c')
            print('~ Mejor checa tu siguiente forma de pago...\n')
            self.sucesor.pagar(monto_a_pagar)
        else:       # Si no completa con ningún tipo de pago imprime lo siguiente
            print('\n*** Mejor vete, no completas con ningún tipo de pago  :c')


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

class Efectivo(CuentaHandler):
    monto = None

    def __init__(self, monto1):
        self.monto = monto1


class Tarjeta(CuentaHandler):
    monto = None

    def __init__(self, monto1):
        self.monto = monto1


class SamsungPay(CuentaHandler):
    monto = None

    def __init__(self, monto1):
        self.monto = monto1


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

if __name__ == '__main__':
    efectivo = Efectivo(150)  # Monto que se tiene en efectivo
    tarjeta = Tarjeta(175)  # Monto que se tiene en la tarjeta
    samsungPay = SamsungPay(200)  # Monto que se tiene en SP

    efectivo.set_sig(tarjeta)
    tarjeta.set_sig(samsungPay)

    efectivo.pagar(200)     # Costo de x artículo
