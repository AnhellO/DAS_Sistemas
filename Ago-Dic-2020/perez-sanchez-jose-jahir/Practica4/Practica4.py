import abc
from abc import abstractmethod, ABC  

class SchoolMember(ABC):
    def __init__(self, **args):
        self.name = args.get('name', '')
        self.age = args.get('age', -1)
        self.id_num = args.get('id_num', 'XXXXXX')
    
    def __str__(self):
        return f"Soy {self.name}!, soy {self.obtener_tipo()}, tengo {self.age} años y mi ID = {self.id_num}"
    
    @abstractmethod
    def obtener_tipo(self):
        pass

class Teacher(SchoolMember):  
    def obtener_tipo(self):
        return "Maestro"

class Student(SchoolMember):
    def obtener_tipo(self):
        return "Estudiante"
        
class Director(SchoolMember):  
    def obtener_tipo(self):
        return "Director"
        
class SchoolMemberFactory:
    @classmethod
    def make(cls, kind, **args):
        try:
            return eval(kind.capitalize())(**args)
        except Exception:
            return f"Error! tipo '{kind}' invalido!"
        except args.get(len(id)) != 6:
            return "Error! tipo ID invalido!"
        
def main():
    kind = input("Qué quieres crear?\n")
    _name = input("Qué nombre tiene?\n")
    obj = SchoolMemberFactory.make(kind, name=_name, age=22, id='54845')
    print(obj)
    
if __name__ == "__main__":
    main()