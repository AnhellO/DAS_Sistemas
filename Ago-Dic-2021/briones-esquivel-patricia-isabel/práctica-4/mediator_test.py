import unittest
from mediator import *

class TestMediator (unittest.TestCase):
    
    def test_revisar_el_dia_desde_alarma(self):
        alarm = Alarm()
        coffeepot = CoffeePot()
        calendar = Calendar()
        mediator = ConcreteMediator(alarm, coffeepot, calendar)
        self.assertEqual('El despertador quiere saber la fecha\nMediador recibe instrucción del despertador\nEl calendario regresa el día de la semana: Martes',alarm.check_calendar())

    def test_revisar_el_dia_actual_desde_calendario(self):
        calendar = Calendar()
        self.assertEqual('Martes',calendar.check_day_of_week())

    def test_revisar_un_dia_random_desde_calendario(self):
        calendar = Calendar()
        self.assertEqual('Miércoles',calendar.check_day_of_week_manual('2021-06-09'))

    def test_activar_cafetera_cuando_desactiva_alarma(self):
        alarm = Alarm()
        coffeepot = CoffeePot()
        calendar = Calendar()
        mediator = ConcreteMediator(alarm, coffeepot, calendar)
        self.assertEqual('El despertador quiere saber la fecha\nMediador recibe instrucción del despertador\nEl calendario regresa el día de la semana: Martes\nLa alarma se apagó\nMediador sabe que se apagó la alarma\nPreparando café',alarm.start_coffee())

    def test_reset_alarma_un_dia_antes_de_TrashDay(self):
        alarm = Alarm()
        coffeepot = CoffeePot()
        calendar = Calendar()
        mediator = ConcreteMediator(alarm, coffeepot, calendar)
        self.assertEqual('El despertador quiere saber la fecha\nMediador recibe instrucción del despertador\nEl calendario regresa el día de la semana: Martes\nMañana es día de basura\nCambiando alarma a 6:00 a.m.',alarm.reset())

if __name__ == '__main__':
    unittest.main()