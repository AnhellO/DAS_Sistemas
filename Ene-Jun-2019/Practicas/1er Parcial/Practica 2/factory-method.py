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
        self.words = {'dob':'hund', 'cat':'katze'}

    def translate(self, word):
        return self.words.get(word, str(word))