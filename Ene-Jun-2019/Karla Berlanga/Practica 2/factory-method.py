from abc import ABC, abstractmethod

class Translator(object):
    """docstring for Translator."""
    def __init__(self, **arg):
        self.language = arg.get('language')
        self.word = arg.get('word')

    @abstractmethod
    def translate(self):
        pass



class SpanishTranslator(Translator):
    def __init__(self, **arg):
        Translator.__init__(self, **arg)
        self.words = {'dog':'perro', 'cat':'gato'}

    def translate(self):
        return """
        Palabra {} traducida al {} : {}
        """.format(self.word, self.language, self.words.get(self.word, str(self.word))).strip()

class GreekTranslator(Translator):
    def __init__(self, **arg):
        Translator.__init__(self, **arg)
        self.words = {'dog':'σκύλος', 'cat':'γάτα'}

    def translate(self):
        return """
        Palabra {} traducida al {} : {}
        """.format(self.word, self.language, self.words.get(self.word, str(self.word))).strip()

class TranslatorAleman(Translator):
    def __init__(self, **arg):
        Translator.__init__(self, **arg)
        self.words = {'dog':'hund', 'cat':'katze'}

    def translate(self):
        return """
        Palabra {} traducida al {} : {}
        """.format(self.word, self.language, self.words.get(self.word, str(self.word))).strip()

class TranslatorFactory(object):

    @staticmethod
    def translates(**arg):
        if arg.get('language') == 'español':
            return SpanishTranslator(**arg)
        elif arg.get('language') == 'griego':
            return GreekTranslator(**arg)
        elif arg.get('language') == 'aleman':
            return TranslatorAleman(**arg)


if __name__ == "__main__":
    translation = TranslatorFactory.translates(language = 'español', word = 'dog')
    print(translation.translate())

    translation2 = TranslatorFactory.translates(language = 'griego', word = 'dog')
    print(translation2.translate())

    translation3 = TranslatorFactory.translates(language = 'aleman', word = 'dog')
    print(translation3.translate())
