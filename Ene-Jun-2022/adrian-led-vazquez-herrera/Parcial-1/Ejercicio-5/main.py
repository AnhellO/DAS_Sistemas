#DAS 8vo semestre
#Parcial 1, E: 5 ocp
#Main

from abc import ABC, abstractmethod 


#   Parent class ---------------------------
class Animal(ABC):
    
    @abstractmethod
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def get_nombre(self) -> str:
        return self.nombre
   
#   Sound classes ---------------------------
class sonido_animal(ABC):
    
    @abstractmethod
    def get_sonido(animal):
        pass
    
class sonido_roar(sonido_animal):
    
    def get_sonido():
        return('roar')
        
class sonido_squeak(sonido_animal):
    
    def get_sonido():
        return('squeak')
    
class sonido_none(sonido_animal):
    
    def get_sonido():
        return 'No sound'

#   Movement class ---------------------------
class movimiento_animal(ABC):
    
    @abstractmethod
    def get_movement(animal):
        pass
    
class movement_swim(movimiento_animal):
    
    def get_movement():
        return 'swim'


#   Species classes ---------------------------
class Lion(Animal):
    
    def __init__(self):
        self.nombre = "Lion"
        self.sound=self.set_sound()
    
    def set_sound(self):
        return (sonido_roar.get_sonido())
        
    def get_sound(self):
        return self.sound

class Mouse(Animal):
    
    def __init__(self):
        self.nombre = "Mouse"
        self.sound=self.set_sound()
    
    def set_sound(self):
        return (sonido_squeak.get_sonido())
        
    def get_sound(self):
        return self.sound
    
class Shark(Animal):
    
    def __init__(self):
        self.nombre= "Shark"
        self.sound=self.set_sound()
        self.movement=self.set_movement()
        
    def set_sound(self):
        return sonido_none.get_sonido()
    
    def get_sound(self):
        return self.sound
    
    def set_movement(self):
        return movement_swim.get_movement()
    
    def get_movement(self):
        return self.movement

class Tiger(Animal):
    
    def __init__(self):
        self.nombre = "Tiger"
        self.sound=self.set_sound()
    
    def set_sound(self):
        return (sonido_roar.get_sonido())
        
    def get_sound(self):
        return self.sound

#   Factory ---------------------------
    
class AnimalFactory:
    
    def create_animal(creature):
        species={
            "Lion": Lion,
            "Mouse": Mouse,
            "Shark": Shark,
            "Tiger": Tiger
            }
        return species[creature]()

#   Test methods ---------------------------

Ark= AnimalFactory

def test_Lion_sound():
    #Revisamos que el leon ruja
    animal=Ark.create_animal("Lion")
    assert animal.get_sound()=="roar"
    
def test_Mouse_sound():
    #Revisamos que el ratón chille
    animal=Ark.create_animal("Mouse")
    assert animal.get_sound()=="squeak"
    
def test_Shark_sound():
    #Revisamos que el tiburón no haga ruido
    animal=Ark.create_animal("Shark")
    assert animal.get_sound()=="No sound"

def test_Shark_movement():
    #Revisamos que el tiburón nade
    animal=Ark.create_animal("Shark")
    assert animal.get_movement()=="swim"

def test_Tiger_sound():
    #Revisamos que el tigre ruja
    animal=Ark.create_animal("Tiger")
    assert animal.get_sound()=="roar"

if __name__ == "__main__":
    
    test_Lion_sound()
    test_Mouse_sound()
    test_Shark_sound()
    test_Shark_movement()
    test_Tiger_sound()
    