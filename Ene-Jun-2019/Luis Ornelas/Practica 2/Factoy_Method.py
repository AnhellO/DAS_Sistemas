from abc import ABC, abstractmethod

class Translator(object):
    def __init__(self, **argumentos):
        self.lenguaje = argumentos.get('lenguaje')
        self.word = argumentos.get('word')

    @abstractmethod
    def translate(self):
        pass

class SpanishTranslator(Translator):
    def __init__(self, **argumentos):
        Translator.__init__(self, **argumentos)
        self.words = {'dog':'perro', 'cat':'gato'}

    def translate(self):
        return 'Palabra {} Traducida al {} : {}'.format(self.word, self.lenguaje, self.words.get(self.word, str(self.word))).strip()

class GreekTranslator(Translator):
    def __init__(self, **argumentos):
        Translator.__init__(self, **argumentos)
        self.words = {'dog':'σκύλος', 'cat':'γάτα'}

    def translate(self):
        return 'Palabra {} Traducida al {} : {}'.format(self.word, self.lenguaje, self.words.get(self.word, str(self.word))).strip()

class TranslatorAleman(Translator):
    def __init__(self, **argumentos):
        Translator.__init__(self, **argumentos)
        self.words = {'dog':'hund', 'cat':'katze'}

    def translate(self):
        return 'Palabra {} Traducida al {} : {}'.format(self.word, self.lenguaje, self.words.get(self.word, str(self.word))).strip()

class TranslatorFactory(object):
    @staticmethod
    def traductor(**argumentos):
        if argumentos.get('lenguaje') == 'Español':
            return SpanishTranslator(**argumentos)
        elif argumentos.get('lenguaje') == 'Griego':
            return GreekTranslator(**argumentos)
        elif argumentos.get('lenguaje') == 'Aleman':
            return TranslatorAleman(**argumentos)

def main():
    traductore = TranslatorFactory.traductor(lenguaje = 'Español', word = 'dog')
    print(traductore.translate())
    traductore1 = TranslatorFactory.traductor(lenguaje='Español', word='cat')
    print(traductore1.translate())
    print('\n')
    traductorg = TranslatorFactory.traductor(lenguaje = 'Griego', word = 'dog')
    print(traductorg.translate())
    traductorg1 = TranslatorFactory.traductor(lenguaje='Griego', word='cat')
    print(traductorg1.translate())
    print('\n')
    traductora = TranslatorFactory.traductor(lenguaje = 'Aleman', word = 'dog')
    print(traductora.translate())
    traductora1 = TranslatorFactory.traductor(lenguaje='Aleman', word='cat')
    print(traductora1.translate())

if __name__ == '__main__':
    main()