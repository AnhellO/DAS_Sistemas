class vehiculo :
    def __init__(self,v,km,c) : 
        self.v=v
        self.km=km
        self.c=c
    def tarifa(self):
        return self.c*100
    def __str__(self):
        return f"Numero1:{self.v}\nNumero2:{self.km}\nNumero3:{self.c}\nTotal:{self.tarifa()}"
    
class autobus(vehiculo):
    def tarifa(self):
        total=(self.c*100)+((self.c*100)*0.1)
        return total
    def __str__(self):
        return f"Numero1:{self.v}\nNumero2:{self.km}\nNumero3:{self.c}\nTotal:{self.tarifa()}"
    
def main():
    v1=vehiculo(100,250,3)
    v2=vehiculo(240,2000,4)
    v3=vehiculo(300,1000,5)
    autobus1=autobus(180,5000,20)
    autobus2=autobus(130,3000,15)
    autobus3=autobus(170,2500,25)
    lista=[autobus1,v1,autobus2,v2,autobus3,v3]
    for a in lista:
        if a.__class__==autobus:
            print("Soy un autobus!\n",a)
    
if __name__=='__main__':
    main()