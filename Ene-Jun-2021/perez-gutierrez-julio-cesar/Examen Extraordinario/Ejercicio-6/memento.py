from __future__ import annotations

class GameCharacter():
    def __init__(self, _score, _inventory, _level, _location):
        self._score = _score
        self._inventory = _inventory
        self._level = _level
        self._location = _location
    
    def restore(self, memento: Memento) -> GameCharacter:
        nuevoOriginador = GameCharacter(memento._score, memento._inventory, memento._level, memento._location)
        return nuevoOriginador
    
    def memento(self) -> Memento:
        nuevoMemento = Memento(self._score, self._inventory, self._level, self._location)
        return nuevoMemento
    
    def mostrarinfo(self, originator: GameCharacter):
        return f'Score:{originator._score}, Inventory:{originator._inventory}, Level:{originator._level}, Location:{originator._location}'
    
    def modinfo(self, score, inventory, level, location):
        self._score = score
        self._inventory = inventory
        self._level = level
        self._location = location
    
    def score(self):
        return self._score
    
    def register_kill(self):
        pass
    
    def add_inventory(self):
        pass
    
    def progress_to_next_level(self):
        pass
    
    def move_foreward(self):
        pass

class Memento(GameCharacter):
    def getEstado(self) -> GameCharacter:
        nuevoOriginador = GameCharacter(self._score, self._inventory, self._level, self._location)
        return nuevoOriginador

# protector 
class CareTaker(Memento):
    def __init__(self):
        self._mementos = []
    
    def save(self, memento : Memento):
        self._mementos.append(memento)
    
    def restore(self) -> Memento:
        return self._mementos.pop()

# client
#if __name__ == '__main__':
    # character = GameCharacter(500, 'Empty', 15, 'North')
    # print(character.mostrarinfo(character))
    # carataker = CareTaker()
    # carataker.save(character.memento())
    # character.modinfo(600, 'Full', 16, 'West')
    # print(character.mostrarinfo(character))
    # character = character.restore(carataker.restore())
    # print(character.mostrarinfo(character))