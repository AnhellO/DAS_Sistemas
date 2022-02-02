########################
# Diccionarios
########################
mi_diccionario_vacio = {}
mi_diccionario_vacio['llave-1'] = 2
mi_diccionario_vacio['llave-2'] = 4
mi_diccionario_vacio['llave-3'] = 8

# Borra un elemento del diccionario
del mi_diccionario_vacio['llave-1']

# Verificamos que una llave existe en el diccionario
if 'llave-2' in mi_diccionario_vacio:
    print('llave-2 existe')

print(f"El valor de llave-2 es: {mi_diccionario_vacio['llave-2']}")

valor = mi_diccionario_vacio.get('llave-2')
print(f"El valor de llave-2 es: {valor}")

# La siguiente línea da un error
# print(f"El valor de llave-1 es: {mi_diccionario_vacio['llave-1']}")
valor = mi_diccionario_vacio.get('llave-1', 'No existe esta llave')
print(f"El valor de llave-1 es: {valor}")

print(mi_diccionario_vacio)

########################
# Tuplas
########################
ejemplo_lista = [1, 2, 3]
ejemplo_tupla = (1, 2, 3)

print(f"Lista: {ejemplo_lista} vs. Tupla {ejemplo_tupla}")

# No podemos alterar las tuplas que ya se definieron previamente
ejemplo_lista.append(4)
# La siguiente línea da error
# ejemplo_tupla.append(4)
print(f"Lista: {ejemplo_lista} vs. Tupla {ejemplo_tupla}")

ejemplo_lista[3] = 10
# La siguiente línea da error
# ejemplo_tupla[3] = 10
print(f"Lista: {ejemplo_lista} vs. Tupla {ejemplo_tupla}")

# Unpacking
x, y, z = ejemplo_tupla
print(f"x = {x}, y = {y}, z = {z}")

# La siguiente línea da error
# x, y = ejemplo_tupla
# La siguiente línea es la manera correcta de hacerlo utilizando la variable "underscore"
a, _, _ = ejemplo_tupla
print(f"a = {a}")

########################
# Ciclos
########################

# Ciclo 'for'
nueva_lista = [1, 2, 5, True, 'string', 10, False, 'otro string', ['otra', 'lista']]

# Ciclo 'for' por defacto en Python. Se comporta como 'foreach'
for item in nueva_lista:
    print(item)

# Simulando un ciclo 'for' clásico en otros lenguajes: for (i = 0; i < N; i++)
N = len(nueva_lista)
for i in range(N):
    print(f"Índice: {i} - Valor: {nueva_lista[i]}")

# Simulando un ciclo 'for' clásico en otros lenguajes: for (i = 1; i < 10; i += 2)
for i in range(1, 10, 2):
    print(i)

# Verificando el tipo de un objeto
tipo = type(nueva_lista)
print(f"El tipo de objeto es: {tipo}")

# Ciclos anidados
for item in nueva_lista:
    if type(item) == str or type(item) == list:
        for item_2 in item:
            print(item_2)

# Iterar un diccionario
nuevo_diccionario = {
    'k-1': 10,
    'k-2': True,
    'k-3': 'some string',
    'k-4': [2, 4, 6, 8, 10]
}

# Accediendo solamente a la llave
for key in nuevo_diccionario:
    print(f"La llave '{key}' tiene el valor: {nuevo_diccionario[key]}")

# Accediendo al par llave -> valor
# Llaves del diccionario
print(nuevo_diccionario.keys())
# Valores del diccionario
print(nuevo_diccionario.values())
# Pares llave->valor del diccionario
print(nuevo_diccionario.items())
for llave, valor in nuevo_diccionario.items():
    print(f"La llave '{llave}' tiene el valor: {valor}")

# Ciclo 'while'
otra_nueva_lista = [1, 2, 5, True, 'string', 10, False, 'otro string', ['otra', 'lista']]
iteracion = 1
while otra_nueva_lista != []:
    item = otra_nueva_lista.pop()
    print(f"El item que se sacó de la lista es: {item}\nLista en la iteración #{iteracion}: {otra_nueva_lista}")
    iteracion += 1
