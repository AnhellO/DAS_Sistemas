import requests
import mysql.connector
from abc import ABC,abstractmethod

#****************[ The Abstract Factory interface ]**************
#declares a set of methods that return
#different abstract products.
class DBases(ABC):
    @abstractmethod
    def register(self):
        pass
    
    @abstractmethod
    def imprimir(self):
        pass


#*******************[ Concrete Factories ]*********************
#produce a family of products that belong to a single
#variant.
class Conects(DBases):
    def register(self):
        return TotalRegister() #product retangle
    
    def imprimir(self):
        return TotalPrint() #producto perimeter   


#****************[ The Abstract Factory interface ]**************
#   Product Register
class Register(ABC):
    @abstractmethod
    def FuctionRegister(self):
        pass


""" Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
"""
class TotalRegister(Register):
    def FuctionRegister(self,users,conn):
        # la variable conn almacena la conexión de la base de datos
        print(conn)
        cur = conn.cursor()
        # creamos un ciclo para poder pasar los datos de la API a unas variables
        for user in users:
            Url = user['url']
            titulo = user['title']
            Autor = user['user']['login']
            State = user['state']
            Number = user['number']
            
            # con este if identificamos si esta vacio o no
            # asi nos eviamos de algunos errores
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

            #insertamos los usuarios a la base de datos
            sql = "INSERT INTO repos(url,numero,titulo,autor,tags,estado,miletítulo,miledesc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (f'{Url}',f'{Number}',f'{titulo}',f'{Autor}',f'{Tags}',f'{State}',f'{Milestone_Title}',f'{Milestone_Desc}')
            cur.execute(sql,val)
            conn.commit()
            print(cur.rowcount, "registro insertado")
        return f"{cur.rowcount} registro insertado"
           
    
#****************[ The Abstract Factory interface ]**************
#   Product Print
class view(ABC):
    @abstractmethod
    def FuctionPrints(self):
        pass


class TotalPrint(view):
    def FuctionPrints(self,conn):
        # nos conectamos a la base de datos mediante la variable que la almacena
        print(conn)
        cur = conn.cursor()
        #consultamos los usuarios de la base de datos
        cur.execute( "SELECT * FROM repos")
        aux = cur.fetchall()
        return aux
         

#****************[ The client code ]**************
"""The client code works with factories and products only through abstract
   types: AbstractFactory and AbstractProduct.
"""
class Client:
    def ClientCode(self,abtractfactory,users,conn):
        #instanciamos a las variables con su abtrafactory y su función
        register = abtractfactory.register()
        printss = abtractfactory.imprimir()
        
        # escojemos que opción usar si registrar o consultar
        check = int(input("Resgistrar Issue (0), Consultar Issue (1)\nOpción: "))
        if check == 0:
            print("========== [ Registros ] ==========")
            print(register.FuctionRegister(users,conn))
        else:
            print("========== [ Consultas ] ==========")
            #print(printss.FuctionPrints(conn))
            aux = printss.FuctionPrints(conn)
            for i in range(len(aux)):
                #return f"\n****** Issue #{Number} ******\n- URL: {Url}\n- Título: {titulo}\n- Autor: {Autor}\n- Tags: {Tags}\n- Estado: {State}\n- Milestone:\n  - Título: {Milestone_Title}\n  - Descripción: {Milestone_Desc}"
                print(f"\n****** Issue #{aux[i][2]} ******")
                print(f"- URL: {aux[i][1]}")
                print(f"- Título: {aux[i][3]}")
                print(f"- Autor: {aux[i][4]}")
                print(f"- Tags: {aux[i][5]}")
                print(f"- Estado: {aux[i][6]}")
                print(f"- Milestone:\n  - Título: {aux[i][7]}\n  - Descripción: {aux[i][8]}")
            

if __name__ == "__main__":
    # obtenemos una petición a la API d github
    url = "https://api.github.com/repos/pallets/flask/issues?q=is%3Aissue+is%3Aclosed"
    users = requests.get(url).json()
    
    # la conexión a la base de datos
    conn = mysql.connector.connect(user='user',password='pass1234',host='localhost',database='prueba',port='3306')
    
    # instanciamos la clase cliente
    client = Client()
    client.ClientCode(Conects(),users,conn)
    
    
    
    
    