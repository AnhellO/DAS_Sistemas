"""Creamos diferentes clases para cada uno de los 
susbsistemas que integra nuestro problema, con diferentes
procesos en los que se encuentra la lavadora

"""
class FuncionDeLavado:
    def __init__(self):
        pass
    
    def LavadoOn(self):
        return "Proceso de Lavado Activado\n"

    def LavadoOff(self):
        return "Proceso de Lavado Desactivado\n"


class FuncionDeEnjuagado:
    def __init__(self):
        pass

    def EnjuagadoOn(self):
        return "Proceso de Enjuagado Acticado\n"

    def EanjuagadoOff(self):
        return "Proceso de Enjuagado Desactivado\n"

class FuncionDeCentrifugado:
    def __init__(self):
        pass

    def CentrifugadoOn(self):
        return "Proceso de Centrigado Acticado\n"

    def CentrigadoOff(self):
        return "Proceso de Centrigado Desactivado\n"

class FuncionDeTerminado:
    def __init__(self):
        pass

    def Terminado(self):
        return "Terminado\n"

"""
Creamos la clase facade, donde integraremos 
todo el sistema complejo anteriror, en uno más
simplificado y mucho más accesible para el usuario
"""
class LavadoraFacade:
    def __init__(self):
        self.lavado=FuncionDeLavado()
        self.enguajado=FuncionDeEnjuagado()
        self.centrifugado=FuncionDeCentrifugado()
        self.terminado=FuncionDeTerminado()

    def ciclo_completo(self):
        resultado=self.lavado.LavadoOn()
        resultado+=self.enguajado.EnjuagadoOn()
        resultado+=self.centrifugado.CentrifugadoOn()
        resultado+=self.terminado.Terminado()
        print(resultado,end="")

        return resultado

    def uso_centrifugado(self):
        resultado=self.centrifugado.CentrifugadoOn()
        resultado+=self.terminado.Terminado()
        print(resultado,end="")

        return resultado

if __name__== " main ":

    facade= LavadoraFacade()
    boton = True

    if boton == True:
        facade.ciclo_completo
        