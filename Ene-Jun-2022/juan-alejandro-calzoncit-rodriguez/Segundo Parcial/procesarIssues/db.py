from pymongo import MongoClient

class app:
        
    # Se establecen los elementos para realizar una conección con Mongo como atributos de la clase    
    def __init__(self) -> None:
        self.MONGO_URI = "mongodb://root:contrasena123@mongo_compose:27017/"
        self.client = MongoClient(self.MONGO_URI)
        self.db = self.client['parcial']
        self.collection = None
        
    # Cambia el nombre de la colección        
    def setCollection(self,name):
        self.collection = self.db[name]

    # Elimina todos los registros de una colección
    def eliminar(self):
        self.collection.delete_many({})

    # Inserta un registros a la colección
    def insertar(self, content):                                   
        self.collection.insert_one(content)