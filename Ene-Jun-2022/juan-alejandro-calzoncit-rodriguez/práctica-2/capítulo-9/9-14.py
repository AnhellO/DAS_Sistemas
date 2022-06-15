import random
from tokenize import String

class Die():

    def __init__(self):
        self.sides = 6

    def set_sides(self, sides):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)


d1 = Die()

op = ''
for x in range(10):
    op += str(d1.roll_die()) + ','

print(op[:-1])


d2 = Die()
d2.set_sides(10)

op = ''
for x in range(10):
    op += str(d2.roll_die()) + ','

print(op[:-1])


d3 = Die()    
d3.set_sides(20)

op = ''
for x in range(10):
    op += str(d3.roll_die()) + ','

print(op[:-1])