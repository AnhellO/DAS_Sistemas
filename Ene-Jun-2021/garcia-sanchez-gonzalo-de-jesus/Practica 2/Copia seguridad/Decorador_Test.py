# Decoradores import CharacterConcreteComponent,ShieldConcreteDecorator,RingConcreteDecorator, ArmorConcreteDecorator, SwordConcreteDecorator
# Decorador_Nat

import unittest
from Decoradores import CharacterConcreteComponent,ShieldConcreteDecorator,RingConcreteDecorator, ArmorConcreteDecorator, SwordConcreteDecorator
class DecoratorTest(unittest.TestCase):
    def test_character_without_equipment(self):
        character = CharacterConcreteComponent(name='Luxor')
        self.assertEqual(
            character.equip(),
            "Luxor equipment:" #Falta  Empty
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

    def test_character_with_Ring(self):
        character = CharacterConcreteComponent(name='Luxor')
        Ring = RingConcreteDecorator(character)
        self.assertEqual(
            Ring.equip(),
            "Luxor equipment:\nRing: Yes"
        )
    def test_character_with_shield(self):
        character = CharacterConcreteComponent(name='Luxor')
        shield = ShieldConcreteDecorator(character)
        self.assertEqual(
            shield.equip(),
            "Luxor equipment:\nShield: Yes"
        )
    def test_character_with_Ring_And_Shield(self):
        character = CharacterConcreteComponent(name='Luxor')
        Ring = RingConcreteDecorator(character)
        shield = ShieldConcreteDecorator(Ring)
        self.assertEqual(
            shield.equip(),
            "Luxor equipment: \nRing: Yes\nShield: Yes"
        )

    def test_character_with_Ring_And_Shield(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        sword = SwordConcreteDecorator(armor)
        Ring = RingConcreteDecorator(sword)
        shield = ShieldConcreteDecorator(Ring)
        self.assertEqual(
            shield.equip(),
            "Luxor equipment:\nArmor: Yes\nSword: Yes\nRing: Yes\nShield: Yes"
        )
if __name__ == "__main__":
    unittest.main()