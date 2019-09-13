class Instrument_music:
    def __init__(self, color, precio, tamaño):
        self.color = color
        self.precio = precio
        self.tamaño = tamaño


    def material():
        pass


    def genero():
        pass

class Guitarra(Instrument_music): 
    def __init__(self, color, precio, tamaño, Cuerdas, modelo, peso):
        super().__init__(color, precio, tamaño) 
        self.Cuerdas = Cuerdas
        self.modelo = modelo
        self.peso = peso 

    def cuerdas(): 
        return self.cuerda

    def afinacion():
        pass

    def imprimir(self):
        print('Color: {} \nPrecio: {} \nTamaño: {}  \nCuerdas: {} \nmodelo: {} \npeso: {}'.format(self.color, self.precio, self.tamaño, self.Cuerdas, self.modelo, self.peso))

print('\n')

class Bateria(Instrument_music): 
    def __init__(self, color, precio, tamaño, Tambores, discos, peso):
        super().__init__(color, precio, tamaño)
        self.Tambores = Tambores
        self.discos = discos
        self.peso = peso

    def tambores():
        return self.Tambores

    def discos():
        return self.Discos

    def imprimir(self):
        print('\nColor: {} \nPrecio: {} \nTamaño: {} \ntambores: {} \ndiscos: {} \npeso: {}'.format(self.color, self.precio, self.tamaño, self.Tambores, self.discos, self.peso))

if __name__ == '__main__':
    guitarra = Guitarra('rojo','10,000','4/4','regular slinky','Stratocaster','1.750 Kg')
    guitarra.imprimir()
    bateria = Bateria('Blanco','10,000','14x5','4','2','75kg')
    bateria.imprimir()
