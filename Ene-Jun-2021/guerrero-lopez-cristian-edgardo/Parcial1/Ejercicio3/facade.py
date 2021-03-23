class Enjuaganding:
    @staticmethod
    def method():
        return "Enjuagando...\n"

class Lavanding:
    @staticmethod
    def method():
        return "Lavando...\n"

class Finalizanding:
    @staticmethod
    def method():
        return "Finalizado!\n"

class Centrifuganding:
    @staticmethod
    def method():
        return "Centrifugando...\n"

class LavadoraFacade:
    def __init__(self):
        self.lavanding=Lavanding()
        self.enguajanding=Enjuaganding()
        self.centrifuganding=Centrifuganding()
        self.fining=Finalizanding()

    def ciclo_completo(self):
        r=self.lavanding.method()
        r+=self.enguajanding.method()
        r+=self.centrifuganding.method()
        r+=self.fining.method()
        print(r,end="")

        return r

    def solo_centrifugado(self):
        r=self.centrifuganding.method()
        r+=self.fining.method()
        print(r,end="")

        return r
'''
FACADE = LavadoraFacade()
RESULTADO = FACADE.ciclo_completo()
print(RESULTADO)
'''