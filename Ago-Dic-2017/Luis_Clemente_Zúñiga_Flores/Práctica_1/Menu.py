import sys
import shlex
import os
from Agencia import Agencia
from Ayuda import Ayuda
from Empleado import Empleado
from Cliente import Cliente
from Automovil import Automovil
from Camion import Camion
from Motocicleta import Motocicleta

class CompraVenta:
    """Class CompraVenta
    """
    # Attributes:

    # Operations

    def main():
        print('Configuración inicial.')
        nomAgencia = input('Nombre de la agencia: ')
        direccion = input('Dirección de la agencia: ')
        nombre = input('Nombre del administrador: ')
        agencia = Agencia(nomAgencia,direccion)
        os.system('cls')
        print('#'*80)
        print('Agencia de automóviles ' + nomAgencia + ' [versión 0.0 2017]\n' + direccion)
        print('#'*80)
        print('Para obtener ayuda, escriba `ayuda` o `help`.')
        print('Para salir escriba `salir` o `exit`')

        while True:
            try:
                #recibe los argumentos
                cmd, *args = shlex.split(input(nombre + '>'))

                #Comandos técnicos
                if cmd=='exit' or cmd=='salir':
                    break

                elif cmd=='agencia':
                    print('*'*80)
                    print('Agencia de automóviles ' + agencia.getNombre() + ' [versión 0.0 2017]\n' + agencia.getDireccion())
                    print('*'*80)

                elif cmd=='cls' or cmd=='clear':
                    os.system('cls')

                elif cmd=='pwd':
                    os.system('echo %cd%')

                #Comandos de administración de la agencia
                elif cmd=='admin':
                    admin = args[0]
                    nombre = admin
                elif cmd=='agencianombre':
                    try:
                        nuevoAgencia = args[0]
                        agencia.setNombre(nuevoAgencia)
                    except:
                        print('Falta el nombre de la agencia')

                elif cmd=='agenciadireccion':
                    try:
                        nuevaDireccion = args[0]
                        agencia.setDireccion(nuevaDireccion)
                    except:
                        print('Falta la dirección de la agencia')

                elif cmd=='help' or cmd=='ayuda':
                    Ayuda.imprimeAyuda(Ayuda)

                elif cmd=='saludo':
                    try:
                        name = args[0]
                        print('Hola "{}"'.format(name))
                    except:
                        print('Faltó el nombre para el saludo!')


                #Comandos para agregar, eliminar, consultar y vender
                
                #agregar empleado
                elif cmd=='empleado':
                    try:
                        nomEmpleado, paternoEmp, maternoEmp, edadEmp, genEmp, dirEmp, telEmp = args
                        numEmp = agencia.getEmpleados()+1
                        empleado = Empleado(nomEmpleado,paternoEmp,maternoEmp,edadEmp,genEmp,dirEmp,telEmp,int(numEmp))
                        agencia.aumentaEmpleados(empleado)
                        print('Empleado nuevo en el sistema')

                    except:
                        print('error al agregar empleado')                           

                #agregar cliente
                elif cmd=='cliente':
                    try:
                        nomCliente, paternoCli, maternoCli, edadCli, genCli, dirCli, telCli = args
                        numCli = agencia.getClientes()+1
                        cliente = Cliente(nomCliente, paternoCli, maternoCli, edadCli, genCli, dirCli, telCli,int(numCli))
                        agencia.aumentaClientes(cliente)
                        print('Cliente nuevo en el sistema')

                    except:
                        print('error al agregar cliente')

                #agregar vehículo
                elif cmd=='vehiculo':
                    try:
                        if len(args)==11:
                            
                            if args[0] == 'auto':
                                auto, marca,modelo,color,motor,trans,puertas,equipado,kml,cantidad,precio = args                                
                                automovil = Automovil(marca,modelo,color,motor,trans,puertas,equipado,kml,int(cantidad),precio)                                
                                agencia.altaAuto(automovil)
                                print('Automóvil agregado al sistema')
                                
                            elif args[0] == 'camion':
                                camion, marca, modelo,color,motor,trans,ejes,potencia,capacidad,cantidad,precio = args                                
                                camion = Camion(marca,modelo,color,motor,trans,str(ejes),str(potencia),str(capacidad),int(cantidad),precio)
                                agencia.altaCamion(camion)
                                print('Camión agregado al sistema')

                        elif len(args)==9:
                            
                            if args[0] == 'moto':
                                moto, marca, modelo, color, motor, trans, cc, cantidad,precio = args
                                motocicleta = Motocicleta(marca,modelo,color,motor,trans,cc,int(cantidad),precio)                                
                                agencia.altaMoto(motocicleta)
                                print('Moto agregada al sistema')
                            
                        else:
                            print('Argumentos incompletos')
                    except:
                        print('Argumentos equivocados')


                #consultar empleados, clientes o vehículos
                elif cmd=='consulta':
                    try:
                        if len(args) == 1:
                            arg1 = args[0]                            
                            if arg1 == 'empleados':
                                agencia.imprimeEmpleados()

                            elif arg1 == 'clientes':
                                agencia.imprimeClientes()

                            elif arg1 == 'autos':
                                agencia.imprimeAutos()                               
                            
                            elif arg1 == 'camiones':
                                agencia.imprimeCamiones()
                            
                            elif arg1 == 'motos':
                                agencia.imprimeMotocicletas()

                        elif len(args) == 2:
                            arg1, arg2 = args
                            if arg1 == 'empleado':
                                print(agencia.getEmpleado(arg2))

                            elif arg1 == 'cliente':
                                print(agencia.getCliente(arg2))                   
                    except:
                        print('argumentos incompletos')              
                
                #Operaciones de venta
                elif cmd == 'venta':
                    try:                    
                        vehiculo, vendedor, cliente, sku = args                    
                        if vehiculo == 'camion':
                            agencia.ventaCamion(vendedor,cliente,sku)
                            print('Un camion con sku ' + sku + ' ha sido vendido')
                        
                        if vehiculo == 'auto':
                            agencia.ventaAuto(vendedor,cliente,sku)
                            print('Un automóvil con sku ' + sku + ' ha sido vendido')
                        
                        if vehiculo == 'moto':
                            agencia.ventaMoto(vendedor,cliente,sku)
                            print('Una motocicleta con sku ' + sku + ' ha sido vendida')
                    except Exception as inst:
                        print(inst)                
                else:
                    print('Comando desconocido: {}'.format(cmd))

            except:
                a = 0


    if __name__ == "__main__":
        main()



