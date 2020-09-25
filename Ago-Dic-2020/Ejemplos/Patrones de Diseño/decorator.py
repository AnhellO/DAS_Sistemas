import abc

# Component
class TextComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self):
        pass
    
# Concrete Component
class NormalTextComponent(TextComponent):
    def __init__(self, text: str):
        self._text = text

    def render(self):
        return f"¡{self._text}!"

# Decorator
class TextDecorator(TextComponent, metaclass=abc.ABCMeta):
    def __init__(self, text_component: TextComponent):
        self._text_component = text_component

    @abc.abstractmethod
    def render(self):
        pass

# Concrete Decorator A
class HighlightTextDecorator(TextDecorator):
    def render(self):
        return f"<strong>{self._text_component.render()}</strong>"

# Concrete Decorator B
class UnderlineTextDecorator(TextDecorator):
    def render(self):
        return f"<u>{self._text_component.render()}</u>"
    
# Concrete Decorator C
class ItalicTextDecorator(TextDecorator):
    def render(self):
        return f"<em>{self._text_component.render()}</em>"


def main():
    # Normal text
    print(NormalTextComponent('Texto Normal').render())
    # Highlighted text
    print(HighlightTextDecorator(NormalTextComponent('Texto Resaltado')).render())
    # Highlighted & underlined text
    print(HighlightTextDecorator(UnderlineTextDecorator(NormalTextComponent('Texto Resaltado y Subrayado'))).render())
    # All formats
    print(HighlightTextDecorator(UnderlineTextDecorator(ItalicTextDecorator(NormalTextComponent('Aplicando todos los formatos')))).render())
    
if __name__ == '__main__':
    main()
