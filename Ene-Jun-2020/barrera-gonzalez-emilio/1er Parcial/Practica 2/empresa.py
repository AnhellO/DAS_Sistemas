#####CLASES#####
class Persona:
    ##CONSTRUCTOR##
    def __init__(self, **args):
        self.nombre=args.get("nombre")
        self.edad=args.get("edad")
        self.estatura=args.get("estatura")
        self.peso=args.get("peso")
        self.fechaNac=args.get("fechaNac")
    ##SETS##
    def set_nobmbre(self, args):
        self.nombre=args
    def set_edad(self, args):
        self.edad=args
    def set_estatura(self, args):
        self.estatura=args
    def set_peso(self, args):
        self.peso=args            
    def set_fechaNac(self, args):
        self.fechaNac=args
    ##GETS##
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_estatura(self):
        return self.estatura
    def get_peso(self):
        return self.peso
    def get_fechaNac(self):
        return self.fechaNac
    def get_IMC(self):
        return self.peso/(self.estatura**2)
    def __str__(self):
        return f"NOMBRE: {self.nombre}\nEDAD: {self.edad}\nESTATURA: {self.estatura}\nPESO: {self.peso}\nFECHANAC: {set_fechaNac}"   
class Empleado(Persona):
    ##CONSTRUCTOR##
    def __init__(self, **args):
        self.nombre=args.get("nombre")
        self.edad=args.get("edad")
        self.estatura=args.get("estatura")
        self.peso=args.get("peso")
        self.fechaNac=args.get("fechaNac")
        self.numEmp=args.get("numEmp")
        self.cargo=args.get("cargo")
    ##SETS##
    def set_numEmp(self, args):
        self.numEmp=args
    def set_cargo(self, args):
        self.cargo=cargo
    ##GETS##
    def get_numEmp(self):
        return self.numEmp
    def get_cargo(self):
        return self.cargo
    def __str__(self):
        return f"NOMBRE: {self.nombre}\nEDAD: {self.edad}\nESTATURA: {self.estatura}\nPESO: {self.peso}\nFECHANAC: {set_fechaNac}"
                + f"\nNUMEMP: {self.numEmp} +  \nCargo: {self.cargo}"
class Empresa():
    ##CONSTRUCTOR##
    def __init__(self,**args):
        self.nombre=args.get("nombre")
        self.tipo=args.get("tipo")
        self.dueno=args.get("dueno") ##RECIBE UNA PERSONA##
        self.empleados=args.get("empleados") ##RECIBE UNA LISTA DE EMPLEADOS##
    ##SETS##
    def set_nombre(self,args):
        self.nombre=args
    def set_tipo(self, args):
        self.tipo=args
    def set_dueno(self, args):
        self.dueno=args;
    def add_empleado(self, Empleado):
        self.empleados.append(Empleado)
    ##GETS##
    def get_nombre(self):
        return self.nombre
    def get_tipo(self):     
        return self.tipo
    def get_dueno(self):
        return self.dueno.__str__()
    def get_empKeys(self):
        r=""
        for i in self.empleados:
            r=r+f"{i.get_numEmp()}\n"
        return r   
    def __str__(self)
        r=""
        for i in self.empleados:
            r=r+f"{i.__str__()}\n"
        return f"\nNombre: {self.nombre} \nTipo{self.tipo} \nDueño: \n{dueno.__str__()} \nEmpleados: {r}"
