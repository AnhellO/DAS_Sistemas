class agencia:
    
    def __init__(self,vendedores,clientes, num_vehiculos):
        self.vendedores = vendedores
        self.clientes = clientes
        self.num_vehiculos = num_vehiculos
    def comprar(self,compras):
        
            print('las compras fueron:',compras)
    def vender(self,vendedores):
        
            print('hay:',vendedores,'vendedores en esta sucursal')
    def existencia(self, num_vehiculos):
        
        print('numero de vehiculos:',num_vehiculos)




class vehiculo(agencia):
    def __init__(self,modelo, marca, color, combustible):
        self.modelo=modelo
        self.marca=marca
        self.color=color
        self.combustible=combustible
        
    def Tipo(self,combustible):
        if combustible <= 30:
            print('es una moto')
        elif combustible <= 50 and combustible > 30:
        
            print('es un automovil de (pequeno)')
        elif combustible <= 70 and combustible > 50:
            print('es un automovil(grande)')

        elif combustible > 70:
            print('es un camion')

    def info(self):
        print ('modelo->', modelo)
        print ('marca->', marca)
        print ('color->', color)


class camion(vehiculo):
    def __init__(self, modelo, marca, color):
        self.modelo=modelo
        self.marca=marca
        self.color=color
    def marca1(self, marca):
        print('la marca del camion es:',marca)
        

class automovil(vehiculo):
    def __init__(self, modelo, marca, color):
        self.modelo=modelo
        self.marca=marca
        self.color=color
    def modelo1(self, modelo):
        print('la modelo del auto es: ',modelo)

class motocicleta(vehiculo):
    def __init__(self, modelo, marca, color):
        self.modelo=modelo
        self.marca=marca
        self.color=color

    def color1(self, color):
        print('el color de la moto es:',color)
    
#ingresar datos
print('DATOS DE LA AGENCIA')
vendedores=int(input('numero de vendedores:'))
clientes=int(input('numero de clientes:'))
num_vehiculos=int(input('numero de vehiculos:'))
compras=int(input('numero de compras:'))

print('DATOS DEl AUTOMOVIL')
modelo=input('modelo:')
marca=input('marca:')
color=input('color:')
combustible=float(input('combustible en litros:'))
#crear objetos
obj=agencia(vendedores,clientes,num_vehiculos)
objec= vehiculo(modelo,marca,color,combustible)
camion=camion(modelo, marca, color)
automovil=automovil(modelo,marca,color)
motocicleta=motocicleta(modelo,marca,color)


obj.comprar(compras)
obj.vender(vendedores)
obj.existencia(num_vehiculos)

objec.Tipo(combustible)
objec.info()
print('\n')

objec.vender(vendedores)
obj.existencia(num_vehiculos)

camion.marca1(marca)
automovil.modelo1(modelo)
motocicleta.color1(color)

