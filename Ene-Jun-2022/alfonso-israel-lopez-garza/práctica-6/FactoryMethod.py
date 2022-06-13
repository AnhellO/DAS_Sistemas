from __future__ import annotations
from abc import ABC, abstractmethod

class Dialog(ABC):
    def render(self):
        dialogo = self.createButton()
        resultado = f"Trabajando con {dialogo.onClick()}"
        return resultado


    @abstractmethod
    def createButton(self):
        pass

class WindowsDialog(Dialog):
    def createButton(self) -> Button:
        return WindowsButton()

class WebDialog(Dialog):
    def createButton(self) -> Button:
        return HTMLButton()

class Button(ABC):
    def render(self):
        pass
    @abstractmethod
    def onClick(self):
        pass

class WindowsButton(Button):
    def onClick(self):
        return "Click en botton de windows"

class HTMLButton(Button):
    def onClick(self):
        return "Click en boton HTML"

def client_code(dialog: Dialog):
    print(f"Dialogo:\n"
          f"{dialog.render()}", end="")

if __name__ == "__main__":
    print("Presionando botton de windows.")
    client_code(WindowsDialog())
    print("\n")

    print("Presionando botton de HTML")
    client_code(WebDialog())
    print("\n")