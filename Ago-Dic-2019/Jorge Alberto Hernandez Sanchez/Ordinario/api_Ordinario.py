import ramapi
import pprint
import pickle
from db_ordinario import database_API

db = database_API()
db.crear_database()

#Tabla Characters

id_character = []
name_character = []
status_character = []
species_characters = []
gender_character = []
origin_character = []
location_character = []
episode_character = []


for i in range(1, 494):
    a = ramapi.Character.get(id= i)
    name_character.append(a['name'])
    status_character.append(a['status'])
    species_characters.append(a['species'])
    gender_character.append(a['gender'])
    origin_character.append(a['origin']['name'])
    location_character.append(a['location']['name'])
    episode_character.append(a['episode'])
print("arrays actualizados")


def llenado_tabla_Characters():
    print("Actualizando tabla Characters...")
    j = 1
    for i in range(1,494):
        db.llenar_tabla_characters(j, name_character[i - 1], status_character[i - 1], species_characters[i - 1], gender_character[i - 1], origin_character[i - 1], location_character[i - 1], str(episode_character[i - 1]))
        j = j + 1
    print("Tabla actualizada")


llenado_tabla_Characters()
print("Mostrando tabla Characters...")
db.mostrar_tabla_characters()

# Tabla Locations

id_locations = []
name_locations = []
tipo_locations = []
dimension_locations = []
residentes_locations = []


for i in range(1, 77):
    b = ramapi.Location.get(id = i)
    name_locations.append(b["name"])
    tipo_locations.append(b["type"])
    dimension_locations.append(b["dimension"])
    residentes_locations.append(b["residents"])
    

def llenado_tabla_Locations():
    print("Actualizando tabla locations...")
    j = 1
    for i in range(1,77):
        db.llenar_tabla_locations(j, name_locations[i - 1], tipo_locations[i - 1], dimension_locations[i - 1], str(residentes_locations[i - 1]))
        j = j + 1
    print("Tabla actualizada")

llenado_tabla_Locations()
print("Mostrando tabla Locations...")
db.mostrar_tabla_locations()

# Tabla Episodes

id_episodes = []
name_episodes = []
air_date_episodes = []
episode = []
characters_episodes = []

for i in range(1,32):
    c = ramapi.Episode.get(id= i)
    name_episodes.append(c["name"])
    air_date_episodes.append(c["air_date"])
    episode.append(c["episode"])
    characters_episodes.append(c["characters"])

def llenado_tabla_Episodes():
    print("Actualizando tabla episodes...")
    j = 1
    for i in range(1, 32):
        db.llenar_tabla_episodes(j, name_episodes[i - 1], air_date_episodes[i - 1], episode[i - 1], str(characters_episodes[i - 1]))
        j = j + 1
    print("Tabla actualizada")

llenado_tabla_Episodes()
print("Mostrando tabla Episodes...")
db.mostrar_tabla_episodes()