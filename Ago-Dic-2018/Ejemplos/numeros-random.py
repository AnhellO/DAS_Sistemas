import random, time

suertudos = [
    'CAMPOS GONZALEZ RUBEN',
    'ENRIQUEZ CARRIZALES DANIEL DE JESUS',
    'GARCIA DE SANTIAGO MAXIMILIANO',
    'GARCIA MUÑOZ JESUS ARMANDO',
    'GUTIERREZ GARCIA CYNTHIA NEFTALI',
    'LOPEZ MEZA ANDRES',
    'MARTINEZ MEDINA ORLANDO MIGUEL',
    'ONTIVEROS PERALES ALMA DANIELA',
    'PEREZ MONTES DAVID ISRAEL',
    'PEREZ MORIN GENESIS D.',
    'RODRIGUEZ GARCIA ANGELA ARACELY',
    'VÁZQUEZ SECA CLAUDIA ABELINA',
    'VELA TORRALBA ERNESTO'
]

rand = random.sample(range(0, len(suertudos)), len(suertudos))

for i in rand:
    print('Acá va un suertudo >:D...')
    time.sleep(2)
    print('-> {}'.format(suertudos[i]))
