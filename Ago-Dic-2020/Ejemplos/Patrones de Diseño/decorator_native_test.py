import pytest

from decorator_native import *

@pytest.mark.parametrize("input, expected", [
    (
        "stalker",
        "Hola Mundo!, y hola stalker!"
    )
])
def test_hello_world_with_name(input, expected):
    assert expected == hello_world_with_name(hello_world, input)

@pytest.mark.parametrize("expected", [
    (
        "Hola clase de diseño y arquitectura de software!\n\ty hola a ti que me estás viendo desde la pantalla >:D!\n"
    )
])
def test_hello_class(capfd, expected):
    hello_class()
    out, _ = capfd.readouterr()
    assert expected == out

@pytest.mark.parametrize("input, expected", [
    (
        1,
        "Hola clase de diseño y arquitectura de software!\n\ty a ti también que me estás viendo desde la pantalla >:D! 10"
    ),
    (
        2,
        "Hola clase de diseño y arquitectura de software!\n\ty a ti también que no me estás viendo desde la pantalla >:C!"
    ),
    (
        3,
        None
    )
])
def test_hello_class_2(input, expected):
    assert expected == hello_class_2(input)

def test_decorador(capfd):
    cafecito()
    out, _ = capfd.readouterr()
    assert "Hehehe\nCafecito! :D\nCon pan!\nY con leche y azúcar >:D!\n" == out
    
    @decorador
    def tecito():
        print("Tecito! :D")
    
    tecito()
    out, _ = capfd.readouterr()
    assert "Hehehe\nTecito! :D\nCon pan!\nY con leche y azúcar >:D!\n" == out