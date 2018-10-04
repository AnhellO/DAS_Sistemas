class Estaciones():
    def __init__(self):
        self.estacion = [89.9,101.2,102.3,100.4]
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index == len(self.estacion):
            raise StopIteration
        return self.estacion[self.index]
        
r= Estaciones()
itr=iter(r)
print(next(itr))