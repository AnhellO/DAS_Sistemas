class Empleado(persona):
    def __init__ (self, **args)
        super(Empleado, self).__init__(**args)
        self.numero_empleado=numero_empleado
        self.ocupacion=ocupacion

     def set_numero_empleado(args):
        self.numero_empleado=args
    def get_numero_empleado():
        return self.numero_empleado
    
    def set_ocupacion(args):
        self.ocupacion=args    
    def get_ocupacion():
        return self.ocupacion
    
    def __str__(self):
		return f'{super(Empleado, self).__str__()}Numero_Empleado: {self._numero_empleado}\nOcupacion: {self._ocupacion}'

