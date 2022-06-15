from abc import ABC, abstractmethod
class Worked(ABC):
    def DailyRoutine(self):
        pass
    def GetUp(self):
        return "se levanta "
    def GoToWork(self):
        return "va al trabajo"
    @abstractmethod
    def work(self):
        return "trabaja"
    def returnToHome(self):
        return "regresa a a casa"
    @abstractmethod
    def relax(self):
        return "se relaja"
    def sleep(self):
        return "se duerme"
class FireFighter(Worked):
    def work(self):
        return super().work()

class Lumberjack(Worked):
    def work(self):
        return super().work()

class Postman(Worked):
    def work(self):
        return super().work()

class Manager(Worked):
    def work(self):
        return super().work()
    def relax(self):
        return super().relax()


