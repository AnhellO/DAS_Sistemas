import psycopg2
import json
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#def connect__to_database():
try:
    conn = psycopg2.connect(database="examen", user="admin", password="123abc", host="localhost", port=5432)
    #return conn 
    print("Jaló la conexion")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    #return False
#connect__to_database()

#conn = psycopg2.connect(user = "admin",password = "123abc", port = "5432", database = "examen")
conn = psycopg2.connect(database="examen", user="admin", password="123abc", host="localhost", port=5432)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor1=conn.cursor()


# # sqlCreateDatabase = "CREATE DATABASE examen"
# # cursor1.execute(sqlCreateDatabase)


cre_table =  """
        CREATE TABLE personas (
            id INT PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            age VARCHAR(255) NOT NULL,
            company VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            eye_color VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            registered VARCHAR(255) NOT NULL,
            about VARCHAR(800) NOT NULL
        )
        """
cursor1.execute(cre_table)


with open('data.json') as json_file:
    data = json.load(json_file)
    count = 0
    for p in data:
       id = int(p['index']+1)
       first_name = p['name']['first']  
       last_name =  p['name']['last']
       age = p['age']
       company = p['company']
       email = p['email']
       eye_color = p['eyeColor']
       address = p['address']
       registered = p['registered']
       about = p['about']   
       sql_insert = f"INSERT INTO personas VALUES('{id}', '{first_name}', '{last_name}', '{age}', '{company}', '{email}', '{eye_color}', '{address}', '{registered}', '{about}')"
       cursor1.execute(sql_insert)
       #cursor1.execute("INSERT INTO personas (id, first_name, last_name, age, company, email, eye_color, address, registered, about) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (id, first_name, last_name, age, company, email, eye_color, address, registered, about))
       #postgres_insert_query = """ INSERT INTO personas (id, first_name, last_name, age, company, email, eye_color, address, registered, about) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
       #record_to_insert = (id, first_name, last_name, age, company, email, eye_color, address, registered, about)
#        query = """INSERT INTO personas (id, first_name, last_name, age, company, email, eye_color, address, registered, about)
# VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"""
       #cursor1.execute(postgres_insert_query, record_to_insert)


def consulta_poke():
    cursor1.execute('SELECT * FROM public.personas')
    for row in cursor1:
        print(row)

consulta_poke()