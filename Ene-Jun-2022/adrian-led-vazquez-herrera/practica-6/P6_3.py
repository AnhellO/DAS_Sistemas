#DAS Práctica 6.3

from abc import ABC, abstractmethod

class worker:
    
    def DailyRoutine(self) -> None:
        self.desc_job()
        self.getUp()
        self.eatBreakfast()
        self.goToWork()
        self.work()
        self.returnToHome()
        self.relax()
        self.sleep()
        
    def desc_job(self):
        print("I'm jobless")
        
    def getUp(self):
        print("I wake up")
    
    def eatBreakfast(self):
        print("I eat breakfast")
    
    def goToWork(self):
        print("I take the bus to work")
    
    def work(self):
        print("I don't have a job")
        
    def returnToHome(self):
        print("I take the bus home")
        
    def relax(self):
        print("I watch TV and drink a beer")
        
    def sleep(self):
        print("Zzz")
        
class FireFighter(worker):
    
    def desc_job(self):
        print("I'm a firefighter")
    
    def work(self):
        print("I stop fires in the city")
        
class Lumberjack(worker):
    
    def desc_job(self):
        print("I'm a Lumberjack")
    
    def work(self):
        print("I cut trees and make them wood planks")
        
class Postman(worker):
    
    def desc_job(self):
        print("I'm a postman")
    
    def work(self):
        print("I deliver mail")
        
class Manager(worker):
    
    def desc_job(self):
        print("I'm a manager")
    
    def work(self):
        print("I manage the time of my clients")
        
    def relax(self):
        print("I drink wine and listen to music")
        
Il_Hwan=FireFighter()
James=Lumberjack()
Cleveland=Postman()
Jenma=Manager()
people=[Il_Hwan, James, Cleveland, Jenma]

for person in people:
    person.DailyRoutine()
    print("")


        
    
        
    