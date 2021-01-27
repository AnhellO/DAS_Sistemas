import peewee
from flask import Flask

app = Flask(__name__)
db = peewee.SqliteDatabase('ram.db')

class Character(peewee.Model):
    # characters
    name = peewee.TextField()
    status = peewee.TextField()
    species = peewee.TextField()
    type = peewee.TextField()
    gender = peewee.TextField()
    image = peewee.TextField()
    url = peewee.TextField()
    created = peewee.TextField()

    class Meta:
        database = db
        db_table = 'character'

class Location(peewee.Model):
    # locations
    name = peewee.TextField()
    type = peewee.TextField()
    url = peewee.TextField()
    created = peewee.TextField()

    class Meta:
        database = db
        db_table = 'location'

class Episode(peewee.Model):
    name = peewee.TextField()
    url = peewee.TextField()
    created = peewee.TextField()

    class Meta:
        database = db
        db_table = 'episode'


def get_tablas():
    return db.get_tables()


def get_characters():
    lista = []
    characters = Character.select(Character.name, Character.status, Character.species,
                                  Character.type, Character.gender, Character.image,
                                  Character.url, Character.created)
    for i in characters:
        lista.append(i)
    return lista


def get_locations():
    lista = []
    locations = Location.select(Location.name, Location.type,
                                Location.url, Location.created)
    for i in locations:
        lista.append(i)
    return lista


def get_episodes():
    lista = []
    episodes = Episode.select(Episode.name, Episode.url, Episode.created)
    for i in episodes:
        lista.append(i)
    return lista


@app.route('/')
def index():
    t = get_tablas()
    return f'''<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Rick y Morty API</title>
            </head>
            <body>
                <br><a href='/index_Characters'><h1 align="center">{t[0]}</h1></a>
                <br><a href='/index_Episodes'><h1 align="center">{t[1]}</h1></a>
                <br><a href='/index_Locations'><h1 align="center">{t[2]}</h1></a>           
            </body>
        </html>
            '''


