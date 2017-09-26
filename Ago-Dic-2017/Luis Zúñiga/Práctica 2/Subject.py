class Subject():
    observers = []
    estado = 0
    def __init__(self):
        self.observers = []
        self.estado = 0
        
    def getState(self):     
        return self.estado
    
    def setState(self,estado):
        self.estado = estado
        self.notifyAllObservers(self)
        
    def attach(self,observer):
        self.observers.append(observer)
            
    def notifyAllObservers(self):
        for i in self.observers:
            i.update()
