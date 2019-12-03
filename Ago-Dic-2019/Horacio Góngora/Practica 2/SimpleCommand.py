from Command import Command

class SimpleCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: Vez, Puedo hacer simples cosas como imprimir :D"
              f"({self._payload})")