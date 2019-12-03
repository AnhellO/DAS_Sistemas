import peewee
import datetime
import ramapi
import pprint

db = peewee.SqliteDatabase('database_api.db')

class characters(peewee.Model):
    id_characters = peewee.IntegerField()
    name = peewee.TextField()
    status = peewee.TextField()
    species = peewee.TextField()
    gender = peewee.TextField()
    origin = peewee.TextField()
    location = peewee.TextField()
    episode = peewee.TextField()

    class Meta:
        database = db 

class locations(peewee.Model):
    id_locations = peewee.IntegerField()
    name = peewee.TextField()
    tipo = peewee.TextField()
    dimension = peewee.TextField()
    residentes = peewee.TextField()
    

    class Meta:
        database = db

class episodes(peewee.Model):
    id_episodes = peewee.IntegerField()
    name = peewee.TextField()
    air_date = peewee.TextField()
    episode = peewee.TextField()
    characters = peewee.TextField()

    class Meta:
        database = db


def main():
    list_of_characters = []
    personajes = characters.select(
        characters.id_characters, characters.name, characters.status, 
        characters.species, characters.gender, characters.origin, characters.location, characters.episode)

    for personaje in personajes:
        character_dictionary = {}
        character_dictionary['id_characters'] = personaje.id_characters
        character_dictionary['name'] = personaje.name
        character_dictionary['status'] = personaje.status
        character_dictionary['species'] = personaje.species
        character_dictionary['gender'] = personaje.gender
        character_dictionary['origin'] = personaje.origin
        character_dictionary['location'] = personaje.location
        character_dictionary['episode'] = personaje.episode
        list_of_characters.append(character_dictionary)


    
    list_of_locations = []
    ubicaciones = locations.select(
        locations.id_locations, locations.name, locations.tipo,
        locations.dimension, locations.residentes)
    for location in ubicaciones:
        location_dictionary = {}
        location_dictionary['id_locations'] = location.id_locations
        location_dictionary['name'] = location.name
        location_dictionary['tipo'] = location.tipo
        location_dictionary['dimension'] = location.dimension
        location_dictionary['residentes'] = location.residentes
        list_of_locations.append(location_dictionary)


    list_of_episodes = []
    episodios = episodes.select(
        episodes.id_episodes, episodes.name, episodes.air_date,
        episodes.episode, episodes.characters)
    for episode in episodios:
        episode_dictionary = {}
        episode_dictionary['id_episodes'] = episode.id_episodes
        episode_dictionary['name'] = episode.name
        episode_dictionary['episode'] = episode.episode
        episode_dictionary['air_date'] = episode.air_date
        episode_dictionary['characters'] = episode.characters
        list_of_episodes.append(episode_dictionary)

    
    #Creando archivo html para personajes
    string_characters = """<!DOCTYPE html>
    <html>
    <head>Characters</head>
    <body style="background-color:white;"><br>"""
    for character in list_of_characters:
        string_characters += "<tbody><tr><td>" + str(character['id_characters']) + "</tbody></td></tr><br>"
        string_characters += "<tbody><tr><td>" + str(character['name']) + "</tbody></td></tr><br>"
        string_characters += "<tbody><tr><td>" + str(character['status']) + "</tbody></td></tr><br>"
        string_characters += "<tbody><tr><td>" + str(character['species']) + "</tbody></td></tr><br>"
        string_characters += "<tbody><tr><td>" + str(character['gender']) + "</tbody></td></tr><br>"
        string_characters += "<tbody><tr><td>" + str(character['origin']) + "</tbody></td></tr><br>"
        string_characters += "<tbody><tr><td>" + str(character['location']) + "</tbody></td></tr><br>"
        string_characters += "<tbody><tr><td>" + str(character['episode']) + "</tbody></td></tr><br>"
    string_characters += """</body></html>"""

    f = open('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_estaticos\\characters\\characters.html', 'w', encoding="utf-8")
    f.write(string_characters)
    f.close()

    #Creando archivo html para locations
    string_locations = """<!DOCTYPE html>
    <html>
    <head>Locations</head>
    <body style="background-color:white;"><br>"""
    for location in list_of_locations:
        string_locations += "<tbody><tr><td>" + str(location['id_locations']) + "</tbody></td></tr><br>"
        string_locations += "<tbody><tr><td>" + str(location['name']) + "</tbody></td></tr><br>"
        string_locations += "<tbody><tr><td>" + str(location['tipo']) + "</tbody></td></tr><br>"
        string_locations += "<tbody><tr><td>" + str(location['dimension']) + "</tbody></td></tr><br>"
        string_locations += "<tbody><tr><td>" + str(location['residentes']) + "</tbody></td></tr><br>"
    string_locations += """</body></html>"""
    e = open('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_estaticos\\locations\\locations.html', 'w', encoding="utf-8")
    e.write(string_locations)
    e.close()

    #Creando archivo html para episodios
    string_episodes = """<!DOCTYPE html>
    <html>
    <head>Episodes</head>
    <body style="background-color:white;"><p><br>"""
    for episode in list_of_episodes:
        string_episodes += "<tbody><tr><td>" + str(episode['id_episodes']) + "</tbody></td></tr><br>"
        string_episodes += "<tbody><tr><td>" + str(episode['name']) + "</tbody></td></tr><br>"
        string_episodes += "<tbody><tr><td>" + str(episode['episode']) + "</tbody></td></tr><br>"
        string_episodes += "<tbody><tr><td>" + str(episode['air_date']) + "</tbody></td></tr><br>"
        string_episodes += "<tbody><tr><td>" + str(episode['characters']) + "</tbody></td></tr><br>"
    string_episodes += """</body></html>"""
    g = open('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_estaticos\\episodes\\episodes.html', 'w')
    g.write(string_episodes)
    g.close()

    

    #Creando html para cada personaje
    for character in list_of_characters:
        string_character = """<!DOCTYPE html>
        <html>
        <head>Character</head>
        <body><p> {} </p>""".format(str(character['name']))
        string_character += "<tbody><tr><td>" + str(character['id_characters']) + "</td></tr><br>"
        string_character += "<tbody><tr><td>" + str(character['name']) + "</tbody></td></tr><br>"
        string_character += "<tbody><tr><td>" + str(character['status']) + "</tbody></td></tr><br>"
        string_character += "<tbody><tr><td>" + str(character['species']) + "</tbody></td></tr><br>"
        string_character += "<tbody><tr><td>" + str(character['gender']) + "</tbody></td></tr><br>"
        string_character += "<tbody><tr><td>" + str(character['origin']) + "</tbody></td></tr><br>"
        string_character += "<tbody><tr><td>" + str(character['location']) + "</tbody></td></tr><br>"
        string_character += "<tbody><tr><td>" + str(character['episode']) + "</tbody></td></tr><br>"
        string_character +=  """</body></html>"""
        h = open('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_estaticos\\characters\\Characters\\{}.html'.format(str(character['name'])), 'w', encoding="utf-8")
        h.write(string_character)
        h.close()

    #Creando html para cada location
    for location in list_of_locations:
        string_location = """
        <!DOCTYPE html>
        <html>
        <head>Locations</head>
        <body><p> {} </p>""".format(str(location['name']))
        string_location += "<tbody><tr><td>" + str(location['id_locations']) + "</td></tr><br>"
        string_location += "<tbody><tr><td>" + str(location['name']) + "</tbody></td></tr><br>"
        string_location += "<tbody><tr><td>" + str(location['tipo']) + "</tbody></td></tr><br>"
        string_location += "<tbody><tr><td>" + str(location['dimension']) + "</tbody></td></tr><br>"
        string_location += "<tbody><tr><td>" + str(location['residentes']) + "</tbody></td></tr><br>"
        string_location += """</body></html>"""
        l = open('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_estaticos\\locations\Locations\\{}.html'.format(location['name']), 'w', encoding="utf-8")
        l.write(string_location)
        l.close()

    #Creando html para cada episodio
    for episode in list_of_episodes:
       string_episode = """
       <!DOCTYPE html>
       <html>
       <head>Characters</head>
       <body><p> {} </p>""".format(str(episode['name']))
       string_episode += "<tbody><tr><td>" + str(episode['id_episodes']) + "</td></tr><br>"
       string_episode += "<tbody><tr><td>" + str(episode['name']) + "</td></tr><br>"
       string_episodes += "<tbody><tr><td>" + str(episode['episode']) + "</tbody></td></tr><br>"
       string_episode += "<tbody><tr><td>" + str(episode['air_date']) + "</td></tr><br>"
       string_episode += "<tbody><tr><td>" + str(episode['characters']) + "</td></tr><br>"
       string_episode += """</tbody></body></html>"""
       m = open('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_estaticos\\episodes\\Episodes\\{}.html'.format(str(episode['name'])), 'w')
       m.write(string_episode)
       m.close()

if __name__ == "__main__":
    main()   