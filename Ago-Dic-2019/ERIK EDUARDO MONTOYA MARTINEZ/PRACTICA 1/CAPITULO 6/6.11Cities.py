cities={'Guadalajara':{'Pais':'Mexico','Habitantes':1450000000,'Hecho':'fundada en 14 de febrero de 1542'},
        'Venecia':{'Pais':'Italia','Habitantes':261905,'Hecho':'fundada en el año 697 d.C'},
        'Caracas':{'Pais':'Venezuela','Habitantes':31980000,'Hecho':'fundada en 5 de julio 1811'}}
for ciudad, informacion in cities.items():
    print("Ciudad: "+ ciudad.title())
    pais=informacion['Pais']
    hab=informacion['Habitantes']
    fact=informacion['Hecho']
    print("\tPais: " + pais.title())
    print("\tHabitantes: " + str(hab))
    print("\tHecho: " + fact.title())