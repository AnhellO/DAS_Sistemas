from BaseCharacter import BaseCharacter
from CharacterConcreteComponent import CharacterConcreteComponent
from ArmorConcreteDecorator import ArmorConcreteDecorator
from SwordConcreteDecorator import SwordConcreteDecorator
from RingConcreteDecorator import RingConcreteDecorator
from NecklaceConcreteDecorator import NecklaceConcreteDecorator

personajeBase = BaseCharacter()
equipoBase = personajeBase.equip()

personajeDecorado = CharacterConcreteComponent(name='Luxor')
equipoDecorado = personajeDecorado.equip()

personajeArmadura = ArmorConcreteDecorator(personajeDecorado)
equipoArmadura = personajeArmadura.equip()

personajeEspada = SwordConcreteDecorator(personajeDecorado.name)
equipoEspada = personajeEspada.equip()

personajeAnillo = RingConcreteDecorator(personajeDecorado.name)
equipoAnillo = personajeAnillo.equip()

personajeCollar = NecklaceConcreteDecorator(personajeDecorado.name)
equipoCollar = personajeCollar.equip()

personajeArmadura_Espada = 0

print(equipoBase)
print(equipoDecorado)
print(equipoArmadura)
print(equipoEspada)
print(equipoAnillo)
print(equipoCollar)
