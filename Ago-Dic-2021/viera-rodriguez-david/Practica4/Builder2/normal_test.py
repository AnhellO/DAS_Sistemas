import unittest

from normal import *

class BuilderTest(unittest.TestCase):
        
    def test_bike_builder(self):
        builder = Bike_Builder()
        builder.set_seats(1)
        builder.set_wheels(2)
        builder.set_pedals(2)
        builder.set_handle(1)
        bike = builder.get_result()

        self.assertEqual(1, bike.seats)
        self.assertEqual(2, bike.wheels)
        self.assertEqual(2, bike.pedals)
        self.assertEqual(1, bike.handle)

    def test_bike_builder_reset(self):
        builder = Bike_Builder()
        builder.set_seats(2)
        builder.set_wheels(2)
        builder.set_pedals(4)
        builder.set_handle(2)
        builder.reset()
        bike = builder.get_result()

        self.assertEqual(None, bike.seats)
        self.assertEqual(None, bike.wheels)
        self.assertEqual(None, bike.pedals)
        self.assertEqual(None, bike.handle)
        
    def test_electric_bike_builder(self):
        builder = Electric_Bike_Builder()
        builder.set_seats(1)
        builder.set_wheels(2)
        builder.set_pedals(2)
        builder.set_handle(1)
        builder.set_battery(True)
        builder.set_motor(True)
        electric_bike = builder.get_result()

        self.assertEqual(1, electric_bike.e_seats)
        self.assertEqual(2, electric_bike.e_wheels)
        self.assertEqual(2, electric_bike.e_pedals)
        self.assertEqual(1, electric_bike.e_handle)
        self.assertEqual(True, electric_bike.battery)
        self.assertEqual(True, electric_bike.motor)

    def test_electric_bike_builder_reset(self):
        builder = Electric_Bike_Builder()
        builder.set_seats(2)
        builder.set_wheels(3)
        builder.set_pedals(4)
        builder.set_handle(1)
        builder.set_battery(False)
        builder.set_motor(True)
        builder.reset()
        electric_bike = builder.get_result()

        self.assertEqual(None, electric_bike.e_seats)
        self.assertEqual(None, electric_bike.e_wheels)
        self.assertEqual(None, electric_bike.e_pedals)
        self.assertEqual(None, electric_bike.e_handle)
        self.assertEqual(None, electric_bike.battery)
        self.assertEqual(None, electric_bike.motor)

if __name__ == "__main__":
    unittest.main()