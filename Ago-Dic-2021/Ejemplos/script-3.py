# Retomando clase pasada 2021-09-06!

class Calculadora:
    # Magic Methods/Functions
    def __init__(self, *lista_numeros) -> None:
        self.lista_numeros = lista_numeros
        
    def operacion(self, operacion: str):
        s = 0
        if operacion in ['multiplicacion', 'division']:
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
        return f'### Números ###\n{self.lista_numeros}'


mi_calculadora = Calculadora(5, 5, 2)
print(mi_calculadora.operacion('suma'))
print(mi_calculadora.operacion('resta'))
print(mi_calculadora.operacion('multiplicacion'))
print(mi_calculadora.operacion('division'))
print(mi_calculadora)

# Keyword arguments y protected attributes

class Persona:
    def __init__(self, **kwargs) -> None:
        self.nombre = kwargs.get('nombre')
        self.edad = kwargs.get('edad')
        self.peso = kwargs.get('peso', 0.0)

    def __str__(self) -> str:
        return f'### Persona ###\nNombre: {self.nombre}\nEdad: {self.edad}\nPeso: {self.peso}'

# p = Persona('Fulanito', 15, 70.5)
p = Persona(nombre='Fulanito', edad=15)
print(p)