@app.route('/index_Characters')
def index_Characters():
    list_characters = []
    characters = get_characters()
    for i in characters:
        list_characters.append(i.name)


    return f'''<!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>Characters</title>
                </head>
                <body>
                    <br><a href="/index_Characters/{list_characters[0]}"><h1 align="center">{list_characters[0]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[1]}"><h1 align="center">{list_characters[1]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[2]}">><h1 align="center">{list_characters[2]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[3]}">><h1 align="center">{list_characters[3]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[4]}">><h1 align="center">{list_characters[4]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[5]}">><h1 align="center">{list_characters[5]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[6]}">><h1 align="center">{list_characters[6]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[7]}"><h1 align="center">{list_characters[7]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[8]}"><h1 align="center">{list_characters[8]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[9]}"><h1 align="center">{list_characters[9]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[10]}"><h1 align="center">{list_characters[10]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[11]}"><h1 align="center">{list_characters[11]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[12]}"><h1 align="center">{list_characters[12]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[13]}"><h1 align="center">{list_characters[13]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[14]}"><h1 align="center">{list_characters[14]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[15]}"><h1 align="center">{list_characters[15]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[16]}"><h1 align="center">{list_characters[16]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[17]}"><h1 align="center">{list_characters[17]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[18]}"><h1 align="center">{list_characters[18]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[19]}"><h1 align="center">{list_characters[19]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[20]}"><h1 align="center">{list_characters[20]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[21]}"><h1 align="center">{list_characters[21]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[22]}"><h1 align="center">{list_characters[22]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[23]}"><h1 align="center">{list_characters[23]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[24]}"><h1 align="center">{list_characters[24]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[25]}"><h1 align="center">{list_characters[25]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[26]}"><h1 align="center">{list_characters[26]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[27]}"><h1 align="center">{list_characters[27]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[28]}"><h1 align="center">{list_characters[28]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[29]}"><h1 align="center">{list_characters[29]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[30]}"><h1 align="center">{list_characters[30]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[31]}"><h1 align="center">{list_characters[31]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[32]}"><h1 align="center">{list_characters[32]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[33]}"><h1 align="center">{list_characters[33]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[34]}"><h1 align="center">{list_characters[34]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[35]}"><h1 align="center">{list_characters[35]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[36]}"><h1 align="center">{list_characters[36]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[37]}"><h1 align="center">{list_characters[37]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[38]}"><h1 align="center">{list_characters[38]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[39]}"><h1 align="center">{list_characters[39]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[40]}"><h1 align="center">{list_characters[40]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[41]}"><h1 align="center">{list_characters[41]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[42]}"><h1 align="center">{list_characters[42]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[43]}"><h1 align="center">{list_characters[43]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[44]}"><h1 align="center">{list_characters[44]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[45]}"><h1 align="center">{list_characters[45]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[46]}"><h1 align="center">{list_characters[46]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[47]}"><h1 align="center">{list_characters[47]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[48]}"><h1 align="center">{list_characters[48]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[49]}"><h1 align="center">{list_characters[49]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[50]}"><h1 align="center">{list_characters[50]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[51]}"><h1 align="center">{list_characters[51]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[52]}"><h1 align="center">{list_characters[52]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[53]}"><h1 align="center">{list_characters[53]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[54]}"><h1 align="center">{list_characters[54]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[55]}"><h1 align="center">{list_characters[55]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[56]}"><h1 align="center">{list_characters[56]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[57]}"><h1 align="center">{list_characters[57]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[58]}"><h1 align="center">{list_characters[58]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[59]}"><h1 align="center">{list_characters[59]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[60]}"><h1 align="center">{list_characters[60]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[61]}"><h1 align="center">{list_characters[61]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[62]}"><h1 align="center">{list_characters[62]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[63]}"><h1 align="center">{list_characters[63]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[64]}"><h1 align="center">{list_characters[64]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[65]}"><h1 align="center">{list_characters[65]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[66]}"><h1 align="center">{list_characters[66]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[67]}"><h1 align="center">{list_characters[67]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[68]}"><h1 align="center">{list_characters[68]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[69]}"><h1 align="center">{list_characters[69]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[70]}"><h1 align="center">{list_characters[70]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[71]}"><h1 align="center">{list_characters[71]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[72]}"><h1 align="center">{list_characters[72]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[73]}"><h1 align="center">{list_characters[73]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[74]}"><h1 align="center">{list_characters[74]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[75]}"><h1 align="center">{list_characters[75]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[76]}"><h1 align="center">{list_characters[76]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[77]}"><h1 align="center">{list_characters[77]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[78]}"><h1 align="center">{list_characters[78]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[79]}"><h1 align="center">{list_characters[79]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[80]}"><h1 align="center">{list_characters[80]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[81]}"><h1 align="center">{list_characters[81]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[82]}"><h1 align="center">{list_characters[82]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[83]}"><h1 align="center">{list_characters[83]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[84]}"><h1 align="center">{list_characters[84]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[85]}"><h1 align="center">{list_characters[85]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[86]}"><h1 align="center">{list_characters[86]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[87]}"><h1 align="center">{list_characters[87]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[88]}"><h1 align="center">{list_characters[88]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[89]}"><h1 align="center">{list_characters[89]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[90]}"><h1 align="center">{list_characters[90]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[91]}"><h1 align="center">{list_characters[91]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[92]}"><h1 align="center">{list_characters[92]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[93]}"><h1 align="center">{list_characters[93]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[94]}"><h1 align="center">{list_characters[94]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[95]}"><h1 align="center">{list_characters[95]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[96]}"><h1 align="center">{list_characters[96]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[97]}"><h1 align="center">{list_characters[97]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[98]}"><h1 align="center">{list_characters[98]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[99]}"><h1 align="center">{list_characters[99]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[100]}"><h1 align="center">{list_characters[100]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[101]}"><h1 align="center">{list_characters[101]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[102]}"><h1 align="center">{list_characters[102]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[103]}"><h1 align="center">{list_characters[103]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[104]}"><h1 align="center">{list_characters[104]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[105]}"><h1 align="center">{list_characters[105]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[106]}"><h1 align="center">{list_characters[106]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[107]}"><h1 align="center">{list_characters[107]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[108]}"><h1 align="center">{list_characters[108]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[109]}"><h1 align="center">{list_characters[109]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[110]}"><h1 align="center">{list_characters[110]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[111]}"><h1 align="center">{list_characters[111]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[112]}"><h1 align="center">{list_characters[112]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[113]}"><h1 align="center">{list_characters[113]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[114]}"><h1 align="center">{list_characters[114]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[115]}"><h1 align="center">{list_characters[115]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[116]}"><h1 align="center">{list_characters[116]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[117]}"><h1 align="center">{list_characters[117]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[118]}"><h1 align="center">{list_characters[118]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[119]}"><h1 align="center">{list_characters[119]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[120]}"><h1 align="center">{list_characters[120]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[121]}"><h1 align="center">{list_characters[121]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[122]}"><h1 align="center">{list_characters[122]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[123]}"><h1 align="center">{list_characters[123]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[124]}"><h1 align="center">{list_characters[124]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[125]}"><h1 align="center">{list_characters[125]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[126]}"><h1 align="center">{list_characters[126]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[127]}"><h1 align="center">{list_characters[127]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[128]}"><h1 align="center">{list_characters[128]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[129]}"><h1 align="center">{list_characters[129]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[130]}"><h1 align="center">{list_characters[130]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[131]}"><h1 align="center">{list_characters[131]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[132]}"><h1 align="center">{list_characters[132]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[133]}"><h1 align="center">{list_characters[133]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[134]}"><h1 align="center">{list_characters[134]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[135]}"><h1 align="center">{list_characters[135]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[136]}"><h1 align="center">{list_characters[136]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[137]}"><h1 align="center">{list_characters[137]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[138]}"><h1 align="center">{list_characters[138]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[139]}"><h1 align="center">{list_characters[139]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[140]}"><h1 align="center">{list_characters[140]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[141]}"><h1 align="center">{list_characters[141]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[142]}"><h1 align="center">{list_characters[142]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[143]}"><h1 align="center">{list_characters[143]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[144]}"><h1 align="center">{list_characters[144]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[145]}"><h1 align="center">{list_characters[145]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[146]}"><h1 align="center">{list_characters[146]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[147]}"><h1 align="center">{list_characters[147]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[148]}"><h1 align="center">{list_characters[148]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[149]}"><h1 align="center">{list_characters[149]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[150]}"><h1 align="center">{list_characters[150]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[151]}"><h1 align="center">{list_characters[151]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[152]}"><h1 align="center">{list_characters[152]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[153]}"><h1 align="center">{list_characters[153]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[154]}"><h1 align="center">{list_characters[154]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[155]}"><h1 align="center">{list_characters[155]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[156]}"><h1 align="center">{list_characters[156]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[157]}"><h1 align="center">{list_characters[157]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[158]}"><h1 align="center">{list_characters[158]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[159]}"><h1 align="center">{list_characters[159]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[160]}"><h1 align="center">{list_characters[160]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[161]}"><h1 align="center">{list_characters[161]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[162]}"><h1 align="center">{list_characters[162]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[163]}"><h1 align="center">{list_characters[163]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[164]}"><h1 align="center">{list_characters[164]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[165]}"><h1 align="center">{list_characters[165]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[166]}"><h1 align="center">{list_characters[166]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[167]}"><h1 align="center">{list_characters[167]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[168]}"><h1 align="center">{list_characters[168]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[169]}"><h1 align="center">{list_characters[169]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[170]}"><h1 align="center">{list_characters[170]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[171]}"><h1 align="center">{list_characters[171]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[172]}"><h1 align="center">{list_characters[172]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[173]}"><h1 align="center">{list_characters[173]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[174]}"><h1 align="center">{list_characters[174]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[175]}"><h1 align="center">{list_characters[175]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[176]}"><h1 align="center">{list_characters[176]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[177]}"><h1 align="center">{list_characters[177]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[178]}"><h1 align="center">{list_characters[178]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[179]}"><h1 align="center">{list_characters[179]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[180]}"><h1 align="center">{list_characters[180]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[181]}"><h1 align="center">{list_characters[181]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[182]}"><h1 align="center">{list_characters[182]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[183]}"><h1 align="center">{list_characters[183]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[184]}"><h1 align="center">{list_characters[184]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[185]}"><h1 align="center">{list_characters[185]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[186]}"><h1 align="center">{list_characters[186]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[187]}"><h1 align="center">{list_characters[187]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[188]}"><h1 align="center">{list_characters[188]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[189]}"><h1 align="center">{list_characters[189]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[190]}"><h1 align="center">{list_characters[190]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[191]}"><h1 align="center">{list_characters[191]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[192]}"><h1 align="center">{list_characters[192]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[193]}"><h1 align="center">{list_characters[193]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[194]}"><h1 align="center">{list_characters[194]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[195]}"><h1 align="center">{list_characters[195]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[196]}"><h1 align="center">{list_characters[196]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[197]}"><h1 align="center">{list_characters[197]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[198]}"><h1 align="center">{list_characters[198]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[199]}"><h1 align="center">{list_characters[199]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[200]}"><h1 align="center">{list_characters[200]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[201]}"><h1 align="center">{list_characters[201]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[202]}"><h1 align="center">{list_characters[202]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[203]}"><h1 align="center">{list_characters[203]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[204]}"><h1 align="center">{list_characters[204]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[205]}"><h1 align="center">{list_characters[205]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[206]}"><h1 align="center">{list_characters[206]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[207]}"><h1 align="center">{list_characters[207]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[208]}"><h1 align="center">{list_characters[208]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[209]}"><h1 align="center">{list_characters[209]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[210]}"><h1 align="center">{list_characters[210]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[211]}"><h1 align="center">{list_characters[211]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[212]}"><h1 align="center">{list_characters[212]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[213]}"><h1 align="center">{list_characters[213]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[214]}"><h1 align="center">{list_characters[214]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[215]}"><h1 align="center">{list_characters[215]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[216]}"><h1 align="center">{list_characters[216]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[217]}"><h1 align="center">{list_characters[217]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[218]}"><h1 align="center">{list_characters[218]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[219]}"><h1 align="center">{list_characters[219]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[220]}"><h1 align="center">{list_characters[220]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[221]}"><h1 align="center">{list_characters[221]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[222]}"><h1 align="center">{list_characters[222]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[223]}"><h1 align="center">{list_characters[223]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[224]}"><h1 align="center">{list_characters[224]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[225]}"><h1 align="center">{list_characters[225]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[226]}"><h1 align="center">{list_characters[226]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[227]}"><h1 align="center">{list_characters[227]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[228]}"><h1 align="center">{list_characters[228]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[229]}"><h1 align="center">{list_characters[229]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[230]}"><h1 align="center">{list_characters[230]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[231]}"><h1 align="center">{list_characters[231]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[232]}"><h1 align="center">{list_characters[232]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[233]}"><h1 align="center">{list_characters[233]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[234]}"><h1 align="center">{list_characters[234]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[235]}"><h1 align="center">{list_characters[235]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[236]}"><h1 align="center">{list_characters[236]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[237]}"><h1 align="center">{list_characters[237]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[238]}"><h1 align="center">{list_characters[238]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[239]}"><h1 align="center">{list_characters[239]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[240]}"><h1 align="center">{list_characters[240]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[241]}"><h1 align="center">{list_characters[241]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[242]}"><h1 align="center">{list_characters[242]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[243]}"><h1 align="center">{list_characters[243]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[244]}"><h1 align="center">{list_characters[244]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[245]}"><h1 align="center">{list_characters[245]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[246]}"><h1 align="center">{list_characters[246]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[247]}"><h1 align="center">{list_characters[247]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[248]}"><h1 align="center">{list_characters[248]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[249]}"><h1 align="center">{list_characters[249]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[250]}"><h1 align="center">{list_characters[250]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[251]}"><h1 align="center">{list_characters[251]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[252]}"><h1 align="center">{list_characters[252]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[253]}"><h1 align="center">{list_characters[253]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[254]}"><h1 align="center">{list_characters[254]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[255]}"><h1 align="center">{list_characters[255]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[256]}"><h1 align="center">{list_characters[256]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[257]}"><h1 align="center">{list_characters[257]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[258]}"><h1 align="center">{list_characters[258]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[259]}"><h1 align="center">{list_characters[259]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[260]}"><h1 align="center">{list_characters[260]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[261]}"><h1 align="center">{list_characters[261]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[262]}"><h1 align="center">{list_characters[262]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[263]}"><h1 align="center">{list_characters[263]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[264]}"><h1 align="center">{list_characters[264]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[265]}"><h1 align="center">{list_characters[265]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[266]}"><h1 align="center">{list_characters[266]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[267]}"><h1 align="center">{list_characters[267]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[268]}"><h1 align="center">{list_characters[268]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[269]}"><h1 align="center">{list_characters[269]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[270]}"><h1 align="center">{list_characters[270]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[271]}"><h1 align="center">{list_characters[271]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[272]}"><h1 align="center">{list_characters[272]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[273]}"><h1 align="center">{list_characters[273]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[274]}"><h1 align="center">{list_characters[274]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[275]}"><h1 align="center">{list_characters[275]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[276]}"><h1 align="center">{list_characters[276]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[277]}"><h1 align="center">{list_characters[277]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[278]}"><h1 align="center">{list_characters[278]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[279]}"><h1 align="center">{list_characters[279]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[280]}"><h1 align="center">{list_characters[280]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[281]}"><h1 align="center">{list_characters[281]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[282]}"><h1 align="center">{list_characters[282]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[283]}"><h1 align="center">{list_characters[283]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[284]}"><h1 align="center">{list_characters[284]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[285]}"><h1 align="center">{list_characters[285]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[286]}"><h1 align="center">{list_characters[286]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[287]}"><h1 align="center">{list_characters[287]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[288]}"><h1 align="center">{list_characters[288]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[289]}"><h1 align="center">{list_characters[289]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[290]}"><h1 align="center">{list_characters[290]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[291]}"><h1 align="center">{list_characters[291]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[292]}"><h1 align="center">{list_characters[292]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[293]}"><h1 align="center">{list_characters[293]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[294]}"><h1 align="center">{list_characters[294]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[295]}"><h1 align="center">{list_characters[295]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[296]}"><h1 align="center">{list_characters[296]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[297]}"><h1 align="center">{list_characters[297]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[298]}"><h1 align="center">{list_characters[298]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[299]}"><h1 align="center">{list_characters[299]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[300]}"><h1 align="center">{list_characters[300]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[301]}"><h1 align="center">{list_characters[301]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[302]}"><h1 align="center">{list_characters[302]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[303]}"><h1 align="center">{list_characters[303]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[304]}"><h1 align="center">{list_characters[304]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[305]}"><h1 align="center">{list_characters[305]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[306]}"><h1 align="center">{list_characters[306]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[307]}"><h1 align="center">{list_characters[307]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[308]}"><h1 align="center">{list_characters[308]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[309]}"><h1 align="center">{list_characters[309]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[310]}"><h1 align="center">{list_characters[310]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[311]}"><h1 align="center">{list_characters[311]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[312]}"><h1 align="center">{list_characters[312]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[313]}"><h1 align="center">{list_characters[313]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[314]}"><h1 align="center">{list_characters[314]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[315]}"><h1 align="center">{list_characters[315]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[316]}"><h1 align="center">{list_characters[316]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[317]}"><h1 align="center">{list_characters[317]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[318]}"><h1 align="center">{list_characters[318]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[319]}"><h1 align="center">{list_characters[319]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[320]}"><h1 align="center">{list_characters[320]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[321]}"><h1 align="center">{list_characters[321]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[322]}"><h1 align="center">{list_characters[322]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[323]}"><h1 align="center">{list_characters[323]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[324]}"><h1 align="center">{list_characters[324]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[325]}"><h1 align="center">{list_characters[325]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[326]}"><h1 align="center">{list_characters[326]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[327]}"><h1 align="center">{list_characters[327]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[328]}"><h1 align="center">{list_characters[328]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[329]}"><h1 align="center">{list_characters[329]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[330]}"><h1 align="center">{list_characters[330]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[331]}"><h1 align="center">{list_characters[331]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[332]}"><h1 align="center">{list_characters[332]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[333]}"><h1 align="center">{list_characters[333]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[334]}"><h1 align="center">{list_characters[334]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[335]}"><h1 align="center">{list_characters[335]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[336]}"><h1 align="center">{list_characters[336]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[337]}"><h1 align="center">{list_characters[337]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[338]}"><h1 align="center">{list_characters[338]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[339]}"><h1 align="center">{list_characters[339]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[340]}"><h1 align="center">{list_characters[340]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[341]}"><h1 align="center">{list_characters[341]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[342]}"><h1 align="center">{list_characters[342]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[343]}"><h1 align="center">{list_characters[343]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[344]}"><h1 align="center">{list_characters[344]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[345]}"><h1 align="center">{list_characters[345]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[346]}"><h1 align="center">{list_characters[346]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[347]}"><h1 align="center">{list_characters[347]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[348]}"><h1 align="center">{list_characters[348]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[349]}"><h1 align="center">{list_characters[349]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[350]}"><h1 align="center">{list_characters[350]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[351]}"><h1 align="center">{list_characters[351]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[352]}"><h1 align="center">{list_characters[352]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[353]}"><h1 align="center">{list_characters[353]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[354]}"><h1 align="center">{list_characters[354]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[355]}"><h1 align="center">{list_characters[355]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[356]}"><h1 align="center">{list_characters[356]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[357]}"><h1 align="center">{list_characters[357]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[358]}"><h1 align="center">{list_characters[358]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[359]}"><h1 align="center">{list_characters[359]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[360]}"><h1 align="center">{list_characters[360]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[361]}"><h1 align="center">{list_characters[361]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[362]}"><h1 align="center">{list_characters[362]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[363]}"><h1 align="center">{list_characters[363]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[364]}"><h1 align="center">{list_characters[364]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[365]}"><h1 align="center">{list_characters[365]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[366]}"><h1 align="center">{list_characters[366]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[367]}"><h1 align="center">{list_characters[367]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[368]}"><h1 align="center">{list_characters[368]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[369]}"><h1 align="center">{list_characters[369]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[370]}"><h1 align="center">{list_characters[370]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[371]}"><h1 align="center">{list_characters[371]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[372]}"><h1 align="center">{list_characters[372]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[373]}"><h1 align="center">{list_characters[373]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[374]}"><h1 align="center">{list_characters[374]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[375]}"><h1 align="center">{list_characters[375]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[376]}"><h1 align="center">{list_characters[376]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[377]}"><h1 align="center">{list_characters[377]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[378]}"><h1 align="center">{list_characters[378]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[379]}"><h1 align="center">{list_characters[379]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[380]}"><h1 align="center">{list_characters[380]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[381]}"><h1 align="center">{list_characters[381]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[382]}"><h1 align="center">{list_characters[382]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[383]}"><h1 align="center">{list_characters[383]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[384]}"><h1 align="center">{list_characters[384]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[385]}"><h1 align="center">{list_characters[385]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[386]}"><h1 align="center">{list_characters[386]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[387]}"><h1 align="center">{list_characters[387]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[388]}"><h1 align="center">{list_characters[388]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[389]}"><h1 align="center">{list_characters[389]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[390]}"><h1 align="center">{list_characters[390]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[391]}"><h1 align="center">{list_characters[391]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[392]}"><h1 align="center">{list_characters[392]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[393]}"><h1 align="center">{list_characters[393]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[394]}"><h1 align="center">{list_characters[394]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[395]}"><h1 align="center">{list_characters[395]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[396]}"><h1 align="center">{list_characters[396]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[397]}"><h1 align="center">{list_characters[397]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[398]}"><h1 align="center">{list_characters[398]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[399]}"><h1 align="center">{list_characters[399]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[400]}"><h1 align="center">{list_characters[400]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[401]}"><h1 align="center">{list_characters[401]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[402]}"><h1 align="center">{list_characters[402]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[403]}"><h1 align="center">{list_characters[403]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[404]}"><h1 align="center">{list_characters[404]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[405]}"><h1 align="center">{list_characters[405]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[406]}"><h1 align="center">{list_characters[406]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[407]}"><h1 align="center">{list_characters[407]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[408]}"><h1 align="center">{list_characters[408]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[409]}"><h1 align="center">{list_characters[409]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[410]}"><h1 align="center">{list_characters[410]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[411]}"><h1 align="center">{list_characters[411]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[412]}"><h1 align="center">{list_characters[412]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[413]}"><h1 align="center">{list_characters[413]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[414]}"><h1 align="center">{list_characters[414]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[415]}"><h1 align="center">{list_characters[415]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[416]}"><h1 align="center">{list_characters[416]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[417]}"><h1 align="center">{list_characters[417]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[418]}"><h1 align="center">{list_characters[418]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[419]}"><h1 align="center">{list_characters[419]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[420]}"><h1 align="center">{list_characters[420]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[421]}"><h1 align="center">{list_characters[421]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[422]}"><h1 align="center">{list_characters[422]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[423]}"><h1 align="center">{list_characters[423]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[424]}"><h1 align="center">{list_characters[424]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[425]}"><h1 align="center">{list_characters[425]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[426]}"><h1 align="center">{list_characters[426]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[427]}"><h1 align="center">{list_characters[427]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[428]}"><h1 align="center">{list_characters[428]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[429]}"><h1 align="center">{list_characters[429]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[430]}"><h1 align="center">{list_characters[430]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[431]}"><h1 align="center">{list_characters[431]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[432]}"><h1 align="center">{list_characters[432]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[433]}"><h1 align="center">{list_characters[433]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[434]}"><h1 align="center">{list_characters[434]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[435]}"><h1 align="center">{list_characters[435]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[436]}"><h1 align="center">{list_characters[436]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[437]}"><h1 align="center">{list_characters[437]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[438]}"><h1 align="center">{list_characters[438]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[439]}"><h1 align="center">{list_characters[439]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[440]}"><h1 align="center">{list_characters[440]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[441]}"><h1 align="center">{list_characters[441]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[442]}"><h1 align="center">{list_characters[442]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[443]}"><h1 align="center">{list_characters[443]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[444]}"><h1 align="center">{list_characters[444]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[445]}"><h1 align="center">{list_characters[445]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[446]}"><h1 align="center">{list_characters[446]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[447]}"><h1 align="center">{list_characters[447]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[448]}"><h1 align="center">{list_characters[448]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[449]}"><h1 align="center">{list_characters[449]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[450]}"><h1 align="center">{list_characters[450]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[451]}"><h1 align="center">{list_characters[451]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[452]}"><h1 align="center">{list_characters[452]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[453]}"><h1 align="center">{list_characters[453]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[454]}"><h1 align="center">{list_characters[454]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[455]}"><h1 align="center">{list_characters[455]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[456]}"><h1 align="center">{list_characters[456]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[457]}"><h1 align="center">{list_characters[457]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[458]}"><h1 align="center">{list_characters[458]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[459]}"><h1 align="center">{list_characters[459]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[460]}"><h1 align="center">{list_characters[460]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[461]}"><h1 align="center">{list_characters[461]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[462]}"><h1 align="center">{list_characters[462]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[463]}"><h1 align="center">{list_characters[463]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[464]}"><h1 align="center">{list_characters[464]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[465]}"><h1 align="center">{list_characters[465]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[466]}"><h1 align="center">{list_characters[466]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[467]}"><h1 align="center">{list_characters[467]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[468]}"><h1 align="center">{list_characters[468]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[469]}"><h1 align="center">{list_characters[469]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[470]}"><h1 align="center">{list_characters[470]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[471]}"><h1 align="center">{list_characters[471]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[472]}"><h1 align="center">{list_characters[472]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[473]}"><h1 align="center">{list_characters[473]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[474]}"><h1 align="center">{list_characters[474]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[475]}"><h1 align="center">{list_characters[475]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[476]}"><h1 align="center">{list_characters[476]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[477]}"><h1 align="center">{list_characters[477]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[478]}"><h1 align="center">{list_characters[478]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[479]}"><h1 align="center">{list_characters[479]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[480]}"><h1 align="center">{list_characters[480]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[481]}"><h1 align="center">{list_characters[481]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[482]}"><h1 align="center">{list_characters[482]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[483]}"><h1 align="center">{list_characters[483]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[484]}"><h1 align="center">{list_characters[484]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[485]}"><h1 align="center">{list_characters[485]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[486]}"><h1 align="center">{list_characters[486]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[487]}"><h1 align="center">{list_characters[487]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[488]}"><h1 align="center">{list_characters[488]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[489]}"><h1 align="center">{list_characters[489]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[490]}"><h1 align="center">{list_characters[490]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[491]}"><h1 align="center">{list_characters[491]}</h1></a>
                    <br><a href="/index_Characters/{list_characters[492]}"><h1 align="center">{list_characters[492]}</h1></a>
                </body>
            </html>
            '''


