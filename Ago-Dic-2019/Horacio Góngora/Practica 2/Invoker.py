from Command import Command

class Invoker:
    """
    The Invoker is associated with one or several commands. It sends a request
    to the command.
    """

    _on_start = None
    _on_finish = None

    """
    Initialize commands.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes. The
        Invoker passes a request to a receiver indirectly, by executing a
        command.
        """

        print("Invoker: Quieres hacer algo antes de empezar?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...haciendo algo realmente importante...")

        print("Invoker: Quieres hacer algo anges de que termine?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()