import unittest

from factory_method import *

class FactoryTest(unittest.TestCase):
    def test_mongo_connection(self):
        mongo = MongoDatabase()
        connection = DatabaseFactory(mongo)
        self.assertEqual('Connected to MongoDB.', connection.get_database_connection())
    
    def test_oracle_connection(self):
        oracle = OracleDatabase()
        connection = DatabaseFactory(oracle)
        self.assertEqual('Connected to Oracle.', connection.get_database_connection())
    
    def test_mysql_connection(self):
        mysql = MySqlDatabase()
        connection = DatabaseFactory(mysql)
        self.assertEqual('Connected to MySQL.', connection.get_database_connection())
    
    def test_default_connection(self):
        connection = DatabaseFactory()
        self.assertEqual('Connected to MySQL.', connection.get_database_connection())

if __name__ == "__main__":
    unittest.main()
