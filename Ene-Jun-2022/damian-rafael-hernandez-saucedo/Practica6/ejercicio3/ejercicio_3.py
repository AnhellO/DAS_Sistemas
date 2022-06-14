from abc import ABC, abstractmethod

#AbstractClass
class Worker(ABC):
    def DailyRoutine(self) -> None:
        self.getUp()
        self.eatBreakfast()
        self.goToWork()
        self.work()
        self.returnToHome()
        self.relax()
        self.sleep()

    # method
    def getUp(self) -> None:
        return "worker getup"

    def eatBreakfast(self) -> None:
        return "worker eat breakfast"

    def goToWork(self) -> None:
        return "worker go to work"
    
    def returnToHome(self) -> None:
        return "worker return to home"
    
    def sleep(self) -> None:
        return "worker is sleep"

    
    #abstract method
    def relax(self) -> None:
        pass

    @abstractmethod
    def work(self) -> None:
        pass
    
    
# Concrete Class 
class FireFighter(Worker):
    
    def work(self) -> None:
        return "FireFighter is working"

class Lumberjack(Worker):
    
    def work(self) -> None:
        return "Lumberjack is working"

class Postman(Worker):
    
    def work(self) -> None:
        return "Postman is working"

class Manager(Worker):
    
    def work(self) -> None:
        return "Manager is working"
    
    def relax(self) -> None:
        return "Manager is relaxing"
        

#client
def client_code(worker_class: Worker) -> None:
    work = []
    work.append(worker_class.getUp())
    work.append(worker_class.eatBreakfast())
    work.append(worker_class.goToWork())
    work.append(worker_class.work())
    work.append(worker_class.returnToHome())
    work.append(worker_class.relax())
    work.append(worker_class.sleep())
    for i in work:
        if i != None:
            print(i)
    print("**************************")


if __name__ == "__main__":
    print("***** WORKER *****\n")
    client_code(FireFighter())
    print("")
    client_code(Lumberjack())
    print("")
    client_code(Postman())
    print("")
    client_code(Manager())
    


    
    