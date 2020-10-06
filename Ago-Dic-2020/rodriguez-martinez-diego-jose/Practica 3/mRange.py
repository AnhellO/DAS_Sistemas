from IIterableCollection import IIterableCollection
from rangeIterator import RangeIterator

class mRange(IIterableCollection):

    """Implementacion de una clase iterable para probar Iterator Pattern Design\n
    start = 0, stop = 100, step = 0"""

    def __init__(self, **kwargs):
        self.start = kwargs.get("start", 0)
        self.stop = kwargs.get("stop", 100)
        self.step = kwargs.get("step",1)



############
    def create_iterator(self):
        return RangeIterator(self)


# #########
#     def __iter__(self):
#         return RangeIterator(self)