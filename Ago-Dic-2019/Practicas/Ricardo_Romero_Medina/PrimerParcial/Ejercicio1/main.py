from vehiculo import Vehiculo
from automovil import Automovil
from avion import Avion
from barco import Barco

def colar(tipo,lista):
    lista1=[]
    for i in range(0,len(lista)):
        if lista[i].get_tipo() == tipo:
            lista1.append(lista[i])

    return lista1
class Main():
    instancia1 = Automovil('','Chevrolet','Negro','2010','5')
    instancia2 = Automovil('','Mustang','Verde','2012','7')
    instancia3 = Automovil('','Honda','Azul','2011','4')
    instancia4 = Automovil('','Nissan','Blanco','2001','2')
    instancia5 = Automovil('','Fiat','Rojo','2019','8')
    
    print('---------------------------------------------------')
    instancia6 = Avion('','Carga','Blanco','2000','85')
    instancia7 = Avion('','Transporte','Rojo','2000','150')
    instancia8 = Avion('','Privado','Negro','2000','5')
    instancia9 = Avion('','AirForce','Azul','2000','500')
    instancia10 = Avion('','No lo tiene ni Obama','Negro','2000','105')
    
    print('---------------------------------------------------')
    instancia11 = Barco('','Pesquero','Azul','2012','51')
    instancia12 = Barco('','Transporte','Rojo','2012','35')
    instancia13 = Barco('','Crucero','Blanco','2012','1000')
    instancia14 = Barco('','No se me ocurre nada','Negro','2012','558')
    instancia15 = Barco('','En este tampoco','Azul','2012','79')
    
    lista=[instancia1,instancia2,instancia3,instancia4,instancia5,instancia6,instancia7,instancia8,
    instancia9,instancia10,instancia11,instancia12,instancia13,instancia14,instancia15]

    lista2 = colar('Maritimo',lista)
    for i in range(len(lista2)):
        print(lista2[i])
        print('----------------------------------------------------------------')

    lista2 = colar('Aereo',lista)
    for i in range(len(lista2)):
        print(lista2[i])
        print('----------------------------------------------------------------')

    lista2 = colar('Terrestre',lista)
    for i in range(len(lista2)):
        print(lista2[i])
        print('----------------------------------------------------------------')
if __name__=='__main__':
    Main()