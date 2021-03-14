class Lavado:
    @staticmethod
    def method():
        return "Lavando...\n"

class Enjuagado:
    @staticmethod
    def method():
        return "Enjuagando...\n"

class Centrifugado:
    @staticmethod
    def method():
        return "Centrifugando...\n"

class Finalizado:
    @staticmethod
    def method():
        return "Finalizado!\n"

class Lavadorafacade:
    def __init__(self):
        self.lavado=Lavado()
        self.enguajado=Enjuagado()
        self.centrifugado=Centrifugado()
        self.fin=Finalizado()

    def ciclo_completo(self):
        r=self.lavado.method()
        r+=self.enguajado.method()
        r+=self.centrifugado.method()
        r+=self.fin.method()
        print(r,end="")
        return r

    def solo_centrifugado(self):
        r=self.centrifugado.method()
        r+=self.fin.method()
        print(r,end="")
        return r