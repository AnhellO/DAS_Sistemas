############Con una función##########################
print('Valor de M:')
M = int(input())
print('Valor de N:')
N = int(input())

def potencia(M, N):

    resultado=1

    for i in range(N):
        resultado *= M

        return resultado
print(M**N)
print(pow(M, N))
print(potencia(M,N))

#########################Con un listas comprimidas########################
print('Valor de M:')
M = int(input())
print('Valor de N:')
N = int(input())

str = [i**N for i in range(0, N)]
print('Potencias, ' + str)


################## Logica encapsulada en la función######################
def __init__(self, Base, Exponente):

            self.Base=Base
        self.Exponente=Exponente

            def set_Base(self, Base):
            self.Base = Base

               def get_Base(self):
                return self.Base

                def set_Exponente(self, Exponente):
            self.Exponente = Exponente

        def get_Exponente(self):
            return self.Exponente

            def __str__ (self)


