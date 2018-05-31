from Observer import Observer

class HexObserver(Observer):

    def __init__(self,Subject):
        self.subject = Subject
        self.subject.attach(self.subject,self) 
        
    
    def update(self):
        print('String Hexadecimal: ' + hex(self.subject.getState(self.subject)))
    
    
