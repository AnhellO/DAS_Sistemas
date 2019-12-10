import requests

class pokeApi():

    def __init__(self):
        pass


    def getPokemon(self,x):
        id=None
        url=None
        height=None
        base_exp=None
        name=None
        order=None
        weight=None

        hp=None
        attack=None
        defense=None
        type=None
        sprite=None

        url="https://pokeapi.co/api/v2/pokemon/"+str(x)+"/"
        r=requests.get(url)
        r=r.json()
        id=x
        height=r['height']
        base_exp=r['base_experience']
        name=r['name']
        order=r['order']
        weight=r['weight']
        hp=r['stats'][5]['base_stat']
        defense=r['stats'][3]['base_stat']
        attack=r['stats'][4]['base_stat']
        type=r['types'][0]['type']['name']
        sprite="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+str(x)+".png"
        return [id,name,url,height,base_exp,order,weight,type,hp,defense,attack,sprite]

    def getPokemonTypes(self,x):
        id=None
        url=None
        name=None
        if (x>0 and x<19) or x ==10001 or x ==10002:
            url="https://pokeapi.co/api/v2/type/"+str(x)+"/"
            r=requests.get(url)
            r=r.json()
            id=x
            name=r['name']
            return [id,name,url]
        else:
            return [None,None,None]
