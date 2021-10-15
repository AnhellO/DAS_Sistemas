##############################Class Memento
    #Aqui es donde pasamos los datos del originador, tambien se dice que tiene una instantanea(snapshot)
    #
class Memento():

    def __init__(self, marca: str, modelo: str, nombre : str):
        self.marca = marca
        self.modelo = modelo
        self.nombre = nombre    
    
    #Metodo para obtener la snapshot mas reciente.
    def get_state(self):
        return (self.marca,self.modelo,self.nombre)

#######################Class originador/creador/Editor
    #La accion principal, el programa de la aplicacion, la forma de este no depende del patron de comportamiento.
class Celular:
    def __init__(self, marca: str, modelo: str, nombre : str):
        self.marca = marca
        self.modelo = modelo
        self.nombre = nombre    

        #Metodo para guardar un celular en la clase memento(una snapshot)
    def save(self):
        return Memento(self.marca, self.modelo, self.nombre)

        #Metodo para regresar a la version anterior guardada en el memento.
    def restore(self, m: Memento): 
        cel = Celular(self.marca,self.modelo,self.nombre)
        self.cel = m.get_state()

    #Extras
        #Metodo para obtener los detalles guardados en el constructor
    def get_detalles_celular(self):
        return (self.marca, self.modelo, self.nombre)
        
        #Metodo para agregar los datos para un nuevo celular
    def agregar_celular(self, new_marca:str, new_modelo:str, new_nombre:str):
        self.marca = new_marca
        self.modelo = new_modelo
        self.nombre = new_nombre    

            

###################Class Cuidador/caretaker
    #El cuidador, el controlador de versiones, tiene el historial y sabe cuando hacer o deshacer 
    #extrallendo de la pila la version anterior
class Cuidador: 
    def __init__(self):
        self.history = []

        #Metodo para borrar la snapshot actual y regresar ala anterior
    def undo(self):
        return  self.history.pop()

        #Metodo para agregar una snapshot a la lista del cuidador
    def doSomething(self, m:Memento):
        self.history.append(m)