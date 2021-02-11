import os
import pymongo
from pymongo import MongoClient
import math
import random

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
        return MongoClient("mongodb://{}:{}@{}:{}".format(self.get_user(), self.get_password(),self.get_host(), self.get_port()))

    # Return random person information. 
    def get_random_person(self) -> dict:
        db = self.connection()['pipl']['people']
        total_documents = db.count()
        random_number = math.floor(random.randint(1, total_documents))
        person = db.find().limit(1).skip(random_number)[0]
        return person