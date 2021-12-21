import pytest
import requests
import mysql.connector
from getAPI import *

class TestGetAPIPytest:
    #NO se puede instanciar una clase abtracta
    """def test_DBases(self):
        dbases = DBases()
        assert dbases.register()
        assert dbases.imprimir()
    """
    
    # test de la interfaz conects
    def test_Conects(self):
        conects = Conects()
        assert conects.register()
        assert conects.imprimir()

#*********** [ test of register y prints ] ****************
    
    def test_TotalRegister(self):
        register = TotalRegister()
        
        url = "https://api.github.com/repos/pallets/flask/issues?q=is%3Aissue+is%3Aclosed"
        users = requests.get(url).json()
        conn = mysql.connector.connect(user='user',password='pass1234',host='localhost',database='prueba',port='3306')
        #print(conn)
        #num = int(len(register.FuctionRegister(users,conn)))
        assert "1 registro insertado" == register.FuctionRegister(users,conn)

    
    def test_TotalPrint(self):
        printss = TotalPrint()
        conn = mysql.connector.connect(user='user',password='pass1234',host='localhost',database='prueba',port='3306')
        cur = conn.cursor()
        #consultamos los usuarios de la base de datos
        cur.execute( "SELECT * FROM repos")
        aux = cur.fetchall()
        assert aux == printss.FuctionPrints(conn)
        
        
        
        
        
        
        
        
        
        
        
        
        
        