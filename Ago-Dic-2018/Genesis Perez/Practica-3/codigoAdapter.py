# Example #1: Language Translator

class EnglishSpeaker:
        def responseToGreeting(self):
                return "Hello to you too!"
        def responseToFarewell(self):
                return "Goodbye my friend."

# Adapter Class
class Translator:
        '''Accespts an english speaker, translates his responses to French.'''
        _englishSpeaker = None
        _englishToFrenchPhrases = {
                "Hello to you too!": "Bonjour à vous aussi",
                "Goodbye my friend.": "Au revoir mon ami"
                }

        def __init__(self, englishSpeaker):
                self._englishSpeaker = englishSpeaker

# Client: Incompatible interface # 2
class FrenchSpeaker:
        '''Accepts an English-To-French Speaker as argument.'''
        _englishToFrenchTranslator = None

        def __init__(self, englishToFrenchTranslator):
                self._englishToFrenchTranslator = englishToFrenchTranslator

        def exchangeGreetings(self):
                print("Salut!")
                print( self._englishToFrenchTranslator._englishToFrenchPhrases[  self._englishToFrenchTranslator._englishSpeaker.responseToGreeting()  ] )

        def exchangeFarewell(self):
                print("Au revoir!")
                print( self._englishToFrenchTranslator._englishToFrenchPhrases[  self._englishToFrenchTranslator._englishSpeaker.responseToFarewell()  ] )

# Create an English Speaking person
englishSpeaker = EnglishSpeaker()

# Create a translator with popular english phrases
englishToFrenchTranslator = Translator(englishSpeaker)

# The French Speaking Person can now get responses in French
frenchSpeaker = FrenchSpeaker(englishToFrenchTranslator)

# Two-way conversation in French
frenchSpeaker.exchangeGreetings()
frenchSpeaker.exchangeFarewell()

# OUTPUT
#Salut!
#Bonjour à vous aussi
#Au revoir!
#Au revoir mon ami
