from abc import ABC, abstractmethod

#creador
class Dialog(ABC):

    @abstractmethod
    def render(self):
        print("button is creating...")

    @abstractmethod
    def createButton(self):
        pass

#creador concreto
class WindowsDialog(Dialog):

    def render(self):
        return Windows.render(self)
    
    def createButton(self):
        return Windows.onClick(self)

class HtmlDialog(Dialog):

    def render(self):
        return Html.render(self)
    
    def createButton(self):
        return Html.onClick(self)


#interfaz
class Button(ABC):
    
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self):
        pass

#producto concreto
class Windows(Button):
    def render(self):
        print("window button appears")
    
    def onClick(self):
        print("window button is pressed")

class Html(Button):
    def render(self):
        print("html button appears")
    
    def onClick(self):
        print("html button is pressed")


def main():
    boton = WindowsDialog()
    boton.render()
    boton.createButton()
    print("----------")
    html = HtmlDialog()
    html.render()
    html.createButton()

if __name__ == "__main__":
    main()    
