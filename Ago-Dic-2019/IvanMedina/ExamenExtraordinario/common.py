from bddpokeapi import bddpokeapi
from pokeApi import pokeApi
import peewee
from flask import Flask
import random

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

db=peewee.SqliteDatabase('pokeapi.db')
app = Flask(__name__)

a=pokeApi()
b=bddpokeapi()

class baseModel(peewee.Model):
    class Meta:
        database = db

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class pokemones(baseModel):
    id=peewee.TextField()
    name = peewee.TextField()
    url = peewee.TextField()
    height = peewee.TextField()
    base_exp = peewee.TextField()
    orders = peewee.TextField()
    weight = peewee.TextField()
    type = peewee.TextField()
    hp = peewee.TextField()
    defense = peewee.TextField()
    attack = peewee.TextField()
    sprite = peewee.TextField()

    class Meta:
        db_table = 'pokemones'

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class pokemontypes(baseModel):
    id=peewee.TextField()
    name = peewee.TextField()
    url = peewee.TextField()

    class Meta:
        db_table = 'pokemontypes'

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def create_conncect():
    db.connect()
    db.create_tables([pokemones, pokemontypes], safe=True)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def get_tables():
    return db.get_tables()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def get_pokemon():
    lista = []
    pokes = pokemones.select(pokemones.id, pokemones.name, pokemones.url, pokemones.height,
                                   pokemones.base_exp, pokemones.orders, pokemones.weight, pokemones.type,
                                   pokemones.hp, pokemones.defense, pokemones.attack,
                                   pokemones.sprite)
    for i in pokes:
        lista.append(i)
    return lista

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def get_pokemontypes():
    lista = []
    typs = pokemontypes.select(pokemontypes.id, pokemontypes.name, pokemontypes.url)
    for i in typs:
        lista.append(i)
    return lista


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def saveNPokemones(x):
    if x <900:
        for i in range(1,x+1):
            print(a.getPokemon(i))
            b.savePokemon(a.getPokemon(i))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def saveTypes():
    for i in range(1,19):
        b.saveType(a.getPokemonTypes(i))
    b.saveType(a.getPokemonTypes(10001))
    b.saveType(a.getPokemonTypes(10002))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ok

@app.route('/index_types')
def index_types():
    tipos = get_pokemontypes()
    t=""
    for x in tipos:
        t=t+"<tr> <td><a href='/index_types/{}'> {} </a> </tr> </td>".format(x.name,x.name)

    doc= '''<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Pokemon</title>
                <div align="center">  <h1>Tipos</h1></div>
            </head>
            <body>

            <table border="1px" align="center">
                %s
            </table>
            </body>
        </html>''' % (t)
    return doc
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ok
@app.route('/index_pokemon')
def index_pokemon():
    tipos = get_pokemon()
    t=""
    for x in tipos:
        t=t+"<tr> <td><a href='/index_pokemon/{}'> {} </a></td><tr>".format(x.name,x.name)
    doc= '''<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Pokemon</title>
                <div align="center">  <h1>Pokemones</h1></div>
            </head>
            <body>
            <table border="1px" align="center">
                %s
            </table>
            </body>
        </html>''' % (t)
    return doc

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.route('/index_types/<string:type>')
def index_types_list(type):

    p = get_pokemon()
    t=""
    typ=""
    for x in p:

        if x.type==type:
            t=t+"<tr> <td><a href='/index_pokemon/{}'> {}</a> </td></tr> <br>".format(x.name,x.name)


    doc= '''<!DOCTYPE html>
               <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <meta http-equiv="X-UA-Compatible" content="ie=edge">
                        <title>Tipos</title>

                    </head>
                    <body>
                    <div> <h1 align='center'>Indice de pokemones tipo %s </h1><div>
                    <br>
                    <table border="1px" align="center">
                    %s
                    </table>
                    </body>
                </html>''' % (type,t)
    return(doc)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ok

@app.route('/index_pokemon/<string:name>')
def view_pokemon(name):
    query=get_pokemon()
    for i in query:
        if i.name == name:
            return '''<!DOCTYPE html>
                       <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                <title>Pokemones</title>

                            </head>
                            <body>
                            <div align="center"><img src='%s' width='20%s'></div>
                            <table border="1px" align="center">
                                <tr align="center"> <td> Id </td> <td> %s </td> </tr>
                                <tr align="center"> <td> Name </td> <td> %s </td> </tr>
                                <tr align="center"> <td> Url </td> <td> %s </td> </tr>
                                <tr align="center"> <td> Height </td> <td> %s </td> </tr>
                                <tr align="center"> <td> Base_exp </td> <td> %s </td> </tr>
                                <tr align="center"> <td> Orde </td> <td> %s </td> </tr>
                                <tr align="center"> <td> Weight  </td> <td> %s </td> </tr>
                                <tr align="center"> <td> Type  </td> <td> %s </td> </tr>
                                <tr align="center"> <td> Hp  </td> <td> %s </td> </tr>
                                <tr align="center"> <td> Defense  </td> <td> %s </td> </tr>
                                <tr align="center"> <td> Attack  </td> <td> %s </td> </tr>
                                <tr align="center"> <td> Sprite  </td> <td> %s </td> </tr>
                            </table>
                            </body>
                       </html>''' % (i.sprite,"%",i.id,i.name,i.url,i.height,i.base_exp,i.orders,i.weight,i.type,i.hp,i.defense,i.attack,i.sprite)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route('/foo')
def foo():
    poks=get_pokemon() #lista completa de pokemones
    exists=True
    p=None
    while(exists==True):
        r=random.randrange(150,900)
        p=a.getPokemon(r)
        for x in poks:
            if x.id==p[0]:
                exists=True
            else:
                exists=False
    if not exists:
        b.savePokemon(p)

    return '''<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Pokemon</title>

            </head>
            <body>
                <div align="center">  <h1>Nuevo pokemon guardado</h1></div>
                <br><a href='/index_pokemon/%s'><h1 align="center"> %s </h1></a>

            </body>
        </html>''' % (p[1],p[2])


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.route('/')
def index():
    t = get_tables()
    return '''<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Pokemon</title>
                <div align="center">  <h1>BIENVENIDO</h1></div>
                <div align="center"><img src="/static/pokemon.png"></div>
                <div align="center">  <h3>IVAN MEDINA</h3></div>
            </head>
            <body>
            <table>
                <tr><a href='/index_pokemon'><h1 align="center"> %s </h1></a></tr>
                <tr><a href='/index_types'><h1 align="center"> %s </h1></a><tr>
                <tr><div align="center"><form action='/foo'><input type="submit" value="Guardar pokemon aleatorio"></form> </div><tr>
            </table>
            </body>
        </html>''' % (t[0],t[1])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#saveNPokemones(100)
#saveTypes()             
create_conncect()
app.debug = True
app.run(port=8000)
