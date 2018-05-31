from Subject import Subject

class Observer():
    
    def __init__(self,Subject):                
        self.subject = Subject
        self.subject.attach(self.subject,self)    
    
    def update(self):
        print('Número decimal original: ' + str(self.subject.getState(self.subject)))
