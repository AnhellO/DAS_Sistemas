#clase ciclo completo
class CicloCompleto(object):
    def ciclo_completo(self):
        print("Lavando...\nEnjuagando...\nCentrifugando...\nFinalizado!")
# clase solo centrifugado        
class SoloCentrifugado(object):    
    def solo_centrifugado(self):
        print("Centrifugando...\nFinalizado!")

# clase facade lavadora
class LavadoraFacade(object):
    #creamos una funcion que contenga a la clase compleja
    def ciclo_completo(self):
         self._ciclo_completo = CicloCompleto()
         self._ciclo_completo.ciclo_completo()
         
    def solo_centrifugado(self):
        self._solo_centrifugado = SoloCentrifugado()
        self._solo_centrifugado.solo_centrifugado()
        
def main():
    # llamamos a la clase facade y corremos desde ella las demas clases     
    lavadora = LavadoraFacade()
    lavadora.ciclo_completo()
    lavadora.solo_centrifugado()
    
if __name__ == '__main__':
    main()             