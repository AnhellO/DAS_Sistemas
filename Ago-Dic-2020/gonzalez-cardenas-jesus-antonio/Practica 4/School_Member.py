from abc import ABC, abstractclassmethod, abstractmethod
import sys

class school_member:
    def __init__(self, **args):
        self.name = args.get('name', '')
        self.age = args.get('age', -1)
        self.id_num = args.get('id', '')

    @abstractmethod
    def member_info(self):
        pass

class Teacher(school_member):
    def member_info(self):
        return f"Soy el profesor {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"


class Student(school_member):
    def member_info(self):
        return f"Soy el alumno {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"

class Personel(school_member):
    def member_info(self):
        return f"Soy el miembro del personal {self.name}!, tengo {self.age} años y mi ID = {self.id_num}"

class school_member_factory:
    @classmethod
    def make(cls, kind, **args):
        # return eval(kind.capitalize())(**args)
        if kind != kind.capitalize():
            raise ValueError("No existe ese tipo, verifique su entrada")
        if args.get('age') <0:
            raise ValueError("Edad negativa")
        #Formato de id? XXXXXX 6 caracteres (?)
        if int(len(args.get('id'))) != 6 :
           raise ValueError("Formato incorrecto de ID")
        return eval(kind.capitalize())(**args)
        
        

def main():
    kind = input("Qué quieres crear?\n")
    _name = input("Qué nombre tiene?\n")
    edad = input("¿Qué edad tiene?\n")
    idd = input("Id del individuo\n") 
    obj = school_member_factory.make(kind, name=_name, age=int(edad), id=idd)
    print(obj.member_info())
    
if __name__ == "__main__":
    main()