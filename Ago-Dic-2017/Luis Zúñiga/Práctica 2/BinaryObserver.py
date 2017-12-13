from Observer import Observer

class BinaryObserver(Observer):
       
    def __init__(self,Subject):
        self.subject = Subject
        self.subject.attach(self.subject,self) 
        
    
    def update(self):
        print('String binario: ' + bin(self.subject.getState(self.subject)))
    
    
