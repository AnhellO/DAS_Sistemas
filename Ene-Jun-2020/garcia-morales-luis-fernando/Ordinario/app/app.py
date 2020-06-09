from flask import Flask, render_template
from models import *
import redis
import json

client = redis.Redis(host='dc_redis', port=6379)
app = Flask(__name__)
cache_heroes = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/heroes")
def DcHeroes():
    dc = []
    
    if(not cache_heroes):
        for i in range(int(SUPER_HEROE.select().count())):
            print(f'vuelta {i}')
            data = SUPER_HEROE.get(SUPER_HEROE.id == i)
            data2 = SUPERHEROES_STATS.get(SUPERHEROES_STATS.id == i)
            dictionary = {
                "id": data.id,
                "name": data.name,
                "full_name": data.full_name,
                "alter_egos": data.alter_egos,
                "aliases": data.aliases,
                "place_of_birth": data.place_of_birth,
                "first_appearance": data.first_appearance,
                "publisher":data.publisher,
                "alignment": data.alignment,
                "gender": data.gender,
                "race": data.race,
                "height": data.height,
                "weigth": data.weight,
                "eye_color" : data.eye_color,
                "hair_color": data.hair_color,
                "occupation": data.occupation,
                "base": data.base,
                "group_affiliation":data.group_affiliation,
                "relatives": data.relatives,
                "image": data.image,
                "intelligence": data2.intelligence,
                "strength": data2.strength,
                "speed": data2.speed,
                "durability": data2.durability,
                "power": data2.power,
                "combat": data2.combat
            }
            valor = json.dumps(dictionary)
            llave = str(i)
            client.set(llave,valor)
            dc.append(dictionary)
            cache_heroes.append(llave)
    else:
        for i in cache_heroes:
            print(f"vuelta {i}")
            dc.append(json.loads(client.get(str(i))))

    return render_template("heroes.html" , dc=dc)

@app.route("/heroes/<hero>")
def Hero(hero):
    if (not (str(hero) in cache_heroes)):
        super_heroes = SUPER_HEROE.get(SUPER_HEROE.id == hero)
        super_stats = SUPERHEROES_STATS.get(SUPERHEROES_STATS.id == hero)
        dc = {
            "id":super_heroes.id,
            "name": super_heroes.name,
            "full_name": super_heroes.full_name,
            "alter_egos": super_heroes.alter_egos,
            "aliases": super_heroes.aliases,
            "place_of_birth": super_heroes.place_of_birth,
            "first_appearance": super_heroes.first_appearance,
            "publisher":super_heroes.publisher,
            "alignment": super_heroes.alignment,
            "gender": super_heroes.gender,
            "race": super_heroes.race,
            "height": super_heroes.height,
            "weigth": super_heroes.weight,
            "eye_color" : super_heroes.eye_color,
            "hair_color": super_heroes.hair_color,
            "occupation": super_heroes.occupation,
            "base": super_heroes.base,
            "group_affiliation":super_heroes.group_affiliation,
            "relatives": super_heroes.relatives,
            "image": super_heroes.image,
            "intelligence": super_stats.intelligence,
            "strength": super_stats.strength,
            "speed": super_stats.speed,
            "durability": super_stats.durability,
            "power": super_stats.power,
            "combat": super_stats.combat
        }
        llave = str(super_heroes.id)
        valor = json.dumps(dc)
        client.set(llave,valor)
    dc = json.loads(client.get(str(hero)))
    return render_template("hero.html", dc = dc)

if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=5000)
    