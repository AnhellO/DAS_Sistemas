class Translator:
    def translate(self):
        pass

class SpanishTranslator(Translator):
    def __init__(self):
        self.words = {'dog':'perro', 'cat':'gato'}

    def translate(self, word):
        return self.words.get(word, str(word))

class GreekTranslator(Translator):
    def __init__(self):
        self.words = {'dog':'σκύλος', 'cat':'γάτα'}

    def translate(self, word):
        return self.words.get(word, str(word))

class TranslatorAleman(Translator):
    def __init__(self):
        self.words = {'dog':'hund', 'cat':'katze'}

    def translate(self, word):
        return self.words.get(word, str(word))


class TranslatorFactory(object):

    @staticmethod
    def create_translator(**arg):
        translators = {
            'spanish': SpanishTranslator,
            'greek': GreekTranslator,
            'german': TranslatorAleman
        }

        return translators[arg.get('language')]()

for word in ['dog', 'cat']:
    spanish = TranslatorFactory.create_translator(language='spanish')
    greek = TranslatorFactory.create_translator(language='greek')
    german = TranslatorFactory.create_translator(language='german')
    print("""
        Word {} in:\nSpanish -> {}\nGreek -> {}\nGerman -> {}'
    """.format(word, spanish.translate(word), greek.translate(word), german.translate(word)).strip())
