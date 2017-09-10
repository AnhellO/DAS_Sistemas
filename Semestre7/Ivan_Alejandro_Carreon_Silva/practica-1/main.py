from Vendedor import *
from Cliente import *
from Agencia import *
from Automovil import *
from Camion import *
from Motocicleta import *

i = Vendedor1.getNombre()+" "+Vendedor1.getApellidoPaterno()+" "+Vendedor1.getApellidoMaterno()+" "+Vendedor1.getSexo()+" "+Vendedor1.getEdad()+" "+Vendedor1.getDomicilio()+" "+Vendedor1.getTelefono()+" "+Vendedor1.getIDVendedor()
i2 = Vendedor2.getNombre()+" "+Vendedor2.getApellidoPaterno()+" "+Vendedor2.getApellidoMaterno()+" "+Vendedor2.getSexo()+" "+Vendedor2.getEdad()+" "+Vendedor2.getDomicilio()+" "+Vendedor2.getTelefono()+" "+Vendedor2.getIDVendedor()
i3 = Vendedor3.getNombre()+" "+Vendedor3.getApellidoPaterno()+" "+Vendedor3.getApellidoMaterno()+" "+Vendedor3.getSexo()+" "+Vendedor3.getEdad()+" "+Vendedor3.getDomicilio()+" "+Vendedor3.getTelefono()+" "+Vendedor3.getIDVendedor()

l = Sagencia.getNombre()+" "+Sagencia.getDireccion()+" "+Sagencia.getEmail()

cl = Cliente1.getNombre()+" "+Cliente1.getApellidoPaterno()+" "+Cliente1.getApellidoMaterno()+" "+Cliente1.getSexo()+" "+Cliente1.getEdad()+" "+Cliente1.getDomicilio()+" "+Cliente1.getTelefono()+" "+Cliente1.getIDCliente()
cl2 = Cliente2.getNombre()+" "+Cliente2.getApellidoPaterno()+" "+Cliente2.getApellidoMaterno()+" "+Cliente2.getSexo()+" "+Cliente2.getEdad()+" "+Cliente2.getDomicilio()+" "+Cliente2.getTelefono()+" "+Cliente2.getIDCliente()
cl3 = Cliente3.getNombre()+" "+Cliente3.getApellidoPaterno()+" "+Cliente3.getApellidoMaterno()+"  "+Cliente3.getSexo()+" "+Cliente3.getEdad()+" "+Cliente3.getDomicilio()+" "+Cliente3.getTelefono()+" "+Cliente3.getIDCliente()

ca = Carro1.getMarca()+" "+Carro1.getModelo()+" - "+Carro1.getColor()+" - "+Carro1.getTransmision()+" - "+Carro1.getCilindros()+" - "+Carro1.getPrecio()+" - "+Carro1.getMotor()+" - "+ Carro1.getPuertas()+" - "+Carro1.getEquipado()+" - "+Carro1.getKmL()
ca2 = Carro2.getMarca()+" "+Carro2.getModelo()+" - "+Carro2.getColor()+" - "+Carro2.getTransmision()+" - "+Carro2.getCilindros()+" - "+Carro2.getPrecio()+" - "+Carro2.getMotor()+" - "+ Carro2.getPuertas()+" - "+Carro2.getEquipado()+" - "+Carro2.getKmL()
ca3 = Carro3.getMarca()+" "+Carro3.getModelo()+" - "+Carro3.getColor()+" - "+Carro3.getTransmision()+" - "+Carro3.getCilindros()+" - "+Carro3.getPrecio()+" - "+Carro3.getMotor()+" - "+ Carro3.getPuertas()+" - "+Carro3.getEquipado()+" - "+Carro3.getKmL()

