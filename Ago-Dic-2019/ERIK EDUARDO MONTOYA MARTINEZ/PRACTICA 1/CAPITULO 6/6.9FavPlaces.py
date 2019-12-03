favorite_places={'Maria':['Galerias', 'Plaza Real','San Luis'], 'Omar':['Muzquiz', 'Encinas'], 'Oscar':['Texas']}

for persona, lugar in favorite_places.items():
    print("\n")
    print("Los lugares favoritos de "+ persona.title()+ " son ")

    for lugar_fav in lugar:
        print(lugar_fav)
