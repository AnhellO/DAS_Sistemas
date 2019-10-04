from Invoker import Invoker
from SimpleCommand import SimpleCommand
from Receiver import Receiver
from ComplexComand import ComplexCommand

def main():
    """
        The client code can parameterize an invoker with any commands.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Di Holi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Enviar un email", "Guardar un reporte"))
    invoker.do_something_important()

if __name__ == "__main__":
    main()