from abc import ABC, abstractmethod

class DataBaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

class MongoDatabase(DataBaseInterface):
    def connect(self):
        return 'Connected to MongoDB.'

class OracleDatabase(DataBaseInterface):
    def connect(self):
        return 'Connected to Oracle.'

class MySqlDatabase(DataBaseInterface):
    def connect(self):
        return 'Connected to MySQL.'

class DatabaseFactory:
    def __init__(self, database: DataBaseInterface = MySqlDatabase()):
        self.database = database

    def get_database_connection(self):
        return self.database.connect()