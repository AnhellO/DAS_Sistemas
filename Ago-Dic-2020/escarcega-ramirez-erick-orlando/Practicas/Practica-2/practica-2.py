class Zoo(object):
     def __init__(self, name, animal, species, food, age):
        self.name = name
        self.animal = animal
        self.species = species
        self.food = food
        self.age = age
    
     def dance(self):
        print(self.name.title() + " is now dancing.")

     def eats(self):
        print(self.name.title() + " is a " + self.species.title() + " " + self.animal.title() + " and " + self.species.title() + "'s favorite food is " + self.food.title())
        
     def info(self):
        print(self.name.title() + " age is " + str(self.age) + " years old.")

class Gorilla(Zoo):
    def __init__(self, name, animal, species, food, age):
        Zoo.__init__(self, name, animal, species, food, age)


    def habilty(self):
        print(self.animal.title() + "s do not know how to fly")

    def power(self):
        print(self.name.title() + "'s power is over 9000! ")
        
    def magic(self):
        print(self.name.title() + " is a stand user")

class Bear(Zoo):
    def __init__(self, name, animal, species, food, age):
        Zoo.__init__(self, name, animal, species, food, age)

    def speed(self):
        print("A " + self.animal.title() + " stamina is better when they're running down a hill")
    
    def level(self):
        print(self.name.title() +"'s karate level is " + str(self.age))

    def hidden(self):
        print(self.name.title() + " usually hides his " + self.food.title() + " under his bed.")


my_gorilla = Gorilla('harambe', 'gorilla', 'silver back', 'lassagna', 14)
my_bear = Bear('Kuma', 'bear', 'Grizzly', 'Honey', 3)

my_gorilla.dance(), my_bear.dance()
my_gorilla.info(), my_bear.info()
my_gorilla.eats(), my_bear.eats()
my_gorilla.habilty(), my_gorilla.power(), my_gorilla.magic()
my_bear.speed(), my_bear.level(), my_bear.hidden()