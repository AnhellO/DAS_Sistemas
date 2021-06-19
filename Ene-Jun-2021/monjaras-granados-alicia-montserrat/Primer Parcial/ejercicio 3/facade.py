class Lavadora_Ciclo_Completo:

    def ciclo_completo(self):
        print("Lavando...\nEnjuagando...\nCentrifugando...\nFinalizado!") 

   
class Lavadora_Solo_Centrifugado:      

    def solo_centrifugado(self):
        print(  "Centrifugando...\nFinalizado!" ) 

# Fachada 
class LavadoraFacade:
    def __init__(self):
        self.lav_ciclo_completo = Lavadora_Ciclo_Completo() 
        self.lav_solo_centrifugado = Lavadora_Solo_Centrifugado() 
   
    def ciclo_completo(self):
        self.lav_ciclo_completo.ciclo_completo()
    
    def solo_centrifugado(self):
        self.lav_solo_centrifugado.solo_centrifugado()  



# Cliente
  
def main():
    facade = LavadoraFacade()
    facade.ciclo_completo()
    facade.solo_centrifugado()


if __name__ == "__main__":
    main()