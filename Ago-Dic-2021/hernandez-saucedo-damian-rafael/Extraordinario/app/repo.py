import base64
import requests
import json
import mysql.connector
from github import Github
from pprint import pprint

"""""
username = "DamianRafael"
g = Github()

user = g.get_user(username)
rep = user.get_repo("damian")

open_issues = rep.get_issues(state='open')
labels = rep.get_labels()
#contents = rep.get_contents("") # obtener todo el contenido del repositorio

i = 0
for issue in open_issues:
    i +=1
    print(str(i)," - ",issue)
"""

class Reposs:
    
    def __init__(self,users,conn):
        self.users = users
        self.conn = conn
        
    
    def registro(self):
        # creamos una caonexion con la bases de datos y hacemos una peticion a la api
        cur = self.conn.cursor()
        for user in self.users:
            Url = user['url']
            titulo = user['title']
            Autor = user['user']['login']
            State = user['state']
            Number = user['number']
            TagEmpty = Tags = user['labels']
            if not TagEmpty:
                Tags = "''"
            if TagEmpty:
                Tags = user['labels'][0]['name']
            MilestoneEmpty = user['milestone']
            if not MilestoneEmpty:
                Milestone_Title = "''"
                Milestone_Desc = "''"
            if MilestoneEmpty:
                Milestone_Title = user['milestone']['title']
                Milestone_Desc = user['milestone']['description']

            # se llena la base de datos
            sql = "INSERT INTO extra(numero,Url,titulo,autor,tags,estado,miletítulo,miledesc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (f'{Number}',f'{Url}',f'{titulo}',f'{Autor}',f'{Tags}',f'{State}',f'{Milestone_Title}',f'{Milestone_Desc}')
            cur.execute(sql,val)
            self.conn.commit()
            print("registrado")
        return f"registrado"
    
    # consulta de la base de datos
    def imprimir(self):
        cur = self.conn.cursor()
        cur.execute( "SELECT * FROM repos")
        aux = cur.fetchall()
        for i in range(len(aux)):
            URL = aux[i][1]
            number = aux[i][2]
            Titulo = aux[i][3]
            Autor = aux[i][4]
            Tags = aux[i][5]
            Estado = aux[i][6]
            Milestone_title = aux[i][7]
            milestone_desc= aux[i][8]
            print(f"\n****** Issue #{number} ******")
            print(f"- URL: {URL}")
            print(f"- Título: {Titulo}")
            print(f"- Autor: {Autor}")
            print(f"- Tags: {Tags}")
            print(f"- Estado: {Estado}")
            print(f"- Milestone:")
            print(f"  - Título: {Milestone_title}")
            print(f"  - Descripción: {milestone_desc}")
        return "lista consultada"


if __name__ == '__main__':
    url = "https://api.github.com/repos/pallets/flask/issues"
    users = requests.get(url).json()
    # la conexión a la base de datos
    conn = mysql.connector.connect(user='user',password='pass1234',host='localhost',database='prueba',port='3306')
    
    repository = Reposs(users,conn)
    r = input("Registrar / Consultar (y/n): ")
    if r == "y":
        repository.registro()
    else:
        repository.imprimir()
    