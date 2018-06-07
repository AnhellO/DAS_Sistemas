from abc import ABC, abstractmethod

''' el patron decorados agrega un al principal por lo que en cada clase
se agrega un decoracion diferente mediante las llamadas ala clase text y decorados '''
class TextRenderer(ABC):

    def __init__(self, text):
        self._text = text

    @abstractmethod
    def render(self):
        pass


class Decorator(TextRenderer,ABC):

    def __init__(self, text):
        self._text = text

    @abstractmethod
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
        return '{}'.format(self._text)

def main():

    inicio = prueba("hello, pipol!")
    inicio.render()
    decorado = DecoratorResaltado(inicio)
    print(decorado.render())
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
