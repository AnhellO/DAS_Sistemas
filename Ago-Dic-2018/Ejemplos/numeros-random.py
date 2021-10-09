import random, time

suertudos = [
    'Aleman Ortiz Javier Eduardo',
    'Almaguer Najera Mario Humberto',
    'Amaya Lopez Edson Gerardo',
    'Briones Esquivel Patricia Isabel',
    'Castro Torres Maria Guadalupe',
    'Cavazos Nelson Saul Alejandro',
    'Cedillo Aparicio Cristina',
    'Cisneros Garcia Isaac Adrian',
    'Coronado Valdes Angel De Jesus',
    'De La Cruz Davila Jesus Salvador',
    'Diaz Delabra Erick',
    'Fernandez Salinas Cristian Alejandro',
    'Ferrer Ferrer Francisco Antonio',
    'Flores Hernandez Juan Arnulfo',
    'Hernandez Saucedo Damian Rafael',
    'Ibarra Espinoza Luis Alberto',
    'Moncada Lara Jesus Uriel',
    'Rodriguez Martinez Jose Adrian',
    'Suarez Villanueva Sergio Armando',
    'Valera Rangel Pablo',
    'Vazquez Herrera Adrian Led',
    'Viera Rodriguez David',
]

patterns = [
    'Factory Method',
    'Abstract Factory',
    'Builder',
    'Prototype',
    'Singleton',
    'Adapter',
    'Bridge',
    'Composite',
    'Decorator',
    'Facade',
    'Flyweight',
    'Proxy',
    'Chain of Responsibility',
    'Command',
    'Iterator',
    'Mediator',
    'Memento',
    'Observer',
    'State',
    'Strategy',
    'Template Method',
    'Visitor',
]

rand = random.sample(range(0, len(suertudos)), len(suertudos))
rand2 = random.sample(range(0, len(patterns)), len(patterns))

for i in rand:
    print('Acá va un suertudo >:D...')
    time.sleep(2)
    print('-> {}'.format(suertudos[i]))

for i in rand2:
    print('Y acá su patrón!')
    time.sleep(2)
    print('-> {}'.format(patterns[i]))