from abc import ABC, abstractmethod

class SchoolMember(ABC):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.age = kwargs.get('age', -1)
        self.id_num = kwargs.get('id', 'XXXXXX')
    
    def __str__(self):
        return f"Soy el {type(self).__name__} {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"

    @abstractmethod
    def funcion_de(self):
        """ Returnea la funcion del puesto"""
        return f"Funcion de {type(self).__name__}: \n"

##################
class Teacher(SchoolMember):

    def funcion_de(self):
        super().funcion_de()
        return "Persona que ayuda a los estudiantes a adquirir conocimientos"

##################
class Janitor(SchoolMember):

    def funcion_de(self):
        super().funcion_de()
        return "Persona empleada como cuidador del edificio de la escuela; limpia y mantiene los edificios"

###################
class Student(SchoolMember):

    def funcion_de(self):
        super().funcion_de()
        return "Persona inscrita en una escuela con el objetivo de adquirir conocimientos"

###################
class SchoolMemberFactory:
    @classmethod
    def make(cls, kind, **kwargs):
        clases = [cls.__name__ for cls in SchoolMember.__subclasses__()]

        if kind.capitalize() not in clases:
            raise ValueError("Error! tipo invalido!")

        return eval(kind.capitalize())(**kwargs)


#######
#######
def main():
    kind = input("Qué quieres crear?\n")
    _name = input("Qué nombre tiene?\n")
    obj = SchoolMemberFactory.make(kind, name=_name, age=22, id='070KGP')
    print(obj)
    print(obj.funcion_de())
    
if __name__ == "__main__":
    main()