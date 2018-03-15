"""Suponga que se está construyendo una librería de clases para representar componentes de GUI.
Se ha decidido que en vez de que un programador defina la posición de los componentes GUI (Button, List, Dialog, etcétera)
sobre una ventana, se incluyan manejadores de disposición de componentes (layout manager), cada uno de los cuales distribuye
un conjunto dado de componentes gráficos de acuerdo a algún esquema de distribución: horizontalmente, verticalmente,
en varias filas, en forma de una matriz, etcétera. Debe ser posible cambiar en tiempo de ejecución la distribución elegida
inicialmente. Suponga que la clase Panel (Cliente) es la que representa a un contenedor de componentes gráficos, diseña una
solución para introducir en la librería los manejadores de componentes (layouts)

Implemente el patrón Strategy en python para dar solución a este ejemplo
Agregue los respectivos diagramas UML de clases que reflejen la solución"""

class Button:
    """A very basic button widget."""
    def __init__(self, submit_func):
        self.on_submit = submit_func   # Poner la funcion estrategia directamente


class List:
    """Listing the values"""
    def __init__(self, list_func):
        self.on_list = list_func


# Probamos cada boton
make = input("""Escribe la distribución
    Button, List
    """)
numbers = range(1, 10) # Lista del 1 al 9

if make == "button":
    s = input("""Qué botón quieres?
    El 1 suma la lista y el 2 enlista horizontalmente
    """)
    if s == "1":
        button1 = Button(sum)
        print ("Probando el primer boton:\n", button1.on_submit(numbers)) # muestra "45"
    elif s == "2":
        button2 = Button(lambda nums: " ".join(map(str, nums)))
        print ("Probando el segundo boton:\n", button2.on_submit(numbers)) # muestra "1 2 3 4 5 6 7 8 9"
elif make == "list":
    for n in numbers:
        print(n)
