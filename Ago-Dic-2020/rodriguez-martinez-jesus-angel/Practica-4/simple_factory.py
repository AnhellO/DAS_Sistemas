from abc import ABC, abstractmethod

# General abstract class.
class SchoolMember(ABC):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.age = kwargs.get('age', -1)
        self.id_num = kwargs.get('id_num', 'XXXXXX')
    
    def __str__(self):
        return f"¡Mi nombre es {self.name}!, soy {self.get_role()}, tengo {self.age} años y mi ID es {self.id_num}"
    
    @abstractmethod
    def get_role(self):
        pass

class Teacher(SchoolMember):
    def get_role(self):
        return "Maestro"

class Student(SchoolMember):
    def get_role(self):
        return "Estudiante"

class Director(SchoolMember):
    def get_role(self):
        return "Director"
               
class SchoolMemberFactory:
    @classmethod
    def make(cls, kind, **kwargs):
        roles = [role.__name__.capitalize() for role in SchoolMember.__subclasses__()]
        # Checks if the role exists, if not then it won't evaluate the expression.
        if kind.capitalize() not in roles:
            return f"[Error]: '{kind}' invalid role"
        return eval(kind.capitalize())(**kwargs)

def main():
    kind = input("¿Qué quieres crear?\n")
    _name = input("¿Qué nombre tiene?\n")
    obj = SchoolMemberFactory.make(kind, name=_name, age=22, id_num='070KGP')
    print(obj)
    print(obj.get_role())

if __name__ == "__main__":
    main()

