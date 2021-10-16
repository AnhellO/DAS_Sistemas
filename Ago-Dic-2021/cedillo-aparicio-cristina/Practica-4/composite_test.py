from composite import *

def test(capsys):
    gerenteGeneral = CompositeElement('Gerente General')
    gerente1 = CompositeElement('Gerente 1')
    gerenteGeneral.add(gerente1)
    gerenteGeneral.details()
    out, _ = capsys.readouterr()
    assert "'Gerente General' es superior de 'Gerente 1'" in out

def test2(capsys):
    gerenteGeneral = CompositeElement('Gerente General')
    programador1 = LeafElement('Programador 1')
    gerenteGeneral.add(programador1)
    gerenteGeneral.details()
    out, _ = capsys.readouterr()
    assert "'Gerente General' es supervisor de 'Programador 1'" in out

def test3(capsys):
    gerenteGeneral = CompositeElement('Gerente General')
    gerente1 = CompositeElement("Gerente 1")
    programador1 = LeafElement('Programador 1-1')
    gerenteGeneral.add(gerente1)
    gerente1.add(programador1)
    gerenteGeneral.details()
    out, _ = capsys.readouterr()
    assert "'Gerente General' es superior de 'Gerente 1'\n'Gerente 1' es supervisor de 'Programador 1-1'" in out

def test4(capsys):
    gerenteGeneral = CompositeElement("Gerente General")
    gerente1 = CompositeElement("Gerente 1")
    gerente2 = CompositeElement("Gerente 2")
    programador11 = LeafElement("Programador 1-1")
    programador12 = LeafElement("Programador 1-2")
    programador21 = LeafElement("Programador 2-1")
    programador22 = LeafElement("Programador 2-2")
    gerenteGeneral.add(gerente1)
    gerenteGeneral.add(gerente2)
    gerente1.add(programador11)
    gerente1.add(programador12)
    gerente2.add(programador21)
    gerente2.add(programador22)
    gerenteGeneral.details()
    out, _ = capsys.readouterr()
    assert "'Gerente General' es superior de 'Gerente 1'\n'Gerente 1' es supervisor de 'Programador 1-1'\n'Gerente 1' es supervisor de 'Programador 1-2'\n'Gerente General' es superior de 'Gerente 2'\n'Gerente 2' es supervisor de 'Programador 2-1'\n'Gerente 2' es supervisor de 'Programador 2-2'" in out

def test5(capsys):
    gerenteGeneral = CompositeElement("Gerente General")
    gerente1 = CompositeElement("Gerente 1")
    gerente2 = CompositeElement("Gerente 2")
    programador11 = LeafElement("Programador 1-1")
    programador12 = LeafElement("Programador 1-2")
    programador21 = LeafElement("Programador 2-1")
    programador22 = LeafElement("Programador 2-2")
    gerenteGeneral.add(gerente1)
    gerenteGeneral.add(gerente2)
    gerente1.add(programador11)
    gerente1.add(programador12)
    gerente2.add(programador21)
    gerente2.add(programador22)
    gerente2.remove(programador21)
    gerenteGeneral.details()
    out, _ = capsys.readouterr()
    assert "'Gerente General' es superior de 'Gerente 1'\n'Gerente 1' es supervisor de 'Programador 1-1'\n'Gerente 1' es supervisor de 'Programador 1-2'\n'Gerente General' es superior de 'Gerente 2'\n'Gerente 2' es supervisor de 'Programador 2-2'" in out