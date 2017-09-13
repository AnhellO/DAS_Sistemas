class Ayuda:
    def imprimeAyuda(self):
        print('='*80)
        print('''\
        \t\tCONOCER SOBRE:
1.Agregar/Eliminar (Clientes, Empleados,Productos).
2.Consultar.
3.Compraventa.\
        ''')
        print('='*80)
        ayudin = int(input('help>> '))
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
        print('''\
            AGREGAR EMPLEADOS, CLIENTES O PRODUCTOS.
            
<<comando>> [\'argumentos\'] Nota: Todos los argumentos son obligatorios')

Ej: empleado Cosme Fulanito Pérez 40 masculino \'Av. Siempreviva #100\'
             555-666-777         
             
<<empleado>> [\'nombre\' \'ap. paterno\' \'ap. materno\' \'edad\' \'género\'
              \'dirección\' \'teléfono\']
              Agrega un empleado al sistema.

<<cliente>> [\'nombre\' \'ap. paterno\' \'ap. materno\' \'edad\' \'género\'
             \'dirección\' \'teléfono\']
             Agrega un cliente al sistema       

<<vehiculo>>
           <<camion>> [\'marca\' \'modelo\' \'color\' \'motor\' \'trans.\'
                        \'ejes\' \'potencia\' \'capacidad\' \'cantidad\' 
                        \'precio\']       
                       Agrega un camión al sistema.
           
           <<auto>> [\'marca\' \'modelo\' \'color\' \'motor\' \'trans.\'
                     \'puertas\' \'equipado <si> <no>\' \'km/l\' \'cantidad\'
                     \'precio\']
                     Agrega un automóvil al sistema.
            
           <<moto>> [\'marca\' \'modelo\' \'color\' \'motor\' \'trans.\' \'cc\'
                      \'cantidad\' \'precio\']'
                     Agrega una motocicleta al sistema.
        ''')
        print('='*80)
        
    
    def imprimeAyudaConsultar(self):
        print('='*80)
        print('''\
        CONSULTAR EMPLEADOS, CLIENTES O PRODUCTOS.
<<comando>> [\'argumentos\'] Nota: Todos los argumentos son obligatorios.
<<consulta>>
        <<clientes>> arroja una lista de los clientes con su respectiva
                     información.        
        
        <<cliente>> [\'numero de cliente\']: arroja la información de un
                    cliente específico.
        
        <<autos>> arroja una lista de los automóviles con su respectiva 
                  información.
        
        <<camiones>> arroja una lista de los camiones con su respectiva
                     información.
                     
        <<motos>> arroja una lista de las motocicletas con su respectiva
                  información.
        ''')        
        print('='*80)
    
    def imprimeAyudaVenta(self):
        print('='*80)
        print('''
        VENTAS.
<<comando>> [\'argumentos\'] Nota: Todos los argumentos son obligatorios.
<<venta>>
        <<camion>> [\'numero de vendedor\' \'numero de cliente\' \'SKU\']
                     Vende un camión.
                     
        <<auto>> [\'numero de vendedor\' \'numero de cliente\' \'SKU\']
                   Vende un auto.
                   
        <<moto>> [\'numero de vendedor\' \'numero de cliente\' \'SKU\']
                   Vende una motocicleta.
        ''')
        print('='*80)
        
