class Animal():
    def __init__(self, edad, tamaño, peso, altura):
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return f"Edad: {self.edad} años\nTamaño: {self.tamaño}\nPeso: {self.peso}kg\nAltura: {self.altura}cm"
    
    def imc(self):
        self.imc = self.peso/self.altura
        return f"El IMC de este animal con un peso de {self.peso} y una altura de {self.altura} es: {self.imc}"

class Perro(Animal):
    def __init__(self, edad, tamaño, peso, altura, nombre):
        super().__init__(edad,tamaño,peso,altura)
        self.nombre = nombre

    def descripcion(self):
        return f"{self.nombre} tiene {self.edad} años, su tamaño es {self.tamaño}, su peso es {self.peso} kg y su altura es de {self.altura} cm."
   
    def hablar(self, sonido):
        return f"{self.nombre} dice {sonido}"
    
    def truco(self, trucazo):
        return f"{self.nombre} {trucazo}"


if __name__ == "__main__":
    firulais = Perro(5,"Medio", 35, 1.2, "Firulais")
    print(firulais)
    print(firulais.descripcion())
    print(firulais.hablar("Woof"))
    print(firulais.truco("hace un triple mortal invertido"))
    print(firulais.imc())

    
