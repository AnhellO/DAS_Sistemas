import unittest

from srp import *


class DecoratorTest(unittest.TestCase):
    def test_principal(self):
        usertest=Usuario("panchito",15,"nueva rosa #333")
        self.assertEqual(usertest.serializar(),{'nombre': 'panchito', 'edad': 15, 'direccion': 'nueva rosa #333'})

    def test_json(self):
        usertest=Usuario("panchito",15,"nueva rosa #333")
        self.assertEqual(usertest.serializar("json"),'{"nombre": "panchito", "edad": 15, "direccion": "nueva rosa #333"}')

if __name__=="__main__":
    unittest.main()