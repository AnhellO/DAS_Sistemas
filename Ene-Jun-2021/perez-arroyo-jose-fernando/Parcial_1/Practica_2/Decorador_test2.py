import unittest

from Decoradores2 import *

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
    def test_character_with_armor_and_sword1(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        sword = SwordConcreteDecorator(armor)
        key = KeyConcreteDecorator(sword)
        self.assertEqual(
            key.equip(),
            "Luxor equipment:\nArmor: Yes\nSword: Yes\nKey: Yes"
        )
    def test_character_with_armor_and_sword2(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        sword = SwordConcreteDecorator(armor)
        key = KeyConcreteDecorator(sword)
        shield = ShieldConcreteDecorator(key)
        self.assertEqual(
            shield.equip(),
            "Luxor equipment:\nArmor: Yes\nSword: Yes\nKey: Yes\nShield: Yes"
        )

if __name__ == "__main__":
    unittest.main()