"""9-14. Dice:

The module random contains functions that generate random num-
bers in a variety of ways . The function randint() returns an integer in the
range you provide . The following code returns a number between 1 and 6:

    from random import randint
    x = randint(1, 6)
    
Make a class Die with one attribute called sides, which has a default
value of 6 . Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has . Make a 6-sided die and roll
it 10 times .
Make a 10-sided die and a 20-sided die. Roll each die 10 times."""

from random import randint

class Dado():
    def __init__(self, lados=6):
        self.lados = lados

    def TirarDado(self):
        return randint(1, self.lados)

d6 = Dado()

resultados = []
for roll_num in range(10):
    resultado = d6.TirarDado()
    resultados.append(resultado)
print(f"\n10 tiradas con un dado de {6} lados:")
print(resultados)

d10 = Dado(lados=10)

resultados = []
for roll_num in range(10):
    resultado = d10.TirarDado()
    resultados.append(resultado)
print(f"\n10 tiradas con un dado de {10} lados:")
print(resultados)

d20 = Dado(lados=20)

resultados = []
for roll_num in range(10):
    resultado = d20.TirarDado()
    resultados.append(resultado)
print(f"\n10 tiradas con un dado de {20} lados:")
print(resultados)