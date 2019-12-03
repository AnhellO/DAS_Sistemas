import peewee
from flask import Flask

app = Flask(__name__)
db = peewee.SqliteDatabase('Ord_DB_RickMorty.db')


class baseModel(peewee.Model):
    class Meta:
        database = db

#---------------------------------------------------------------------------------------------------
class Characters(baseModel):
    id = peewee.TextField()
    name = peewee.TextField()
    status = peewee.TextField()
    species = peewee.TextField()
    tipe = peewee.TextField()
    gender = peewee.TextField()
    nameOrigin = peewee.TextField()
    urlOrigin = peewee.TextField()
    nameLocation = peewee.TextField()
    urlLocation = peewee.TextField()
    image = peewee.TextField()
    episodes = peewee.TextField()
    url = peewee.TextField()
    created = peewee.TextField()

    class Meta:
        data_table = 'Characters'

#---------------------------------------------------------------------------------------------------
class Location(baseModel):
    id = peewee.TextField()
    name = peewee.TextField()
    tipe = peewee.TextField()
    dimension = peewee.TextField()
    residents = peewee.TextField()
    url = peewee.TextField()
    created = peewee.TextField()

    class Meta:
        db_table = 'Location'

#---------------------------------------------------------------------------------------------------
class Episode(baseModel):
    id = peewee.TextField()
    name = peewee.TextField()
    air_date = peewee.TextField()
    episode = peewee.TextField()
    characters = peewee.TextField()
    url = peewee.TextField()
    created = peewee.TextField()

    class Meta:
        dn_table = 'Episode'


def gettablas():
    return db.get_tables()


def getcharacters():
    lista = []
    characters = Characters.select(Characters.id, Characters.name, Characters.status, Characters.species, Characters.tipe, Characters.gender, Characters.nameOrigin, Characters.urlOrigin, Characters.nameLocation, Characters.urlLocation, Characters.image,Characters.episodes, Characters.url, Characters.created)
    for i in characters:
        lista.append(i)
    return lista


def getlocations():
    lista = []
    locations = Location.select(Location.id, Location.name, Location.tipe, Location.dimension, Location.residents, Location.url, Location.created)
    for i in locations:
        lista.append(i)
    return lista


def getepisodes():
    lista = []
    episodes = Episode.select(Episode.id, Episode.name, Episode.air_date, Episode.episode, Episode.characters, Episode.url, Episode.created)
    for i in episodes:
        lista.append(i)
    return lista


