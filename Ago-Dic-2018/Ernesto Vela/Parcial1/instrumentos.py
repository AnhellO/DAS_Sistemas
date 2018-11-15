class Instrumentos_Musicales():
    def __init__(self, nombre, color):
        self.marca = marca
        self.tipo = tipo

    def setMarca(marca):
        self.marca = marca

    def getMarca():
        return self.marca

    def setTipo(tipo):
        self.tipo = tipo

    def getTipo():
        return self.tipo

class Guitarra(Instrumentos_Musicales):
    def __init__(self, marca, tipo, peso, color, patrocinador):
        self.marca = marca
        self.tipo = tipo
        self.peso = peso
        self.color = color
        self.patrocinador = patrocinador

    def setPeso(self, peso):
        self.peso = peso

    def getPeso(self):
        return self.peso

    def setColor(self, col):
        self.color = col

    def getColor(self):
        return self.color

    def setPatrocinador(self, pat):
        self.patrocinador = pat

    def getPatrocinador(self):
        return self.patrocinador

    def romperGuitarra(self):
        print ("La guitarra {} fue rota!".format(self.marca))

    def girarGuitarra(self):
        print("La guitarra {} hizo un giro!".format(self.marca))

    def __str__(self):
        return "Marca: {} \nTipo: {} \nPeso: {} \nColor: {} \nPatrocinador: {}".format(self.marca, self.tipo, self.peso, self.color, self.patrocinador)

class Bateria(Instrumentos_Musicales):
    def __init__(self, marca, tipo, tamano, numdiscos, numpedales):
        self.marca = marca
        self.tipo = tipo
        self.tamano = tamano
        self.numdiscos = numdiscos
        self.numpedales = numpedales

    def setTamano(self, tam):
        self.tamano = tam

    def getTamano(self):
        return self.tamano

    def setNumDiscos(self, disc):
        self.numdiscos = disc

    def getNumDiscos(self):
        return self.numdiscos

    def setNumPedales(self, ped):
        self.numpedales = ped

    def getNumPedales(self):
        return self.numpedales

    def lanzarBaquetas(self):
        print ("Las baquetas de la bateria {} estan en el aire".format(self.marca))

    def RedobleEpico(self):
        print("La bateria {} se rifo un redoble epico!".format(self.marca))
#Sobreescribir _str_
    def __str__(self):
        return "Marca: {} \nTipo: {} \nTamano: {} \nNumero de discos: {} \nNumero de Pedales: {}".format(self.marca, self.tipo, self.tamano, self.numdiscos, self.numpedales)

if __name__ == "__main__":
    guitarra = Guitarra("Gibson", "Electrica", "Pesada", "Maple", "Slash")
    bateria = Bateria("Pearl Road Show", "Clasica", "Grande", 6, 2)
    print(guitarra)
    print()
    print(bateria)
    print()
    bateria.lanzarBaquetas()
    print()
    guitarra.girarGuitarra()
    print()
    bateria.RedobleEpico()
    print()
    guitarra.romperGuitarra()
