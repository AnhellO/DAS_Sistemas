
# #Clases y objetos
# class Calculadora:
#     #Magic methods
#     def __init__(self,*lista_numeros) -> None:
#         self.lista_numeros = lista_numeros
        

#     #Funciones
#     def operacion(self,operacion: str):
#         s=0
#         if operacion in ['multriplicacion', 'division']:
#             s = 1
        
#         for i in self.lista_numeros:
#             if operacion == 'suma':
#                 s += i
#             elif operacion == 'resta':                
#                 s -= i
#             elif operacion == 'multriplicacion':                
#                 s *= i
#             elif operacion == 'division':
#                 s /= i
#         return s
        


#     def __str__(self) -> str:
#         return f'### Numeros ###\n: {self.lista_numeros}'


# mi_calculadora2 = Calculadora([5, 5,3,2])
# print(mi_calculadora2.operacion('suma'))
# print(mi_calculadora2.operacion('resta'))
# print(mi_calculadora2.operacion('multriplicacion'))
# print(mi_calculadora2.operacion('division'))
# print(mi_calculadora2)

# Clases y objetos
class Calculadora:
    # Magic methods
    def _init_(self, *lista_numeros) -> None:
        self.lista_numeros = lista_numeros

    # Funciones
    def operacion(self, operacion: str):
        operacionResultado = 0
        if operacion in ['multiplicacion', 'division']:
            operacionResultado = 1

        for i in self.lista_numeros:
            if operacion == 'suma':
                operacionResultado += i
            elif operacion == 'resta':
                operacionResultado -= i
            elif operacion == 'multiplicacion':
                operacion *= i
            elif operacion == 'division':
                operacion /= i
        return operacionResultado

    def suma(self) -> int:
        suma = 0
        for i in self.lista_numeros:
            suma += i
        return suma

    def resta(self):
        resta = 0
        for i in self.lista_numeros:
            resta -= i
        return resta

    def multiplicacion(self):
        mult = 1
        for i in self.lista_numeros:
            mult += i
        return mult

    def division(self):
        div = 1
        for i in self.lista_numeros:
            div += i
        return div

    def _str_(self) -> str:
        return 'Numeros: {}'.format(self.lista_numeros)


mi_calculadora_2 = Calculadora(5, 5, 2)
print(mi_calculadora_2.operacion('suma'))
print(mi_calculadora_2.operacion('resta'))
print(mi_calculadora_2.operacion('multiplicacion'))
print(mi_calculadora_2.operacion('division'))
print(mi_calculadora_2)

class Persona:
    def __init__(self,**kwargs) -> None:
        self.nombre = kwargs.get('nombre')
        self.edad = kwargs.get('edad')       
        self.peso = kwargs.get('peso') 

        
    def __str__(self) -> str:
        return f'### Persona ###\nNombre: {self.nombre} \nEdad: {self.edad} \nPeso: {self.peso}'
    
        

p = Persona(nombre ='fuñanito',edad=21,peso=70)        

print(p)
