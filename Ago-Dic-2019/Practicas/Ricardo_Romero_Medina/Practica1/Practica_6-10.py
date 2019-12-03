personas={
    'Jose':[15,38,49,75],
    'Osvaldo':[20,26,32,12],
    'Diego':[10,94,78,55],
    'Onofre':[15,12,33,59],
    'Jorge':[60,99,39,49]
}

nombre=personas.keys()

numero=personas.values()

val=personas.items()

for nombre,numero in val:
    print("Los numeros favoritos de ",nombre," son ",numero)