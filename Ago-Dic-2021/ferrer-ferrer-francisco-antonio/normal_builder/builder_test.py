import unittest

from builder import *

class BuilderTest(unittest.TestCase):
    def test_create_car_without_builder(self):
        car = Car(5, 'standard', 10, True)

        self.assertEqual(5, car.seats)
        self.assertEqual('standard', car.engine)
        self.assertEqual(10, car.trip_computer)
        self.assertEqual(True, car.gps)
        
    def test_simple_car_creation_with_builder_but_without_director(self):
        builder = CarBuilder()
        builder.set_seats(5)
        builder.set_engine('standard')
        builder.set_trip_computer(10)
        builder.set_gps(True)
        car = builder.get_result()

        self.assertEqual(5, car.seats)
        self.assertEqual('standard', car.engine)
        self.assertEqual(10, car.trip_computer)
        self.assertEqual(True, car.gps)

    def test_car_builder_reset(self):
        builder = CarBuilder()
        builder.set_seats(5)
        builder.set_engine('standard')
        builder.set_trip_computer(10)
        builder.set_gps(True)
        builder.reset()
        car = builder.get_result()

        self.assertEqual(None, car.seats)
        self.assertEqual(None, car.engine)
        self.assertEqual(None, car.trip_computer)
        self.assertEqual(None, car.gps)
        
    def test_create_car_manual_without_builder(self):
        car_manual = Manual('descripción asientos', 'descripción transmisión', 'descripción de la computadora de viaje', 'descripción del GPS')
        
        self.assertEqual('descripción asientos', car_manual.desc_seats)
        self.assertEqual('descripción transmisión', car_manual.desc_engine)
        self.assertEqual('descripción de la computadora de viaje', car_manual.desc_trip_computer)
        self.assertEqual('descripción del GPS', car_manual.desc_gps)
        
    def test_create_car_manual_with_builder_but_without_director(self):
        builder = CarManualBuilder()
        builder.set_seats('descripción asientos')
        builder.set_engine('descripción transmisión')
        builder.set_trip_computer('descripción de la computadora de viaje')
        builder.set_gps('descripción del GPS')
        car_manual = builder.get_result()
        
        self.assertEqual('descripción asientos', car_manual.desc_seats)
        self.assertEqual('descripción transmisión', car_manual.desc_engine)
        self.assertEqual('descripción de la computadora de viaje', car_manual.desc_trip_computer)
        self.assertEqual('descripción del GPS', car_manual.desc_gps)

    def test_car_manual_builder_reset(self):
        builder = CarManualBuilder()
        builder.set_seats('descripción asientos')
        builder.set_engine('descripción transmisión')
        builder.set_trip_computer('descripción de la computadora de viaje')
        builder.set_gps('descripción del GPS')
        builder.reset()
        car_manual = builder.get_result()

        self.assertEqual(None, car_manual.desc_seats)
        self.assertEqual(None, car_manual.desc_engine)
        self.assertEqual(None, car_manual.desc_trip_computer)
        self.assertEqual(None, car_manual.desc_gps)
        
        

if __name__ == "__main__":
    unittest.main()