import pytest
import requests
import mysql.connector
from repo import *


class TestGetAPIPytest:
    
    # teste de repo
    def test_repos(self):
        url = "https://api.github.com/repos/pallets/flask/issues"
        users = requests.get(url).json()
        conn = mysql.connector.connect(user='user',password='pass1234',host='localhost',database='prueba',port='3306')
        repos = Reposs(users,conn)
        assert repos.registro()
        assert repos.imprimir()
        
    # test registro
    def test_registro(self):
        url = "https://api.github.com/repos/pallets/flask/issues"
        users = requests.get(url).json()
        conn = mysql.connector.connect(user='user',password='pass1234',host='localhost',database='prueba',port='3306')
        res = Reposs(users,conn)
        assert "registrado" == res.registro()
    
    # test imprimir
    def test_imprimir():
        url = "https://api.github.com/repos/pallets/flask/issues"
        users = requests.get(url).json()
        conn = mysql.connector.connect(user='user',password='pass1234',host='localhost',database='prueba',port='3306')
        imp = Reposs(users,conn)
        assert "lista consultada" == imp.imprimir()
    
    
        