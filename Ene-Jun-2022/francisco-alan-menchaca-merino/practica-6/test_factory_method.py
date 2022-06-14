from factory_method import Dialog, WindowsDialog, WebDialog
from factory_method import Button, WindowsButton, HtmlButton
from factory_method import ButtonHandler
import pytest


class TestFactoryMethod:
    def test_button_handler(self):
        button_handler = ButtonHandler(WindowsDialog())
        assert isinstance(button_handler.creator, Dialog)
        assert isinstance(button_handler.creator, WindowsDialog)
        button_handler.create_button()
        assert isinstance(button_handler.button, WindowsButton)

        button_handler = ButtonHandler(WebDialog())
        assert isinstance(button_handler.creator, Dialog)
        assert isinstance(button_handler.creator, WebDialog)
        button_handler.create_button()
        assert isinstance(button_handler.button, HtmlButton)

    def test_windows_button(self):
        button_handler = ButtonHandler(WindowsDialog())
        button_handler.create_button()
        windows_button = button_handler.get_button()
        assert isinstance(windows_button, Button)
        assert isinstance(windows_button, WindowsButton)

        render_msg_expected = "Rendering WindowsButton"
        onclick_msg_expected = "WindowsButton: onClick, doing an Action"
        assert windows_button.render() == render_msg_expected
        assert windows_button.onClick() == onclick_msg_expected

    def test_html_button(self):
        button_handler = ButtonHandler(WebDialog())
        button_handler.create_button()
        html_button = button_handler.get_button()
        assert isinstance(html_button, Button)
        assert isinstance(html_button, HtmlButton)

        render_msg_expected = "Rendering HtmlButton"
        onclick_msg_expected = "HtmlButton: onClick, doing an Action"
        assert html_button.render() == render_msg_expected
        assert html_button.onClick() == onclick_msg_expected


if __name__ == '__main__':
    pytest.main()
