from abc import ABCMeta, abstractclassmethod

class IHandler(metaclass=ABCMeta):
    @abstractclassmethod
    def set_sucesor(sucesor):
        pass

    @abstractclassmethod
    def handle(cargo):
        pass

class Compensacion50(IHandler):
    def __init__(self):
        self.sucesor = None
    def set_sucesor(self, sucesor):
        self.sucesor = sucesor
    def handle(self, cargo):
        if cargo >=50:
            data = cargo // 50
            recor = cargo % 50
            print(f"Compensación {data} $50")
            if recor != 0:
                self.sucesor.handle(recor)
        else:
            self.sucesor.handle(cargo)

class Compensacion20(IHandler):
    def __init__(self):
        self.sucesor = None
    def set_sucesor(self, sucesor):
        self.sucesor = sucesor
    def handle(self, cargo):
        if cargo >=20:
            data = cargo // 20
            recor = cargo % 20
            print(f"Compensación {data} $20")
            if recor != 0:
                self.sucesor.handle(recor)
        else:
            self.sucesor.handle(cargo)

class Compensacion10(IHandler):
    def __init__(self):
        self.sucesor = None
    def set_sucesor(self, sucesor):
        self.sucesor = sucesor
    def handle(self, cargo):
        if cargo >=10:
            data = cargo // 10
            recor = cargo % 10
            print(f"Compensación {data} $10")
            if recor != 0:
                self.sucesor.handle(recor)
        else:
            self.sucesor.handle(cargo)

class ATMChain:
    def __init__(self):
        self.chainof1 = Compensacion50()
        self.chainof2 = Compensacion20()
        self.chainof3 = Compensacion10()

        self.chainof1.set_sucesor(self.chainof2)
        self.chainof2.set_sucesor(self.chainof3)

if __name__ == "__main__":
    ATM = ATMChain()
    ATM.chainof1.handle(300)
