from abc import ABC, abstractmethod

# Interface
class ItemElements(ABC):

    @abstractmethod
    def accept(self):
        pass


# Element A
class Element_A(ItemElements):
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name+" Element A"

    def accept(self, visitor):
        return visitor.visit(self)


# Element B
class Element_B(ItemElements):
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name+" Element B"

    def accept(self, visitor):
        return visitor.visit(self)


# Interface visitor
class Visitor():

    @abstractmethod
    def visit(self, itemelement):
        pass


# Concret Visitor
class ConcretVisitor(Visitor):
    
    def visit(self, item):
        name = item.get_name()
        return "He's a "+name


# Cliente
def Client(items):
    visitor = ConcretVisitor()
    visitorArr = []
    for item in items:
        visitorArr.append(item.accept(visitor))
    print(visitorArr)
    return visitorArr

if __name__ == '__main__':
    items = [
        Element_A("Student"),
        Element_A("Teacher"),
        Element_B("Student"),
        Element_B("Teacher"),        
    ]
    typee = Client(items)
    for person in typee:
        print(person) 