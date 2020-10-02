import unittest

from factory_method_second_refactoring_sprint import *

class FacthoryMethodTest(unittest.TestCase):
    def test_generic_bicycle_factory(self):
        bicycle = Bicycle()
        self.assertEqual(bicycle.get_type(), 'Bicicleta')
        self.assertEqual(bicycle.llantas.part_type(), 'llantas genéricas')
        self.assertEqual(bicycle.manillar.part_type(), 'manillar genérico')
        self.assertEqual(bicycle.parts(), ['llantas genéricas', 'manillar genérico'])

    def test_mountain_bicycle_factory(self):
        bicycle = Bicycle(MountainFactory)
        self.assertEqual(bicycle.get_type(), 'Bicicleta')
        self.assertEqual(bicycle.llantas.part_type(), 'llantas 4x4')
        self.assertEqual(bicycle.manillar.part_type(), 'manillar rígido')
        self.assertEqual(bicycle.parts(), ['llantas 4x4', 'manillar rígido'])

    def test_road_bicycle_factory(self):
        bicycle = Bicycle(RoadFactory)
        self.assertEqual(bicycle.get_type(), 'Bicicleta')
        self.assertEqual(bicycle.llantas.part_type(), 'llantas para carretera')
        self.assertEqual(bicycle.manillar.part_type(), 'manillar deportivo')
        self.assertEqual(bicycle.parts(), ['llantas para carretera', 'manillar deportivo'])

if __name__ == "__main__":
    unittest.main()
