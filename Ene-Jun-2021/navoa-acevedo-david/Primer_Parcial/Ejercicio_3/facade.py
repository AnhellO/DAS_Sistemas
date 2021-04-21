
#Clases del ciclo de lavado
class lavando:
    #Etapa 1. Lavado
    def lavado(self):
        print("Lavando...")

class enjuagando:
    #Etapa 2. Enjuagado
    def enjuagado(self):
        print("Enjuagando...")

class centrifugando:
    #Etapa 3. Centrifugado
    def centrifugado(self):
        print("Centrifugando...")

class finalizado:
    #Etapa 4. Finalizado de ciclo
    def finalizar(self):
        print("Finalizado!")

class LavadoraFacade:

    def __init__(self):
        self.lavando = lavando()
        self.enjuagando = enjuagando()
        self.centrifugando = centrifugando()
        self.finalizando = finalizado()

    #Lista de ciclos
    def ciclo_completo(self):
        self.lavando.lavado()
        self.enjuagando.enjuagado()
        self.centrifugando.centrifugado()
        self.finalizando.finalizar()

    def solo_centrifugado(self):
        self.centrifugando.centrifugado()
        self.finalizando.finalizar()

    def solo_lavado(self):
        self.lavando.lavado()
        self.finalizando.finalizar()

    def solo_enjuagado(self):
        self.enjuagando.enjuagado()
        self.finalizando.finalizar()
