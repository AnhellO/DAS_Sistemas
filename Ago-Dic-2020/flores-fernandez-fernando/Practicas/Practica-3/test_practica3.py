import Practica3

def test_turn_on():
    ON= Practica3.TurnedOn().changeState()
    assert ON == "ON"    

def test_turn_off():
    OFF= Practica3.TurnedOff().changeState()
    assert OFF == "OFF"

def test_getState():
    state = Practica3.RadioStation().getState()
    assert state == None

def test_setState():
    Radio = Practica3.RadioStation()
    ON = Practica3.TurnedOn()
    Radio.setState(ON)
    Radio.changeState()
    state = Radio.getState()
    assert state == "ON"
