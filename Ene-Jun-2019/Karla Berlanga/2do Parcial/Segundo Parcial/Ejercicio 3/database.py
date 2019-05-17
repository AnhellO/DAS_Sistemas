import sqlite3

class DataBase():

    def __init__(self, file):
        self.connection = sqlite3.connect(file)

    def CreateTable(self):
        # Se crea la base de datos
        cursor = self.connection.cursor()
        try:
            # Se verifica que la tabla no exista. Se crea la tabla
            cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      title text,
                                      first text,
                                      last text,
                                      gender int,
                                      birthday text,
                                      age int,
                                      phone text,
                                      email text,
                                      street text,
                                      city text,
                                      state text
                                )""")
            return ("LA TABLA users SE CREÓ EXITOSAMENTE")

        except sqlite3.OperationalError:
            return ("OCURRIÓ UN ERROR")

        self.connection.commit()


    def SaveUser(self, user):
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()
        # Se hace la siguiente consulta para verificar que el usuario no este duplicado, se hace mediante el email

        cursor.execute('''SELECT email FROM users WHERE email = "{}"'''.format(user.email))
        # Se guarda el resultado de la consulta anterior en la variable resultados, puede contener un email o None
        resultados = cursor.fetchone()


        if resultados is None:
            # Si el email=None, se inserta el usuario
            parametros = {
            'TITLE':user.title,
            'FIRST': user.first,
            'LAST':user.last,
            'GENDER': 0 if user.gender=='female' else 1,
            'BIRTHDAY': user.date,
            'AGE':int(user.age),
            'PHONE': user.phone,
            'EMAIL': user.email,
            'STREET': user.street,
            'CITY':user.city,
            'STATE': user.state
            }
            try:
                cursor.execute( "INSERT INTO users (id, title, first, last, gender, birthday, age, phone, email, street, city, state) VALUES(null,:TITLE,:FIRST,:LAST,:GENDER,:BIRTHDAY,:AGE,:PHONE,:EMAIL,:STREET,:CITY,:STATE);", parametros)
                print("EL USUARIO {} {} SE INSERTÓ EXITOSAMENTE A LA BASE DE DATOS".format(user.first,user.last))
            except:
                return("ERROR AL INSERTAR EL USUARIO A LA BASE DE DATOS")
            self.connection.commit()
        else:
            return "EL USUARIO {} {} YA EXISTE EN LA BASE DE DATOS".format(user.first,user.last)

def main():
    #Se crea la tabla
    db = DataBase('users.db')
    print(db.CreateTable())

if __name__ == '__main__':
    main()
