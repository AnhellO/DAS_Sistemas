# Implementa la funcionalidad necesaria utilizando el patrón de diseño
# Decorador para que el texto también pueda ser impreso de las siguientes
# maneras en HTML:
# Resaltado: <b>Texto</b>
# Cursiva: <i>Texto</i>
# Subrayado: <u>Texto</u>
# El texto deberá de poder mostrarse con uno o varios de los formatos especificados
# Ejemplo:
#   ¡Texto Normal!
#   <b>¡Texto Resaltado!</b>
#   <b><u>¡Texto Resaltado y Subrayado!</u></b>
#   <b><u><i>¡Aplicando todos los formatos!</i></u></b>

import abc

class Abstracta_Texto(metaclass = abc.ABCMeta):
    """Clase Abstracta de texto, todos las clases de texto deben tener esta estructura"""
    def render(self):
        pass

class TextRenderer(Abstracta_Texto):
    """Tipo de texto que implementa la clase abstacta arriba (Abstracta_Texto)"""
    def __init__(self, text):
        self._text = text

    def render(self):
        """Función que regresa el texto ingresado"""
        return self._text

class Abstracta_Decorador(Abstracta_Texto, metaclass = abc.ABCMeta):
    """Clase Abstracta de Decorador, implementa la clase abstracta de texto,
    todos los decoradores deben implementar estos metodos"""
    def __init__(self, textodecorado):
       self.textodecorado = textodecorado

    def render(self):
       return self.textodecorado.render()

class Resaltado_Decorador(Abstracta_Decorador):
   """implementa la clase abtsracta de arriba"""
   def __init__(self, textodecorado):
      Abstracta_Decorador.__init__(self, textodecorado)

   def render(self):
      """Decora el texto agregándole las etiquetas <b></b>"""
      return "<b>" + self.textodecorado.render() + "</b>"

class Subrayado_Decorador(Abstracta_Decorador):
    """implementa la clase abtsracta de arriba"""
    def __init__(self, textodecorado):
        Abstracta_Decorador.__init__(self, textodecorado)

    def render(self):
        """Decora el texto agregándole las etiquetas <u></u>"""
        return "<u>" + self.textodecorado.render() + "</u>"

class Cursiva_Decorador(Abstracta_Decorador):
    """implementa la clase abtsracta de arriba"""
    def __init__(self, textodecorado):
        Abstracta_Decorador.__init__(self, textodecorado)

    def render(self):
        """Decora el texto agregándole las etiquetas <i></i>"""
        return "<i>" + self.textodecorado.render() + "</i>"

# Los decoradores sirven para agregar funcionalidades al objeto en tiempo
# de ejecucion, es decir, "decoran" al objeto

def main():
    # creamos un objeto de la clase TextRender e imprimimos el texto
    texto = TextRenderer("¡Texto Normal!")
    print(texto.render())

    # Creamos un objeto de la clase TextRender y lo decoramos con las etiquetas
    # de resaltado de HTML
    texto2 = Resaltado_Decorador(TextRenderer("¡Texto Resaltado!"))
    print(texto2.render())

    # Creamos un objeto de la clase TextRender y lo decoramos dos veces
    texto3 = Resaltado_Decorador(Cursiva_Decorador(TextRenderer("¡Texto Resaltado y Subrayado!")))
    print(texto3.render())

    # Creamos un objeto de la clase TextRender y lo decoramos tres veces!!!
    texto4 = Resaltado_Decorador(Cursiva_Decorador(Subrayado_Decorador(TextRenderer("¡Aplicando todos los formatos!"))))
    print(texto4.render())

if __name__ == "__main__":
    main()
