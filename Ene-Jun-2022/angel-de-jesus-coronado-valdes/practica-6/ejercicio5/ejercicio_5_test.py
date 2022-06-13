import pytest

from ejercicio_5 import *

@pytest.mark.parametrize("items,expected",[
    (
        Client().client_code(WindowsDialog()),
        "Creador:\nIMAGE WINDOW\nBUTTON WINDOW"
    ),
    (
        Client().client_code(WebDialog()),
        "Creador:\n<img>HTML IMG</img>\n<input>Button HTML</input>"
    ),
])

def test_cliente_code(items,expected):
    assert items == expected