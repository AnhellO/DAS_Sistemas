from random import randint

class die():
    
    def __init__(self, sides):

        self.sides = sides

    def roll_die(self):

        number = randint(1,self.sides)
        print("The number that rolled was: " + str(number))

#Testing different dies
six_sides_die = die(6)
x = 0
print("six sides die : \n")
while x != 10:
    six_sides_die.roll_die()
    x += 1

ten_sides_die = die(10)
x = 0
print("ten sides die : \n")
while x != 10:
    ten_sides_die.roll_die()
    x += 1

twenty_sides_die = die(20)
x = 0
print("twenty sides die : \n")
while x != 10:
    twenty_sides_die.roll_die()
    x += 1