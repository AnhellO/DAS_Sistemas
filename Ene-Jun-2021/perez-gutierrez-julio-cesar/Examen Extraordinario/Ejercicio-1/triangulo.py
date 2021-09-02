class Triangulo():
    def __init__(self, angulo1, angulo2, angulo3, lado1, lado2, lado3):
        self.angulo1 = angulo1
        self.angulo2 = angulo2
        self.angulo3 = angulo3
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.num_de_lados = 3
    
    def __str__(self):
        return f"Angulo 1 = {self.angulo1}\nAngulo 2 = {self.angulo2}\n" \
                f"Angulo 3 = {self.angulo3}\nLado 1 = {self.lado1}\n" \
                f"Lado 2 = {self.lado2}\nLado 3 = {self.lado3}"
    
    def verificar_angulos(self):
        return self.angulo1 + self.angulo2 + self.angulo3 == 180

if __name__ == '__main__':
###########################_angulos_#_lados_####################
    mi_triangulo = Triangulo(90, 30, 60 , 50, 50, 50)
    print(mi_triangulo)
    print(mi_triangulo.verificar_angulos())