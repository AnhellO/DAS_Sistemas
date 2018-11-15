class InstrumentosMusicales():
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def setNombre(nom):
        self.nombre = nom

    def getNombre():
        return self.nombre

    def setColor(col):
        self.color = col

    def getColor():
        return self.color

class Guitarra(InstrumentosMusicales):
    def __init__(self, nombre, color, tipo, material, tamaño):
        self.nombre = nombre
        self.color = color
        self.tipo = tipo
        self.material = material
        self.tamaño = tamaño

#Nuevas funciones de clase
    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def setMaterial(self, mat):
        self.material = mat

    def getMaterial(self):
        return self.material

    def setTamaño(self, tam):
        self.tamaño = tam

    def getTamaño(self):
        return self.tamaño

    def TocarNota(self,nota):
        print ("{} Tocó un: {} !!! :O".format(self.nombre, nota))

    def rockear(self):
        print("{} está rockeando sin control!! O.o".format(self.nombre))
#Sobreescribir __str__
    def __str__(self):
        return "Nombre: {} \nColor: {} \nTipo: {} \nMaterial: {} \nTamaño: {}".format(self.nombre, self.color, self.tipo, self.material, self.tamaño)

class Bateria(InstrumentosMusicales):
    def __init__(self, nombre, color, numeroplatos, marca, numerobombos):
        self.nombre = nombre
        self.color = color
        self.numeroplatos = numeroplatos
        self.marca = marca
        self.numerobombos = numerobombos

#Nuevas funciones de clase
    def setNumeroPlatos(self, num):
        self.numeroplatos = num

    def getNumeroPlatos(self):
        return self.numeroplatos

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setNumeroBombos(self, numerobombos):
        self.numerobombos = numerobombos

    def getNumeroBombos(self):
        return self.numerobombos

    def solo(self):
        print ("{} Tocó un solo de batería como un Dios !!! :O".format(self.nombre))

    def cambiarRitmo(self, ritmo):
        print("{} cambió a un ritmo de {}!! O.o".format(self.nombre, ritmo))
#Sobreescribir __str__
    def __str__(self):
        return "Nombre: {} \nColor: {} \nNumero de Platos: {} \nMarca: {} \nNumero de Bombos: {}".format(self.nombre, self.color, self.numeroplatos, self.marca, self.numerobombos)

if __name__ == "__main__":
    guitarra = Guitarra("Guitarrón", "Roja", "Electrica", "Metal", "Grande")
    guitarra2 = Guitarra("La mejor guitarrita", "Azul", "Acústica", "Madera", "Mediana")
    bateria = Bateria("La Bate", "Negra", 5, "Yamaha", 2)
    print("La Banda va a empezar a tocar una gran canción!!")
    print("Integrantes!!:")
    print(guitarra)
    print("=============================================================")
    print(bateria)
    print("=============================================================")
    print(guitarra2)
    print("=============================================================")
    guitarra.setTipo("Perrona")
    print(guitarra)
    print("=============================================================")
    guitarra.TocarNota("Fa")
    guitarra2.TocarNota("Fa")
    guitarra.rockear()
    bateria.solo()
    guitarra.TocarNota("Sol")
    bateria.cambiarRitmo("Jazz")
    guitarra.TocarNota("Mi")
    guitarra2.TocarNota("Re")
    guitarra.rockear()
    guitarra.TocarNota("Fa")
    bateria.solo()
    print("Fin de la canción, aplausos!!!")
