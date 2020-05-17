
class CuentaHandler(object):

    def __init__(self,sucesor):
        self.sucesor = sucesor

    def set_sucesor(self,sucesor):
        pass

    def pagar(self,monto):
        pass

#se crean tres cuentas con capacidades de pagar distintas
class cuentaUno(CuentaHandler):
    def __init__(self):
       self.capacity = 150

    def pagar(self,monto):
        if monto == self.capacity:
            return f'Tu pago se realizo correctamente'
        elif monto != self.capacity:
            self.set_sucesor(cuentaDos)
            print("Tu pago no se realizo")
            return monto


class cuentaDos(CuentaHandler):
    def __init__(self):
        self.capacity = 250

    def pagar(self,monto):
        if monto == self.capacity:
            return f'Tu pago se realizo correctamente'
        elif monto != self.capacity:
            self.set_sucesor(cuentaTres)
            print("Tu pago no se realizo")
            return monto


class cuentaTres(CuentaHandler):
    def __init__(self):
        self.capacity = 200
    def pagar(self, monto):
        if monto == self.capacity:
            return f'Tu pago se realizo correctamente'
        elif monto != self.capacity:
            return f'No quedan mas formas de pago'


if __name__ == "__main__":
    #se crean instancias de las cuentas
    c1 = cuentaUno()
    c2 = cuentaDos()
    c3 = cuentaTres()

    #se llama al def pagar y se delega la responsabilidad hasta la tercer cuenta
    pagar1 = c1.pagar(200)
    pagar2 = c2.pagar(pagar1)
    pagar3 = c3.pagar(pagar2)

    #pruebas
    print(pagar1)
    print(pagar2)
    print(pagar3)




