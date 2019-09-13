ciudad={
    'Paris':{
        'Pais':'Francia',
        'Poblacion':'67,028,048 habitantes',
        'Hechos':'Tiene una superficie de 675,417 km',
    },
    'Tokyo':{
        'Pais':'Japon',
        'Poblacion':'9,273,000 habitantes',
        'Hechos':'Tiene una superficie de 406,58 km',
    },
    'Barcelona':{
        'Pais':'España',
        'Poblacion':'1,620,324 habitantes',
        'Hechos':'Tiene una superficie de 102,15 km',
    }
}

pais=ciudad.keys()

info=ciudad.values()

val=ciudad.items()

for pais,info in val:
    print(pais,info)