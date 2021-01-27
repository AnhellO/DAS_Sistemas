class SchoolMember:
    def __init__(self, **args):
        self.name = args.get('name', '')
        self.age = args.get('age', -1)
        self.id_num = args.get('id_num', 'XXXXXX')
    
    def __str__(self):
        return f"Soy {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"

class Teacher(SchoolMember):
    def __str__(self):
        return f"Soy el maestro {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"

class Student(SchoolMember):
    def __str__(self):
        return f"Soy el alumno {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"
        
class SchoolMemberFactory:
    @classmethod
    def make(cls, kind, **args):
        try:
            return eval(kind.capitalize())(**args)
        except Exception:
            return f"Error! tipo '{kind}' invalido!"
        

def main():
    kind = input("Qué quieres crear?\n")
    _name = input("Qué nombre tiene?\n")
    obj = SchoolMemberFactory.make(kind, name=_name, age=22, id_num='070KGP')
    print(obj)
    
if __name__ == "__main__":
    main()