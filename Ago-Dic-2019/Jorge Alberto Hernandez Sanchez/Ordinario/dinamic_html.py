from jinja2 import Environment, FileSystemLoader
import orm_db


#html dinamico para characters
env = Environment(loader=FileSystemLoader('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_dinamicos'))
template = env.get_template('Personajes.html')


personajes = orm_db.characters.select(orm_db.characters.id_characters, orm_db.characters.name, orm_db.characters.status, 
        orm_db.characters.species, orm_db.characters.gender, orm_db.characters.origin, 
        orm_db.characters.location, orm_db.characters.episode)
dic_characters = {
    'hmtl_name' : 'Characters'
}
j = 1
for personaje in personajes:
    dic = {
        'id{}'.format(j) : '{}'.format(str(personaje.id_characters)),
        'name{}'.format(j) : '{}'.format(str(personaje.name)),
        'status{}'.format(j) : '{}'.format(str(personaje.status)),
        'species{}'.format(j) : '{}'.format(str(personaje.species)),
        'gender{}'.format(j) : '{}'.format(str(personaje.gender)),
        'origin{}'.format(j) : '{}'.format(str(personaje.origin)),
        'location{}'.format(j) : '{}'.format(str(personaje.location)),
        'episode{}'.format(j) : '{}'.format(str(personaje.episode))
        }
    dic_characters.update(dic)
    j = j + 1

html = template.render(dic_characters)

f = open('Characters.html', 'w', encoding="utf-8")
f.write(html)
f.close()

# Creando hmtl dinamico para Locations
env2 = Environment(loader=FileSystemLoader('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_dinamicos'))
template2 = env.get_template('Ubicaciones.html')

ubicaciones = orm_db.locations.select(
        orm_db.locations.id_locations, orm_db.locations.name, orm_db.locations.tipo,
        orm_db.locations.dimension, orm_db.locations.residentes)

k = 1
dic_locations = {
    'hmtl_name' : 'Locations'
}
for location in ubicaciones:
    dic2 = {
        'id{}'.format(k) : '{}'.format(location.id_locations),
        'name{}'.format(k) : '{}'.format(location.name),
        'tipo{}'.format(k) : '{}'.format(location.tipo),
        'dimension{}'.format(k) : '{}'.format(location.dimension),
        'residentes{}'.format(k) : '{}'.format(location.residentes)
    }
    dic_locations.update(dic2)
    k = k + 1

html2 = template2.render(dic_locations)

g = open('Locations.html', 'w', encoding="utf-8")
g.write(html2)
g.close()

#Creando html dinamico para episodios
env3 = Environment(loader=FileSystemLoader('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_dinamicos'))
template3 = env.get_template('Episodios.html')

episodios = orm_db.episodes.select(
        orm_db.episodes.id_episodes, orm_db.episodes.name, orm_db.episodes.air_date,
        orm_db.episodes.episode, orm_db.episodes.characters)
l = 1
dic_episodes = {
    'hmtl_name' : 'Episodes'
}
for episodio in episodios:
    dic3 = {
        'id{}'.format(l) : '{}'.format(episodio.id_episodes),
        'name{}'.format(l) : '{}'.format(episodio.name),
        'episode{}'.format(l) : '{}'.format(episodio.episode),
        'air_date{}'.format(l) : '{}'.format(episodio.air_date),
        'characters{}'.format(l) : '{}'.format(episodio.characters)
    }
    dic_episodes.update(dic3)
    l = l + 1


html3 = template3.render(dic_episodes)

h = open('Episodes.html', 'w', encoding="utf-8")
h.write(html)
h.close()

#Creando html dinamico para cada personaje
env4 = Environment(loader=FileSystemLoader('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_dinamicos'))
template4 = env.get_template('Personaje.html')


for personaje in personajes:
    dic4 = {
        'html_name' : 'Character',
        'id': '{}'.format(str(personaje.id_characters)),
        'name' : '{}'.format(str(personaje.name)),
        'status' : '{}'.format(str(personaje.status)),
        'species' : '{}'.format(str(personaje.species)),
        'gender' : '{}'.format(str(personaje.gender)),
        'origin' : '{}'.format(str(personaje.origin)),
        'location' : '{}'.format(str(personaje.location)),
        'episode' : '{}'.format(str(personaje.episode))
        }
    html4 = template4.render(dic4)
    m = open('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_dinamicos\\characters\\{}.html'.format(str(personaje.name)), 'w', encoding="utf-8")
    m.write(html4)
    m.close()


#Creando hmtl dinamicos para cada ubicacion
env5 = Environment(loader=FileSystemLoader('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_dinamicos'))
template5 = env.get_template('Ubicacion.html')
for location in ubicaciones:
    dic5 = {
        'html_name' : 'Location',
        'id' : '{}'.format(location.id_locations),
        'name' : '{}'.format(location.name),
        'tipo' : '{}'.format(location.tipo),
        'dimension' : '{}'.format(location.dimension),
        'residentes' : '{}'.format(location.residentes)
        }
    html5 = template5.render(dic5)
    o = open('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_dinamicos\\locations\\{}.html'.format(str(location.name)), 'w', encoding="utf-8")
    o.write(html5)
    o.close()

#Creando html dinamico para cada episodio
env6 = Environment(loader=FileSystemLoader('C:\\Users\\jorge\\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_dinamicos'))
template6 = env.get_template('Episodio.html')

for episodio in episodios:
    dic6 = {
        'html_name' : 'Episode',
        'id' : '{}'.format(episodio.id_episodes),
        'name' : '{}'.format(episodio.name),
        'episode' : '{}'.format(episodio.episode),
        'air_date' : '{}'.format(episodio.air_date),
        'characters' : '{}'.format(episodio.characters)
        }
    html6 = template6.render(dic6)
    p = open('C:\\Users\\jorge\Documents\\Cursos\\DAS_Sistemas\\Ago-Dic-2019\\Jorge Alberto Hernandez Sanchez\\Ordinario\\html_dinamicos\\epiosdes\\{}.html'.format(str(episodio.name)), 'w', encoding="utf-8")
    p.write(html6)
    p.close()