# Implementa la funcionalidad necesaria utilizando el patrón de diseño
# Factory Method para que sea posible traducir una o varias palabras en
# base al idioma requerido.
# Las palabras y el idioma a traducir tendrán que ingresarse a través de
# la terminal/consola
# Ejemplo:
#   dog griego # Entrada
#   Palabra "dog" traducida al griego: σκύλος # Salida

class Translator:
    def translate(self):
        pass

class SpanishTranslator(Translator):
    def __init__(self):  # constructor
        self.words = {'dog':'perro', 'cat':'gato'}

    def translate(self, word):  # traducir una palabra específica
        return self.words.get(word, str(word))

class GreekTranslator(Translator):
    def __init__(self):  # constructor
        self.words = {'dog':'σκύλος', 'cat':'γάτα'}

    def translate(self, word):  # traducir una palabra específica
        return self.words.get(word, str(word))

class TranslatorAleman(Translator):
    def __init__(self):  # constructor
        self.words = {'dog':'hund', 'cat':'katze'}

    def translate(self, word):  # traducir una palabra específica
        return self.words.get(word, str(word))

class TranslateFactory:
    def getLanguage(self, lan):
        """Dado el nombre de un idioma, la siguiente función regresa un
        objeto de cierto tipo dependiendo del idioma ingresado"""
        if lan == 'español':
            return SpanishTranslator()  # objeto regresado
        if lan == 'griego':
            return GreekTranslator()  # objeto regresado
        if lan == 'alemán':
            return TranslatorAleman()  # objeto regresado

# El factory-method es un patrón que lidia con el problema de crear objetos
# sin tener que especificar la clase exacta del objeto que será creado
 
def main():
    # Ingresamos la palabra a traducir y el idioma al que la queremos traducir
    palabra, idioma = list(map(str, input().strip().split()))
    translateFactory = TranslateFactory()  # objeto de la clase TranslateFactory
    # Ejecutamos función getLanguage, la cual nos va a regresar un objeto
    # de la clase a la que pertenece el idioma
    language = translateFactory.getLanguage(idioma)
    # Imprimimos la traducción
    print('Palabra "',palabra,'" traducida al ' ,idioma,': ',language.translate(palabra), sep = '')

if __name__ == "__main__":
    main()
