# Ej listas comprimidas [x for x in ('hola', 'clase', 'das', 'stmen') for char in x if char in ('a', 'e', 'i', 'o', 'u')]

class Banda:

    """docstring for Banda"""
    def __init__(self, **args):
        self.nombre = args.get('nombre')
        self.integrantes = args.get('integrantes')
        self.genero = args.get('genero')
        self.logo = args.get('logo')


class Impresor:

    """docstring for Impresor"""
    def __init__(self, objeto = None):
        self.objetos = {}

        if objeto:
            self.agregarObjeto(objeto)

    def agregarObjeto(self, objeto):
        self.objetos[objeto.__class__.__name__] = objeto

    def getPropiedades(self, objeto):
        #print(objeto.__dict__.keys())
        args = [i for i in objeto.__dict__.keys() if not i.startswith('_')]
        values = [i for i in objeto.__dict__.values()]
        return dict(zip(args, values))

    def imprimeObjeto(self, objeto):
        iObjeto = self.objetos.get(objeto.__class__.__name__)
        print(self.getPropiedades(iObjeto) if iObjeto else "No existe el objeto")


class Conector:

    """docstring for Conector"""
    def __init__(self, **args):
        self.motor = args.get('motor') if args.get('motor') else 'mysql'
        self.credenciales = args.get('credenciales') if args.get('crendenciales') else {'usr':'', 'pass':''}
        self.esquema = args.get('esquema')

    def setConexion(self, motor='mysql'):
        self.motor = motor

    def crearConexion(self, motor=None):
        if motor:
            self.setConexion(motor)

        self.motor.lower()

        if self.motor == 'mysql':
            return "Nueva conexión a MySql"
        elif self.motor == 'mongo':
            return "Nueva conexión a MongoDB"
        elif self.motor == 'sql-server':
            return "Nueva conexión a SQL Server"
        else:
            return "Raise excepción"


banda = Banda(nombre="Los Rockan' Rollas", logo="/some/path/to/perdition.png")

printer = Impresor()
printer.agregarObjeto(banda)
printer.imprimeObjeto(banda)

conector = Conector()
conexion = conector.crearConexion()
print(conexion)
conexion = conector.crearConexion('mongo')
print(conexion)
#conexion = banda.conectaBandasDB()
#if conexion:
    #print("La conexión se realizó exitosamente!")
