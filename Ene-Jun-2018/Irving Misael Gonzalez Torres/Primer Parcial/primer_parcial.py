import abc

class Root(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def print(self ):
        pass
############################################################################
class Folder_Etc(Root):
  
    def print(self ):
    	print("/etc")

class Folder_Var(Root):

    def print(self ):
    	print("/var")

class Folder_bin(Root):

    def print(self ):
    	print("/bin")

class Folder_usr(Root):

    def print(self):
    	print("/usr")

class Folder_home(Root):

    def print(self):
    	print("/home")
###################################################################

class composite_Folder(Root):
    def init(self):
        self.roots = []

    def print(self):
        for ru in self.roots:
            ru.ruta(roots)

    def add(self, ru):
        self.roots.append(ru)


def main():
	h1 = Folder_Etc()
   	h2 = Folder_Var()
   

   	folder = composite_Folder()
   	folder.add(h1)
   	folder.add(h2)

   	Folder.print("hereda de:")


if __name__ == "__main__":
    main()


