
#Facade recurre a las clases que realizan las diferentes tareas, por lo que es necesario
#crear una clase por tarea

#mi primer clase es la de el ciclo de lavado completo
class cicloCompleto():
    def lavar(self):
        print ("Lavando...\nEnjuagando...\nCentrifugando...\nFinalizado!")

#mi segunda clase es el del ciclo cuando solo se pide centrifugado
class soloCentrifugado():
    def lavar(self):
        print("Centrifugando...\nFinalizado!")

#mi tercer clase es cuando solo se pide enjuagar
class soloEnjuagar():
    def lavar(self):
        print("Enjuagando...\nFinalizado!")


#por ultimo tenemos la clase que va a contener los diferentes ciclos y en base a esta se van a llamr
class LavadoraFacade():
    def __init__(self):
        self.ciclocom=cicloCompleto()
        self.soloCent=soloCentrifugado()
        self.soloEnj=soloEnjuagar()

    def ciclo_completo(self):
        self.ciclocom.lavar()

    def solo_centrifugado(self):
        self.soloCent.lavar()

    def soloEnjuagar(self):
        self.soloEnj.lavar()



if __name__=="__main__":
    lavar=LavadoraFacade()
    lavar.ciclo_completo()