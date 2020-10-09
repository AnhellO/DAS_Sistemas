import unittest

from builder import *

class BuilderTest(unittest.TestCase):
    def test_pizza_sencilla_18_pulgadas(self):
        builder = PizzaBuilder(18)
        pizza = builder.build()

        self.assertIsInstance(pizza, Pizza)
        self.assertEqual(
            'Mi pizza es de 18" con los siguientes ingredientes: salsa de tomate y queso',
            str(pizza)
        )

    def test_pizza_doble_queso_pepperoni_14_pulgadas(self):
        builder = PizzaBuilder(14)
        builder.addCheese()
        builder.addPepperoni()
        pizza = builder.build()

        self.assertIsInstance(pizza, Pizza)
        self.assertEqual(
            'Mi pizza es de 14" con los siguientes ingredientes: salsa de tomate, queso, doble queso y pepperoni',
            str(pizza)
        )

    def test_pizza_con_todo_20_pulgadas(self):
        builder = PizzaBuilder(20)
        builder.addCheese()
        builder.addPepperoni()
        builder.addSalami()
        builder.addPimientos()
        builder.addCebolla()
        builder.addChampiñones()
        pizza = builder.build()

        self.assertIsInstance(pizza, Pizza)
        self.assertEqual(
            'Mi pizza es de 20" con los siguientes ingredientes: salsa de tomate, queso, doble queso, pepperoni, salami, pimientos, cebolla y champiñones',
            str(pizza)
        )
    

if __name__ == "__main__":
    unittest.main()
