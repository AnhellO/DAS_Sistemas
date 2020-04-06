from ClasesYObjetos2 import Empleado
class Empresa(Empleado):
    def __init__(self, **args):
        super(Empresa, self).__init__(**args)
        self.nombreEmp = args.get('nombreEmp')
        self.tipo = args.get('tipo')
        self.representante = args.get('representante')
        self.numEmpleados = args.get('numEmpleados')

    def set_nombre(self, nombreEmp):
        self.nombreEmp = nombreEmp
    def get_nombre(self):
        return self.nombreEmp
    
    def set_tipo(self, tipo):
        self.tipo = tipo
    def get_tipo(self):
        return self.tipo
    
    def set_representante(self, representante):
        self.representante = representante
    def get_representante(self):
        return self.representante
    
    def set_numEmpleados(self,numEmpleados):
        self.numEmpleados = numEmpleados
    def get_numEmpleados(self):
        self.numEmpleados
    def __str__(self):
        return f'nombreEmp: {self.nombreEmp}\n tipo: {self.tipo}\n representante: {self.representante}\n numEmpleados: {self.numEmpleados}'

empresa = Empleado(nombreEmp='Tucsa', tipo='Privada', representante='Angela Sanchez')
print (empresa)