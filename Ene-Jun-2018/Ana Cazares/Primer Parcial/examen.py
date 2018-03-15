import abc

class Padre(metaclass=abc.ABCMeta)#de aqui heredo
@abc.abstractmethod
    def draw(self, documento):
        pass

class etc(Padre):
    def draw(self, documento):
        print("/etc" + documento)

class var(Padre):
    def draw(self, documento):
        print("/var"+documento)

class bin(Padre):
    def draw(self, documento):
        print("/bin"+ documento)

class usr(Padre):
    def draw(self, documento)
    print("/usr"+ documento)

class home(Padre):
    def draw (self, documento)
    print("/home"+ documento)

class log(var):
    def draw(self, documento)
    print("/log"+documento)

class mail(var):
    def draw(self, documento)
    print("/mail"+ documento)

class lib(usr):
    def draw(self, documento)
    print("/lib"+ documento)

class include(usr):
    def draw(self, documento)
    print("/include"+documento)

class local(usr):
    def draw (self, documento)
    print("/local"+documento)

class users(home):
    def draw(self, documento)
    print("/users"+documento)

class Drawing(Padre):
    def _init_(self)
    self.Padre=[]

    def draw(self, documento):
        for pa in self.Padre:
            pa.draw(documento)

    def add(self, pa):
        self.Padre.append(pa)

    def remove(self, pa):
        self.Padre.remove(pa)

    def clear(self):
        print("clearong all the Padre from drawing")
        self.Padre=[]

    if_name_=='_main_':
        hijo1=mail()
        hijo2=lib()
        
        drawing=Drawing()
        drawing.add(hijo1)
        drawing.add(hijo2)

        drawing.draw("herede de padre")
        drawing.clear()

        drawing.add(hijo1)
        drawing.add(hijo2)
        drawing.draw("herede de usr")
        
        

    
