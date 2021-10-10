from abc import ABC, abstractmethod, abstractclassmethod

class IPago(ABC):

    @abstractmethod
    def solicitar():
        '''Metodo de la interfaz'''

class CuentaBanco(IPago):
    
    def __init__(self, dinero = 0) -> None:
        self.dinero = dinero

    def set_dinero(self, dinero : int):
        self.dinero = dinero

    def get_dinero(self):
        return "El saldo de la persona es: {}".format(self.dinero)

    def solicitar():
        print('Cuenta de banco: Trabajando en la solicitud de pago')

class TarjetaCreditoProxy(IPago):
    
    def __init__(self, cuenta_banco: CuentaBanco) -> None:
        self.cuenta_banco = CuentaBanco()

    def solicitar(self, cantidad_dinero):
        if self.checar_validacion():
            self.cuenta_banco.set_dinero(cantidad_dinero)
            self.registrar_transferencia()

    
    def checar_validacion(self):
        print('Proxy: Checando validacion')
        #Codigo para verificar la validacion
        return True

    def registrar_transferencia(self):
        print('Proxy: Registrado la hora de transferencia')
        #Codigo para registrar la hora actual en un .txt


#Parte del cliente
cuenta_banco = CuentaBanco()
proxy = TarjetaCreditoProxy(cuenta_banco)
proxy.solicitar(1000)
print(proxy.cuenta_banco.get_dinero())
        