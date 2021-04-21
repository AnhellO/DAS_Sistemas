class Enjuagar:
    @staticmethod
    def method():
        return "Enjuagando...\n"

class Lavar:
    @staticmethod
    def method():
        return "Lavando...\n"

class Finalizar:
    @staticmethod
    def method():
        return "Finalizado!\n"

class Centrifugar:
    @staticmethod
    def method():
        return "Centrifugando...\n"

class LavadoraFacade:
    def __init__(self):
        self.lavar=Lavar()
        self.enguajar=Enjuagar()
        self.centrifugar=Centrifugar()
        self.finalizar=Finalizar()

    def ciclo_completo(self):
        resultado=self.lavar.method()
        resultado+=self.enguajar.method()
        resultado+=self.centrifugar.method()
        resultado+=self.finalizar.method()
        print(resultado,end="")

        return resultado

    def solo_centrifugado(self):
        resultado=self.centrifugar.method()
        resultado+=self.finalizar.method()
        print(resultado,end="")

        return resultado
'''
FACADE = LavadoraFacade()
RESULTADO = FACADE.ciclo_completo()
print(RESULTADO)
'''