from abc import ABCMeta, abstractmethod

class SchoolMember(metaclass = ABCMeta):
    def __init__(self, **args):
        self.name = args.get('name', '')
        self.age = args.get('age', -1)
        self.id_num = args.get('id_num', 'XXXXXX')
    
    def __str__(self):
        return f"Soy {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"
    
    @abstractmethod
    def Saludar(self):
        pass

class Teacher(SchoolMember):
    def __str__(self):
        return super().__str__().replace("Soy", "Soy el ticher")
    
    def Saludar(self):
        return f"Buenos dias me llamo: {self.name}"

class Student(SchoolMember):
    def __str__(self):
        return f"Soy el alumno {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"
    
    def Saludar(self):
        return f"Buenos dias me llamo: {self.name}"

class Visitor(SchoolMember):
    def __str__(self):
        return f"Soy el visitante {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"
    
    def Saludar(self):
        return f"Buenos dias me llamo: {self.name}"    
class SchoolMemberFactory:
    @classmethod
    def make(cls, kind, **args):
        print(len(args.get("id_num", "XXXXXX")))
       
        # valida el tamaño del ID
        if len(args.get("id_num", "XXXXXX")) != 6:
            return "Error! El tamaño del ID debe ser de 6 caracteres"
        #validar que edad sea numero
        if isinstance(args.get('age', -1),int) == False:
            return "Error! la Edad debe ser numero"
            
            # valida que el kind sea correcto
        if kind != "Student" and kind != "Visitor" and kind != "Teacher" :
            print(kind)
            return f"Error! tipo '{kind}' invalido!"
        
        return eval(kind.capitalize())(**args)

def main():
    kind = input("Qué quieres crear?\n")
    _name = input("Qué nombre tiene?\n")
    obj = SchoolMemberFactory.make(kind, name = _name, age = 22, id = '01P3')
    print(obj)
    
if __name__ == "__main__":
    main()