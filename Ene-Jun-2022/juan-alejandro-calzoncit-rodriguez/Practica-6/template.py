import abc

# Clase abstracta
class Worker(metaclass=abc.ABCMeta):    
    
    # Template method
    def DailyToutine(self):
        self.getUp()
        self.eatBreakfast()
        self.goToWork()
        self.work()
        self.returnWork()
        self.relax()
        self.sleep()        
    
    def getUp(self):
        print('Despertando')
    
    def eatBreakfast(self):
        print('Comiendo el desayuno')

    def goToWork(self):
        print('Yendo al trabajo')

    @abc.abstractmethod
    def work(self):
        pass

    def returnWork(self):
        print('Regresando del trabajo')

    def relax(self):        
        print('Momento chill')

    def sleep(self):
        print('Mimir')

# Clase concreta
class FireFighter(Worker):
    def work(self):
        print('Soy un bombero')
        
# Clase concreta
class Lumberjack(Worker):
    def work(self):
        print('Soy un leñador')

# Clase concreta
class Postman(Worker):
    def work(self):
        print('Soy un cartero')

# Clase concreta
class Manager(Worker):
    def work(self):
        print('Soy un gerente')

    def relax(self):
        print('Viendo una serie')

def main():
    obj = FireFighter()
    obj.DailyToutine()
    print()
    obj = Lumberjack()
    obj.DailyToutine()
    print()
    obj = Postman()
    obj.DailyToutine()       
    print()
    obj = Manager()
    obj.DailyToutine()


if __name__ == '__main__':
    main()