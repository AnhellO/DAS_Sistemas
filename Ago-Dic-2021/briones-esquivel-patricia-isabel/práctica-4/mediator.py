from __future__ import annotations
from abc import ABC
from datetime import datetime

class Mediator(ABC):
    def notify(self, sender:object, event: str):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, alarm: Alarm, coffepot: CoffeePot, calendar: Calendar):
        self._alarm = alarm
        self._alarm.mediator = self
        self._coffeepot = coffepot
        self._coffeepot.mediator = self
        self._calendar = calendar
        self._calendar.mediator = self


    def notify(self, sender:object, event):
        cadena = ''
        #dia = self._calendar.check_day_of_week_manual('2021-10-12')
        dia = self._calendar.check_day_of_week()
        if event == "RevisarDia":
            cadena += 'El despertador quiere saber la fecha\n'
            cadena += 'Mediador recibe instrucción del despertador\n'
            cadena += f'El calendario regresa el día de la semana: {dia}'
            return cadena

        elif event == "AlarmaApagada":
            cadena += 'La alarma se apagó\n'
            cadena += 'Mediador sabe que se apagó la alarma\n'
            #Solo se sirve café entre semana 
            if dia == 'Lunes' or dia == 'Martes' or dia == 'Miércoles' or dia == 'Jueves':
                cadena += self._coffeepot.make_coffee()
                return cadena

            else:
                cadena = 'Hoy no hay café.'
                return cadena
            
        elif event == "TrashDay":
            if dia == 'Martes' or dia == 'Jueves':
                cadena += 'Mañana es día de basura\n'
                cadena += 'Cambiando alarma a 6:00 a.m.'
                return cadena
            else:
                cadena += 'Mañana no es día de basura\n'
            
        else:
            return 'No se reconoce la instrucción.'

class BaseComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator


class Alarm(BaseComponent):
    def check_calendar(self):
        return self.mediator.notify(self, "RevisarDia")

    def start_coffee(self):
        cadena = ''
        cadena += self.check_calendar()
        cadena += ("\n")
        cadena += self.mediator.notify(self, "AlarmaApagada")
        return cadena

    def reset(self):
        cadena = ''
        cadena += self.check_calendar()
        cadena += ("\n")
        cadena += self.mediator.notify(self, "TrashDay")
        return cadena

class CoffeePot(BaseComponent):
    def make_coffee(self):
        return 'Preparando café'

class Calendar(BaseComponent):
    def check_day_of_week_manual(self, date: str):
        dt_object = datetime.strptime(date, "%Y-%m-%d")
        dow = dt_object.isoweekday() 
        day_of_week = ''
        if dow == 1:
            day_of_week = 'Lunes'
        if dow == 2:
            day_of_week = 'Martes'
        if dow == 3:
            day_of_week = 'Miércoles'
        if dow == 4:
            day_of_week = 'Jueves'
        if dow == 5:
            day_of_week = 'Viernes'
        if dow == 6:
            day_of_week = 'Sábado'
        if dow == 7:
            day_of_week = 'Domingo'

        return day_of_week

    def check_day_of_week(self):    
        dow = datetime.today().isoweekday()
        day_of_week = ''
        if dow == 1:
            day_of_week = 'Lunes'
        if dow == 2:
            day_of_week = 'Martes'
        if dow == 3:
            day_of_week = 'Miércoles'
        if dow == 4:
            day_of_week = 'Jueves'
        if dow == 5:
            day_of_week = 'Viernes'
        if dow == 6:
            day_of_week = 'Sábado'
        if dow == 7:
            day_of_week = 'Domingo'
        return day_of_week


def main():
    alarm = Alarm()
    coffeepot = CoffeePot()
    calendar = Calendar()
    mediator = ConcreteMediator(alarm, coffeepot, calendar)
    print(alarm.reset())

if __name__ == "__main__":
    main()