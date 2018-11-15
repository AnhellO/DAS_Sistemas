class Instrumento_Musical:
    def __init__(self, nombre='', clasificacion='', marca=''):
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca

    def setNombre(self, valor):
        self.nombre = valor

    def setClasificacion(self, valor):
        self.clasificacion = valor

    def setMarca(self, valor):
        self.marca = valor

    def getNombre(self):
        return self.nombre

    def getClasificacion(self):
        return self.clasificacion

    def getMarca(self):
        return self.marca

    def tocar(self):
        print("Tocando musica")

    def presentacion(self):
        print("Hola, soy un Instrumento Musical")

    def __str__(self):
        return 'Nombre: {} \nClasificacion: {} \nMarca: {}'.format(self.nombre, self.clasificacion, self.marca)

class Guitarra(Instrumento_Musical):
    def __init__(self, nombre='', clasificacion='', marca='',  color='', origen='', numcuerdas=''):
        Instrumento_Musical.__init__(self, nombre, clasificacion, marca)
        self.color = color
        self.origen = origen
        self.numcuerdas = numcuerdas

    def setColor(valor):
        self.color = valor

    def setOrigen(valor):
        self.origen = valor

    def setNumcuerdas(valor):
        self.numcuerdas = valor

    def getColor():
        return self.color

    def getOrigen():
        return self.origen

    def getNumcuerdas():
        return self.numcuerdas

    def decorar():
        print("Se agregó una estampa")

    def cambiarCuerdas():
        print("Se cambió una cuerda")

    def __str__(self):
        return 'Nombre: {} \nClasificacion: {} \nMarca: {} \nColor: {} \nOrigen: {} \nNumero de cuerdas: {}'.format(self.nombre, self.clasificacion, self.marca, self.color, self.origen, self.numcuerdas)

class Bateria(Instrumento_Musical):
    def __init__(self, nombre='', clasificacion='', marca='', color='', desarmada='', numpiezas=''):
        Instrumento_Musical.__init__(self, nombre, clasificacion, marca)
        self.color = color
        self.desarmada = desarmada
        self.numpiezas = numpiezas

    def setColor(valor):
        self.color = valor

    def setDesarmada(valor):
        self.desarmada = valor

    def setNumpiezas(valor):
        self.numpiezas = valor

    def getColor():
        return self.color

    def getDesarmada():
        return self.desarmada

    def getNumPiezas():
        return self.numpiezas

    def armarse(self):
        print("Se está armando la bateria")

    def cambiarPieza(self):
        print("Se cambió una pieza")

    def __str__(self):
        return 'Nombre: {} \nClasificacion: {} \nMarca: {} \nColor: {} \nDesarmada: {} \nNumero de piezas: {}'.format(self.nombre, self.clasificacion, self.marca, self.color, self.desarmada, self.numpiezas)

class main():
    instrumento1= Instrumento_Musical('Violin', 'Cuerdas', 'Fender')
    print(instrumento1, instrumento1.presentacion())

    print ("")

    instrumento2 = Instrumento_Musical('Saxofon', 'Viento', 'Fender')
    print(instrumento2, instrumento2.tocar())

    print ("")

    guitarra = Instrumento_Musical('Guitarra', 'Cuerdas', 'Gibson')
    print(guitarra)

    guitarra2 = Instrumento_Musical(Guitarra('Guitarra', 'Cuerdas', 'Gibson', 'Negra', 'Europeo', '5'))
    print(guitarra2)

    bateria = Instrumento_Musical(Bateria('Bateria', 'Percusion', 'DW', 'Verde', 'Desarmada', '8'))
    print(bateria)
