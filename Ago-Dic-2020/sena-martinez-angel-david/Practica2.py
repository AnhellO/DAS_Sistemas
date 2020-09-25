class Persona():
    def __init__(self, edad, peso, altura):
        self.edad = edad
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return f"Edad: {self.edad} años\nPeso:{self.peso}\nAltura:{self.altura}m"
    
    def pesoideal(self):
        self.peso_ideal = 0.75 * (self.altura * 100) - 62.5
        return f"El peso ideal de esta persona es de: {self.peso_ideal} kg"
    
    def imc(self):
        self.imc = self.peso / (self.altura * self.altura)
        return f"El Indice de Masa Corporal de esta persona es de: {self.imc}"

class Estudiante(Persona):
    
    def __init__(self, edad, peso, altura, nombre):
        Persona.__init__(self,edad, peso, altura)
        self.nombre=nombre

    def descripcion(self):
        return f"{self.nombre} tiene {self.edad} años, su peso es de {self.peso} y su altura es de: {self.altura} m."
   
    def hijos(self,sons):
        return f"{self.nombre} tiene {sons} hijos"
    
    

if __name__ == "__main__":
    student = Estudiante(25, 90, 1.80, "David")
    print(student)
    print(student.descripcion())
    print(student.pesoideal())
    print(student.imc())
    print(student.hijos(4))