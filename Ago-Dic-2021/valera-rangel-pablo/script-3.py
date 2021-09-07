class Calculadora:
    #pass #ESTO SIRVE PARA QUE NO TIRE ERROR ES COMO PA DECIRLE QUE NO HAGA NADA AUN#
    # Magic Methods
    def __init__(self, *lista_numeros) -> None:
        self.lista_numeros = lista_numeros

    def operacion(self, operacion: str):
        s = 1
        for i in self.lista_numeros:
            if operacion == 'suma':
                s += i
            elif operacion == 'resta':
                s -= i
            elif operacion == 'multiplicacion':
                s *= i
            elif operacion == 'division':
                s /= i
        return s

    def __str__(self):
        return f'### Numeros ###\nA: {self.lista_numeros}'


mi_calculadora_2 = Calculadora(5, 5, 2)
print(mi_calculadora_2.operacion('suma'))
print(mi_calculadora_2.operacion('resta'))
print(mi_calculadora_2.operacion('multiplicacion'))
print(mi_calculadora_2.operacion('division'))


class Persona:
    def __init__(self, **kwargs) -> None:
        self.nombre = kwargs.get('nombre')
        self.edad = kwargs.get('edad')
        self.peso = kwargs.get('peso',0.0)



    def __str__(self) -> str:
        return f'### Persona ###\nNombre: {self.nombre}\n Edad: {self.edad}\n Peso: {self.peso}'

#p = Persona('Fulanito', 15, 70.5)
p = Persona(nombre='Fulanito', edad=15, peso=70.5)
print(p)
