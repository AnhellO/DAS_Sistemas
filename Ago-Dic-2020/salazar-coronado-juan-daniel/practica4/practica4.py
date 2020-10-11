from abc import ABC
from abc import abstractmethod

class SchoolMember(ABC):
    def __init__(self, **args):
        self.name = args.get('name', '')
        self.age = args.get('age', -1)
        self.id_num = args.get('id', '')
    
    def __str__(self):
        return f"Soy {self.tipo()}, me llamo {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"

    @abstractmethod
    def tipo(self):
        pass

class Teacher(SchoolMember):
    def tipo(self):
        return "Maestro/a"

class Student(SchoolMember):
    def tipo(self):
        return "Estudiante"

class Employee(SchoolMember):
    def tipo(self):
        return "Empleado/a"

class SchoolMemberFactory:
    @classmethod
    def make(cls, kind, **args):
        #Se puede reemplazar así:
        if kind.capitalize() == "Student" or kind.capitalize() == "Teacher" or kind.capitalize() == "Employee":
            return eval(kind.capitalize())(**args)
        
        return f"Error! tipo '{kind}' invalido!"
        
        #try:
        #    return eval(kind.capitalize())(**args)
        #except Exception:
        #    return f"Error! tipo '{kind}' invalido!"
        
def main():
    kind = input("Qué quieres crear?\n")
    _name = input("Qué nombre tiene?\n")
    obj = SchoolMemberFactory.make(kind, name=_name, age=21, id='17289193')
    print(obj)
    
if __name__ == "__main__":
    main()