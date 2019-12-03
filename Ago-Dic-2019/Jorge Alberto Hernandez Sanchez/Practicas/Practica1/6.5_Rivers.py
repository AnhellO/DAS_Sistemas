rivers = {'nile' : "Egipto", 'rin' : "Alpes Suizos", 'ganges' : "Himalaya Occidental"}

for rios in rivers.values():
    print("El rio", rios, "atraviesa ", rios.title())
print("------------------------------------------------")
for rio in rivers:
    print(rio.title())
print("------------------------------------------------")
for river in rivers.values():
    print(river.title())