class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
mi_iterador = iter(dias)
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
