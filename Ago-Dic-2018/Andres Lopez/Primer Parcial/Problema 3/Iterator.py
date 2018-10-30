class Iterator:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self
    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

estaciones = ['89.9', '101.2', '102.3', '100.4']
myiterator = iter(estaciones)
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))