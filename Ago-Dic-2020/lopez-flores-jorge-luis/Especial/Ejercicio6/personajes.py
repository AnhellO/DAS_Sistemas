import abc
import copy

class personaje():
    @abc.abstractmethod
    def clone(self):
        return copy.copy(self)

class Heroe(personaje):
    def __init__(self, nombre, imagen, altura, peso, inteligencia, habilidades):
        super().__init__()
        self.nombre = nombre
        self.imagen = imagen
        self.altura = altura
        self.peso = peso
        self.inteligencia = inteligencia
        self.habilidades = habilidades

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_imagen(self, imagen):
        self.imagen = imagen

    def get_imagen(self):
        return self.imagen

    def set_altura(self, altura):
        self.alt = altura

    def get_altura(self):
        return self.altura

    def set_peso(self, peso):
        self.peso = peso

    def get_peso(self):
        return self.peso

    def set_inteligencia(self, inteligencia):
        self.inteligencia = inteligencia

    def get_inteligencia(self):
        return self.inteligencia

    def set_habilidades(self, habilidades):
        self.habilidades = habilidades

    def get_habilidades(self):
        return self.habilidades

    def __str__(self):
        return f"Nombre: {self.nombre} \nImagen:{self.imagen} \nAltura:{self.altura} \nPeso:{self.peso} \nInteligencia:{self.inteligencia} \nHabilidad:{self.habilidades}"

    def clone(self):
        return self

class personaje_Cache:
    # Cache to store useful information
    cache = {}

if __name__ == '__main__':

    Heroino = Heroe("legolas", "https://www.google.com/search?q=legolas&client=ubuntu&hs=1rs&channel=fs&sxsrf=ALeKk02qwltSsyqmelrGe9woE4tuz13rYw:1612168332260&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjDooyGo8juAhVHSK0KHYwqB_sQ_AUoAXoECAsQAw&biw=1294&bih=667#imgrc=oVBL_0LLQKXpwM","170cm", "50kg", "sabe mucho", "tira flechas")
    Villano = Heroino.clone()
    print(Heroino)
    print("\n###############\n")

    Villano.set_nombre("Sauron")
    Villano.set_imagen("https://www.google.com/search?q=Sauron&client=ubuntu&hs=5dD&channel=fs&sxsrf=ALeKk027AtS4TN74nz7BHHrvB8SF4X7AsQ:1612168746036&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjxhLPLpMjuAhVRbKwKHajLCEoQ_AUoAXoECBQQAw&biw=1294&bih=667#imgrc=vEGtRz7ySdZnIM")
    Villano.set_altura("2 metros")
    Villano.set_peso("100 kilos")
    Villano.set_inteligencia("Bobo")
    Villano.set_habilidades("ninguna")
    print(Villano)
    Hechizero = Heroino.clone()
    print("\n###############\n")

    Hechizero.set_nombre("Gandalf")
    Hechizero.set_imagen("https://www.google.com/search?q=Sauron&client=ubuntu&hs=5dD&channel=fs&sxsrf=ALeKk027AtS4TN74nz7BHHrvB8SF4X7AsQ:1612168746036&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjxhLPLpMjuAhVRbKwKHajLCEoQ_AUoAXoECBQQAw&biw=1294&bih=667#imgrc=vEGtRz7ySdZnIM")
    Hechizero.set_altura("metro y medio")
    Hechizero.set_peso("45 kilos")
    Hechizero.set_inteligencia("Avispadon")
    Hechizero.set_habilidades("Tumba paredes")
    print(Hechizero)
    Mounstro = Heroino.clone()
    print("\n###############\n")

    Mounstro.set_nombre("Gollum")
    Mounstro.set_imagen("https://www.google.com/search?q=Gollum&client=ubuntu&hs=f0D&channel=fs&sxsrf=ALeKk0064inNNPNzvxVW0Nal9cj4pliR3Q:1612170146416&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjbyZPnqcjuAhXOmq0KHXEdBmQQ_AUoAXoECAgQAw&biw=1294&bih=667#imgrc=jMgwf6fhh6-d-M")
    Mounstro.set_altura("1 metro")
    Mounstro.set_peso("30 kilos")
    Mounstro.set_inteligencia("Malo")
    Mounstro.set_habilidades("Convencimiento")
    print(Mounstro)
