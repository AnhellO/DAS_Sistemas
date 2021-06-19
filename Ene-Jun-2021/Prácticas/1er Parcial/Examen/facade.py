# Subsistema 1
class Lavado:
    def lavar(self):
        print("Lavando...")
  
# Subsistema 2
class Enjuagado:
    def enjuagar(self):
        print("Enjuagando...")
  
# Subsistema 3
class Centrifugado:
    def centrifugar(self):
        print("Centrifugando...")

# Facade  
class LavadoraFacade:
    def __init__(self):
        self.lavado = Lavado()
        self.enjuagado = Enjuagado()
        self.centrifugado = Centrifugado()
  
    def ciclo_completo(self): 
        self.lavado.lavar()
        self.enjuagado.enjuagar()
        self.centrifugado.centrifugar()
        print("Finalizado!")

    def solo_centrifugado(self):
        self.centrifugado.centrifugar()
        print("Finalizado!")
