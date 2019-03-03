import abc

class TextRenderer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def render(self):
        pass

class TextoNormal(TextRenderer):
    def __init__(self, text):
        self._text = text

    def render(self):
        return '¡' + self._text + '!'


class DecoradorT(TextRenderer, metaclass=abc.ABCMeta):

    def __init__(self, textod):
        self.textod = textod

    def render(self):
        return self.textod.render()


class Resaltado(TextRenderer):

    def __init__(self, textod):
        DecoradorT.__init__(self, textod)

    def render(self):
        return '<b>' + self.textod.render() + '</b>'

class Cursiva(TextRenderer):

    def __init__(self, textod):
        DecoradorT.__init__(self, textod)

    def render(self):
        return '<i>' + self.textod.render() + '</i>'

class Subrayado(TextRenderer):

    def __init__(self, textod):
        DecoradorT.__init__(self, textod)

    def render(self):
        return '<u>' + self.textod.render() + '</u>'


def main():
    renderer = TextoNormal('Texto Normal')
    print(renderer.render())

    renderer2 = Resaltado(TextoNormal('Texto Resaltado'))
    print(renderer2.render())

    renderer3 = Resaltado(Subrayado(TextoNormal('Texto Resaltado y Subrayado')))
    print(renderer3.render())

    renderer4 = Resaltado(Subrayado(Cursiva(TextoNormal('Aplicando todos los formatos'))))
    print(renderer4.render())

if __name__ == '__main__':
    main()