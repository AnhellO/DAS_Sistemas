import unittest
import pytest
from command import *


@pytest.mark.parametrize(
    ["command_name","command","resultado_esperado"],
    [
        ("1", ENCENDIDO, "comando registrado")
    ]
)

def test_Comando_ON_Registrado(command_name,command, resultado_esperado):
    assert INVOKER.register(command_name, command) == resultado_esperado


##########################################################################################
@pytest.mark.parametrize(
    ["command_name","command","resultado_esperado"],
    [
        ("2", APAGADO, "comando registrado")
    ]
)

def test_Comando_OFF_Registrado(command_name,command, resultado_esperado):
    assert INVOKER.register(command_name, command) == resultado_esperado    

##############################################################################################

@pytest.mark.parametrize(
    ["command_name","resultado_esperado"],
    [
        ("3", "Comando no reconocido")
    ]
)

def test_ComandoNoReconocido(command_name, resultado_esperado):
    assert INVOKER.execute(command_name) == resultado_esperado  