@app.route('/index_Locations')
def index_Locations():
    list_locaciones = []
    location = get_locations()
    for i in location:
        list_locaciones.append(i.name)


    return f'''<!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <meta http-equiv="X-UA-Compatible" content="ie=edge">
                        <title>Locations</title>
                    </head>
                    <body>
                        <br><a href="/index_Locations/{list_locaciones[0]}"><h1 align="center">{list_locaciones[0]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[1]}"><h1 align="center">{list_locaciones[1]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[2]}"><h1 align="center">{list_locaciones[2]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[3]}"><h1 align="center">{list_locaciones[3]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[4]}"><h1 align="center">{list_locaciones[4]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[5]}"><h1 align="center">{list_locaciones[5]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[6]}"><h1 align="center">{list_locaciones[6]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[7]}"><h1 align="center">{list_locaciones[7]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[8]}"><h1 align="center">{list_locaciones[8]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[9]}"><h1 align="center">{list_locaciones[9]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[10]}"><h1 align="center">{list_locaciones[10]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[11]}"><h1 align="center">{list_locaciones[11]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[12]}"><h1 align="center">{list_locaciones[12]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[13]}"><h1 align="center">{list_locaciones[13]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[14]}"><h1 align="center">{list_locaciones[14]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[15]}"><h1 align="center">{list_locaciones[15]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[16]}"><h1 align="center">{list_locaciones[16]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[17]}"><h1 align="center">{list_locaciones[17]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[18]}"><h1 align="center">{list_locaciones[18]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[19]}"><h1 align="center">{list_locaciones[19]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[20]}"><h1 align="center">{list_locaciones[20]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[21]}"><h1 align="center">{list_locaciones[21]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[22]}"><h1 align="center">{list_locaciones[22]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[23]}"><h1 align="center">{list_locaciones[23]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[24]}"><h1 align="center">{list_locaciones[24]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[25]}"><h1 align="center">{list_locaciones[25]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[26]}"><h1 align="center">{list_locaciones[26]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[27]}"><h1 align="center">{list_locaciones[27]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[28]}"><h1 align="center">{list_locaciones[28]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[29]}"><h1 align="center">{list_locaciones[29]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[30]}"><h1 align="center">{list_locaciones[30]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[31]}"><h1 align="center">{list_locaciones[31]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[32]}"><h1 align="center">{list_locaciones[32]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[33]}"><h1 align="center">{list_locaciones[33]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[34]}"><h1 align="center">{list_locaciones[34]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[35]}"><h1 align="center">{list_locaciones[35]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[36]}"><h1 align="center">{list_locaciones[36]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[37]}"><h1 align="center">{list_locaciones[37]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[38]}"><h1 align="center">{list_locaciones[38]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[39]}"><h1 align="center">{list_locaciones[39]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[40]}"><h1 align="center">{list_locaciones[40]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[41]}"><h1 align="center">{list_locaciones[41]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[42]}"><h1 align="center">{list_locaciones[42]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[43]}"><h1 align="center">{list_locaciones[43]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[44]}"><h1 align="center">{list_locaciones[44]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[45]}"><h1 align="center">{list_locaciones[45]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[46]}"><h1 align="center">{list_locaciones[46]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[47]}"><h1 align="center">{list_locaciones[47]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[48]}"><h1 align="center">{list_locaciones[48]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[49]}"><h1 align="center">{list_locaciones[49]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[50]}"><h1 align="center">{list_locaciones[50]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[51]}"><h1 align="center">{list_locaciones[51]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[52]}"><h1 align="center">{list_locaciones[52]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[53]}"><h1 align="center">{list_locaciones[53]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[54]}"><h1 align="center">{list_locaciones[54]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[55]}"><h1 align="center">{list_locaciones[55]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[56]}"><h1 align="center">{list_locaciones[56]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[57]}"><h1 align="center">{list_locaciones[57]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[58]}"><h1 align="center">{list_locaciones[58]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[59]}"><h1 align="center">{list_locaciones[59]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[60]}"><h1 align="center">{list_locaciones[60]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[61]}"><h1 align="center">{list_locaciones[61]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[62]}"><h1 align="center">{list_locaciones[62]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[63]}"><h1 align="center">{list_locaciones[63]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[64]}"><h1 align="center">{list_locaciones[64]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[65]}"><h1 align="center">{list_locaciones[65]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[66]}"><h1 align="center">{list_locaciones[66]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[67]}"><h1 align="center">{list_locaciones[67]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[68]}"><h1 align="center">{list_locaciones[68]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[69]}"><h1 align="center">{list_locaciones[69]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[70]}"><h1 align="center">{list_locaciones[70]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[71]}"><h1 align="center">{list_locaciones[71]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[72]}"><h1 align="center">{list_locaciones[72]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[73]}"><h1 align="center">{list_locaciones[73]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[74]}"><h1 align="center">{list_locaciones[74]}</h1></a>
                        <br><a href="/index_Locations/{list_locaciones[75]}"><h1 align="center">{list_locaciones[75]}</h1></a>
                    </body>
                </html>
                '''


