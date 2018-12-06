from abc import ABC, abstractmethod
import requests
import json
import sqlite3
from bs4 import BeautifulSoup
import random
import time

class Persona():

    def __init__(self, id, first, last, city, cellphone, email, age, gender, taqueria):

        self.id = id
        self.first = first
        self.last = last
        self.city = city
        self.cellphone = cellphone
        self.email = email
        self.age = age
        self.gender = gender
        self.taqueria = taqueria

    def comer(self, cantidad):
        print('{} ha empezado a comer sus {} taquitos con mucho amor\n'.format(self.first, cantidad))

    def ordenar_taquito(self):
        taquitoid = random.randint(1,50)
        cantidad = random.randint(2,12)
        db = sqlite3.connect(self.taqueria)
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO Orden (
                id_cliente,
                id_taco,
                Cantidad,
                Total)
            VALUES (
                :id_cliente,
                :id_taco,
                :cantidad,
                :total
            )''',
            {
            'id_cliente': self.id,
            'id_taco': taquitoid,
            'cantidad': cantidad,
            'total': 15 * cantidad
            }
        )
        db.commit()
        cursor.execute('''SELECT Nombre FROM Tacos WHERE Id = :id''', {'id': taquitoid})
        nombre = ''.join(cursor.fetchone())
        print('{} ha ordenado {} taquito(s) de {}, que rico! :O'.format(self.first, cantidad, nombre))
        return cantidad



class Taquito():

    def __init__(self, id, nombre, relleno, aderezo, salsa, sazonador, tortilla, precio):
        self.id = id
        self.nombre = nombre
        self.relleno = relleno
        self.aderezo = aderezo
        self.salsa = salsa
        self.sazonador = sazonador
        self.tortilla = tortilla
        self.precio = precio

class AbstractApiClients(ABC):

    @abstractmethod
    def get_clients():
        pass

class AbstractApiTaco(ABC):

    @abstractmethod
    def get_info():
        pass

class AbstractDb(ABC):

    @abstractmethod
    def createDB():
        pass

    @abstractmethod
    def insert_cliente():
        pass

    @abstractmethod
    def get_cliente():
        pass

    @abstractmethod
    def insert_ingrediente():
        pass

    @abstractmethod
    def insert_taco():
        pass


class ClientsApi(AbstractApiClients):

    def __init__(self,url):

        self.url = url

    def get_clients(self):

        request = requests.get(self.url, params = {'results': 30, 'nat': 'es'})
        if request.status_code == 200:
            listaclientes = request.json()
        else:
            print('Request Fallido')
        return listaclientes

class TacoApi(AbstractApiTaco):

    def __init__(self,url):

        self.url = url

    def get_info(self):

        request = requests.get(self.url)
        soup = BeautifulSoup(request.content, 'html.parser')

        nombretaco = soup.find('h1', attrs={'class': 'light'})
        nombretaco = nombretaco.text.strip()

        nombreing = soup.find_all('h5')[1].a.get('href')
        link = self.url + nombreing[1:]

        nombreing = nombreing.replace('/', ' ')
        inglist = nombreing.split()

        contribuidores = soup.find_all('h6')
        contlist = []
        for contribuidor in contribuidores:
            resultado = contribuidor.text.strip()
            contlist.append(resultado)

        recetas = soup.find_all('div', attrs={'class': 'recipe'})
        recipelist = []
        for recipe in recetas:
            location = recipe.text.find('tags')
            result = recipe.text[:location].strip()
            recipelist.append(result)

        tags = soup.find_all('div', attrs={'class': 'recipe'})
        taglist = []
        for tag in tags:
            location = tag.text.find('tags')
            res = tag.text[location:].rstrip()
            taglist.append(res)
        #time.sleep(1)
        return nombretaco, link, inglist, contlist, recipelist, taglist


class Sqlite(AbstractDb):

    def __init__(self,dbname):

        self.dbname = dbname

    def createDB(self):

        db = sqlite3.connect(self.dbname)
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Ingredientes (
	           Nombre TEXT NOT NULL,
	           Receta TEXT,
	           Contribuidores TEXT,
	           Tags TEXT,
	           PRIMARY KEY(Nombre)
               );'''
        )
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clientes (
	           Id INTEGER PRIMARY KEY AUTOINCREMENT,
	           Nombre TEXT,
	           Apellido TEXT,
	           Ciudad TEXT,
	           Celular TEXT,
	           Email TEXT,
	           Edad INTEGER,
	           Genero TEXT
               );'''
        )
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tacos (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Link TEXT,
                Nombre TEXT,
                Relleno	TEXT,
                Aderezo	TEXT,
                Salsa TEXT,
                Sazonador TEXT,
                Tortilla TEXT,
	            Precio INTEGER,
                FOREIGN KEY(Salsa) REFERENCES Ingredientes(Nombre),
                FOREIGN KEY(Aderezo) REFERENCES Ingredientes(Nombre),
                FOREIGN KEY(Tortilla) REFERENCES Ingredientes(Nombre),
                FOREIGN KEY(Sazonador) REFERENCES Ingredientes(Nombre),
                FOREIGN KEY(Relleno) REFERENCES Ingredientes(Nombre)
                );'''
        )
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Orden (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INTEGER,
                id_taco INTEGER,
                Cantidad INTEGER,
                Total INTEGER,
                Status TEXT,
                FOREIGN KEY(id_taco) REFERENCES Tacos(Id),
                FOREIGN KEY(id_cliente) REFERENCES Clientes(Id)
                );'''
        )
        db.commit()
        db.close()

    def insert_cliente(self, listaclientes):

        db = sqlite3.connect(self.dbname)
        cursor = db.cursor()

        for i in range(0, len(listaclientes['results'])):
            cursor.execute('''
				INSERT INTO clientes (
                    Nombre,
                    Apellido,
                    Ciudad,
                    Celular,
                    Email,
                    Edad,
                    Genero)
                VALUES (
					:nombre,
					:apellido,
					:ciudad,
					:celular,
					:email,
					:edad,
					:genero
				)''',
				{
				'nombre': listaclientes['results'][i]['name']['first'],
				'apellido': listaclientes['results'][i]['name']['last'],
				'ciudad': listaclientes['results'][i]['location']['city'],
				'celular': listaclientes['results'][i]['cell'],
				'email': listaclientes['results'][i]['email'],
				'edad': listaclientes['results'][i]['dob']['age'],
				'genero': listaclientes['results'][i]['gender']
				}
			)
        db.commit()
        db.close()

    def get_cliente(self):

        db = sqlite3.connect(self.dbname)
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM clientes''')
        clientes = cursor.fetchall()
        cliente = random.choice(clientes)
        objeto = Persona(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5], cliente[6], cliente[7], self.dbname)
        return objeto

    def insert_ingrediente(self, info):
        db = sqlite3.connect(self.dbname)
        cursor = db.cursor()


        for i in range(len(info[2])):
            cursor.execute('''
                SELECT * FROM Ingredientes
                WHERE Nombre = :nombre
                ''',
                {
                'nombre': info[2][i]
                })
            if cursor.fetchall() == []:
                cursor.execute('''
                    INSERT INTO Ingredientes (
                        Nombre)
                    VALUES (
                        :nombre
                    )''',
                    {
                    'nombre': info[2][i]
                    }
                )
        db.commit()

        for i in range(len(info[3])):

            cursor.execute('''UPDATE Ingredientes SET Contribuidores = :contribuidores WHERE Nombre = :nombre''',{'contribuidores': info[3][i], 'nombre': info[2][i]})
            db.commit()

        for i in range(len(info[4])):
            cursor.execute('''UPDATE Ingredientes SET Receta = :receta WHERE Nombre = :nombre''',{'receta': info[4][i], 'nombre': info[2][i]})
            db.commit()

        for i in range(len(info[5])):
            cursor.execute('''UPDATE Ingredientes SET Tags = :tags WHERE Nombre = :nombre''',{'tags': info[5][i], 'nombre': info[2][i]})
            db.commit()


        db.close()

    def insert_taco(self,info):

        db = sqlite3.connect(self.dbname)
        cursor = db.cursor()

        cursor.execute('''
            SELECT * FROM Tacos
            WHERE Nombre = :nombre
            ''',
            {
            'nombre': info[0]
            })

        if cursor.fetchall() == []:
            cursor.execute('''
                INSERT INTO Tacos (
                    Nombre)
                VALUES (
                    :nombre
                )''',
                {
                'nombre': info[0]
                }
            )
        db.commit()

        cursor.execute('''UPDATE Tacos SET Link = :link WHERE Nombre = :nombre''',{'link': info[1], 'nombre': info[0]})
        db.commit()

        cursor.execute('''UPDATE Tacos SET Relleno = :relleno, Aderezo = :aderezo, Salsa = :salsa, Sazonador = :sazonador, Tortilla = :tortilla
                        WHERE Nombre = :nombre''',{'relleno': info[2][0], 'aderezo': info[2][1], 'salsa': info[2][2], 'sazonador': info[2][3],
                        'tortilla': info[2][4], 'nombre': info[0]})
        db.commit()

        cursor.execute('''UPDATE Tacos SET Precio = :precio WHERE Nombre = :nombre''',{'precio': 15, 'nombre': info[0]})
        db.commit()