@app.route('/')
def index():
    t = gettablas()
    return f'''<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Rick y Morty</title>
                <div align="center"><img src="static/RMLogo.jpg"></div>
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
    list_nombres = []
    cha = getcharacters()
    for i in cha:
        list_nombres.append(i.name)


    return f'''<!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>Personajes</title>
                    <div align="center"><img src="static/RMLogo.jpg"></div>
                </head>
                <body>
                    <br><a href="/index_Characters/{list_nombres[0]}"><h1 align="center">{list_nombres[0]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[1]}"><h1 align="center">{list_nombres[1]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[2]}">><h1 align="center">{list_nombres[2]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[3]}">><h1 align="center">{list_nombres[3]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[4]}">><h1 align="center">{list_nombres[4]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[5]}">><h1 align="center">{list_nombres[5]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[6]}">><h1 align="center">{list_nombres[6]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[7]}"><h1 align="center">{list_nombres[7]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[8]}"><h1 align="center">{list_nombres[8]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[9]}"><h1 align="center">{list_nombres[9]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[10]}"><h1 align="center">{list_nombres[10]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[11]}"><h1 align="center">{list_nombres[11]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[12]}"><h1 align="center">{list_nombres[12]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[13]}"><h1 align="center">{list_nombres[13]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[14]}"><h1 align="center">{list_nombres[14]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[15]}"><h1 align="center">{list_nombres[15]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[16]}"><h1 align="center">{list_nombres[16]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[17]}"><h1 align="center">{list_nombres[17]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[18]}"><h1 align="center">{list_nombres[18]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[19]}"><h1 align="center">{list_nombres[19]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[20]}"><h1 align="center">{list_nombres[20]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[21]}"><h1 align="center">{list_nombres[21]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[22]}"><h1 align="center">{list_nombres[22]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[23]}"><h1 align="center">{list_nombres[23]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[24]}"><h1 align="center">{list_nombres[24]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[25]}"><h1 align="center">{list_nombres[25]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[26]}"><h1 align="center">{list_nombres[26]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[27]}"><h1 align="center">{list_nombres[27]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[28]}"><h1 align="center">{list_nombres[28]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[29]}"><h1 align="center">{list_nombres[29]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[30]}"><h1 align="center">{list_nombres[30]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[31]}"><h1 align="center">{list_nombres[31]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[32]}"><h1 align="center">{list_nombres[32]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[33]}"><h1 align="center">{list_nombres[33]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[34]}"><h1 align="center">{list_nombres[34]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[35]}"><h1 align="center">{list_nombres[35]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[36]}"><h1 align="center">{list_nombres[36]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[37]}"><h1 align="center">{list_nombres[37]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[38]}"><h1 align="center">{list_nombres[38]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[39]}"><h1 align="center">{list_nombres[39]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[40]}"><h1 align="center">{list_nombres[40]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[41]}"><h1 align="center">{list_nombres[41]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[42]}"><h1 align="center">{list_nombres[42]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[43]}"><h1 align="center">{list_nombres[43]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[44]}"><h1 align="center">{list_nombres[44]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[45]}"><h1 align="center">{list_nombres[45]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[46]}"><h1 align="center">{list_nombres[46]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[47]}"><h1 align="center">{list_nombres[47]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[48]}"><h1 align="center">{list_nombres[48]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[49]}"><h1 align="center">{list_nombres[49]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[50]}"><h1 align="center">{list_nombres[50]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[51]}"><h1 align="center">{list_nombres[51]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[52]}"><h1 align="center">{list_nombres[52]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[53]}"><h1 align="center">{list_nombres[53]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[54]}"><h1 align="center">{list_nombres[54]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[55]}"><h1 align="center">{list_nombres[55]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[56]}"><h1 align="center">{list_nombres[56]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[57]}"><h1 align="center">{list_nombres[57]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[58]}"><h1 align="center">{list_nombres[58]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[59]}"><h1 align="center">{list_nombres[59]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[60]}"><h1 align="center">{list_nombres[60]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[61]}"><h1 align="center">{list_nombres[61]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[62]}"><h1 align="center">{list_nombres[62]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[63]}"><h1 align="center">{list_nombres[63]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[64]}"><h1 align="center">{list_nombres[64]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[65]}"><h1 align="center">{list_nombres[65]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[66]}"><h1 align="center">{list_nombres[66]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[67]}"><h1 align="center">{list_nombres[67]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[68]}"><h1 align="center">{list_nombres[68]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[69]}"><h1 align="center">{list_nombres[69]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[70]}"><h1 align="center">{list_nombres[70]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[71]}"><h1 align="center">{list_nombres[71]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[72]}"><h1 align="center">{list_nombres[72]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[73]}"><h1 align="center">{list_nombres[73]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[74]}"><h1 align="center">{list_nombres[74]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[75]}"><h1 align="center">{list_nombres[75]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[76]}"><h1 align="center">{list_nombres[76]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[77]}"><h1 align="center">{list_nombres[77]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[78]}"><h1 align="center">{list_nombres[78]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[79]}"><h1 align="center">{list_nombres[79]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[80]}"><h1 align="center">{list_nombres[80]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[81]}"><h1 align="center">{list_nombres[81]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[82]}"><h1 align="center">{list_nombres[82]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[83]}"><h1 align="center">{list_nombres[83]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[84]}"><h1 align="center">{list_nombres[84]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[85]}"><h1 align="center">{list_nombres[85]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[86]}"><h1 align="center">{list_nombres[86]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[87]}"><h1 align="center">{list_nombres[87]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[88]}"><h1 align="center">{list_nombres[88]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[89]}"><h1 align="center">{list_nombres[89]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[90]}"><h1 align="center">{list_nombres[90]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[91]}"><h1 align="center">{list_nombres[91]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[92]}"><h1 align="center">{list_nombres[92]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[93]}"><h1 align="center">{list_nombres[93]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[94]}"><h1 align="center">{list_nombres[94]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[95]}"><h1 align="center">{list_nombres[95]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[96]}"><h1 align="center">{list_nombres[96]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[97]}"><h1 align="center">{list_nombres[97]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[98]}"><h1 align="center">{list_nombres[98]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[99]}"><h1 align="center">{list_nombres[99]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[100]}"><h1 align="center">{list_nombres[100]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[101]}"><h1 align="center">{list_nombres[101]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[102]}"><h1 align="center">{list_nombres[102]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[103]}"><h1 align="center">{list_nombres[103]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[104]}"><h1 align="center">{list_nombres[104]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[105]}"><h1 align="center">{list_nombres[105]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[106]}"><h1 align="center">{list_nombres[106]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[107]}"><h1 align="center">{list_nombres[107]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[108]}"><h1 align="center">{list_nombres[108]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[109]}"><h1 align="center">{list_nombres[109]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[110]}"><h1 align="center">{list_nombres[110]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[111]}"><h1 align="center">{list_nombres[111]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[112]}"><h1 align="center">{list_nombres[112]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[113]}"><h1 align="center">{list_nombres[113]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[114]}"><h1 align="center">{list_nombres[114]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[115]}"><h1 align="center">{list_nombres[115]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[116]}"><h1 align="center">{list_nombres[116]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[117]}"><h1 align="center">{list_nombres[117]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[118]}"><h1 align="center">{list_nombres[118]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[119]}"><h1 align="center">{list_nombres[119]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[120]}"><h1 align="center">{list_nombres[120]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[121]}"><h1 align="center">{list_nombres[121]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[122]}"><h1 align="center">{list_nombres[122]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[123]}"><h1 align="center">{list_nombres[123]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[124]}"><h1 align="center">{list_nombres[124]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[125]}"><h1 align="center">{list_nombres[125]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[126]}"><h1 align="center">{list_nombres[126]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[127]}"><h1 align="center">{list_nombres[127]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[128]}"><h1 align="center">{list_nombres[128]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[129]}"><h1 align="center">{list_nombres[129]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[130]}"><h1 align="center">{list_nombres[130]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[131]}"><h1 align="center">{list_nombres[131]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[132]}"><h1 align="center">{list_nombres[132]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[133]}"><h1 align="center">{list_nombres[133]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[134]}"><h1 align="center">{list_nombres[134]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[135]}"><h1 align="center">{list_nombres[135]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[136]}"><h1 align="center">{list_nombres[136]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[137]}"><h1 align="center">{list_nombres[137]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[138]}"><h1 align="center">{list_nombres[138]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[139]}"><h1 align="center">{list_nombres[139]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[140]}"><h1 align="center">{list_nombres[140]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[141]}"><h1 align="center">{list_nombres[141]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[142]}"><h1 align="center">{list_nombres[142]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[143]}"><h1 align="center">{list_nombres[143]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[144]}"><h1 align="center">{list_nombres[144]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[145]}"><h1 align="center">{list_nombres[145]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[146]}"><h1 align="center">{list_nombres[146]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[147]}"><h1 align="center">{list_nombres[147]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[148]}"><h1 align="center">{list_nombres[148]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[149]}"><h1 align="center">{list_nombres[149]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[150]}"><h1 align="center">{list_nombres[150]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[151]}"><h1 align="center">{list_nombres[151]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[152]}"><h1 align="center">{list_nombres[152]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[153]}"><h1 align="center">{list_nombres[153]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[154]}"><h1 align="center">{list_nombres[154]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[155]}"><h1 align="center">{list_nombres[155]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[156]}"><h1 align="center">{list_nombres[156]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[157]}"><h1 align="center">{list_nombres[157]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[158]}"><h1 align="center">{list_nombres[158]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[159]}"><h1 align="center">{list_nombres[159]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[160]}"><h1 align="center">{list_nombres[160]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[161]}"><h1 align="center">{list_nombres[161]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[162]}"><h1 align="center">{list_nombres[162]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[163]}"><h1 align="center">{list_nombres[163]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[164]}"><h1 align="center">{list_nombres[164]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[165]}"><h1 align="center">{list_nombres[165]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[166]}"><h1 align="center">{list_nombres[166]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[167]}"><h1 align="center">{list_nombres[167]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[168]}"><h1 align="center">{list_nombres[168]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[169]}"><h1 align="center">{list_nombres[169]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[170]}"><h1 align="center">{list_nombres[170]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[171]}"><h1 align="center">{list_nombres[171]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[172]}"><h1 align="center">{list_nombres[172]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[173]}"><h1 align="center">{list_nombres[173]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[174]}"><h1 align="center">{list_nombres[174]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[175]}"><h1 align="center">{list_nombres[175]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[176]}"><h1 align="center">{list_nombres[176]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[177]}"><h1 align="center">{list_nombres[177]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[178]}"><h1 align="center">{list_nombres[178]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[179]}"><h1 align="center">{list_nombres[179]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[180]}"><h1 align="center">{list_nombres[180]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[181]}"><h1 align="center">{list_nombres[181]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[182]}"><h1 align="center">{list_nombres[182]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[183]}"><h1 align="center">{list_nombres[183]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[184]}"><h1 align="center">{list_nombres[184]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[185]}"><h1 align="center">{list_nombres[185]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[186]}"><h1 align="center">{list_nombres[186]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[187]}"><h1 align="center">{list_nombres[187]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[188]}"><h1 align="center">{list_nombres[188]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[189]}"><h1 align="center">{list_nombres[189]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[190]}"><h1 align="center">{list_nombres[190]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[191]}"><h1 align="center">{list_nombres[191]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[192]}"><h1 align="center">{list_nombres[192]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[193]}"><h1 align="center">{list_nombres[193]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[194]}"><h1 align="center">{list_nombres[194]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[195]}"><h1 align="center">{list_nombres[195]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[196]}"><h1 align="center">{list_nombres[196]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[197]}"><h1 align="center">{list_nombres[197]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[198]}"><h1 align="center">{list_nombres[198]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[199]}"><h1 align="center">{list_nombres[199]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[200]}"><h1 align="center">{list_nombres[200]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[201]}"><h1 align="center">{list_nombres[201]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[202]}"><h1 align="center">{list_nombres[202]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[203]}"><h1 align="center">{list_nombres[203]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[204]}"><h1 align="center">{list_nombres[204]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[205]}"><h1 align="center">{list_nombres[205]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[206]}"><h1 align="center">{list_nombres[206]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[207]}"><h1 align="center">{list_nombres[207]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[208]}"><h1 align="center">{list_nombres[208]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[209]}"><h1 align="center">{list_nombres[209]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[210]}"><h1 align="center">{list_nombres[210]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[211]}"><h1 align="center">{list_nombres[211]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[212]}"><h1 align="center">{list_nombres[212]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[213]}"><h1 align="center">{list_nombres[213]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[214]}"><h1 align="center">{list_nombres[214]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[215]}"><h1 align="center">{list_nombres[215]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[216]}"><h1 align="center">{list_nombres[216]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[217]}"><h1 align="center">{list_nombres[217]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[218]}"><h1 align="center">{list_nombres[218]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[219]}"><h1 align="center">{list_nombres[219]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[220]}"><h1 align="center">{list_nombres[220]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[221]}"><h1 align="center">{list_nombres[221]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[222]}"><h1 align="center">{list_nombres[222]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[223]}"><h1 align="center">{list_nombres[223]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[224]}"><h1 align="center">{list_nombres[224]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[225]}"><h1 align="center">{list_nombres[225]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[226]}"><h1 align="center">{list_nombres[226]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[227]}"><h1 align="center">{list_nombres[227]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[228]}"><h1 align="center">{list_nombres[228]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[229]}"><h1 align="center">{list_nombres[229]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[230]}"><h1 align="center">{list_nombres[230]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[231]}"><h1 align="center">{list_nombres[231]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[232]}"><h1 align="center">{list_nombres[232]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[233]}"><h1 align="center">{list_nombres[233]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[234]}"><h1 align="center">{list_nombres[234]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[235]}"><h1 align="center">{list_nombres[235]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[236]}"><h1 align="center">{list_nombres[236]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[237]}"><h1 align="center">{list_nombres[237]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[238]}"><h1 align="center">{list_nombres[238]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[239]}"><h1 align="center">{list_nombres[239]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[240]}"><h1 align="center">{list_nombres[240]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[241]}"><h1 align="center">{list_nombres[241]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[242]}"><h1 align="center">{list_nombres[242]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[243]}"><h1 align="center">{list_nombres[243]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[244]}"><h1 align="center">{list_nombres[244]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[245]}"><h1 align="center">{list_nombres[245]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[246]}"><h1 align="center">{list_nombres[246]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[247]}"><h1 align="center">{list_nombres[247]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[248]}"><h1 align="center">{list_nombres[248]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[249]}"><h1 align="center">{list_nombres[249]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[250]}"><h1 align="center">{list_nombres[250]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[251]}"><h1 align="center">{list_nombres[251]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[252]}"><h1 align="center">{list_nombres[252]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[253]}"><h1 align="center">{list_nombres[253]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[254]}"><h1 align="center">{list_nombres[254]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[255]}"><h1 align="center">{list_nombres[255]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[256]}"><h1 align="center">{list_nombres[256]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[257]}"><h1 align="center">{list_nombres[257]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[258]}"><h1 align="center">{list_nombres[258]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[259]}"><h1 align="center">{list_nombres[259]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[260]}"><h1 align="center">{list_nombres[260]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[261]}"><h1 align="center">{list_nombres[261]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[262]}"><h1 align="center">{list_nombres[262]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[263]}"><h1 align="center">{list_nombres[263]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[264]}"><h1 align="center">{list_nombres[264]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[265]}"><h1 align="center">{list_nombres[265]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[266]}"><h1 align="center">{list_nombres[266]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[267]}"><h1 align="center">{list_nombres[267]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[268]}"><h1 align="center">{list_nombres[268]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[269]}"><h1 align="center">{list_nombres[269]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[270]}"><h1 align="center">{list_nombres[270]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[271]}"><h1 align="center">{list_nombres[271]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[272]}"><h1 align="center">{list_nombres[272]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[273]}"><h1 align="center">{list_nombres[273]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[274]}"><h1 align="center">{list_nombres[274]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[275]}"><h1 align="center">{list_nombres[275]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[276]}"><h1 align="center">{list_nombres[276]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[277]}"><h1 align="center">{list_nombres[277]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[278]}"><h1 align="center">{list_nombres[278]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[279]}"><h1 align="center">{list_nombres[279]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[280]}"><h1 align="center">{list_nombres[280]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[281]}"><h1 align="center">{list_nombres[281]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[282]}"><h1 align="center">{list_nombres[282]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[283]}"><h1 align="center">{list_nombres[283]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[284]}"><h1 align="center">{list_nombres[284]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[285]}"><h1 align="center">{list_nombres[285]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[286]}"><h1 align="center">{list_nombres[286]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[287]}"><h1 align="center">{list_nombres[287]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[288]}"><h1 align="center">{list_nombres[288]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[289]}"><h1 align="center">{list_nombres[289]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[290]}"><h1 align="center">{list_nombres[290]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[291]}"><h1 align="center">{list_nombres[291]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[292]}"><h1 align="center">{list_nombres[292]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[293]}"><h1 align="center">{list_nombres[293]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[294]}"><h1 align="center">{list_nombres[294]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[295]}"><h1 align="center">{list_nombres[295]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[296]}"><h1 align="center">{list_nombres[296]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[297]}"><h1 align="center">{list_nombres[297]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[298]}"><h1 align="center">{list_nombres[298]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[299]}"><h1 align="center">{list_nombres[299]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[300]}"><h1 align="center">{list_nombres[300]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[301]}"><h1 align="center">{list_nombres[301]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[302]}"><h1 align="center">{list_nombres[302]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[303]}"><h1 align="center">{list_nombres[303]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[304]}"><h1 align="center">{list_nombres[304]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[305]}"><h1 align="center">{list_nombres[305]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[306]}"><h1 align="center">{list_nombres[306]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[307]}"><h1 align="center">{list_nombres[307]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[308]}"><h1 align="center">{list_nombres[308]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[309]}"><h1 align="center">{list_nombres[309]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[310]}"><h1 align="center">{list_nombres[310]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[311]}"><h1 align="center">{list_nombres[311]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[312]}"><h1 align="center">{list_nombres[312]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[313]}"><h1 align="center">{list_nombres[313]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[314]}"><h1 align="center">{list_nombres[314]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[315]}"><h1 align="center">{list_nombres[315]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[316]}"><h1 align="center">{list_nombres[316]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[317]}"><h1 align="center">{list_nombres[317]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[318]}"><h1 align="center">{list_nombres[318]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[319]}"><h1 align="center">{list_nombres[319]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[320]}"><h1 align="center">{list_nombres[320]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[321]}"><h1 align="center">{list_nombres[321]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[322]}"><h1 align="center">{list_nombres[322]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[323]}"><h1 align="center">{list_nombres[323]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[324]}"><h1 align="center">{list_nombres[324]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[325]}"><h1 align="center">{list_nombres[325]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[326]}"><h1 align="center">{list_nombres[326]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[327]}"><h1 align="center">{list_nombres[327]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[328]}"><h1 align="center">{list_nombres[328]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[329]}"><h1 align="center">{list_nombres[329]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[330]}"><h1 align="center">{list_nombres[330]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[331]}"><h1 align="center">{list_nombres[331]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[332]}"><h1 align="center">{list_nombres[332]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[333]}"><h1 align="center">{list_nombres[333]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[334]}"><h1 align="center">{list_nombres[334]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[335]}"><h1 align="center">{list_nombres[335]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[336]}"><h1 align="center">{list_nombres[336]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[337]}"><h1 align="center">{list_nombres[337]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[338]}"><h1 align="center">{list_nombres[338]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[339]}"><h1 align="center">{list_nombres[339]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[340]}"><h1 align="center">{list_nombres[340]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[341]}"><h1 align="center">{list_nombres[341]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[342]}"><h1 align="center">{list_nombres[342]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[343]}"><h1 align="center">{list_nombres[343]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[344]}"><h1 align="center">{list_nombres[344]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[345]}"><h1 align="center">{list_nombres[345]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[346]}"><h1 align="center">{list_nombres[346]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[347]}"><h1 align="center">{list_nombres[347]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[348]}"><h1 align="center">{list_nombres[348]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[349]}"><h1 align="center">{list_nombres[349]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[350]}"><h1 align="center">{list_nombres[350]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[351]}"><h1 align="center">{list_nombres[351]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[352]}"><h1 align="center">{list_nombres[352]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[353]}"><h1 align="center">{list_nombres[353]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[354]}"><h1 align="center">{list_nombres[354]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[355]}"><h1 align="center">{list_nombres[355]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[356]}"><h1 align="center">{list_nombres[356]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[357]}"><h1 align="center">{list_nombres[357]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[358]}"><h1 align="center">{list_nombres[358]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[359]}"><h1 align="center">{list_nombres[359]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[360]}"><h1 align="center">{list_nombres[360]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[361]}"><h1 align="center">{list_nombres[361]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[362]}"><h1 align="center">{list_nombres[362]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[363]}"><h1 align="center">{list_nombres[363]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[364]}"><h1 align="center">{list_nombres[364]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[365]}"><h1 align="center">{list_nombres[365]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[366]}"><h1 align="center">{list_nombres[366]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[367]}"><h1 align="center">{list_nombres[367]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[368]}"><h1 align="center">{list_nombres[368]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[369]}"><h1 align="center">{list_nombres[369]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[370]}"><h1 align="center">{list_nombres[370]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[371]}"><h1 align="center">{list_nombres[371]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[372]}"><h1 align="center">{list_nombres[372]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[373]}"><h1 align="center">{list_nombres[373]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[374]}"><h1 align="center">{list_nombres[374]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[375]}"><h1 align="center">{list_nombres[375]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[376]}"><h1 align="center">{list_nombres[376]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[377]}"><h1 align="center">{list_nombres[377]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[378]}"><h1 align="center">{list_nombres[378]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[379]}"><h1 align="center">{list_nombres[379]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[380]}"><h1 align="center">{list_nombres[380]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[381]}"><h1 align="center">{list_nombres[381]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[382]}"><h1 align="center">{list_nombres[382]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[383]}"><h1 align="center">{list_nombres[383]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[384]}"><h1 align="center">{list_nombres[384]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[385]}"><h1 align="center">{list_nombres[385]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[386]}"><h1 align="center">{list_nombres[386]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[387]}"><h1 align="center">{list_nombres[387]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[388]}"><h1 align="center">{list_nombres[388]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[389]}"><h1 align="center">{list_nombres[389]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[390]}"><h1 align="center">{list_nombres[390]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[391]}"><h1 align="center">{list_nombres[391]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[392]}"><h1 align="center">{list_nombres[392]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[393]}"><h1 align="center">{list_nombres[393]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[394]}"><h1 align="center">{list_nombres[394]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[395]}"><h1 align="center">{list_nombres[395]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[396]}"><h1 align="center">{list_nombres[396]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[397]}"><h1 align="center">{list_nombres[397]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[398]}"><h1 align="center">{list_nombres[398]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[399]}"><h1 align="center">{list_nombres[399]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[400]}"><h1 align="center">{list_nombres[400]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[401]}"><h1 align="center">{list_nombres[401]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[402]}"><h1 align="center">{list_nombres[402]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[403]}"><h1 align="center">{list_nombres[403]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[404]}"><h1 align="center">{list_nombres[404]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[405]}"><h1 align="center">{list_nombres[405]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[406]}"><h1 align="center">{list_nombres[406]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[407]}"><h1 align="center">{list_nombres[407]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[408]}"><h1 align="center">{list_nombres[408]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[409]}"><h1 align="center">{list_nombres[409]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[410]}"><h1 align="center">{list_nombres[410]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[411]}"><h1 align="center">{list_nombres[411]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[412]}"><h1 align="center">{list_nombres[412]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[413]}"><h1 align="center">{list_nombres[413]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[414]}"><h1 align="center">{list_nombres[414]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[415]}"><h1 align="center">{list_nombres[415]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[416]}"><h1 align="center">{list_nombres[416]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[417]}"><h1 align="center">{list_nombres[417]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[418]}"><h1 align="center">{list_nombres[418]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[419]}"><h1 align="center">{list_nombres[419]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[420]}"><h1 align="center">{list_nombres[420]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[421]}"><h1 align="center">{list_nombres[421]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[422]}"><h1 align="center">{list_nombres[422]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[423]}"><h1 align="center">{list_nombres[423]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[424]}"><h1 align="center">{list_nombres[424]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[425]}"><h1 align="center">{list_nombres[425]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[426]}"><h1 align="center">{list_nombres[426]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[427]}"><h1 align="center">{list_nombres[427]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[428]}"><h1 align="center">{list_nombres[428]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[429]}"><h1 align="center">{list_nombres[429]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[430]}"><h1 align="center">{list_nombres[430]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[431]}"><h1 align="center">{list_nombres[431]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[432]}"><h1 align="center">{list_nombres[432]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[433]}"><h1 align="center">{list_nombres[433]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[434]}"><h1 align="center">{list_nombres[434]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[435]}"><h1 align="center">{list_nombres[435]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[436]}"><h1 align="center">{list_nombres[436]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[437]}"><h1 align="center">{list_nombres[437]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[438]}"><h1 align="center">{list_nombres[438]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[439]}"><h1 align="center">{list_nombres[439]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[440]}"><h1 align="center">{list_nombres[440]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[441]}"><h1 align="center">{list_nombres[441]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[442]}"><h1 align="center">{list_nombres[442]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[443]}"><h1 align="center">{list_nombres[443]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[444]}"><h1 align="center">{list_nombres[444]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[445]}"><h1 align="center">{list_nombres[445]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[446]}"><h1 align="center">{list_nombres[446]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[447]}"><h1 align="center">{list_nombres[447]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[448]}"><h1 align="center">{list_nombres[448]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[449]}"><h1 align="center">{list_nombres[449]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[450]}"><h1 align="center">{list_nombres[450]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[451]}"><h1 align="center">{list_nombres[451]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[452]}"><h1 align="center">{list_nombres[452]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[453]}"><h1 align="center">{list_nombres[453]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[454]}"><h1 align="center">{list_nombres[454]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[455]}"><h1 align="center">{list_nombres[455]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[456]}"><h1 align="center">{list_nombres[456]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[457]}"><h1 align="center">{list_nombres[457]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[458]}"><h1 align="center">{list_nombres[458]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[459]}"><h1 align="center">{list_nombres[459]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[460]}"><h1 align="center">{list_nombres[460]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[461]}"><h1 align="center">{list_nombres[461]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[462]}"><h1 align="center">{list_nombres[462]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[463]}"><h1 align="center">{list_nombres[463]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[464]}"><h1 align="center">{list_nombres[464]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[465]}"><h1 align="center">{list_nombres[465]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[466]}"><h1 align="center">{list_nombres[466]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[467]}"><h1 align="center">{list_nombres[467]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[468]}"><h1 align="center">{list_nombres[468]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[469]}"><h1 align="center">{list_nombres[469]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[470]}"><h1 align="center">{list_nombres[470]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[471]}"><h1 align="center">{list_nombres[471]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[472]}"><h1 align="center">{list_nombres[472]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[473]}"><h1 align="center">{list_nombres[473]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[474]}"><h1 align="center">{list_nombres[474]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[475]}"><h1 align="center">{list_nombres[475]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[476]}"><h1 align="center">{list_nombres[476]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[477]}"><h1 align="center">{list_nombres[477]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[478]}"><h1 align="center">{list_nombres[478]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[479]}"><h1 align="center">{list_nombres[479]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[480]}"><h1 align="center">{list_nombres[480]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[481]}"><h1 align="center">{list_nombres[481]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[482]}"><h1 align="center">{list_nombres[482]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[483]}"><h1 align="center">{list_nombres[483]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[484]}"><h1 align="center">{list_nombres[484]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[485]}"><h1 align="center">{list_nombres[485]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[486]}"><h1 align="center">{list_nombres[486]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[487]}"><h1 align="center">{list_nombres[487]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[488]}"><h1 align="center">{list_nombres[488]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[489]}"><h1 align="center">{list_nombres[489]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[490]}"><h1 align="center">{list_nombres[490]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[491]}"><h1 align="center">{list_nombres[491]}</h1></a>
                    <br><a href="/index_Characters/{list_nombres[492]}"><h1 align="center">{list_nombres[492]}</h1></a>
                </body>
            </html>
            '''


@app.route('/index_Locations')
def index_Locations():
    list_locaciones = []
    locaciones = getlocations()
    for i in locaciones:
        list_locaciones.append(i.name)


    return f'''<!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <meta http-equiv="X-UA-Compatible" content="ie=edge">
                        <title>Locaciones</title>
                        <div align="center"><img src="static/RMLogo.jpg"></div>
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
    epi = getepisodes()
    list_episode = []
    for i in epi:
        list_episode.append(i.name)

    return f'''<!DOCTYPE html>
                        <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                <title>Episodios</title>
                                <div align="center"><img src="static/RMLogo.jpg"></div>
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
def index_CharactersSpec(name):
    characters = getcharacters()
    for i in characters:
        if i.name == name:
            return f'''<!DOCTYPE html>
                       <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                <title>Personaje</title>
                                <div align="center"><img src="/static/RMLogo.jpg"></div>
                            </head>
                            <body>
                                <br><h1 align="center">Id -> {i.id}</h1></a>
                                <br><h1 align="center">Name -> {i.name}</h1></a>
                                <br><h1 align="center">Status -> {i.status}</h1></a>
                                <br><h1 align="center">Specie -> {i.species}</h1></a>
                                <br><h1 align="center">Gender -> {i.gender}</h1></a>
                                <br><h1 align="center">Origin -> {i.nameOrigin}</h1></a>
                                <br><h1 align="center">Image - > {i.image}</h1></a>
                                <br><h1 align="center">Episodes - > {i.episodes}</h1></a>
                            </body>
                       </html>
                '''


@app.route('/index_Locations/<string:name>')
def index_LocationsSpec(name):
    query = getlocations()
    for i in query:
        if i.name == name:
            return f'''<!DOCTYPE html>
                       <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                <title>Locacion</title>
                                <div align="center"><img src="/static/RMLogo.jpg"></div>
                            </head>
                            <body>
                                <br><h1 align="center">Id -> {i.id}</h1></a>
                                <br><h1 align="center">Name -> {i.name}</h1></a>
                                <br><h1 align="center">Type -> {i.tipe}</h1></a>
                                <br><h1 align="center">Dimension -> {i.dimension}</h1></a>
                                <br><h1 align="center">Residents -> {i.residents}</h1></a>
                            </body>
                       </html>
                '''


@app.route('/index_Episodes/<string:name>')
def index_EpisodesSpec(name):
    query = getepisodes()
    for i in query:
        if i.name == name:
            return f'''<!DOCTYPE html>
                       <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                <title>Locacion</title>
                                <div align="center"><img src="/static/RMLogo.jpg"></div>
                            </head>
                            <body>
                                <br><h1 align="center">Id -> {i.id}</h1></a>
                                <br><h1 align="center">Name -> {i.name}</h1></a>
                                <br><h1 align="center">Air_Date -> {i.air_date}</h1></a>
                                <br><h1 align="center">Episode -> {i.episode}</h1></a>
                                <br><h1 align="center">Characters -> {i.characters}</h1></a>
                            </body>
                       </html>
                '''



def main():
    app.debug = True
    app.run(port=8000)

if __name__ == '__main__':
    main()