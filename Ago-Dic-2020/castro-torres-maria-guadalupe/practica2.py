class Persona(object):

    def __init__(self, nombre,edad,peso,estatura):
        self.nombre=nombre
        self.edad=edad
        self.peso=peso
        self.estatura=estatura

    def set_nombre(self,nombre):
        self.nombre=nombre
    def get_nombre(self):
        return self.nombre   
    def set_edad(self,edad):
        self.edad=edad
    def get_edad(self):
        return self.edad
    def set_peso(self,peso):
        self.peso=peso
    def get_peso(self):
        return self.peso
    def set_estatura(self,estatura):
        self.estatura=estatura
    def get_estatura(self):
        return self.estatura

    "funcion imc"
    def imc(self,estatura, peso):
        res=((peso)/(estatura**2))
        return print('IMC'+str(res)) 



    def __str__(self):
        return f'Nombre:{self.nombre} \n Edad:{self.edad} años \n Peso: {self.peso} kg \n Estatura: {self.estatura}cm '  

Mipersona = Persona (nombre = 'Santiago', edad = '22 ', peso = '68', estatura = '165')
print (Mipersona)
Mipersona.imc( peso=68,estatura= 165)



class Alumno(Persona):
    def __init__(self,nombre,edad,peso,estatura,matricula,estatus):
        super(). __init__(nombre, edad, peso, estatura)
        self.matricula=matricula
        self.estatus=estatus
      
       

    def set_matricula(self,matricula):
        self.matricula=matricula
    def get_matricula(self):
        return self.matricula   
    def set_estatus(self,estatus):
        self.estatus=estatus
    def get_estatus(self):
        return self.estatus
      
     

    def __str__(self):
       return f'Nombre: {self.nombre} \n Edad: {self.edad} años \nPeso: {self.peso} kg \nEstatura: {self.estatura} cm \nMatricula: {self.matricula}  \nEstatus: {self.estatus}'

    def hablar(self, mensaje):
        """Mostrar mensaje de saludo del estudiante"""
        return  f'{ mensaje } soy { self .nombre }' 

    def descripcion(self):
        """Mostrar descrpcion del estudiante"""
        return  f'{ self .nombre } tiene { self.edad } años, su peso es {self.peso} y tiene una estatura de {self.estatura}cm su matricula es {self.matricula} y su estado actualmente es {self.estatus}'     
   
  
   
              

alumno = Alumno (nombre = 'Jose', edad = '39 ', peso = '85', estatura = '185',  matricula = '14050864', estatus = 'activo')
print (alumno) 
print(alumno.hablar("hola")  )
print(alumno.descripcion() )   
print(alumno.imc(peso=85, estatura=185)) 



  