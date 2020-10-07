from abc import abstractmethod, ABCMeta

class InternalState(metaclass = ABCMeta): ##creamos la interfaz de los estado hace que cambie el estado
    @abstractmethod
    def change_state(self):
        pass

class TurnedOn(InternalState):  ##estado encendido
    def change_state(self):
        print("Turning ON the Antenna!!!")
        return "ON"

class TurnedOff(InternalState):  ##estado apagado
    def change_state(self):
        print("Turning OFF the Antenna!!!")
        return "OFF"
    
class RadioStation(InternalState): ##contexto
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, status):
        self.state = status

    def change_state(self):
        self.state = self.state.change_state()
    
    def how_internal(self):
        print('The radios internal state is currently: {}'.format(radio.get_state()))

radio = RadioStation()
on = TurnedOn()
off = TurnedOff()

def main():
    des = ""
    while (des != "exit"):
        radio.how_internal()
        des = input("Change internal state to: ")
        if(des == "on"):
            radio.set_state(on)
            radio.change_state()
        if(des == "off"):
            radio.set_state(off)
            radio.change_state()
            
if __name__ == "__main__":
    main()