@app.route('/index_Episodes')
def index_Episodes():
    episodes = get_episodes()
    list_episode = []
    for i in episodes:
        list_episode.append(i.name)

    return f'''<!DOCTYPE html>
                        <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                <title>Episodes</title>
                            </head>
                            <body>
                                <br><a href="index_Episodes/{list_episode[0]}"><h1 align="center">{list_episode[0]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[1]}"><h1 align="center">{list_episode[1]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[2]}"><h1 align="center">{list_episode[2]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[3]}"><h1 align="center">{list_episode[3]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[4]}"><h1 align="center">{list_episode[4]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[5]}"><h1 align="center">{list_episode[5]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[6]}"><h1 align="center">{list_episode[6]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[7]}"><h1 align="center">{list_episode[7]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[8]}"><h1 align="center">{list_episode[8]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[9]}"><h1 align="center">{list_episode[9]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[10]}"><h1 align="center">{list_episode[10]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[11]}"><h1 align="center">{list_episode[11]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[12]}"><h1 align="center">{list_episode[12]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[13]}"><h1 align="center">{list_episode[13]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[14]}"><h1 align="center">{list_episode[14]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[15]}"><h1 align="center">{list_episode[15]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[16]}"><h1 align="center">{list_episode[16]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[17]}"><h1 align="center">{list_episode[17]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[18]}"><h1 align="center">{list_episode[18]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[19]}"><h1 align="center">{list_episode[19]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[20]}"><h1 align="center">{list_episode[20]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[21]}"><h1 align="center">{list_episode[21]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[22]}"><h1 align="center">{list_episode[22]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[23]}"><h1 align="center">{list_episode[23]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[24]}"><h1 align="center">{list_episode[24]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[25]}"><h1 align="center">{list_episode[25]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[26]}"><h1 align="center">{list_episode[26]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[27]}"><h1 align="center">{list_episode[27]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[28]}"><h1 align="center">{list_episode[28]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[29]}"><h1 align="center">{list_episode[29]}</h1></a>
                                <br><a href="index_Episodes/{list_episode[30]}"><h1 align="center">{list_episode[30]}</h1></a>
                            </body>
                        </html>
                        '''


