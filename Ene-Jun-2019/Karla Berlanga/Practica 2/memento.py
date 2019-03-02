class Memento(object):

    def __init__(self, state):
        self.state = state

    def getState(self):
        return self.state

class TextEditor(Memento):

    def __init__(self):
        self.state = ''

    def setState(self, state):
        self.state = self.state + ' ' + state

    def getState(self):
        return self.state

    def saveStateToMemento(self):
        return Memento(self.state)

    def getStateFromMemento(self, memento):
        self.state = memento.getState()

class CareTaker(Memento):

    def __init__(self):
        self.lista = []

    def addMemento(self, state):
        temp = Memento(state)
        elemento = temp.getState()
        self.lista.append(elemento)

    def getMemento(self, index):
        return self.lista[index]



if __name__ == '__main__':

    care_taker = CareTaker()
    text = TextEditor()

    text.setState('This is the first sentence')
    text.setState('This is the second.')
    care_taker.addMemento(text.saveStateToMemento())

    text.setState('This is the third.')
    care_taker.addMemento(text.saveStateToMemento())

    text.setState('This is the fourth.')
    care_taker.addMemento(text.saveStateToMemento())
    print(text.getState())

    text.getStateFromMemento(care_taker.getMemento(0))
    print(text.getState())
