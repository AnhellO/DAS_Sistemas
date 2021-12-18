from random import randint

class Die():
    def __init__(self, sides = 6) -> None:
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)

# dado de 6 lados
d6 = Die()

results = []
for i in range(10):
    result = d6.roll_dice()
    results.append(result)
print(results)

# dado de 10 lados

d10 = Die(sides = 10)

results = []
for i in range(10):
    result = d10.roll_dice()
    results.append(result)
print(results)

# dado de 20 lados

d20 = Die(sides = 20)

results = []
for i in range(10):
    result = d20.roll_dice()
    results.append(result)
print(results)

