#mi fachada
class LavadoraFacade(object):
    #los metodos que se muetsran y que ejecutan la 
    #funcion del subsistema
    def solo_lavar(self):
        self._lavar = Lavar()
        self._lavar.subsistema_operation()
    
    def solo_enjuagar(self):
        self._enjuagar = Enjuagar()
        self._enjuagar.subsistema_operation()
    def solo_centrifugado(self):
        self._centrifugado = Centrifugado()
        self._centrifugado.subsistema_operation()
    
    def ciclo_completo(self):
        self._ciclo_completo = Completo()
        self._ciclo_completo.subsistema_operation()

#las clases de los subsistemas 
class Lavar(object):
    def subsistema_operation(self):
        print("Lavando...\nFinalizado!")

class Enjuagar(object):
    def subsistema_operation(self):
        print("Enjuagando...\nFinalizado!")

class Centrifugado(object):
    def subsistema_operation(self):
        print("Centrifugando...\nFinalizado!")

class Completo(object):
    def subsistema_operation(self):
        print ("Lavando...\nEnjuagando...\nCentrifugando...\nFinalizado!")

#if __name__ == "__main__":
    #LavadoraFacade().solo_enjuagar()
