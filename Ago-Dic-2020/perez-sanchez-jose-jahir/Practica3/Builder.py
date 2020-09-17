class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder=builder
    
    def getMoto(self):
        moto = Moto()

        cuerpo = self.__builder.getCuerpo()
        moto.setCuerpo(cuerpo)

        motor = self.__builder.getMotor()
        moto.setMotor(motor)

        i = 0
        while i < 2:
            llanta = self.__builder.getLLanta()
            moto.setLLanta(llanta)
            i +=1

        return moto

class Moto:
    def __init__(self):
        self.__llantas = list()
        self.__motor = None
        self.__cuerpo = None
    
    def setCuerpo(self, cuerpo):
        self.__cuerpo = cuerpo
    
    def setLLanta(self, llanta):
        self.__llantas.append(llanta)

    def setMotor(self, motor):
        self.__motor = motor
    
    def especificaciones(self):
        print(f"cuerpo: {self.__cuerpo.tipo}")
        print(f"caballos de fuerza del motor: {self.__motor.caballos}")
        print(f"Tamaño de llanta: {self.__llantas[0].tamaño}")

class Builder:

    def getLLanta(self): pass
    def getMotor(self): pass
    def getCuerpo(self): pass


class ItalikaBuilder(Builder):
    def getLLanta(self):
        llanta = Llanta()
        llanta.tamaño = 15
        return llanta
    
    def getMotor(self):
        motor = Motor()
        motor.caballos = 250
        return motor   

    def getCuerpo(self):
        cuerpo = Cuerpo()
        cuerpo.tipo = "C90"
        return cuerpo


class Llanta:
    tamaño = None

class Motor:
    caballos = None

class Cuerpo:
    tipo = None

def Italika(string): 
    italikaBuilder = ItalikaBuilder()
    director = Director()
    print("Italika")
    director.setBuilder(italikaBuilder)
    italika = director.getMoto()
    italika.especificaciones()

def main():
    name = input("Dame la marca: ")
    if name == "Italika":
        print(Italika(name))


if __name__ == "__main__":
    main()


    

