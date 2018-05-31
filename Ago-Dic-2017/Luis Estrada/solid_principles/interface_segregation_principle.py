from abc import ABCMeta, abstractmethod

class Animal:
  __metaclass__ = ABCMeta
  species = ''
  legs = 0

  @abstractmethod
  def speak(self):
    pass

class Egg:
  __metaclass__ = ABCMeta

  @abstractmethod
  def hatch(self):
    pass

class Viviparous:
  __metaclass__ = ABCMeta

  @abstractmethod
  def birth(self):
    pass

class Oviparous:
  __metaclass__ = ABCMeta

  @abstractmethod
  def lay(self):
    pass

class ChickenEgg(Egg):
  def hatch(self):
    return Chicken()

class Chicken(Animal, Oviparous):
  species = "Gallus gallus domesticus"
  legs = 2

  def speak(self):
    return "Cluck"

  def lay(self):
    return ChickenEgg()

def birthSays(parent):
  return parent.birth().speak()
