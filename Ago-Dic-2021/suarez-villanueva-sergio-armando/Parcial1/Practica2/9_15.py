import queue
from collections import OrderedDict

Doc=open("P9_15_data.txt","r")
ClientDat = Doc.readlines()
Datos = []
for i in ClientDat:
    Datos.append(i.split())
Doc.close()

class Services():
    def __init__(self):
        self.SL = OrderedDict()
        self.SL[1] = 'Retiro'
        self.SL[2] = 'Depósito'
        self.SL[3] = 'Estado de cuenta'
        self.SL[4] = 'Apertura de cuenta'
        self.SL[5] = 'Cancelación de cuenta'
    
    def Get_Service(self, index):
        return self.SL[index]

class ServMeth():
    
    def Retiro(self,Cant, nom):
        return (str(nom) + " ha retirado $" + str(Cant))
    
    def Depos(self,Cant, nom):
        return(str(nom) + " ha depositado $" + str(Cant))
               
    def Estado(self,Nom):
        return("El estado de cuenta de " + Nom + " es de $100")
    
    def Apert(self,Nom,Num):
        return("Se ha abierto la cuenta de " + Nom + " con un balance de $" + str(Num))
    
    def Cance(self,Nom):
        return("Se ha cancelado la cuenta de " + Nom)
    
ServiceList = Services()    

class Client():
    
    def __init__(self, Turn, name, Lname, Service, Dinero):
        self.Turn = Turn
        self.Name = name
        self.Apell = Lname
        self.Serv = Service
        self.Dinero = Dinero
    
    def Get_Client(self,ServiceL):
        data = "Nombre: " + str(self.Name)+ "  " + str(self.Apell)
        data += "\nTurno: " + str(self.Turn) + "\nServicio: " + str(ServiceL.Get_Service(self.Serv))
        return data
    
    def Get4Cashier(self):
        data=[]
        data.append(self.Name)
        data.append(self.Serv)
        data.append(self.Dinero)
        return data

class Cashier():
    
    def __init__(self, name, ID):
        self.Name = name
        self.ID = ID
        self.ServMeth = ServMeth()
    
    def Check_Serv(self, Data):
        Methods = {
            1:self.ServMeth.Retiro(Data[-1], Data[0]),
            2:self.ServMeth.Depos(Data[-1], Data[0]),    
            3:self.ServMeth.Estado(Data[0]),
            4:self.ServMeth.Apert(Data[0],Data[-1]),
            5:self.ServMeth.Cance(Data[0])
            }
        s = str(Methods.get(Data[1]))
        return s
             
Cajero = Cashier("Jesus", 1)

ClientQ=queue.Queue()
for i in range(len(Datos)):
    ClientQ.put(Client(i+1,Datos[i][0],Datos[i][1],int(Datos[i][2]), int(Datos[i][3])))

while not ClientQ.empty():
    print(Cajero.Check_Serv(ClientQ.get().Get4Cashier()))
    '''Se llama al método que usa los métodos del cajero con los datos de los clientes'''