else:
    print("La lista está vacía")

########################
# Funciones
########################

def suma(a, b):
    return a + b

print(f"El valor de la función suma() es = {suma(5, 5)}")

########################
# Clases y Objetos
########################

class Calculadora:
    
    # TODO: Revisar variables de clase
    # variable_de_clase = 'x'
    
    # Constructor en Python
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._protected = 'protegido'
        self.__private = 'privado'
    
    def suma(self):
        return self.a + self.b

    def resta(self):
        return self.a - self.b

    def multiplicacion(self):
        return self.a * self.b

    def division(self):
        if self.a % self.b == 0:
            return self.a // self.b
        
        return self.a / self.b
    
    # Setter clásico pero ahora en Python
    def set_private(self, valor):
        self.__private = valor
    
    # Getter clásico pero ahora en Python
    def get_private(self):
        return self.__private
    
    # Esta es una función protegida
    def __private_function():
        pass

    def __str__(self):
        return f"Class Calculadora\n" \
            + f"Atributo A: {self.a}\n" \
            + f"Atributo B: {self.b}"

# Creamos una instancia (u objeto) de la clase 'Calculadora'
mi_calculadora = Calculadora(5, 6)
# Accedemos a los atributos de la instancia (u objeto)
print(f"Atributo 'a' = {mi_calculadora.a}")
print(f"Atributo 'b' = {mi_calculadora.b}")

# Mandamos llamar a las funciones de la instancia (u objeto)
print(f"Función 'suma()' = {mi_calculadora.suma()}")
print(f"Función 'resta()' = {mi_calculadora.resta()}")
print(f"Función 'multiplicacion()' = {mi_calculadora.multiplicacion()}")
print(f"Función 'division()' = {mi_calculadora.division()}")

# Tratando de acceder a atributos protegidos y privados
print(f"Atributo protegido = {mi_calculadora._protected}")
print(f"Atributo privado = {mi_calculadora.get_private()}")

# Accediendo la instancia directamente
print(mi_calculadora)

# TODO: Revisar variables de clase
# # Accediendo a un atributo o variable de clase
# print(f"Valor de la variable de clase: {mi_calculadora.variable_de_clase}")

# mi_calculadora_2 = Calculadora(100, 8)
# mi_calculadora_2.variable_de_clase = 'y'
# print(f"Valor de la variable de clase: {mi_calculadora.variable_de_clase}")
# # Accedemos a los atributos de la 2da instancia (u objeto)
# print(f"Atributo 'a' = {mi_calculadora_2.a}")
# print(f"Atributo 'b' = {mi_calculadora_2.b}")
# print(f"Valor de la variable de clase: {mi_calculadora.variable_de_clase}")
# print(f"Valor de la variable de clase: {mi_calculadora_2.variable_de_clase}")

# Herencia

class CalculadoraCientifica(Calculadora):
    # Constructor que manda llamar al constructor de la clase padre
    def __init__(self, a, b):
        super().__init__(a, b)

    def potencia(self):
        return self.a ** self.b

# Creamos una instancia (u objeto) de la clase 'Calculadora'
mi_calculadora_cientifica = CalculadoraCientifica(9, 10)
# Accedemos a los atributos de la instancia (u objeto)
print(f"Atributo 'a' = {mi_calculadora_cientifica.a}")
print(f"Atributo 'b' = {mi_calculadora_cientifica.b}")

# Mandamos llamar a las funciones de la instancia (u objeto)
print(f"Función 'suma()' = {mi_calculadora_cientifica.suma()}")
print(f"Función 'resta()' = {mi_calculadora_cientifica.resta()}")
print(f"Función 'multiplicacion()' = {mi_calculadora_cientifica.multiplicacion()}")
print(f"Función 'division()' = {mi_calculadora_cientifica.division()}")
print(f"Función 'potencia()' = {mi_calculadora_cientifica.potencia()}")