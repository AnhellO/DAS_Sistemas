import abc
#Se utilizan los decoradores para agregar funcionalidades al objeto sin alterar su estructura
#Clase abstracta o Componente
class TextRenderer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def render(self):
        pass

#Clase base, que implementa la clase TextRenderer(componente)
class NormalText(TextRenderer):
    def __init__(self, text):
        self._text = text

    def render(self):
        return "¡" + self._text + "!"


#Clase Decorador, implementa la clase abstracta TextRenderer, todos los decoradores la implementan
class TextDecorator(TextRenderer, metaclass=abc.ABCMeta):

    def __init__(self, decoratedText):
        self.decoratedText = decoratedText

    def render(self):
        return self.decoratedText.render()

#Tipo de decorador, para este caso, Highlighted, Italic y Underline son tipos de decoradores, implementan la clase abstracta
class Highlighted(TextRenderer):

    def __init__(self, decoratedText):
        TextDecorator.__init__(self, decoratedText)

    def render(self):
        return "<b>" + self.decoratedText.render() + "</b>"

class Italic(TextRenderer):

    def __init__(self, decoratedText):
        TextDecorator.__init__(self, decoratedText)

    def render(self):
        return "<i>" + self.decoratedText.render() + "</i>"

class Underline(TextRenderer):

    def __init__(self, decoratedText):
            TextDecorator.__init__(self, decoratedText)

    def render(self):
            return "<u>" + self.decoratedText.render() + "</u>"



if __name__ == '__main__':
    #Objeto normal (NormalText), en este caso no se utilizan decoradores
    renderer = NormalText('Texto Normal')
    print(renderer.render())

    #Se crea un texto resaltado
    #Aqui se decora el objeto llamando NormalText dentro de otra funcion Highlighted
    renderer2 = Highlighted(NormalText('Texto Resaltado'))
    print(renderer2.render())

    #Se crea un texto resaltado y subrayado
    #Aqui se decora el objeto llamando NormalText dentro de otra funcion Underline y a su vez
    #se decora tal objeto dentro de la funcion Highlighted
    renderer3 = Highlighted(Underline(NormalText('Texto Resaltado y Subrayado')))
    print(renderer3.render())

    #Se crea un texto aplicando todos los formatos
    #Aqui se decora el objeto llamando NormalText dentro de otra funcion Ialic y a su vez
    #se decora tal objeto dentro de la funcion Underline y por ultimo se decora
    #tal objeto dentro de la funcion Highlighted
    renderer4 = Highlighted(Underline(Italic(NormalText('Aplicando todos los formatos'))))
    print(renderer4.render())
