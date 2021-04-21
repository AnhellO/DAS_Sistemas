
class Ciclo_Lavadora:
    def lavar(self): 
        print("Lavando...")

    def enjuagar(self): 
        print("Enjuagando...")

    def centrifugar(self): 
        print("Centrifugando...")
    
    def terminar(self):
        print("Finalizado!")

class Ciclo_Centrifuga:

    def solo_centrifugado(self): 
        print("Centrifugando...")

    def terminar(self):
        print("Finalizado!")

class LavadoraFacade:

    def __init__(self):
        self.ciclo_lavadora   = Ciclo_Lavadora()
        self.ciclo_centrifuga = Ciclo_Centrifuga()

    def ciclo_completo(self):
        self.ciclo_lavadora.lavar()
        self.ciclo_lavadora.enjuagar()
        self.ciclo_lavadora.centrifugar()
        self.ciclo_lavadora.terminar()
    
    def solo_centrifugado(self):
        self.ciclo_centrifuga.solo_centrifugado()
        self.ciclo_centrifuga.terminar()
 
 

if __name__ == "__main__":
    pass
     