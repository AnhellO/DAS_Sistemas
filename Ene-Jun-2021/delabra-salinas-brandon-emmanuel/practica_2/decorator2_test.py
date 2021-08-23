import unittest

from decorator2 import *

class DecoratorTest(unittest.TestCase):
    def test_character_without_equipment(self):
        character = CharacterConcreteComponent(name='Luxor')
        self.assertEqual(
            character.equip(),
            "Luxor equipment: Empty"
        ) 

    def test_character_with_armor(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        self.assertEqual(
            armor.equip(),
            "Luxor equipment:\nArmor: Yes"
        )

    def test_character_with_sword(self):
        character = CharacterConcreteComponent(name='Luxor')
        sword = SwordConcreteDecorator(character)
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

    def test_character_with_armor_sword_and_Ring(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        sword = SwordConcreteDecorator(armor)
        ring = RingConcreteDecorator(sword)
        self.assertEqual(
            ring.equip(),
            "Luxor equipment:\nArmor: Yes\nSword: Yes\nRing: Yes"
        )

    def test_character_with_armor_sword_boots_and_Shield(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        sword = SwordConcreteDecorator(armor)
        ring = RingConcreteDecorator(sword)
        shield = ShieldConcreteDecorator(ring)
        self.assertEqual(
            shield.equip(),
            "Luxor equipment:\nArmor: Yes\nSword: Yes\nRing: Yes\nShield: Yes"
        )


if __name__ == "__main__":
    unittest.main() 
