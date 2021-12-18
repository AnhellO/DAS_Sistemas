import pytest 
from practica4 import * 

class pruebaelevador:
    def test_firtFloor(self):
        floor = firstFloor()
        assert floor.pushDownBtn()
        assert floor.pushUpBtn()

    def test_secondFloor(self):
        floor = secondFloor()
        assert floor.push()
        assert floor.pushUpBtn()

    def test_presentState(self):
        floor = Elevador()
        assert floor.presentState()
        assert floor.pushDownBtn()
        assert floor.pushUpAndDownBtns()
        assert floor.noBtnPushed()
        

    




