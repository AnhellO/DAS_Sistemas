import unittest
# from BaseCharacter import BaseCharacter
# from CharacterConcreteComponent import CharacterConcreteComponent
# from ArmorConcreteDecorator import ArmorConcreteDecorator
# from SwordConcreteDecorator import SwordConcreteDecorator
# from RingConcreteDecorator import RingConcreteDecorator
# from NecklaceConcreteDecorator import NecklaceConcreteDecorator
from Decoradornativo import *
from decorator import *


class DecoratorTest(unittest.TestCase):
    def test_character_without_equipment(self):
        character = CharacterConcreteComponent(name='Luxor')
        self.assertEqual(
            character.equip(),
            "Luxor equipment: Empty"
        )

    def test_character_with_armor(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character.name)
        self.assertEqual(
            armor.equip(),
            "Luxor equipment:\nArmor: Yes"
        )

    def test_character_with_sword(self):
        character = CharacterConcreteComponent(name='Luxor')
        sword = SwordConcreteDecorator(character.name)
        self.assertEqual(
            sword.equip(),
            "Luxor equipment:\nSword: Yes"
        )

    def test_character_with_armor_and_sword(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        sword = SwordConcreteDecorator(armor)
        self.assertEqual(
            sword.equip(),
            "Luxor equipment:\nArmor: Yes\nSword: Yes"
        )

    def test_character_with_ring(self):
        character = CharacterConcreteComponent(name='Luxor')
        ring = RingConcreteDecorator(character.name)
        self.assertEqual(
            ring.equip(),
            "Luxor equipment:\nRing: Yes"
        )

    def test_character_with_necklace(self):
        character = CharacterConcreteComponent(name='Luxor')
        necklace = NecklaceConcreteDecorator(character.name)
        self.assertEqual(
            necklace.equip(),
            "Luxor equipment:\nNeckLace: Yes"
        )


if __name__ == "__main__":
    unittest.main()
