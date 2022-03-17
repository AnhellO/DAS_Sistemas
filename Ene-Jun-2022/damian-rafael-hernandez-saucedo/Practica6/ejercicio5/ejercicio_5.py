from __future__ import annotations
from abc import ABC, abstractmethod

# Interface 
class Dialog(ABC):
    
    @abstractmethod
    def CreateButton(self):
        pass
    
    def RenderOperaction(self) -> str:
        operation = self.CreateButton()
        return f"Creador:\n{operation.Render()}\n{operation.OnClick()}"


# methods web, window
class WindowsDialog(Dialog):
    
    def CreateButton(self) -> Button:
        return WindowsButton()

class WebDialog(Dialog):
    def CreateButton(self) -> Button:
        return HtmlButton()


# Interface Button
class Button(ABC):
    
    @abstractmethod
    def Render(self) -> str:
        pass

    @abstractmethod
    def OnClick(self) -> str:
        pass


# methods button window, web
class WindowsButton(Button):
    def Render(self) -> str:
        return "IMAGE WINDOW"
    
    def OnClick(self) -> str:
        return "BUTTON WINDOW"

class HtmlButton(Button):
    def Render(self) -> str:
        return "<img>HTML IMG</img>"
    
    def OnClick(self) -> str:
        return "<input>Button HTML</input>"


# code Client
class Client:
    def client_code(self,creator: Dialog) -> None:
        return creator.RenderOperaction()


if __name__ == "__main__":
    client = Client()
    print("WINDOW")
    window = client.client_code(WindowsDialog())
    print(window)
    print("")
    print("WEB")
    web = client.client_code(WebDialog())
    print(web)
    

    
    