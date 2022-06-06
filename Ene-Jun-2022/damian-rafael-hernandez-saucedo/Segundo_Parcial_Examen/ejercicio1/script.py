import pymongo
import requests

class Conexion:
    def __init__(self,client,diccionario):
        self.client = client
        self.diccionario = diccionario
    
    def Insertar_Datos(self):
        db  = self.client["traba"]
        dic = {}
        listilla = []
        
        for item in self.diccionario:
            for key, value in item.items():
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        dic.update({ckey2:value2})
                else:
                    dic.update({key:value})
            lis.append(dic)
            dic = {}
            
        for lista in lis:
            print(db.trabajo.insert_many([lista]))
        


def main():
    mon = pymongo.MongoClient("mongodb://root:root123@mongo_DB:27017/")
    url = "https://api.github.com/repos/pallets/flask/issues?q=is%3Aissue+is%3Aopened+is%3Aclosed"
    dic = users = requests.get(url).json()

    con = Conexion(mon,dic)
    con.Insertar_Datos()

if __name__ == "__main__":
    main()
