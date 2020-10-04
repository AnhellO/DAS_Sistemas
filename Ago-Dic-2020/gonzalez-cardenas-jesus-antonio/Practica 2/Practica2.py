class Vehiculo(object):
    def __init__(self, name, date_of_release, passengers, number_of_wheels, terrain, type_of_vehicle):
        self.name = name
        self.date_of_release = date_of_release
        self.passengers = passengers
        self.number_of_wheels = number_of_wheels
        self.terrain = terrain
        self.type_of_vehicle = type_of_vehicle

    def specs(self):
        print(f"{self.name} salió en la fecha: {self.date_of_release}, tiene el número de llantas: {self.number_of_wheels} y es para el terreno tipo: {self.terrain}")
        print('Numero de pasajeros = ' + str(self.passengers))

    def movev(self, km):
        print(f"{self.name} se ha movido {km} unidades")

    def stop(self):
        print(self.name +' se ha detenido')

class Camion(Vehiculo):
    numero_actual_de_pasajeros = 0
    cuenta = 0.000
    cobro = 0.000
    def __init__(self, name, date_of_release, passengers, number_of_wheels, terrain, type_of_vehicle,):
        super().__init__(name, date_of_release, passengers, number_of_wheels, terrain, type_of_vehicle)

    def SubePasajero (self, numero_de_pasajeros_que_subieron):
        numero_de_pasajeros_que_subieron = int(numero_de_pasajeros_que_subieron)
        caja  = float(numero_de_pasajeros_que_subieron) * self.cobro
        self.cuenta = self.cuenta + caja
        self.numero_actual_de_pasajeros = self.numero_actual_de_pasajeros + numero_de_pasajeros_que_subieron
        print(f"Se han subido {numero_de_pasajeros_que_subieron}, se ha ingresado: {caja}")

    def BajaPasajero(self, numero_de_pasajeros_que_bajaron):
        self.numero_actual_de_pasajeros = self.numero_actual_de_pasajeros - numero_de_pasajeros_que_bajaron
        print(f"Se han bajado {numero_de_pasajeros_que_bajaron}")

    def CamionStatus(self):
        print(f"Hay {self.numero_actual_de_pasajeros} actualmente en el camión y hay {self.cuenta} en la cuenta")

    def SetCuota(self,cta):
        cta = float(cta)
        self.cobro = cta

class Jet(Vehiculo):
    def __init__(self, name, date_of_release, passengers, number_of_wheels, terrain, type_of_vehicle, mg_ammo, missile_ammo):
        self.mg_ammo = mg_ammo
        self.missile_ammo = missile_ammo
        super().__init__(name, date_of_release, passengers, number_of_wheels, terrain, type_of_vehicle)

    def ShootMG(self,shoots):
        if shoots > self.mg_ammo:
            data1 = shoots - self.mg_ammo
            print(f"No se pueden hacer la cantidad de disparos solicitados, faltan {data1} unidades de munición")
        else:
            self.mg_ammo = self.mg_ammo - shoots
            print(f"Se ha disparado satisfactoriamente, se usaron {shoots} unidades de munición")

    def ShootMissiles(self,shoots):
        if shoots > self.missile_ammo:
            data1 = shoots - self.missile_ammo
            print(f"No se pueden hacer la cantidad de disparos solicitados, faltan {data1} misiles")
        else:
            self.missile_ammo = self.missile_ammo - shoots
            print(f"Se ha disparado satisfactoriamente, se usaron {shoots} misiles")

    def JetStatus(self):
        print(f"Munición de MG = {self.mg_ammo}")
        print(f"Munición de Misiles = {self.missile_ammo}")

    def SendMessageToBase(self, mess):
        print(f"Tu mensaje {mess} ha sido recibido por nuestra base")   
        

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


