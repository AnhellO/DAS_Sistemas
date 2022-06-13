from abc import ABC, abstractmethod
from concurrent.futures.thread import _worker

class Worker(ABC):
    def DailyRoutine(self):
        self.rutina = ""
        self.rutina += self.getUp()
        self.rutina += self.eatBreakfast()
        self.rutina += self.goToWork()
        self.rutina += self.work()
        self.rutina += self.returnToHome()
        self.rutina += self.relax()
        self.rutina += self.sleep()
        return self.rutina

    def getUp(self):

        return "Despierta, "

    def eatBreakfast(self):

        return "Almuerza, "
    def goToWork(self):
        return "Va a trabajar, "

    @abstractmethod
    def work(self):
        pass

    def returnToHome(self):
        return "Regresa a casa, "

    def relax(self):
        return "Se relaja, "

    def sleep(self):
        return "Se duerme."


class FireFighter(Worker):
    def work(self):
        return "Apaga incendio, "

class Lumberjack(Worker):
    def work(self):
        return"Corta leña, "

class Postman(Worker):
    def work(self):
        return "Entrega cartas, "

class Manager(Worker):
    def work(self):
        return "Papeleo, "

def client_code(worker: Worker) ->None:
    return worker.DailyRoutine()