from MySQLdb._mysql import connection

class DatabaseFactory:
    def database_connection(self):
        raise NotImplementedError()

class default(DatabaseFactory):
    def default_connection(self):
        return defaultDatabase()

class oracle_connection(DatabaseFactory):
    def database_connection(self):
        return oracle()

class mongo(DatabaseFactory):
    def database_connection(self):
        return connection.get_database_connection()

class mysql:
    def MySqlDatabase(self):
        return 'Connected to MySQL'

    def database_connection(self):
        return connection.get_database_connection()

class oracle:
    def OracleDatabase(self):
        return 'Connected to Oracle', connection.get_database_connection()

class MongoDatabase:
    def database_connection(self):
        return 'Connected to MongoDB'

class MySqlDatabase:
    def database_connection(self):
        return 'Connected to MySQL', connection.get_database_connection()

class defaultDatabase:
    def database_connection(self):
        return 'Connected to MySQL', connection.get_database_connection()