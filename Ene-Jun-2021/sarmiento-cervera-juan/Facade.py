class Lavado:
    def lava(self): 
        print("Lavando ")   
class Enjuagado:  
    def enjuaga(self): 
        print("Enjuagando ") 
class Secado:
    def seca(self): 
        print("Secando")   
class Lavadora: 
    #Patron de diseño Facade 
    #Solo segui un ejemplo que vi porque la vdd no le entiendo a este diseño
    def _init_(self): 
        self.Lavado = Lavado() 
        self.Enjuagado = Enjuagado() 
        self.Secado = Secado() 
    def inicio_lavado(self): 
        self.Lavado.lava() 
        self.Enjuagado.enjuaga() 
        self.Secado.seca() 
if __name__ == "_main_": 
 #Metodo Main (No entiendo bien porque se usa pero en las "explicaiones" lo usaban) 
    Lavadora = Lavadora() 
    Lavadora.inicio_lavado()