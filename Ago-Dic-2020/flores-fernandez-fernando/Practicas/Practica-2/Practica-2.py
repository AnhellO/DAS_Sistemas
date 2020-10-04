class Dunedain:
    def __init__(self,nombre,ocupacion,hp,sp):
        self.nombre = nombre
        self.ocupacion = ocupacion
        self.hp = hp
        self.vivo = True
        self.sp = sp
    
    def saludar(self):
        print (f"Mae govannen mi nombre es: {self.nombre}")
    
    def comer(self,comida):
        subhp = self.hp + comida
        print(f"Al comer tus HealtPoints subieron de: {str(self.hp)} A: {str(subhp)}")
        self.hp = subhp 
    
    def cambiar_ocupacion(self,ocupacion):
        ocupacionco = self.ocupacion
        self.ocupacion = ocupacion 
        print(f"Tu Ocupacion cambió de: {ocupacionco} A: {self.ocupacion}")
    
    def status(self):
        print(f"Nombre: {self.nombre}\nOcupacion: {self.ocupacion}\nHealt Points: {str(self.hp)}\nStrike Points: {str(self.sp)}\nVivo: {str(self.vivo)}")
    
              
              
class Ranger(Dunedain):
    def __init__(self,nombre,ocupacion,hp,sp):
        self.nombre = nombre
        self.ocupacion = ocupacion
        self.hp = hp
        self.vivo = True 
        self.sp = sp
    
    def atacar(self):
        print(f"{self.nombre} Dio una estocada que infligio: {str(self.sp)} puntos de daño")
    
    def recibir_daño(self,sp):
        if self.hp <= sp:
            print(f"{self.nombre} Recibió: {str(sp)} Puntos de daño\n{self.nombre} A muerto")
            self.vivo=False
            self.hp = 0
        else:
            print(f"{self.nombre} Recibió: {str(sp)} Puntos de daño")
            self.hp -= sp
        
              
d1 = Dunedain("Nan","Herrero",50,20)

r1 = Ranger("Fer","Ranger",50,30)

d1.saludar()
r1.atacar()
r1.recibir_daño(20)
r1.comer(20)
r1.recibir_daño(80)
r1.status()