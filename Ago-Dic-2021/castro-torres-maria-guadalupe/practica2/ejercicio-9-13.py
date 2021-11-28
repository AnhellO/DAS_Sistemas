from random import randint

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

#Haga un dado de 6 caras y muestre los resultados de 10 tiradas.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("\n10 rollos de un dado de 6 caras:")
print(results)

#Haga un dado de 10 caras y muestre los resultados de 10 tiradas.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rollos de un dado de 10 caras:")
print(results)

#Haga un dado de 20 caras y muestre los resultados de 10 tiradas.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rollos de un dado de 20 carase:")
print(results)
