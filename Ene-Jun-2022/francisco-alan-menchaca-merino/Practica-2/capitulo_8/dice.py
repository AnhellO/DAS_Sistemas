from random import randint


class Dice():
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)


results = []
dice = Dice(sides=6)
for girar_num in range(10):
    result = dice.roll_dice()
    results.append(result)

print("\nDado 6 caras: 10 tiros")
print(results)

results = []
dice = Dice(sides=10)
for girar_num in range(10):
    result = dice.roll_dice()
    results.append(result)

print("\nDado 10 caras: 10 tiros")
print(results)

results = []
dice = Dice(sides=20)
for girar_num in range(10):
    result = dice.roll_dice()
    results.append(result)

print("\nDado 20 caras: 10 tiros")
print(results)
