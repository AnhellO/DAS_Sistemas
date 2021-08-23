class Vehiculo(object):
    random=50

    def __init__(self,velocidad_maxima,kilometraje,velocidad):
        self.velocidad_maxima=velocidad_maxima
        self.kilometraje=kilometraje
        self.velocidad=velocidad

    def tarifa(self,asientos:int=40):
        tarifa_inicial=asientos*100
        return tarifa_inicial


    def __str__(self)->str:
        return f"La velocidad maxima es {self.velocidad_maxima}, el kilometraje es {self.kilometraje}, la velocidad es {self.velocidad}"


class Autobus(Vehiculo):
    def __init__(self,velocidad_maxima,kilometraje,velocidad):
        Vehiculo.__init__(self,velocidad_maxima,kilometraje,velocidad)



if __name__=="__main__":
    a1=Autobus(150,25000,100)
    v1=Vehiculo(200,30000,120)
    a2=Autobus(158,55000,110)
    v2=Vehiculo(220,88000,120)
    lista_vehiculos=[a1,v1,a2,v2]

    for v in lista_vehiculos:
        if isinstance(v,Autobus):
            mantenimiento=v.tarifa()*.10
            tarifa_final=v.tarifa()+mantenimiento
            print(f"Soy un autobus! -> {v}, mi tarifa total es {tarifa_final}")
