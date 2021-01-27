# ---------------------------------------------------------------------------------------------------------------------
# # #  PARTE 1  # # #
# ---------------------------------------------------------------------------------------------------------------------


class Persona(object):

    def __init__(self, **args):
        self.nombre = args.get('nombre')
        self.edad = args.get('edad')
        self.sexo = args.get('sexo')
        self.estatura = args.get('estatura')
        self.peso = args.get('peso')

    # ----------------------------------------------------------

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    # ---------------------------------------------------------

    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self):
        return self.edad

    # ---------------------------------------------------------

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_sexo(self):
        return self.sexo

    # ---------------------------------------------------------

    def set_estatura(self, estatura):
        self.estatura = estatura

    def get_estatura(self):
        return self.estatura

    # ---------------------------------------------------------

    def set_peso(self, peso):
        self.peso = peso

    def get_peso(self):
        return self.peso

    # ----------------------------------------------------------

    def imc(self):
        pe = self.get_peso()
        es = self.get_estatura()

        imc = pe / (es * es)
        return "{0:.4f}".format(imc)

    # ----------------------------------------------------------

    def __str__(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad} años\nSexo: {self.sexo}\nPeso: {self.peso} kgs.\nEstatura: {self.estatura} mts.\nIMC: {self.imc()}'

# E J E M P L O S


p1 = Persona(nombre='Luis', edad=45, sexo='Masculino', estatura=1.80, peso=108)
p2 = Persona(nombre='Carlos', edad=36, sexo='Masculino', estatura=1.75, peso=81)
p3 = Persona(nombre='Emmanuel', edad=27, sexo='Masculino', estatura=1.68, peso=63)

print(p1.__str__(), '\n')
print(p2.__str__(), '\n')
print(p3.__str__(), '\n')


# ---------------------------------------------------------------------------------------------------------------------
# # #  PARTE 2  # # #
# ---------------------------------------------------------------------------------------------------------------------


class Empleado(Persona):

    def __init__(self, **args):
        super(Empleado, self).__init__(**args)
        self._id = args.get('id')
        self._puesto = args.get('puesto')

    # ----------------------------------------------------------

    def set_id(self, idn):
        self._id = idn

    def get_id(self):
        return self._id

    # ----------------------------------------------------------

    def set_puesto(self, puesto):
        self._puesto = puesto

    def get_puesto(self):
        return self._puesto

    # ----------------------------------------------------------

    def __str__(self):
        return f'{super(Empleado, self).__str__()}\nID de empleado: {self._id}\nPuesto: {self._puesto}'

# E J E M P L O


slave = Empleado(id=9, puesto='Chef')

slave.set_nombre('Mario')
slave.set_edad(27)
slave.set_sexo('Masculino')
slave.set_estatura(1.8)
slave.set_peso(90)

print(slave, '\n')


# ---------------------------------------------------------------------------------------------------------------------
# # #  PARTE 3  # # #
# ---------------------------------------------------------------------------------------------------------------------

class Empresa(Empleado):

    def __init__(self, **args):
        super(Empresa, self).__init__(**args)
        self._nombre_empresa = args.get('nombre_empresa')
        self._direccion = args.get('direccion')
        self._rfc = args.get('rfc')
        self._conj_emp = args.get('conj_emp')

    def set_nombre_empresa(self, nombre_empresa):
        self._nombre_empresa = nombre_empresa

    def get_nombre_empresa(self):
        return self._nombre_empresa

    # ----------------------------------------------------------

    def set_direccion(self, direccion):
        self._direccion = direccion

    def get_direccion(self):
        return self._direccion

    # ----------------------------------------------------------

    def set_rfc(self, rfc):
        self._rfc = rfc

    def get_rfc(self):
        return self._rfc

    # ----------------------------------------------------------

    def set_conj_emp(self, conj_emp):
        self._conj_emp = conj_emp

    def get_conj_emp(self):
        return self._conj_emp

    # ----------------------------------------------------------

    def __str__(self):
        return f'{super(Empresa, self).__str__()}\nNombre de la empresa: {self._nombre_empresa}\n' \
               f'Dirección de la empresa: {self._direccion}\nRFC de la empresa: {self._rfc}\n'

# E J E M P L O S


slave1 = Empresa(nombre_empresa='Krusty Krab', direccion='Acámbaro, #999, Saltillo, Coah.', rfc='CC090509IDK')
slave2 = Empresa(nombre_empresa='Krusty Krab', direccion='Acámbaro, #999, Saltillo, Coah.', rfc='CC090509IDK')

slave1.set_nombre('Ricardo')
slave1.set_edad(27)
slave1.set_sexo('Masculino')
slave1.set_estatura(1.8)
slave1.set_peso(90)
slave1.set_id(1)
slave1.set_puesto('Cocinero')

slave2.set_nombre('Rodrigo')
slave2.set_edad(18)
slave2.set_sexo('Masculino')
slave2.set_estatura(1.90)
slave2.set_peso(81)
slave2.set_id(2)
slave2.set_puesto('Mesero')

print(slave1, '\n', slave2, '\n')
