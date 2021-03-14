'''
La clase enguajado solo regresa un texto con un salto de línea
'''
class Lavado:
    @staticmethod
    def method():
        return "Lavando...\n"

'''
La clase enguajado solo regresa un texto con un salto de línea
'''
class Enjuagado:
    @staticmethod
    def method():
        return "Enjuagando...\n"

'''
La clase enguajado solo regresa un texto con un salto de línea
'''
class Centrifugado:
    @staticmethod
    def method():
        return "Centrifugando...\n"

'''
La clase enguajado solo regresa un texto con un salto de línea
'''
class Finalizado:
    @staticmethod
    def method():
        return "Finalizado!\n"


class LavadoraFacade:
    def __init__(self):
        self.lavado=Lavado()
        self.enguajado=Enjuagado()
        self.centrifugado=Centrifugado()
        self.fin=Finalizado()
    '''
    En el ciclo completo, lo que se hace es juntar las salidas de cada función
    en una variable y se regresa dicha variable
    '''
    def ciclo_completo(self):
        r=self.lavado.method()
        r+=self.enguajado.method()
        r+=self.centrifugado.method()
        r+=self.fin.method()
        print(r,end="")

        return r
        
    '''
    En el ciclo completo, lo que se hace es juntar las salidas de cada función
    en una variable y se regresa dicha variable
    '''
    def solo_centrifugado(self):
        r=self.centrifugado.method()
        r+=self.fin.method()
        print(r,end="")

        return r
'''
FACADE = LavadoraFacade()
RESULTADO = FACADE.ciclo_completo()
print(RESULTADO)
'''