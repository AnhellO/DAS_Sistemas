import abc

class Context:

    def __init__(self, strategy):
        self._strategy = strategy

    def context(self):
        self._strategy.sort()

    def set_strategy(self, strategy):
        self._strategy = strategy


class Strategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def sort(self):
        pass


class QuickSort(Strategy):

    def sort(self):
        print('Ya ordene con QuickSort!')


class MergeSort(Strategy):

    def sort(self):
        print('Ya ordene con MergeSort!')


class BubbleSort(Strategy):

    def sort(self):
        print('Ya ordene con BubbleSort')


def main():
    # Aquí estoy ordenando 1000000 elementos
    quick_sort = QuickSort()
    context = Context(quick_sort)
    context.context()

    # Aquí estoy ordenando 100000 elementos
    merge_sort = MergeSort()
    context.set_strategy(merge_sort)
    context.context()

    # Aquí estoy ordenando 100 elementos
    bubble_sort = BubbleSort()
    context.set_strategy(bubble_sort)
    context.context()


if __name__ == "__main__":
    main()