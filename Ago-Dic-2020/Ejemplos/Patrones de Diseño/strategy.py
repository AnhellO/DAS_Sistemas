import abc

# Interfaz estrategia
class SortStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sort(self):
        pass

# Estrategia concreta 1
class BubbleSortConcreteStrategy(SortStrategy):
    def sort(self):
        return 'Ordenando con bubble sort!'

# Estrategia concreta 2
class MergeSortConcreteStrategy(SortStrategy):
    def sort(self):
        return 'Ordenando con merge sort!'

# Estrategia concreta 3
class QuickSortConcreteStrategy(SortStrategy):
    def sort(self):
        return 'Ordenando con quick sort!'

# Contexto
class SortContext(object):
    def __init__(self, items: list, strategy: SortStrategy = None):
        self._items = items
        self._strategy = strategy

    def sort_context(self):
        # Da la opción de que el cliente elija su propia estrategia
        if self._strategy != None:
            return self._strategy.sort()

        # En caso contrario, deja que el contexto determine la estrategia
        if len(self._items) <= 100:
            return BubbleSortConcreteStrategy().sort()

        if len(self._items) <= 10000:
            return MergeSortConcreteStrategy().sort()

        return QuickSortConcreteStrategy().sort()

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def __str__(self):
        return f'Lista: {self._items}\nEstrategia: {self._strategy}'

# Cliente
def main():
    items = [i for i in range(0, 1000)]
    context = SortContext(items)
    # Utilizando la estrategia por default
    print(context.sort_context())

    # Seleccionando una estrategia concreta
    quick_sorter = QuickSortConcreteStrategy()
    context.set_strategy(quick_sorter)
    print(context.sort_context())
    
    # Seleccionando otra estrategia concreta
    bubble_sorter = BubbleSortConcreteStrategy()
    context.set_strategy(bubble_sorter)
    print(context.sort_context())
    

if __name__ == '__main__':
    main()