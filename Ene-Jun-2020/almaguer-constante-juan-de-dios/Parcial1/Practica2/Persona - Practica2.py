#persona con cinco atributos con peso y estatura

class Persona(object):
    def __init__(self, **args):
        self.nombre = args.get('nombre')
        self.estatura = args.get('estatura')
        self.peso = args.get('peso')
        self.edad = args.get('edad')
        self.nacionalidad = args.get('nacionalidad')

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_estatura(self, estatura):
        self.estatura = estatura

    def get_estatura(self):
        return self.estatura

    def set_peso(self, peso):
        self.peso = peso

    def get_peso(self):
        return self.peso

    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self):
        return self.edad

    def set_nacionalidad(self,nacionalidad):
        self.nacionalidad = nacionalidad

    def get_nacionalidad(self):
        return self.nacionalidad

    def __str__(self):
        return f'Nombre = {self.nombre}\nEstatura = {self.estatura}\nPeso = {self.peso}\nEdad = {self.edad}\n' \
               f'Nacionalidad = {self.nacionalidad}'

    def calcIMC(self):
        peso = self.get_peso()
        est = self.get_estatura()
        IMC = (peso/est * est)
        return f'IMC: {IMC}'

class Empleado(Persona):

    def __init__(self, **args):
        super(Empleado, self).__init__(**args)
        self.id = args.get('id')
        self.puesto = args.get('puesto')

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_puesto(self, puesto):
        self.puesto = puesto

    def get_puesto(self):
        return self.puesto

    def __str__(self):
        return f'ID = {self.id}\nPuesto = {self.puesto}\n{super(Empleado, self).__str__()}'

class Empresa(Empleado):

    def __init__(self, **args):
        self.nombre_emp = args.get('nombre_emp')
        self.razon = args.get('razon')
        self.año_fundacion = args.get('año_fundacion')
        self.conjunto = args.get('conjunto')


    def set_nombre_emp(self,nombre_emp):
        self.nombre_emp = nombre_emp

    def get_nombre_emp(self):
        return self.nombre_emp

    def set_razon(self, razon):
        self.id = id

    def get_razon(self):
        return self.razon

    def set_año_fundacion(self, año_fundacion):
        self.año_fundacion = año_fundacion

    def get_año_fundacion(self):
        return self.año_fundacion

    def set_conjunto(self,conjunto):
        self.conjunto = conjunto

    def get_conjunto(self):
         return self.conjunto

    def __str__(self):
        empleados = self.get_conjunto()
        return f'{empleados}'
        #repemp = emp.replace("\n", ", ")

    def add_worker(self):
        empleados = empresa.get_conjunto()
        empleados.append(self.__str__())
        return empleados

    def search_worker(id: str):
        empleados = empresa.get_conjunto()
        for empleado in empleados:
            for k,v in empleado.items():
               if id in str(v):
                  return f'{k} : {v}'


emp1 = Empleado(id = '1563551', puesto='Empleado',nombre='Daniel', estatura=1.90, peso= 100, edad=28,
                     nacionalidad='Mexicana')
emp2 = Empleado(id = '15325', puesto='Empleado',nombre='Juan', estatura=1.70, peso= 68, edad=22,
                     nacionalidad='Mexicana')
emp3 = Empleado(id = '153547', puesto='Empleado',nombre='Jorge', estatura=1.74, peso= 72, edad=25,
                     nacionalidad='Mexicana')
dic_emp1 = emp1.__dict__
dic_emp2 = emp2.__dict__
dic_emp3 = emp3.__dict__

empresa = Empresa(nombre_emp= 'Jochos', razon='Ventas',año_fundacion='1997', conjunto=[dic_emp1, dic_emp2])

add_worker = Empresa.add_worker(dic_emp3)
search_worker = Empresa.search_worker("15325")

print(add_worker)
print(search_worker)




