from abc import ABC, abstractmethod


class Worker(ABC):
    """
    The Worker Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive
    operations.

    Concrete subclasses should implement these operations, but leave the
    template method itself intact.
    """

    def dailyRoutine(self):
        """
        The template method defines the skeleton of an algorithm.
        """

        self.getUp()
        self.eatBreakfast()
        self.goToWork()
        self.work()
        self.returnToHome()
        self.relax()
        self.sleep()

    def getUp(self):
        print("- getUp: Waking up, and getting out of bead")

    def eatBreakfast(self):
        print("- eatBeakfast: Eating a delicious breakfast")

    def goToWork(self):
        print("- goToWork: Going to work")

    @abstractmethod
    def work(self):
        pass

    def returnToHome(self):
        print("- returnToHome: Coming home after work")

    def relax(self):
        pass

    def sleep(self):
        print("- sleep: Sleeping after a long day at work")


class FireFighter(Worker):
    def work(self):
        print("- work: Putting out house fires")


class Lumberjack(Worker):
    def work(self):
        print("- work: Chopping some wood")


class Postman(Worker):
    def work(self):
        print("- work: Sending letters from house to house")


class Manager(Worker):
    def work(self):
        print("- work: Categorizing company priorities")

    def relax(self):
        print("- relax: Taking a nap and relaxing for a few minutes")


if __name__ == '__main__':
    print("FireFighter daily Routine:")
    FireFighter().dailyRoutine()
    print("")

    print("Lumberjack daily Routine:")
    Lumberjack().dailyRoutine()
    print("")

    print("Postman daily Routine:")
    Postman().dailyRoutine()
    print("")

    print("Manager daily Routine:")
    Manager().dailyRoutine()
