import pymongo
import requests

# conexion a la base de datos
class Conexion:
    def __init__(self,client,diccionario):
        self.client = client
        self.diccionario = diccionario
    # insertar a las coleción de mongo
    def Insertar_Datos(self):
        db  = self.client["prueba"]
        dic = {}
        lis = []
        print("Nombre de la DB: ",db.name)
        
        for item in self.diccionario:
            for clave, valor in item.items():
                if isinstance(valor, dict):
                    for clave2, valor2 in valor.items():
                        dic.update({clave2:valor2})
                else:
                    dic.update({clave:valor})
            lis.append(dic)
            dic = {}
            
        for lista in lis:
            print(db.pet.insert_many([lista]))
        
        print("**************************************************************+")
        col = db['pet']
        for x in col.find():
            print(x)

# funcion main
def main():
    client = pymongo.MongoClient("mongodb://root:root123@mongo_DB:27017/")
    url = "https://api.github.com/repos/pallets/flask/issues?q=is%3Aissue+is%3Aopened+is%3Aclosed"
    diccionario = users = requests.get(url).json()
    con = Conexion(client,diccionario)
    con.Insertar_Datos()

if __name__ == "__main__":
    main()