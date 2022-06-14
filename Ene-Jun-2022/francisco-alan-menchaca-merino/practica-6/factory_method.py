from abc import ABC, abstractmethod


class Dialog(ABC):

    def render(self):
        pass

    @abstractmethod
    def createButton(self):
        pass


class WindowsDialog(Dialog):
    def createButton(self):
        return WindowsButton()


class WebDialog(Dialog):
    def createButton(self):
        return HtmlButton()


class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self):
        pass


class WindowsButton(Button):
    def render(self):
        return "Rendering WindowsButton"

    def onClick(self):
        return "WindowsButton: onClick, doing an Action"


class HtmlButton(Button):
    def render(self):
        return "Rendering HtmlButton"

    def onClick(self):
        return "HtmlButton: onClick, doing an Action"


class ButtonHandler():

    def __init__(self, creator):
        self.creator = creator
        self.button = None

    def create_button(self):
        self.button = self.creator.createButton()

    def get_button(self):
        return self.button


if __name__ == "__main__":
    print("\nCreting a Windows Button:")
    button_handler = ButtonHandler(WindowsDialog())
    button_handler.create_button()
    windows_button = button_handler.get_button()

    print(windows_button.render())
    print(windows_button.onClick())

    print("\nCreting a HTML Button:")
    button_handler = ButtonHandler(WebDialog())
    button_handler.create_button()
    html_button = button_handler.get_button()

    print(html_button.render())
    print(html_button.onClick())
