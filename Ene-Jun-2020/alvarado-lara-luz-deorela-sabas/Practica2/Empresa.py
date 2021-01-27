from Empleado import Empleado
class Empresa(Empleado):
    def __init__(self, nombre, edad, peso, estatura, pasatiempo, id, puesto, company, since, address, empleados):
        super().__init__(nombre, edad, peso, estatura, pasatiempo, id, puesto)
        self.company = company='Zildjian'
        self.since = since = '1623'
        self.address = address = '22 Longwater Drive Norwell, MA 02061 R/A No.'
        self.empleados = empleados
    
    def set_company(self, company):
        self.company = company
    def get_company(self):
        return self.company
    def set_since(self, since):
        self.since = since
    def get_since(self):
        return self.since
    def set_address(self, address):
        self.addres = address
    def get_address(self):
        return self.address
    def set_empleados(self, empleados):
        self.empleados = empleados
    def get_empleados(self):
        return self.empleados
    #FUNCIONES DE CLASE
    def __str__(self):
        return f'Empleados:{super(Empresa, self).__str__()}\nCompany: {self.company}\nSince: {self.since}\nAddress: {self.address}\n'

#CREAMOS LA INSTANCIA 
"""
comp = Empresa(nombre='Juan', edad='19', peso= '50 kg', estatura='1.60', pasatiempo= 'Leer', id= '05589625', puesto= 'Gerente', company='Yamaha', since =1980, address='Mty Nuevo leon 1950 ', empleados = '')
print(comp)
"""

#LISTA PARA MANIPULAR LOS EMPLEADOS QUE SERAN REGISTRADOS
emp = []
trabajador = Empresa('','','','','','','','','','','')
#FUNCION PARA INGRESAR EMPLEADOS NUEVOS
def registro():
    #INDICAMOS EL N° DE EMPLEADOS QUE QUEREMOS INGRESAR
    n = int(input('Cuantos empleados desea registrar? '))
    for x in range(n):
        x+=1
        print('---Ingrese la inf. del empleado---')
        i = input('Nombre: ')
        trabajador.set_nombre(i.title())
        i = input('Edad: ')
        trabajador.set_edad(i.title())
        i = input('Peso: ')
        trabajador.set_peso(i)
        i = input('Estatura: ')
        trabajador.set_estatura(i)
        i = input('Pasatiempo: ')
        trabajador.set_pasatiempo(i.title())
        i = input('ID: ')
        trabajador.set_id(i)
        i = input('Puesto: ')
        trabajador.set_puesto(i.title())
        emp.append(trabajador)
        print('\n   ----Empleado Registrado:----   \n{}\n'.format(trabajador))

#EJECUTAMOS LA FUNCION PARA INGRESAR EMPLEADOS
registro()

