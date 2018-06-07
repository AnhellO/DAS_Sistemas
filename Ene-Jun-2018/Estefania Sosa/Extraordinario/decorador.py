import abc

''' el patron decorados agrega un al principal por lo que en cada clase 
se agrega un decoracion diferente mediante las llamadas ala clase text y decorados '''
class TextRenderer(metaclass=abc.ABCMeta):

    def __init__(self, text):
        self._text = text

    @abc.abstractmethod
    def render(self):
        pass


class Decorator(TextRenderer,metaclass=abc.ABCMeta):

    def __init__(self, text):
        self._text = text

    @abc.abstractmethod
    def render(self):
        return self._text

class DecoratorResaltado(Decorator):

    def render(self):
        return '<b>¡{}!</b>'.format(self._text)


class DecoratorCursiva(Decorator):


    def render(self):
        return '<b><u>{}</u></b>'.format(self._text)


class DecoratorSubrayado(Decorator):


    def render(self):
        return '<b><u><i>{}</i></u></b>'.format(self._text)

class prueba(TextRenderer):
    
    def __init__(self, text):
        self._text = text


    def render(self):
        pass

def main():

    inicio = prueba('III')
    decorado = DecoratorResaltado(inicio)
    decorado2 = DecoratorCursiva(decorado)
    decorado3 = DecoratorSubrayado(decorado2)
    decorado3.render()
    print(decorado.render())
    print(decorado2.render())
    print(decorado3.render())

    #cursiva = DecoratorCursiva()
    #concrete_decorator_b.operation()


if __name__ == "__main__":
    main()
