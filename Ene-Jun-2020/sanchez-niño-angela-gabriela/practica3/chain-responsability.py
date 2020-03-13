from abc import ABCMeta, abstractmethod
class CuentaHandler(metaclass = ABCMeta):

    @abstractmethod
    def set_sucesor(self,sucesor):
        pass

    @abstractmethod
    def pagar(self,monto):
        pass

class tarjeta(CuentaHandler):
    def __init__(self):
        self._sucesor = None
    
    def set_sucesor(self,sucesor):
        self._sucesor = sucesor

    def pagar(self,monto):
        if monto >= 150:
            rest = monto-150
            print(f'Se ha realizado tu pago pero queda a deber ${rest}')
            if rest != 0:
                self.set_sucesor(efectivo.pagar(rest))
                
        else:
            self.set_sucesor(efectivo.pagar(monto))

class efectivo(CuentaHandler):
    def __init__(Self):
        self._sucesor = None
    
    def set_sucesor(self,sucesor):
        self._sucesor = sucesor
    
    def pagar(monto):
        if monto >= 50:
            rest = monto-50
            print (f'Se ha realizado tu pago, tu deuda queda en ${rest}')
            print(f'PAGO REALIZADO CON EXITO')


if __name__ == "__main__":
    x = tarjeta()
    x.pagar(200)
    







