rivers = {

'Nilo':'Egipto',
'Rio Bravo':'NorteAmerica',
'Rio Amazonas':'Brasil'
}

for key,value in rivers.items():
    print("El rio "+key+" corre a traves de "+value)

print()

for key in rivers:
    print(key)

print()

for key,value in rivers.items():
    print(value)
