from abc import ABC, abstractmethod
class Button(ABC):
    @abstractmethod
    def render(self):
        return
    def onClick(self):
        return
class windowsButton(Button):
    def existir():
        pass
class HTMLButton(Button):
    def existir():
        pass

class dialog(Button, ABC):
    def render(self):
        return super().render()
    @abstractmethod
    def createButoon(self)->Button:
        return"se creo un boton"
class windowsDialog(dialog):
    def createButoon(self) -> Button:
        super().createButoon()
        return "WindowsButton"
class webDialog (dialog):
    def createButoon(self) -> Button:
        return super().createButoon()