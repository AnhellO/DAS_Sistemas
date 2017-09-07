
class Agencia:
    """Class Agencia
    """
    # Campos:
    __nombre = ""  # (String)
    __direccion = ""  # (String)
    __numeroDeEmpleados = 0  # (int)
    __numeroDeClientes = 0  # (int)
    __empleados = []
    __clientes = []
    __autos = []
    __camiones = []
    __motos = []
    __dict_ventas = {'vendedor': 0, 'comprador':0, 'sku': 'valor'}
    __lista_ventas = []
    __totalCamiones = 0
    __totalAutos = 0
    __totalMotos = 0

    # Operations
    #Constructor
    def __init__(self, nombre='', direccion='', numeroDeEmpleados =0, numeroDeClientes=0):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__numeroDeEmpleados = numeroDeEmpleados
        self.__numeroDeClientes = numeroDeClientes
    
    #Métodos
    
    #Operaciones para Agencia
    
    def estableceNombre(self, nombre):       
        self.__nombre = nombre

    def obtenNombre(self):
        return self.__nombre
    
    def estableceDireccion(self,direccion):
        self.__direccion = direccion

    def obtenDireccion(self):
        return self.__direccion
    
    #Operaciones de compra y venta
    
    def ventaCamion(self,vendedor,comprador,sku):
        self.__dict_ventas={'vendedor': vendedor, 'comprador': comprador, 'sku': sku}
        self.__lista_ventas.append(self.__dict_ventas)
        self.bajaCamion(self.searchCamion(sku))        
       
    
    #Bug en esta función con el self.bajaAuto --> bajaAuto() ---> reduceExistencias()
    def ventaAuto(self,vendedor,comprador,sku):
        self.__dict_ventas={'vendedor': vendedor, 'comprador': comprador, 'sku': sku}
        self.__lista_ventas.append(self.__dict_ventas)
        self.bajaAuto(self.searchAuto(sku))
        
    
    
    def ventaMoto(self,vendedor,comprador,sku):
        self.__dict_ventas={'vendedor': vendedor, 'comprador': comprador, 'sku': sku}
        self.__lista_ventas.append(self.__dict_ventas)
        self.bajaMoto(self.searchMoto(sku))
        
    def imprimeVentas(self):
        for i in self.__lista_ventas:
            print (i) 
   
    #operaciones para camiones    
    def altaCamion(self,camion):
        self.__camiones.append(camion)
        self.__totalCamiones+=1
        
    def bajaCamion(self,camion):
        camion.reduceExistencias()
    
    def imprimeCamiones(self):
        for i in self.__camiones:
            print(i.datosDeCamion())

    def searchCamion(self,sku):
        for i in self.__camiones:
            if sku == i.devuelveSku():
                return i
                break
                
    #operaciones para autos                    
    def altaAuto(self,auto):
        self.__autos.append(auto)
        self.__totalAutos+=1
    
    def imprimeAutos(self):
        for i in self.__autos:
            print(i.datosDeAuto())
    
    #Bug con el método reduceExistencias() <-- ventaAuto()
    #'NoneType' object has no attribute 'reduceExistencias'
    def bajaAuto(self,auto):
        auto.reduceExistencias()  
        print('baja auto')
       
    
    def searchAuto(self,sku):
        for i in self.__camiones:
            if sku == i.devuelveSku():
                return i
                break
    
    #Operaciones para motos
    def altaMoto(self,moto):
        self.__motos.append(moto)
        self.__totalMotos+=1
        
    def imprimeMotocicletas(self):
        for i in self.__motos:
            print(i.datosDeMoto())
                
    def bajaMoto(self, moto):
        moto.reduceExistencias()
        
    def searchMoto(self, sku):
        for i in self.__motos:
            if sku == i.devuelveSku():
                return i
                break
                
    #Operaciones sobre clientes y empleados
    
    def bajaCliente(self, numeroDeCliente):
        self.__clientes[int(numeroDeCliente)-1] = None
        
    def bajaEmpleado(self, numeroDeEmpleado):
       self.__empleados[int(numeroDeEmpleado)-1] = None        

    def aumentaEmpleados(self,empleado):
        self.__empleados.append(empleado)
        self.__numeroDeEmpleados+=1

    def devuelveEmpleado(self,cant):
        print(cant)
        return self.__empleados[int(cant)-1].datosDeEmpleado()

    def devuelveEmpleados(self):
        return self.__numeroDeEmpleados

    def imprimeEmpleados(self):
        for i in self.__empleados:
            print(i.datosDeEmpleado())

    def devuelveCliente(self, cant):
        return self.__clientes[int(cant)-1].datosDeCliente()

    def aumentaClientes(self,cliente):
        self.__clientes.append(cliente)
        self.__numeroDeClientes+=1

    def imprimeClientes(self):
        for i in self.__clientes:
            print(i.datosDeCliente())

    def devuelveClientes(self):
        return self.__numeroDeClientes
 
            
    
   
    
    
         
            
   

