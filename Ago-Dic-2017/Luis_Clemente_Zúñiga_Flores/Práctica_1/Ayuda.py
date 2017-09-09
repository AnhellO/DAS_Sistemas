class Ayuda:
    def imprimeAyuda(self):
        print('='*80)
        print('\t\tCONOCER SOBRE:\n1.Agregar/Eliminar (Clientes, Empleados, Productos).\n2.Consultar.\n3.Compraventa.\n')
        print('='*80)
        ayudin = int(input('help>> '))
        #ayudin = int(input('\t\tCONOCER SOBRE:\n1.Agregar/Eliminar (Clientes, Empleados, Productos).\n2.Consultar.\n3.Compraventa.\nhelp>> '))
        if ayudin == 1:
            self.imprimeAyudaAgregar(self)
        elif ayudin ==2:
            self.imprimeAyudaConsultar(self)
        elif ayudin ==3:
            self.imprimeAyudaVenta(self)
        else:
            print(ayudin)
            
    def imprimeAyudaAgregar(self):
        print('='*80)       
        print('\nAGREGAR EMPLEADOS, CLIENTES O PRODUCTOS\n')
        print('\n<<comando>> [\'argumentos\'] Nota: Todos los argumentos son obligatorios')
        print('\n  Ej: empleado Cosme Fulanito Pérez 40 masculino \'Av. Siempreviva #100\'\n\t 555-666-777')         
        print('\n<<empleado>> [\'nombre\' \'ap. paterno\' \'ap. materno\' \'edad\' \'género\' \'dirección\' \n\t\t\'teléfono\']')
        print('\t\tAgrega un empleado al sistema\n')
        print('<<cliente>> [\'nombre\' \'ap. paterno\' \'ap. materno\' \'edad\' \'dirección\' \n\t\t\'teléfono\']')
        print('\t\tAgrega un cliente al sistema\n')       
        print('<<vehiculo>>')
        print('\t<<camion>> [\'marca\' \'modelo\' \'color\' \'motor\' \'trans.\' \'ejes\' \'potencia\' \n\t\t\t\'capacidad\' \'cantidad\' \'precio\']')       
        print('\t\tAgrega un camión al sistema\n')
        print('\t<<auto>> [\'marca\' \'modelo\' \'color\' \'motor\' \'trans.\' \'puertas\' \n\t\t\t\'equipado <si> <no>\' \'km/l\' \'cantidad\' \'precio\']')
        print('\t\tAgrega un automóvil al sistema\n')
        print('\t<<moto>> [\'marca\' \'modelo\' \'color\' \'motor\' \'trans.\' \'cc\' \'cantidad\' \'precio\']')
        print('\t\tAgrega una motocicleta al sistema\n')                  
        print('='*80)
        
    def imprimeAyudaConsultar(self):
        print('='*80)
        print('\nCONSULTAR EMPLEADOS, CLIENTES O PRODUCTOS.\n')
        print('\n<<comando>> [\'argumentos\'] Nota: Todos los argumentos son obligatorios')
        print('\n<<consulta>>')
        print('\n\t<<clientes>> arroja una lista de los clientes con su respectiva información.')        
        print('\n\t<<cliente>> [\'numero de cliente\']: arroja la información de un cliente específico')
        print('\n\t<<autos>> arroja una lista de los automóviles con su respectiva información.')
        print('\n\t<<camiones>> arroja una lista de los camiones con su respectiva información.')
        print('\n\t<<motos>> arroja una lista de las motocicletas con su respectiva información.')
        print('='*80)
    
    def imprimeAyudaVenta(self):
        print('='*80)
        print('\nVENTAS\n')
        print('\n<<comando>> [\'argumentos\'] Nota: Todos los argumentos son obligatorios')
        print('\n<<venta>>')
        print('\n\t<<camion>> [\'numero de vendedor\' \'numero de cliente\' \'SKU\']')
        print('\n\t\tVende un camión')
        print('\n\t<<auto>> [\'numero de vendedor\' \'numero de cliente\' \'SKU\']')
        print('\n\t\tVende un auto')
        print('\n\t<<moto>> [\'numero de vendedor\' \'numero de cliente\' \'SKU\']')
        print('\n\t\tVende una motocicleta')
        print('='*80)
        
