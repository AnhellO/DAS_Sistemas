import abc
#abc (Abstract Base Classes)
#metaclase Es una clase cuyas instancias son las clases
#en pocas palabras: como los objetos son instancias de una clase
#las clases son instancias de una metaclase.

#Banco es la interface/super clase
class Banco(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sueldob(self, cantidad):
        pass

#Salario es la hoja
class Salario(Banco):

    def __init__(self,sueldo):
        self.sueldo = sueldo
    def sueldob(self, cantidad): 
        return self.sueldo

#Sueldo es donde se aplica el Composite
class Sueldo(Banco):
    def __init__(self):
        self.bancos = []

    def sueldob(self, cantidad):
        self.sueldodept = 0
        for sh in self.bancos:
            self.sueldodept = self.sueldodept + sh.sueldob(cantidad)
        return self.sueldodept

    def add(self, sh):
        self.bancos.append(sh)

    #def remove(self, sh):
        #self.bancos.remove(sh)

    def clear(self):
        print("Nomina final en $ pesos mexicanos ")
        self.bancos = []

if __name__ == '__main__':
    empl1 = Salario(1500)
    empl2 = Salario(1200)
    
   
    sueldox = Sueldo()
    sueldox.add(empl1)
    sueldox.add(empl2)
   

    empl3 = Salario(1000)
    sueldoxB = Sueldo()
    sueldoxB.add(empl3)

    sueldox.add(sueldoxB);

    x = sueldox.sueldob("")
    print (x)

    sueldox.clear()

    sueldox.add(empl1)