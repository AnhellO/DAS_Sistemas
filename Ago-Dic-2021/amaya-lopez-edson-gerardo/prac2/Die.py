from random import randint

class Die():
    def __init__(self, sides=6):        
        self.sides = sides

    def roll_die(self):        
        return randint(1, self.sides)


die_six = Die()

resultados = []

for tiro in range(10):
    result = die_six.roll_die()
    resultados.append(result)


print('Ejetcicio 9.13'.center(100,"="))

print("10 tiros con un rango 1-6")
print(resultados)


die_20 = Die(sides=20)

resultados = []

for tiro in range(10):
    result = die_20.roll_die()
    resultados.append(result)

print("\n10 tiros con un rango 1-20")
print(resultados)

print(''.center(100,"=")) 