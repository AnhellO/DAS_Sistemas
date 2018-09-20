from collections import deque

class Switch(object):
    """Clase Invocador"""
    def __init__(self):
        self._history = deque()

    @property
    def history(self):
        return self._history

    def execute(self, command):
        self._history.appendleft(command)
        command.execute()

class Command(object):
    """Interfaz de comando"""
    def __init__(self, obj):
        self._obj = obj

    def execute(self):
        raise NotImplementedError

class TurnOnCommand(Command):
    """Comando para encender la luz"""
    def execute(self):
        self._obj.turn_on()

class TurnOffCommand(Command):
    """Comando para apagar la luz"""
    def execute(self):
        self._obj.turn_off()

class Light(object):
    """Clase Reseptor"""
    def turn_on(self):
        print("La luz esta ON")

    def turn_off(self):
        print("La luz esta OFF")

class LightSwitchClient(object):
    """Clase cliente"""
    def __init__(self):
        self._lamp = Light()
        self._switch = Switch()

    @property
    def switch(self):
        return self._switch

    def press(self, cmd):
        cmd = cmd.strip().upper()
        if cmd == "ON":
            self._switch.execute(TurnOnCommand(self._lamp))
        elif cmd == "OFF":
            self._switch.execute(TurnOffCommand(self._lamp))
        else:
            print("Argumento 'ON' o 'OFF' es requerido")

if __name__ == "__main__":
    light_switch = LightSwitchClient()
    print("Prueba de ON.")
    light_switch.press("ON")
    print("Prueba de OFF.")
    light_switch.press("OFF")
    print("Prueba de comando invalida.")
    light_switch.press("****")

    print("Comando historia:")
    print(light_switch.switch.history)
