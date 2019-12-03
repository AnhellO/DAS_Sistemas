favorite_places = {"Anita": "Islandia", "Andrea": "Biblioteca", "Melissa": "Parques"}

"""for key, value in favorite_places.items():
    print("El lugar favorito de", key, "es", value ,"\n")"""

favorite_places["Enrique"] = "Museos"
favorite_places["Mauricio"] = "Su habitacion"
favorite_places["Rebeca"] = "Escuela"

print("Ingresa uno desde el teclado")
favorite_places[input("Persona: ")] = input("Lugar favorito: ")

for key, value in favorite_places.items():
    print("El lugar favorito de", key, "es", value ,"\n")
