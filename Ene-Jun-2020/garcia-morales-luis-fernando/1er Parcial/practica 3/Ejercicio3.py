from abc import abstractmethod, ABCMeta
class CuentaHandler(metaclass=ABCMeta):

    @abstractmethod
    def set_sucesor(self,sucesor):
        pass

    @abstractmethod
    def pagar(self, monto):
        pass
class Tarjeta(CuentaHandler):
    def __init__(self):
        self.sucesor = None

    def set_sucesor(self, sucesor):
        self.sucesor = sucesor

    def pagar(self, monto):
        fondo = 150
        if monto >=fondo:
            resto = monto-fondo
            print(f"Se tomo ${fondo} disponibles de tarjeta, restan ${resto}")
            if resto != 0:
                self.set_sucesor(Efectivo.pagar(resto))
        else:
            self.sucesor.pagar("Se ha realizado la transaccion con exito")
class Efectivo(CuentaHandler):
    def pagar(monto):
        print(f"Se ha generado un formato de pago de ${monto} en efectivo")
        print("Transaccion realizada con exito")
def main():
    pago = Tarjeta()
    pago.pagar(200)

if __name__ == '__main__':
    main()
    