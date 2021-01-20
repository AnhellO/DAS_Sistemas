from abc import ABC, abstractmethod

class SchoolMember:
    def __init__(self, **args):
        self.name = args.get('name', '')
        self.age = args.get('age', 22)
        self.id_num = args.get('id_num', '070KGP')
    
    def __str__(self):
        return f"Soy el {self.data()} {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"

    @abstractmethod
    def data(self):
        pass

class Teacher(SchoolMember):
    def data(self):
        return f"profesor"

class Student(SchoolMember):
    def data(self):
        return f"estudiante"

class Coach(SchoolMember):
    def data(self):
        return f"Coach"

class SchoolMemberFactory:
    @classmethod
    def make(cls, kind, **args):
        functions = [cls.__name__ for cls in SchoolMember.__subclasses__()]
        if kind.capitalize() not in functions:
            raise ValueError("# ERROR # Esa fucion no es valida. intente: Student, Teacher, Coach.")
        return eval(kind.capitalize())(**args)    

def main():
    kind = input("Qué quieres crear?\n")
    _name = input("Qué nombre tiene?\n")
    obj = SchoolMemberFactory.make(kind, name=_name, age=22, id_num='070KGP')
    print(obj)
    
if __name__ == "__main__":
    main()