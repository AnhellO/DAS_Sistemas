from abc import ABC, abstractmethod


class Worker(ABC):
    
    def dailyRoutine(self):
        self.getUp()
        self.eatBreakfast()
        self.goTowork()
        self.work()
        self.returnToHome()
        self.relax()
        self.sleep()
    
    def getUp(self):
        print("get up")

    def eatBreakfast(self):
        print("eat brackfast")

    
    def goTowork(self):
        print("go to work")

    @abstractmethod
    def work(self):
        print("work")

    def returnToHome(self):
        print("return to home")

    def relax(self):
        print("relax")

    def sleep(self):
        print("sleep")


class FireFigther(Worker):

    def work(self):
        print("fire figther work")

class LumberJack(Worker):

    def work(self):
        print("lumber jack work")

class Postman(Worker):

    def work(self):
        print("postman work")

class Manager(Worker):

    def work(self):
        print("manager work")

    def relax(self):
        print("manager relax")

if __name__ == "__main__":

    fire_fighter = FireFigther()
    fire_fighter.dailyRoutine()
    print()

    lumber_jack = LumberJack()
    lumber_jack.dailyRoutine()
    print()
    
    postman = Postman()
    postman.dailyRoutine()
    print()
    
    manager = Manager()
    manager.dailyRoutine()