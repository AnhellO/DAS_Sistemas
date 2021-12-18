# Super Hero
class Hero:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age
        self.poderes = [""]
        self.debilidad = [""]

    def __str__(self):
        return f'Mi Super Heroe es {self.gender} y tiene {self.age} años de edad con los siguientes poderes: {"".join(self.poderes[:-1])} y {self.poderes[-1]}, y su debilidad es {self.debilidad[-1]}'

# Concrete Builder (Builder)
class HeroBuilder():
    
    def __init__(self, gender, age):
        self.hero = Hero(gender, age)

    def addVolar(self):
        self.hero.poderes.append("volar")

    def addSfuerza(self):
        self.hero.poderes.append("super fuerza")

    def addVlaser(self):
        self.hero.poderes.append("vision laser")

    def addSvel(self):
        self.hero.poderes.append("super velocidad")

    def addProca(self):
        self.hero.poderes.append("piel roca")

    def addTelepatia(self):
        self.hero.poderes.append("telepatia")
    
    def addFuego(self):
        self.hero.debilidad.append("fuego")
    
    def addKripto(self):
        self.hero.debilidad.append("kriptonita")
    
    def addElectricidad(self):
        self.hero.debilidad.append("electricidad")

    def addHielo(self):
        self.hero.debilidad.append("hielo")
    
    def addBplata(self):
        self.hero.debilidad.append("balas de plata")

    def build(self):
        return self.hero