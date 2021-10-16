from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):  
    "La interfaz comando, que todos los comandos implementarán"
    @staticmethod
    @abstractmethod
    def execute():
        """
        The required execute method that all command objects
        will use
        """

class Invoker:
    "la clase Invoker "
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        "Registrar comandos en el Invoker"
        self._commands[command_name] = command
        return "comando registrado"

    def execute(self, command_name):
        "Ejecuta cualquier comando registrado"
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            return "Comando no reconocido"

class Receiver:
    "El receptor"

    @staticmethod
    def run_command_1():
        "instrucciones a ejecutar"
        return "TV ENCENDIDA"

    @staticmethod
    def run_command_2():
        "instrucciones a ejecutar"
        return "TV APAGADA"

class Command1(ICommand): 
    """
    Un objeto Command, que implementa la interfaz ICommand y 
    ejecuta el comando en el receptor designado
    """
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_1()

class Command2(ICommand):  
    """
    Un objeto Command, que implementa la interfaz ICommand y 
    ejecuta el comando en el receptor designado

    """
    def __init__(self, receiver):
        self._receiver = receiver
    def execute(self):
        self._receiver.run_command_2()

# The CLient
# Create a receiver
RECEIVER = Receiver()
# Create Commands
ENCENDIDO = Command1(RECEIVER)
APAGADO = Command2(RECEIVER)
# Register the commands with the invoker
INVOKER = Invoker()
INVOKER.register("1", ENCENDIDO)
INVOKER.register("2", APAGADO)
# Execute the commands that are registered on the Invoker
INVOKER.execute("1")
INVOKER.execute("2")
INVOKER.execute("1")
INVOKER.execute("2")