Kansas = {"Pais": "Estados Unidos", "Poblacion": "2,911,641 habitantes", "dato": "Su capital es Topeka y su ciudad mas poblada es Wichita"}
Venecia = {"Pais": "Italia", "poblacion": "261,905 habitantes", "dato":"Tiene un centro historico declarado patrimonio de la humanidad"}
Paris = {"Pais": "Francia", "poblacion":"2,206,488 habitantes", "dato":"Capital de Francia, lugar de la Torre Eiffel"}

cities = {"Kansas": Kansas, "Venecia": Venecia, "Paris": Paris}

for key, value in cities.items():
    print(key, value,"\n")