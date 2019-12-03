rios={
    'Rio Amazonas':'Peru,Colombia y Brasil',
    'Rio Misisipi':'Minesota, Wisconsin, Iowa, Misuri, Illinois, Kentucky, Tennessee, Arkansas, Misisipi y Luisiana',
    'Rio Nilo':'Egipto'
}

rio=rios.keys()
estado=rios.values()
ele=rios.items()

for rio,estado in ele:
    print("El ", rio ," atraviesa a ", estado)

for rio in rios:
    print(rio)

for estado in rios:
    print(estado)