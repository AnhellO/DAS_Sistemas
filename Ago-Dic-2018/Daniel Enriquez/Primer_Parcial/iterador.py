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
    def borrar(self):
        for i in range(0,4):
            if next(mi_iterador) == borra:
                dias.pop(next(mi_iterador))

dias = [1, 2, 3, 4, 5]
borra=2
mi_iterador = iter(dias)
print(next(mi_iterador))
borrar(mi_iterador)
print(next(mi_iterador))
borrar(mi_iterador)
print(next(mi_iterador))
borrar(mi_iterador)
print(next(mi_iterador))
borrar(mi_iterador)
print(next(mi_iterador))
borrar(mi_iterador)
print(next(mi_iterador))
borrar(mi_iterador)

print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
print(next(mi_iterador))