@app.route('/index_Characters/<string:name>')
def index_CharacterEspecifico(name):
    query = get_characters()
    for i in query:
        if i.name == name:
            return f'''<!DOCTYPE html>
                       <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                <title>Character</title>
                            </head>
                            <body>
                                <br><h1 align="center">Name -> {i.name}</h1></a>
                                    <br><h1 align="center">Status -> {i.status}</h1></a>
                                    <br><h1 align="center">Specie -> {i.species}</h1></a>
                                    <br><h1 align="center">Gender -> {i.gender}</h1></a>
                                    <br><h1 align="center">Image - > {i.image}</h1></a
                            </body>
                       </html>
                '''


@app.route('/index_Locations/<string:name>')
def index_LocationEspecifica(name):
    query = get_locations()
    for i in query:
        if i.name == name:
            return f'''<!DOCTYPE html>
                       <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                <title>Location</title>
                            </head>
                            <body>
                                <br><h1 align="center">Name -> {i.name}</h1></a>
                                <br><h1 align="center">Type -> {i.type}</h1></a>
                                <br><h1 align="center">Url -> {i.url}</h1></a>
                                <br><h1 align="center">Created -> {i.created}</h1></a>
                            </body>
                       </html>
                '''

@app.route('/index_Episodes/<string:name>')
def index_EpisodeEspecifico(name):
    query = get_episodes()
    for i in query:
        if i.name == name:
            return f'''<!DOCTYPE html>
                       <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                <title>Episode</title>
                            </head>
                            <body>
                                <br><h1 align="center">Name -> {i.name}</h1></a>
                                <br><h1 align="center">Url -> {i.url}</h1></a>
                                <br><h1 align="center">Created -> {i.created}</h1></a>
                            </body>
                       </html>
                '''

def main():
    #get_characters()
    app.debug = True
    app.run(port=5000)

if __name__ == '__main__':
    main()