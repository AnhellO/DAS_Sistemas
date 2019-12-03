Ciudades=['Saltillo', 'Monterrey', 'Piedras Negras', 'San Pedro', 'Guadalajara']

print(Ciudades[0].title())
print(Ciudades[1].title())
print(Ciudades[2].title())
print(Ciudades[3].title())
print(Ciudades[4].title())

mensaje="Mi ciudad favorita es " + Ciudades[0].title()+ "."
print(mensaje)
M1="Me gusta viajar a " + Ciudades[4].title()+"."
print(M1)

Ciudades.append('Ramos Arizpe')
Ciudades[2]='Monclova'
Ciudades.insert(0, 'Acuña')

popped_Ciudades=Ciudades
Ciudades.pop()
Ciudades.sort()
print(sorted(Ciudades))
Ciudades.reverse()
Ciudades.sort(reverse=True)
print(Ciudades)


