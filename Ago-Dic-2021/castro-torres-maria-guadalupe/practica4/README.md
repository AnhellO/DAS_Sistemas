###PRACTICA-4 PATRON COMMAND###

###Sintésis sobre lo comprendido acerca del patrón de diseño###

El patrón de comando es un patrón de diseño de comportamiento, en el que existe una abstracción entre un objeto que invoca un comando y el objeto que lo ejecuta.
Por ejemplo, un botón llamará al Invocador , que llamará a un Comando prerregistrado , que ejecutará el Receptor .
Una clase concreta delegará una solicitud a un objeto de comando, en lugar de implementar la solicitud directamente.
El uso de un patrón de diseño de comandos permite separar inquietudes y resolver problemas de inquietudes de forma independiente entre sí.
Por ejemplo, registrar la ejecución de un comando y su resultado.


Descripción del ejemplo implementado, desde el problema hasta la forma de implementar la solución y el por qué

En el ejemplo creado es para encender y apagar una television

creamos el receiver que es el objeto que recibirá y ejecutará el comando.

~~~ class Receiver:
    "El receptor"

    @staticmethod
    def run_command_1():
        "instrucciones a ejecutar"
        return "TV ENCENDIDA"

    @staticmethod
    def run_command_2():
        "instrucciones a ejecutar"
        return "TV APAGADA" ~~~


Invoker: El objeto que envía el comando al receptor. Por ejemplo, un botón.  

~~~class Invoker:
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
            return "Comando no reconocido"~~~


Objeto de comando : en sí mismo, un objeto, que implementa un método de ejecución o acción, y contiene toda la información necesaria para ejecutarlo


~~~class ICommand(metaclass=ABCMeta):  
    "La interfaz comando, que todos los comandos implementarán"
    @staticmethod
    @abstractmethod
    def execute():
        """
        The required execute method that all command objects
        will use
        """ ~~~

Cliente : la aplicación o componente que conoce el receptor, el invocador y los comandos.

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




Recursos desde los cuáles estudiaste, investigaste e implementaste el patrón

https://refactoring.guru/es/design-patterns/command
http://www3.uji.es/~belfern/Docencia/Presentaciones/ProgramacionAvanzada/Tema2/accion.html#28
https://www.geeksforgeeks.org/command-method-python-design-patterns/
https://www.youtube.com/watch?v=9qA5kw8dcSU