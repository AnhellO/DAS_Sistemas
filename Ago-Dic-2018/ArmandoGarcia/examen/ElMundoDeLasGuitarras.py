class InstrumentoMusical(object):
    def __init__(self,tipo,sonido,color):
        self.tipo = tipo
        self.sonido = sonido
        self.color = color

    def Get_tipo(self):
        return self.tipo
    def Get_sonio(self):
        return self.sonido
    def Get_color(self):
        return self.color
    def set_tipo(self,n):
        self.tipo = n
    def set_sonido(self,n):
        self.sonido = n
    def set_color(self,):
        self.color = n
    def __str__(self):
        return " %s: %s, %s" % (str(self.tipo), self.sonido, self.color)

class Guitarra(InstrumentoMusical):
    def __init__(self,tipo,sonido,color,cuerdas,tama,rango):
        InstrumentoMusical.__init__(self,tipo,sonido,color)
        self.cuerdas = cuerdas
        self.tama = tama
        self.rango= rango

    def set_cuerdas(self,d):
        self.cuerdas = d
    def set_tam(self,d):
        self.tama = d
    def sert_rango(self,d):
        self.rango = d
    def Get_cuerdas(self,d):
        self.cuerdas = cuerdas
    def Get_tam(self):
        self.tama = tama
    def GEt_rango(self):
        self.rango =rango
    def Cancion1(self):
        print("Vamos a reunirnos y cantar nuestra cancion la C A N C I O N de la hogera y si quieres intentemos cantarla a la carrera")
    def Promocion(sefl):
        print("Visitenos en nuestra tienda para adquirir mas instrumentos")
    def __str__(self):
        return 'Tipo: {} \nsonido: {} \ncolor:{} \ncuerdas: {} \ntamaño: {}  \nRango: {}'.format(self.tipo, self.sonido, self.color,self.cuerdas,self.tama,self.rango)


class Bateria(InstrumentoMusical):
    def __init__(self,tipo,sonido,color,num_platillos,num_tambores,num_pedales):
        InstrumentoMusical.__init__(self,tipo,sonido,color)
        self.num_platillos = num_platillos
        self.num_tambores =num_tambores
        self.num_pedales = num_pedales


    def set_platillos(self,d):
        self.num_platillos = d

    def set_tambores(self,d):
        self.num_tambores = d
    def set_pedales(self,d):
        self.num_pedales = d

    def Get_platilos(self):
        self.num_platillos = num_platillos
    def Get_tambores(self):
        self.num_tambores = num_tambores
    def Get_pedales(self):
        self.num_tambores = tambores
    def matilda(self):
        print("mmmm mmm mmmtt mmm mmm mmm mm mmm")
    def matilda2(self):
        print("imaginese la tonada por favor")
    def __str__(self):
        return 'Tipo: {} \nsonido: {} \ncolor:{} \nNumero de platillos: {} \nNumero de tambores: {}  \nNumero de pedales: {}'.format(self.tipo, self.sonido, self.color,self.num_platillos,self.num_tambores,self.num_pedales)


if __name__ == '__main__':
    guitarra1=Guitarra("electrica","fuerte","Blanco","6","mediano","alto")
    guitarra2=Guitarra("acustica","bajo","negro","7","grande","bajo")
    guitarra3=Guitarra("normal","bajo","azul","6","pequeña","medio")
    guitarra4=Guitarra("normal","alto","verde","3","grande","medio")
    guitarra5=Guitarra("normal","bajo","cafe","5","grande","mediano")
    print(guitarra1)
    print(guitarra2)
    print(guitarra3)
    print(guitarra4)
    print(guitarra5)
    bateria1=Bateria("normal","fuerte","azul","2","5","2")
    bateria2=Bateria("normal","fuerte","negro","2","9","2")
    bateria3=Bateria("normal","fuerte","verde","2","8","2")
    bateria4=Bateria("normal","fuerte","rojo","2","7","2")
    bateria5=Bateria("normal","fuerte","blanco","2","6","2")
    print(bateria1)
    print(bateria2)
    print(bateria3)
    print(bateria4)
    print(bateria5)
