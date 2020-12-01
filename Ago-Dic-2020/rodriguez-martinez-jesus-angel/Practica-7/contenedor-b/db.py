import os
import pymongo
from pymongo import MongoClient
import datetime
import pprint

class Db:
    # Constructor
    def __init__(self, **kwargs):
        self.__host = kwargs.get("host",os.environ["MONGO_INITDB_HOSTNAME"])
        self.__user = kwargs.get("headers", os.environ["MONGO_INITDB_ROOT_USERNAME"])
        self.__password =  kwargs.get("password", os.environ["MONGO_INITDB_ROOT_PASSWORD"])
        self.__port = kwargs.get("port", os.environ["MONGO_INITDB_PORT"])
    # Getters
    def get_host(self) -> str:
        return self.__host
    def get_user(self) -> str:
        return self.__user
    def get_password(self) -> str:
        return self.__password
    def get_port(self) -> str:
        return self.__port
    # Setters
    def set_host(self, host : str):
        self.__host = host
    def set_user(self, user : str):
        self.__host = user
    def set_password(self, password : str):
        self.__host = password
    def set_port(self, port : str):
        self.__host = port
    # Connect to the db.
    def connection(self) -> object:
        print("Generando una nueva conexión a la base de datos...")
        return MongoClient("mongodb://{}:{}@{}:{}".format(self.get_user(), self.get_password(),self.get_host(), self.get_port()))

    # Store people information and then show their info.
    def save_people(self, people : dict):
        db = self.connection()['pipl']['people']
        print("Conexión realizada con éxito en:\nmongodb://{}:{}@{}:{}".format(self.get_user(), self.get_password(),self.get_host(), self.get_port()))
        post_id = db.insert_many(people['data'])
        cursor = db.find({})
        if cursor:
            for document in cursor:
                print(document)
        print("Se han registrado 100 personas en la base de datos...")
