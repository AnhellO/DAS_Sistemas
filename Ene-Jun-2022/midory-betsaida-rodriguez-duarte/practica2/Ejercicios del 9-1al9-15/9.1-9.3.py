#9.1
class Restaurante():

    def __init__(self, nombreRes, tipoCoci):
        self.nombreRes = nombreRes
        self.tipiCoci = tipoCoci

    
    def describe_restaurante(self):
        print("El nombre del res es" + self.nombreRes + "y su tipo es " + self.tipiCoci)

    def abierto():
        print("El restaurante es abierto")



#9.2
res = Restaurante("Toscana", "Comida italiana")# objeto 1
print(res.nombreRes)
res.describe_restaurante()
res.abierto

res1= Restaurante("compadres", "Comida mexicana")# objeto 2
res.describe_restaurante()
res.abierto

res2= Restaurante("Escolleas", "Comida de mariscos")#objeto 3
res.describe_restaurante()
res.abierto



#9.3

class Usuario():

    def __init__(self, nombre, segundoNom, edad):
        self.nombre = nombre
        self.segundoNom = segundoNom
        self.edad = edad

    def desc_usuario(self):
        print(self.nombre, self.segundoNom, self.edad)

    def saludo(self):
        print("Hola cuidate del covid " + self.nombre)

usu = Usuario("julio", "cesar", 24)
usu.saludo()
usu.desc_usuario()


    







        

