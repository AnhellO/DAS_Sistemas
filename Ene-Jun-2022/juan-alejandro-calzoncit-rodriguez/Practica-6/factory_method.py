from abc import ABC, abstractmethod

# Clase creadora
class Dialog(ABC):
    
    @abstractmethod
    def createButton(self): # Metódo factory
        pass

    def render(self):        
        okButton = self.createButton()
        print(okButton.onClick())
        print(okButton.render())

# Creador concreto
class WindowsDialog(Dialog):
    def createButton(self):
        return WindowsButton()

# Creador concreto
class WebDialog(Dialog):
    def createButton(self):
        return HTMLButton()

# Interface producto
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self):
        pass

# Producto concreto
class WindowsButton(Button):
    def render(self):
        return 'Representa un botón en estilo Windows'

    def onClick(self):
        return 'Vincula un evento clic de OS nativo'

# Producto concreto
class HTMLButton(Button):
    def render(self):
        return 'Representa un botón en HTML'

    def onClick(self):
        return 'Vincula un evento clic de navegador web'

class Application:
    def __init__(self):
        self.dialog : Dialog

    def initialize(self,OS):
        if (OS == "Windows"):
            self.dialog = WindowsDialog()
        elif (OS == "Web"):
            self.dialog = WebDialog()
        else:
            print("Error! Unknown operating system.")

    def main(self,OS):
        self.initialize(OS)
        self.dialog.render()

if __name__ == '__main__':
    wind = Application()
    wind.main('Windows')     
    print()
    html = Application()
    html.main('Web')  


# def Application(dialog : Dialog):         Acuerdate de borrarlo                        
            
#     dialog.render()

# if __name__ == '__main__':
#     wind = WindowsDialog()
#     Application(wind)
#     print()
#     html = WebDialog()
#     Application(html)    