from Page import Page
import abc

#Strategy es la interfaz comun para todos los ConcreteStrategt,
# es decir, el comportamiento es comun. 
class Type(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def url(self):
        pass
    def type(self):
        pass
    def desc(self):
        pass
#Concrete Strategy: aqui se implementa usando la interfaz Strategy(Type)
#todos comparten el mimso comportamiento 
class HTML(Type):
    def url(self):
        return f'Page:'
    def type(self):
        return 'HTML'
    def desc(self):
        return '<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.</p>'
class XML(Type):
    def url(self):
        return ''
    def type(self):
        return ''
    def desc(self):
        return ''
class JSON(Type):
    def url(self):
        return ''
    def type(self):
        return ''
    def desc(self):
        return ''

class context(Page):
    def __init__(self, objects: list, strategy: Type = None):
        self._objects = objects
        self._strategy = strategy
    
    def cont(self):
        if self._strategy != None:
            return self._strategy.type
        
