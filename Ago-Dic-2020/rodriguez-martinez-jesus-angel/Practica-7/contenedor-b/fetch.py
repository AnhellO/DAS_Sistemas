from db import Db
from api import Api

if __name__ == '__main__':
    print("Insertando registros en la base de datos...")
    # Obtains people information.
    people = Api().get_people()
    # Stores people information.
    Db().save_people(people)