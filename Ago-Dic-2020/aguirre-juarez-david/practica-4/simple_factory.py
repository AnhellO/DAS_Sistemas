from abc import ABC
from abc import abstractmethod
import sys

class SchoolMember(ABC):
	def __init__(self, **args):
		self.name = args.get('name', '')
		self.age = args.get('age', -1)
		self.id_num = args.get('id_num', 'XXXXXX')

	def __str__(self):
		return f"Me llamo {self.name}!, soy {self.get_type_name()}, tengo {self.age} años y mi ID = {self.id_num}"

	@abstractmethod
	def get_type_name(self):
		pass

class Teacher(SchoolMember):
	def get_type_name(self):
		return "Maestro"

class Student(SchoolMember):
	def get_type_name(self):
		return "Estudiante"

class Secretary(SchoolMember):
	def get_type_name(self):
		return "Secretario"

class SchoolMemberFactory:
	@classmethod
	def make(cls, kind, **args):
		cmodule = sys.modules[__name__]

		# capitalize if don't start with capital letter
		if len(kind) > 1 and not (kind[0].isupper() and kind[1].islower()):
			kind = kind.capitalize()

		# checks the length of the ID
		if len(args.get("id_num", "XXXXXX")) != 6:
			return "Error! formato de ID invalido!"

		# checks if the kind is a valid type
		if not (hasattr(cmodule, kind) and SchoolMember in getattr(cmodule, kind).__bases__):
			return f"Error! tipo '{kind}' invalido!"

		return eval(kind)(**args)


def main():
	kind = input("Qué quieres crear?\n")
	_name = input("Qué nombre tiene?\n")
	obj = SchoolMemberFactory.make(kind, name=_name, age=22, id_num='070KGP')
	print(obj)

if __name__ == "__main__":
	main()