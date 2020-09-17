from IIterator import IIterator

class RangeIterator(IIterator):
    
    """Iterador Concreto de clase mRange para el ejemplo de patron Iterator"""

    def __init__(self, rangeIterable):
        self.start = rangeIterable.start
        self.stop = rangeIterable.stop
        self.step = rangeIterable.step

    def getNext(self):
        if self.start < self.stop:
            x = self.start
            self.start += self.step
            return x
        else:
            raise Exception("AtEndOfIteratorException")

    def hasMore(self):
        return self.start < self.stop



############
    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     if self.start < self.stop:
    #         x = self.start
    #         self.start += 1 + self.step
    #         return x
    #     else:
    #         raise StopIteration
