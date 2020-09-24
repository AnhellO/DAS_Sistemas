from abc import abstractmethod, ABCMeta

class InternalState(metaclass = ABCMeta): ##creamos la interfaz de los estado hace que cambie el estado
    @abstractmethod
    def changeState(self):
        pass

class TurnedOn(InternalState):  ##estado encendido
    def changeState(self):
        print("Turning ON the Antenna!!!")
        return "ON"

class TurnedOff(InternalState):  ##estado apagado
    def changeState(self):
        print("Turning OFF the Antenna!!!")
        return "OFF"
    
class RadioStation(InternalState): ##contexto
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, status):
        self.state = status

    def changeState(self):
        self.state = self.state.changeState()
    
    def howinternal(self):
        print('The radios internal state is currently: {}'.format(Radio.getState()))

Radio = RadioStation()
ON = TurnedOn()
OFF = TurnedOff()

def main():
    des= ""
    while (des != "exit"):
        Radio.howinternal()
        des= input("Change internal state to: ")
        if(des == "on"):
            Radio.setState(ON)
            Radio.changeState()
        if(des == "off"):
            Radio.setState(OFF)
            Radio.changeState()
            
if __name__ == "__main__":
    main()