mo = Moto1.getMarca()+" "+Moto1.getModelo()+" - "+Moto1.getColor()+" - "+Moto1.getTransmision()+" - "+Moto1.getCilindros()+" - "+Moto1.getPrecio()+" - "+Moto1.getMotor()+" - "+Moto1.getTipo()+" - "+Moto1.getCenCub()
mo2 = Moto2.getMarca()+" "+Moto2.getModelo()+" - "+Moto2.getColor()+" - "+Moto2.getTransmision()+" - "+Moto2.getCilindros()+" - "+Moto2.getPrecio()+" - "+Moto2.getMotor()+" - "+Moto2.getTipo()+" - "+Moto2.getCenCub()
mo3 = Moto3.getMarca()+" "+Moto3.getModelo()+" - "+Moto3.getColor()+" - "+Moto3.getTransmision()+" - "+Moto3.getCilindros()+" - "+Moto3.getPrecio()+" - "+Moto3.getMotor()+" - "+Moto3.getTipo()+" - "+Moto3.getCenCub()

cam = camion1.getMarca()+" "+camion1.getModelo()+" - "+camion1.getColor()+" - "+camion1.getTransmision()+" - "+camion1.getCilindros()+" - "+camion1.getPrecio()+" - "+camion1.getMotor()+" - "+camion1.getEjes()+" - "+camion1.getPotencia()
cam2 = camion2.getMarca()+" "+camion2.getModelo()+" - "+camion2.getColor()+" - "+camion2.getTransmision()+" - "+camion2.getCilindros()+" - "+camion2.getPrecio()+" - "+camion2.getMotor()+" - "+camion2.getEjes()+" - "+camion2.getPotencia()

opcion = 7

print("=" * 80)

while (opcion != 0):
    print("Compra y venta de medios de transporte prrones \n")
    print("¿A que se debe su visita?")
    print("1: Solo estoy viendo los vehiculos, gracias :v")
    print("2: Comprar vehiculo.")
    print("3: Vender vehiculo.")
    print("4: Ver clientes frecuentes.")
    print("5: Conocer empleados.")
    print("6: Informacion sobre nosotros.")
    print("0: Salir.")



    gato = int(input(""))


    if gato == 1 :
        print('Automoviles \n')
        print(ca + "\n" + ca2 + "\n" + ca3)
        print("=" * 80)
        print('Motocicletas \n')
        print(mo + "\n" + mo2 + "\n" + mo3)
        print("=" * 80)
        print('Camiones \n')
        print(cam + "\n" + cam2)
        print("=" * 80)
    elif gato == 2:
        vv = Sagencia.ventaVehiculo( (Cliente2.getNombre()+" "+Cliente2.getApellidoPaterno()+" "+Cliente2.getApellidoMaterno()+"\n" ),(Carro1.getMarca()+" "+Carro1.getModelo()+"\n" ),(Vendedor1.getNombre() )+" "+(Vendedor1.getApellidoPaterno()+" "+Vendedor1.getApellidoMaterno() ) )
        print(vv)
        print("=" * 80)
        cc = Sagencia.ventaVehiculo( (Cliente3.getNombre()+" "+Cliente3.getApellidoPaterno()+" "+Cliente3.getApellidoMaterno()+"\n" ),(camion1.getMarca()+" "+camion1.getModelo()+"\n" ),(Vendedor2.getNombre() )+" "+(Vendedor2.getApellidoPaterno()+" "+Vendedor2.getApellidoMaterno() ) )
        print(cc)
        print("=" * 80)
        mm = Sagencia.ventaVehiculo( (Cliente1.getNombre()+" "+Cliente1.getApellidoPaterno()+" "+Cliente1.getApellidoMaterno()+"\n" ),(Moto3.getMarca()+" "+Moto3.getModelo()+"\n" ),(Vendedor3.getNombre() )+" "+(Vendedor3.getApellidoPaterno()+" "+Vendedor3.getApellidoMaterno() ) )
        print(mm)
        print("=" * 80)
    elif gato == 3:
        print('Estamos trabajando en eso :v')
        print("=" * 80)
    elif gato == 4:
        print(cl +"\n"+ cl2 +"\n"+ cl3)
        print("=" *80)
    elif gato ==5:
        print(i +"\n"+ i2  +"\n"+ i3)
        print("=" * 80)
    elif gato ==6:
        print(l)
        print("=" * 80)
    elif gato == 0:
        exit()
