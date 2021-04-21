import pytest

from cajero_chain import *

@pytest.mark.parametrize("suites, expected", [
    (50,"Dar 1 de 50\n"),
    (80, 'Dar 1 de 50\nDar 1 de 20\nDar 1 de 10\n'),
    (20, 'Dar 1 de 20\n'),
    (10, 'Dar 1 de 10\n'),
    (140, 'Dar 2 de 50\nDar 2 de 20\n'),
    (160, 'Dar 3 de 50\nDar 1 de 10\n')
    ])
def test_run_all(capfd, suites, expected):
    CajeroATMChain().chain1.handle(suites)
    out, _ = capfd.readouterr()
    assert out == expected
