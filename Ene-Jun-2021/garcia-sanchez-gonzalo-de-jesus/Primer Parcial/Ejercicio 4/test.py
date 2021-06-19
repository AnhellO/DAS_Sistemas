#Goncho
import pytest
from Ejercicio_4 import Dispensador50,CajeroHandler,dispensador_chain

@pytest.mark.parametrize("expected", [
    (
        'Repartiendo 3 Billete de $50',
        'Repartiendo 1 Billete de $20',
        'Repartiendo 1 Billete de $10'
    )
])
def test_ciclo_completo(capfd, expected):
    Dispensador50().dispensador_chain(180)
    out, _ = capfd.readouterr()
    assert out == expected

        