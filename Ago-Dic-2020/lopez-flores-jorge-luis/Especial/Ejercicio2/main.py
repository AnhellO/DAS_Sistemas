from Autobus import *
eleccion=random.choice(tipos)
if eleccion == 'coche':
        coche = Autobus(200, 15000, 5)
        tarifa= coche.capacidad * 100
        print('Soy un auto', coche)
        print ('Mi tarifa total es de:', tarifa)

elif eleccion == 'autobus':
        autobus = Autobus(250, 30000, 40)
        camion = autobus.capacidad * 100
        tarifa = camion + (camion*0.1)
        print('Soy un autobus',autobus)
        print ('Mi tarifa total es de:', tarifa)

else:
        trailer = Autobus(300, 300000, 6 )
        tarifa = trailer.capacidad * 100
        print('Soy un trailer',trailer)
        print('mi tarifa total es de:', tarifa)



