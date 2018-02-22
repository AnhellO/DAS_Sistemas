import abc

class Context:

    def __init__(self, strategy):
        self._strategy = strategy

    def context(self):
        self._strategy.algorithm_interface()


class Strategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def algorithm_interface(self):
        pass


class ConcreteStrategyA(Strategy):

    def algorithm_interface(self):
        print('Estamos en el algoritmo A!')


class ConcreteStrategyB(Strategy):

    def algorithm_interface(self):
        print('Estamos en el algoritmo B!')


class ConcreteStrategyC(Strategy):

    def algorithm_interface(self):
        print('Estamos en el algoritmo C!, y en este si hacemos algo: {}'.format(2 ** 5))


def main():
    concrete_strategy_a = ConcreteStrategyA()
    context = Context(concrete_strategy_a)
    context.context()

    concrete_strategy_b = ConcreteStrategyB()
    context = Context(concrete_strategy_b)
    context.context()

    concrete_strategy_c = ConcreteStrategyC()
    context = Context(concrete_strategy_c)
    context.context()


if __name__ == "__main__":
    main()