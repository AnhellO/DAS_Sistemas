from __future__ import annotations
from abc import ABC, abstractmethod



class Elevador:

    _state = None

    def __init__(self, state: State) -> None:
        self.setElevador(state)

    # method to change the state of the object
    def setElevador(self, state: State):

        self._state = state
        self._state.elevador = self

    def presentState(self):
        print(f"Elevador is in {type(self._state).__name__}")

    # los métodos para ejecutar la funcionalidad del ascensor.
    def pushDownBtn(self):
        self._state.pushDownBtn()

    def pushUpBtn(self):
        self._state.pushUpBtn()

    # Si se pulsan ambos botones a la vez, no debería suceder nada
    def pushUpAndDownBtns(self) -> None:
        print("Vaya, debes presionar un botón a la vez")

    # si no se presionó ningún botón, solo debe esperar abierto para los invitados
    def noBtnPushed(self) -> None:
        print("Pulse cualquier botón. Arriba o abajo")


# La interfaz de estado 
class State(ABC):
    @property
    def elevador(self) -> Elevador:
        return self._elevador

    @elevador.setter
    def elevador(self, elevador: Elevador) -> None:
        self._elevador = elevador

    @abstractmethod
    def pushDownBtn(self) -> None:
        pass

    @abstractmethod
    def pushUpBtn(self) -> None:
        pass



# Tenemos dos estados del ascensor: cuando está en el primer piso y el segundo piso
class firstFloor(State):

    
    def pushDownBtn(self) -> None:
        print("Ya en el piso de abajo")

    
    def pushUpBtn(self) -> None:
        print("Ascensor subiendo un piso.")
        self.elevador.setElevador(secondFloor())


class secondFloor(State):

    # si se presiona el botón hacia abajo, debe moverse un piso hacia abajo y abrir la puerta
    def pushDownBtn(self) -> None:
        print("Ascensor bajando un piso...")
        self.elevator.setElevator(firstFloor())

    # if up button is pushed nothing should happen
    def pushUpBtn(self) -> None:
        print("Ya en el piso superior")


if __name__ == "__main__":
    # El código de cliente.

    myElevador = Elevador(firstFloor())
    myElevador.presentState()

    # Up button is pushed
    myElevador.pushUpBtn()

    myElevador.presentState()