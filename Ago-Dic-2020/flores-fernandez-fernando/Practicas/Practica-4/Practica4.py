from abc import ABCMeta, abstractmethod

class SchoolMember(metaclass = ABCMeta):
    def __init__(self, **args):
        self.name = args.get('name', '')
        self.age = args.get('age', -1)
        self.id_num = args.get('id_num', 'XXXXXX')
    
    def __str__(self):
        return f"Soy {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"
    
    @abstractmethod
    def saludar(self):
        pass

class Teacher(SchoolMember):
    def saludar(self):
        return f"Buenos dias me llamo: {self.name}"

class Student(SchoolMember):
    def saludar(self):
        return f"Buenos dias me llamo: {self.name}"

class Visitor(SchoolMember):
    def saludar(self):
        return f"Buenos dias me llamo: {self.name}"    

class SchoolMemberFactory:
    @classmethod
    def make(cls, kind, **kwargs):
       
        # valida el tamaño del ID
        if len(kwargs.get("id_num", "XXXXXX")) != 6:
            return "Error! El tamaño del ID debe ser de 6 caracteres"
       
        #validar que edad sea numero
        if isinstance(kwargs.get('age', -1),int) == False:
            return "Error! la Edad debe ser numero"
            
        # valida que el kind sea correcto
        tipos = [tipo.__name__.capitalize() for tipo in SchoolMember.__subclasses__()] #crea una lista con los nombres de las subclases para compararla con el   
        if kind.capitalize() not in tipos:                                             # input del usuario
             return f"[Error]: '{kind}' invalid kind"
        return eval(kind.capitalize())(**kwargs)
        
def main():
    kind = input("Qué quieres crear?\n")
    _name = input("Qué nombre tiene?\n")
    obj = SchoolMemberFactory.make(kind, name = _name, age = 22, id = '01P3')
    print(obj)
    
if __name__ == "__main__":
    main()