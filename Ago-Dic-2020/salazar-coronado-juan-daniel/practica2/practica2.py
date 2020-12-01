class Estudiante():
    def __init__(self, nombre, edad, semestre, carrera):
        self.nombre = nombre
        self.edad = edad
        self.semestre = semestre
        self.carrera = carrera

    def presentacion(self):
        return f"Soy {self.nombre}, tengo {self.edad} años y estoy en {self.semestre} semestre."

    def get_carrera(self):
        carreras = {
            'ISC': "Ing. En sistemas computacionales",
            'IIS': "Ing. Industrial y de sistemas",
            'IEC': "Ing. En electronica y comunicaciones",
            'ITC': "Ingeniero en tecnología y comunicaciones",
            'LSA': "Lic. En sistemas computacionales y administrativos",
            'IA': "Ingeniero automotriz"
        }
        return "Estudio la carrera de " + carreras.get(self.carrera)
    
    def motivacion_promedio(self, promedio):
        if promedio >= 70 and promedio <= 79:
            return "necesito esforzarme más"
        
        if promedio > 79 and promedio <= 89:
            return "lo estoy haciendo bien, pero puedo hacerlo mejor"
        
        if promedio >= 90 and promedio <= 100:
            return "voy muy bien, debo seguir así"
        
        return "-> promedio fuera de los parametros normales <-"

class ServicioSocialYPracticas(Estudiante):
    def __init__(self, nombre, edad, semestre, carrera, servicio, practicas):
        super().__init__(nombre, edad, semestre, carrera)
        self.servicio = servicio
        self.practicas = practicas
        
    def estado(self):
        if self.servicio and self.practicas:
            return "Ya realice el servicio social y las practicas profesionales"
        
        if not self.servicio and not self.practicas:
            return "No he realizado el servicio social ni las practicas profesionales"
        
        if self.servicio and not self.practicas:
            return "Ya realice el servicio social pero no he realizado las practicas profesionales"
        
        if not self.servicio and self.practicas:
            return "No he realizado el servicio social pero ya realice las practicas profesionales"

    def programas_servicio(self):
        programas = ['Identidad institucional', 'Asistente de investigación', 'Pagina Web Sistemas']
        if self.servicio == False:
            print("Puedes realizar el servicio social en los siguientes programas: ")
            return programas

    def empresas_practicas(self):
        empresas = ['Banamex', 'Central de talento universitario SC', 'Tecno Profesionales Rubik']
        if self.practicas == False:
            print("Puedes realizar las practicas profesionales en las siguientes empresas: ")
            return empresas

estudiante1 = Estudiante("Daniel", "21", "Septimo", "ISC")

print(estudiante1.presentacion())
print(estudiante1.get_carrera())
print("En base a mi promedio " + estudiante1.motivacion_promedio(88.34))

estudiante1ssyp = ServicioSocialYPracticas("Daniel", "21", "Septimo", "ISC", True, False)

print(estudiante1ssyp.estado())
print(estudiante1ssyp.programas_servicio())
print(estudiante1ssyp.empresas_practicas())

