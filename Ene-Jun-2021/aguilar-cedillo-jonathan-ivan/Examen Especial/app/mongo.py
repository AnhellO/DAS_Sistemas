import pymongo

#   CONEXION A BASE DE DATOS

MONGO_HOST='db'
MONGO_PORT='27017'
MONGO_USER='das-sistemas'
MONGO_PASS='eespecial-2021!'
MONGO_URI= "mongodb://{}:{}@{}:{}/".format(MONGO_USER, MONGO_PASS, MONGO_HOST,MONGO_PORT)
MONGO_TIMEOUT=15000
print(MONGO_URI)

def mongo():
    try:
        cliente=pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIMEOUT)
        return cliente
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido "+errorTiempo)
        return errorTiempo
    except pymongo.errors.ServerSelectionTimeoutError as errorConexion:
        print("Fallo al conectarse a mongodb "+errorConexion)
        return errorConexion
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Se nego la conexion "+errorConexion)
        return errorConexion
    except Exception as e:
        print(e)
