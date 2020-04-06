from ClasesYObjetos import Persona
class Empleado(Persona):
    def __init__(self, **args):
        super(Empleado, self).__init__(**args)
        self.Id = args.get('Id')
        self.PosicionDesempenada = args.get('PosicionDesempenada')
    
    def set_Id(self, Id):
        self.Id = Id
    def get_Id(self):
        return self.Id
    
    def set_PosicionDesempenada(self, PosicionDesempenada):
        self.PosicionDesempenada = PosicionDesempenada
    def get_PosicionDesempenada(self, PosicionDesempenada):
        return self.PosicionDesempenada
    
    def __str__(self):
        return str(Empleado.__str__)+f'\nId: {self.Id}\nPosicion Desempeñada: {self.PosicionDesempenada}'

empleado = Empleado(Nombre='Fernando', Apellidos='Garcia', Edad=21,Estatura=1.80,Peso=60,Id=14008851, PosicionDesempenada='Sistemas')
print(empleado)
print('-------------------------------------------')