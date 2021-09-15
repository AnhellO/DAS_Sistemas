from random import randint

class Die():
    def __init__(self, sides = 6) -> None:
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


die1 = Die()
die2 = Die()
die2.sides = 10
die3 = Die()
die3.sides = 20

for i in range(1,10):
    print(die1.roll_die())
    
for i in range(1,10):
    print(die2.roll_die())
    
for i in range(1,10):
    print(die3.roll_die())
