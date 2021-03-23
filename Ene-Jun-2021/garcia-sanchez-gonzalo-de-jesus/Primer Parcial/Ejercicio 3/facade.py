#Goncho

# Parte  donde se hace el cilco completo del lavado
class ciclo_completo:
    def ciclo_completo(self):
        print("Lavando...\nEnjuagando...\nCentrifugando...\nFinalizado!")

#Parte donde solamente se hace el centrifugado
class solo_centrifugado:
    def solo_centrifugado(self):
        print("Centrifugando...\nFinalizado!")

# Fachada Lavadora
class LavadoraFacade(object):
    #Funciones donde elavoramos la parte compleja de facade
    def ciclo_completo(self):
        self.Lavando = ciclo_completo() 
        self.Lavando.ciclo_completo()

    def solo_centrifugado(self):
        self.Centrifugando = solo_centrifugado() 
        self.Centrifugando.solo_centrifugado()

# traemos a llamar a facade para cada uno de los casos anteriores mencionados
def main():
    lavadora = LavadoraFacade()
    lavadora.ciclo_completo()
    lavadora.solo_centrifugado()
    
if __name__ == "__main__":
    main()