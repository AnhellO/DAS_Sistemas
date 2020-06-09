#Ejercicio2
 #clase persona con cinco atributos, dos de ellos peso,estatura, obtener indice de peso (IMC)
 #nombre,edad,sexo,peso,estatura

class persona:
    def __init__(self,nombre,edad,sexo,peso,estatura):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.peso=peso
        self.estatura=estatura

    def set_nombre(args):
        self.nombre=args
    def get_nombre():
        return self.nombre 
    
    def set_edad(args):
        self.edad=args    
    def get_edad():
        return self.edad 
    
    def set_sexo(args):
        self.sexo=args
    def get_sexo():
        return self.sexo
    
    def set_peso(args):
        self.peso(args)
    def get_peso():
        return self.peso

    def set_estatura(args):
        self.estatura=args
    def get_estatura():
        return self.estatura
       
    def IMC(self):
        print('EL IMC ES')
        IMC=self.peso/(self.estatura)**2 
        return IMC
    def __str__(self):
		return f'Nombre: {self.nombre}\nEdad: {self.edad}\nSexo: {self.sexo}\nPeso:{self.peso}\nEstatura{self.estatura}'
    
persona1=persona("Emilio",21,"Hombre",81,1.82)
print(persona1)
print(persona1.IMC())



