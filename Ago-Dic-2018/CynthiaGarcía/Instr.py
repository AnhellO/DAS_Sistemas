from abc import ABC, abstractmethod

class Instrumento:

    def __init__(self, marca, color, material):
        self.marca = marca
        self.color = color
        self.material = material

    @abstractmethod
    def afinar_guitarra(self):
        pass

    @abstractmethod
    def stock_instrumento(self):
        pass


class Guitarra(Instrumento):

    def __init__(self, marca, color, material, numcuerdas='', distorcionador='', ajustevol=''):
        self.marca=marca
        self.color=color
        self.material=material
        self.numcuerdas=numcuerdas
        self.distorcionador=distorcionador
        self.ajustevol=ajustevol
        
    def get_material(self):
        return self.material

    def afinar_guitarra(self):
        print('Se esta afinando la guitarra')

    def stock_instrumento(self):
        pregunta=input('En que pais vives?')
        if pregunta == ('Mexico'):
           print('Existente!!') 

    #print('Esta existente el instrumento: {}\nmarca: {}\ncolor: {}\nmaterial: {}\nnumero de cuerdas: {}'.format(self.marca, self.color, self.material, self.numcuerdas))

class Bateria(Instrumento):
    def __init__(self, marca, color, material, tamaño='', numpiezas='', platillos='', pedal=''):
        self.marca=marca
        self.color=color
        self.material=material
        self.tamaño = tamaño
        self.numpiezas=numpiezas
        self.platillos=platillos
        self.pedal=pedal

    def sucursal_bateria(self):
        input('si desea consultar teclea s')
        print("la encuentras en sucursal Centro!")

    def compra_bateria(self):
        pregunta=input('Si desea comprar escriba Si?')
        if pregunta == ('Si'):
           print('www.BateriasatodoMexico.com')


if __name__ == '__main__':     
    Guitarra = Guitarra('Yamaha','guindo', 'metal', 6, 'Si', 'No' )
    Guitarra.afinar_guitarra()
    Guitarra.stock_instrumento()

    Bateria = Bateria('Yamaha', 'negro', 'metal', 'Infantil', 8, 2, 2)
    Bateria.sucursal_bateria()
    Bateria.compra_bateria()
  