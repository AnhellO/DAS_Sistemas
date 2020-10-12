from abc import ABC, abstractmethod

class SchoolMember(ABC):

    def __init__(self, **args):
        self.name = args.get('name', '')
        self.age = args.get('age', -1)
        self.id_num = args.get('id_num', 'XXXXXX')
    
    def __str__(self):
        return f"Soy el/la {self.identity()} {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"

    @abstractmethod
    def identity(self):
        return ""

class Teacher(SchoolMember):
    def identity(self):
        return "Maestr@"

class Student(SchoolMember):
    def identity(self):
        return "Estudiante"

class Secretary(SchoolMember):
    def identity(self):
        return "Secretari@"
        
class SchoolMemberFactory:
    @classmethod
    def make(cls, kind, **args):
        #recorro las clases existentes y guardo los nombres
        identidades = [identidad.__name__.capitalize() for identidad in SchoolMember.__subclasses__()]
        #checo si el tipo es igual a los nombres de las clases.
        if kind.capitalize() in identidades:
            return eval(kind.capitalize())(**args)
        return f"Error: '{kind}' type not found"   


def main():
    kind = input("Qué quieres crear?\n")
    _name = input("Qué nombre tiene?\n")
    obj = SchoolMemberFactory.make(kind, name=_name, age=22 , id_num='070KGP')
    print(obj)
    
if __name__ == "__main__":
    main()