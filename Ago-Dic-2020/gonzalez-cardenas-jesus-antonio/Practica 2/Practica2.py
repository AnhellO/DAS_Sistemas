class Vehiculo(object):
    def __init__ (self, name, dateRelease, passengers, numOfWheels, terrain, typeVehicle):
        self.name = name
        self.dateRelease = dateRelease
        self.passengers = passengers
        self.numOfWheels = numOfWheels
        self.terrain = terrain
        self.typeVehicle = typeVehicle

    def specs(self):
        print(self.name+' salió en la fecha '+ self.dateRelease +', tiene el número de llantas: ' +str(self.numOfWheels) +'. Y es para el terreno tipo: ' +self.terrain)
        print('Numero de pasajeros = ' + str(self.passengers))

    def movev(self, km):
        print(self.name +' se ha movido ' + str(km)+' unidades')

    def stop(self):
        print(self.name +' se ha detenido')

class Camion(Vehiculo):
    NumActualDePasajeros = 0
    Cuenta = 0.000
    cobro = 0.000
    def __init__ (self, name, dateRelease, passengers, numOfWheels, terrain, typeVehicle,):
        Vehiculo.__init__(self, name, dateRelease, passengers, numOfWheels, terrain, typeVehicle)

    def SubePasajero (self, numSub):
        numSub = int(numSub)
        caja  = float(numSub) * self.cobro
        self.Cuenta = self.Cuenta + caja
        self.NumActualDePasajeros = self.NumActualDePasajeros + numSub
        print('Se han subido ' +str(numSub)+ ', se ha ingresado:'+str(caja))

    def BajaPasajero(self, numBaj):
        self.NumActualDePasajeros = self.NumActualDePasajeros - numBaj
        print('Se han bajado ' +str(numBaj))

    def CamionStatus(self):
        print('Hay '+str(self.NumActualDePasajeros)+' actualmente en el camión y hay '+str(self.Cuenta)+' en la cuenta')

    def SetCuota(self,cta):
        cta = float(cta)
        self.cobro = cta

class Jet(Vehiculo):
    def __init__ (self, name, dateRelease, passengers, numOfWheels, terrain, typeVehicle, MGAmmo, MissileAmmo):
        self.MGAmmo = MGAmmo
        self.MissileAmmo = MissileAmmo
        Vehiculo.__init__(self, name, dateRelease, passengers, numOfWheels, terrain, typeVehicle)

    def ShootMG(self,Shoots):
        if Shoots > self.MGAmmo:
            data1 = Shoots - self.MGAmmo
            print('No se pueden hacer la cantidad de disparos solicitados, faltan '+str(data1)+' unidades de munición')
        else:
            self.MGAmmo = self.MGAmmo - Shoots
            print('Se ha disparado satisfactoriamente, se usaron '+str(Shoots)+' unidades de munición')

    def ShootMissiles(self,Shoots):
        if Shoots > self.MissileAmmo:
            data1 = Shoots - self.MissileAmmo
            print('No se pueden hacer la cantidad de disparos solicitados, faltan '+str(data1)+' misiles')
        else:
            self.MissileAmmo = self.MissileAmmo - Shoots
            print('Se ha disparado satisfactoriamente, se usaron '+str(Shoots)+' misiles')

    def JetStatus(self):
        print('Munición de MG = ' +str(self.MGAmmo))
        print('Munición de Misiles = ' +str(self.MissileAmmo))

    def SendMessageToBase(self, mess):
        print('Tu mensaje "'+mess+ '" ha sido recibido por nuestra base')   
        

camion_uno = Camion('Mercedes-Benz O371', 'Decada de 1980', 28, 4, 'Urbano', 'Transporte publico')
jet_uno = Jet('F-22 Raptor', 'Año 2003', 1, 3, 'Aereo', 'Combate', 5000, 15)

camion_uno.specs()
camion_uno.movev(12)
camion_uno.stop()
camion_uno.SetCuota(11.5)
camion_uno.SubePasajero(5)
camion_uno.BajaPasajero(2)
camion_uno.CamionStatus()
print('\n')

jet_uno.specs()
jet_uno.movev(1000)
jet_uno.stop()
jet_uno.ShootMG(1000)
jet_uno.ShootMissiles(7)
jet_uno.JetStatus()
jet_uno.SendMessageToBase('Acabo de cometer un crimen de guerra')


