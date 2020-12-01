import random, time

suertudos = [
    'Aguilar Cedillo Jonathan Ivan',
    'Aguirre Juarez David',
    'Castro Torres Maria Guadalupe',
    'Cedillo Aparicio Cristina',
    'Chavez Muñoz Juan Arnoldo',
    'Escarcega Ramirez Erick Orlando',
    'Flores Fernandez Fernando',
    'Gonzalez Cardenas Jesus Antonio',
    'Lopez Flores Jorge Luis',
    'Morin Hinojosa Esly Abigail',
    'Perez Sanchez Jose Jahir',
    'Rodriguez Martinez Diego Jose',
    'Rodriguez Martinez Jesus Angel',
    'Salazar Coronado Juan Daniel',
    'Sena Martinez Angel David',
]

rand = random.sample(range(0, len(suertudos)), len(suertudos))

for i in rand:
    print('Acá va un suertudo >:D...')
    time.sleep(2)
    print('-> {}'.format(suertudos[i]))
