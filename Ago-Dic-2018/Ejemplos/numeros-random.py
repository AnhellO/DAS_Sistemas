import random, time

suertudos = [
    'BUCIO MONTES HECTOR DANIEL',
    'FLORES PARDO NOEMI ESTHER',
    'GONGORA TREVIÑO JOSE HORACIO',
    'HERNANDEZ SANCHEZ JORGE ALBERTO',
    'LLANES NAVA LUIS OSVALDO',
    'MEDINA MARTINEZ JUAN IVAN',
    'MONTOYA MARTINEZ ERIK EDUARDO',
    'ONOFRE SUAREZ JOSE EDUARDO',
    'ROMERO MEDINA RICARDO FRANCISCO',
]

rand = random.sample(range(0, len(suertudos)), len(suertudos))

for i in rand:
    print('Acá va un suertudo >:D...')
    time.sleep(2)
    print('-> {}'.format(suertudos[i]))
