import peewee
db = peewee.SqliteDatabase('baseRyM.db')

class baseModel(peewee.Model):
    class Meta:
        database = db


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


def get_character():
    lista = []
    characters = Characters.select(Characters.id, Characters.name, Characters.status, Characters.species,
                                   Characters.tipe, Characters.gender, Characters.nameOrigin, Characters.urlOrigin,
                                   Characters.nameLocation, Characters.urlLocation, Characters.image,
                                   Characters.episodes, Characters.url, Characters.created)
    for i in characters:
        lista.append(i)
    return lista


def get_location():
    lista = []
    locations = Location.select(Location.id, Location.name, Location.tipe, Location.dimension, Location.residents,
                                Location.url, Location.created)
    for i in locations:
        lista.append(i)
    return lista


def get_episode():
    lista = []
    episodes = Episode.select(Episode.id, Episode.name, Episode.air_date, Episode.episode, Episode.characters,
                              Episode.url, Episode.created)
    for i in episodes:
        lista.append(i)
    return lista


def crear_indexPrincipal():
    tablas = db.get_tables()

    string_html = f'''<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Rick y Morty</title>
                <div align="center"><img src="Rick_and_Morty_logo.png"></div>
            </head>
            <body>
                <br><a href="characters-index.html"><h1 align="center">{tablas[0]}</h1></a>
                <br><a href="episodes-index.html"><h1 align="center">{tablas[1]}</h1></a>
                <br><a href="locations-index.html"><h1 align="center">{tablas[2]}</h1></a>           
            </body>
        </html>
        '''
    f = open("index.html", "w")
    f.write(string_html)
    f.close()


def crear_indexCharacters():
    query = get_character()
    list_nombres = []
    for i in query:
        list_nombres.append(i.name)

    string_html = f'''<!DOCTYPE html>
            <html lang="en"> <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>Personajes</title>
                    <div align="center"><img src="Rick_and_Morty_logo.png"></div>
                </head>
                <body>
                    <br><a href="Personajes/1.html"><h1 align="center">{list_nombres[0]}</h1></a>
                    <br><a href="Personajes/2.html"><h1 align="center">{list_nombres[1]}</h1></a>
                    <br><a href="Personajes/3.html"><h1 align="center">{list_nombres[2]}</h1></a>
                    <br><a href="Personajes/4.html"><h1 align="center">{list_nombres[3]}</h1></a>
                    <br><a href="Personajes/5.html"><h1 align="center">{list_nombres[4]}</h1></a>
                    <br><a href="Personajes/6.html"><h1 align="center">{list_nombres[5]}</h1></a>
                    <br><a href="Personajes/7.html"><h1 align="center">{list_nombres[6]}</h1></a>
                    <br><a href="Personajes/8.html"><h1 align="center">{list_nombres[7]}</h1></a>
                    <br><a href="Personajes/9.html"><h1 align="center">{list_nombres[8]}</h1></a>
                    <br><a href="Personajes/10.html"><h1 align="center">{list_nombres[9]}</h1></a>
                    <br><a href="Personajes/11.html"><h1 align="center">{list_nombres[10]}</h1></a>
                    <br><a href="Personajes/12.html"><h1 align="center">{list_nombres[11]}</h1></a>
                    <br><a href="Personajes/13.html"><h1 align="center">{list_nombres[12]}</h1></a>
                    <br><a href="Personajes/14.html"><h1 align="center">{list_nombres[13]}</h1></a>
                    <br><a href="Personajes/15.html"><h1 align="center">{list_nombres[14]}</h1></a>
                    <br><a href="Personajes/16.html"><h1 align="center">{list_nombres[15]}</h1></a>
                    <br><a href="Personajes/17.html"><h1 align="center">{list_nombres[16]}</h1></a>
                    <br><a href="Personajes/18.html"><h1 align="center">{list_nombres[17]}</h1></a>
                    <br><a href="Personajes/19.html"><h1 align="center">{list_nombres[18]}</h1></a>
                    <br><a href="Personajes/20.html"><h1 align="center">{list_nombres[19]}</h1></a>
                    <br><a href="Personajes/21.html"><h1 align="center">{list_nombres[20]}</h1></a>
                    <br><a href="Personajes/22.html"><h1 align="center">{list_nombres[21]}</h1></a>
                    <br><a href="Personajes/23.html"><h1 align="center">{list_nombres[22]}</h1></a>
                    <br><a href="Personajes/24.html"><h1 align="center">{list_nombres[23]}</h1></a>
                    <br><a href="Personajes/25.html"><h1 align="center">{list_nombres[24]}</h1></a>
                    <br><a href="Personajes/26.html"><h1 align="center">{list_nombres[25]}</h1></a>
                    <br><a href="Personajes/27.html"><h1 align="center">{list_nombres[26]}</h1></a>
                    <br><a href="Personajes/28.html"><h1 align="center">{list_nombres[27]}</h1></a>
                    <br><a href="Personajes/29.html"><h1 align="center">{list_nombres[28]}</h1></a>
                    <br><a href="Personajes/30.html"><h1 align="center">{list_nombres[29]}</h1></a>
                    <br><a href="Personajes/31.html"><h1 align="center">{list_nombres[30]}</h1></a>
                    <br><a href="Personajes/32.html"><h1 align="center">{list_nombres[31]}</h1></a>
                    <br><a href="Personajes/33.html"><h1 align="center">{list_nombres[32]}</h1></a>
                    <br><a href="Personajes/34.html"><h1 align="center">{list_nombres[33]}</h1></a>
                    <br><a href="Personajes/35.html"><h1 align="center">{list_nombres[34]}</h1></a>
                    <br><a href="Personajes/36.html"><h1 align="center">{list_nombres[35]}</h1></a>
                    <br><a href="Personajes/37.html"><h1 align="center">{list_nombres[36]}</h1></a>
                    <br><a href="Personajes/38.html"><h1 align="center">{list_nombres[37]}</h1></a>
                    <br><a href="Personajes/39.html"><h1 align="center">{list_nombres[38]}</h1></a>
                    <br><a href="Personajes/40.html"><h1 align="center">{list_nombres[39]}</h1></a>
                    <br><a href="Personajes/41.html"><h1 align="center">{list_nombres[40]}</h1></a>
                    <br><a href="Personajes/42.html"><h1 align="center">{list_nombres[41]}</h1></a>
                    <br><a href="Personajes/43.html"><h1 align="center">{list_nombres[42]}</h1></a>
                    <br><a href="Personajes/44.html"><h1 align="center">{list_nombres[43]}</h1></a>
                    <br><a href="Personajes/45.html"><h1 align="center">{list_nombres[44]}</h1></a>
                    <br><a href="Personajes/46.html"><h1 align="center">{list_nombres[45]}</h1></a>
                    <br><a href="Personajes/47.html"><h1 align="center">{list_nombres[46]}</h1></a>
                    <br><a href="Personajes/48.html"><h1 align="center">{list_nombres[47]}</h1></a>
                    <br><a href="Personajes/49.html"><h1 align="center">{list_nombres[48]}</h1></a>
                    <br><a href="Personajes/50.html"><h1 align="center">{list_nombres[49]}</h1></a>
                    <br><a href="Personajes/51.html"><h1 align="center">{list_nombres[50]}</h1></a>
                    <br><a href="Personajes/52.html"><h1 align="center">{list_nombres[51]}</h1></a>
                    <br><a href="Personajes/53.html"><h1 align="center">{list_nombres[52]}</h1></a>
                    <br><a href="Personajes/54.html"><h1 align="center">{list_nombres[53]}</h1></a>
                    <br><a href="Personajes/55.html"><h1 align="center">{list_nombres[54]}</h1></a>
                    <br><a href="Personajes/56.html"><h1 align="center">{list_nombres[55]}</h1></a>
                    <br><a href="Personajes/57.html"><h1 align="center">{list_nombres[56]}</h1></a>
                    <br><a href="Personajes/58.html"><h1 align="center">{list_nombres[57]}</h1></a>
                    <br><a href="Personajes/59.html"><h1 align="center">{list_nombres[58]}</h1></a>
                    <br><a href="Personajes/60.html"><h1 align="center">{list_nombres[59]}</h1></a>
                    <br><a href="Personajes/61.html"><h1 align="center">{list_nombres[60]}</h1></a>
                    <br><a href="Personajes/62.html"><h1 align="center">{list_nombres[61]}</h1></a>
                    <br><a href="Personajes/63.html"><h1 align="center">{list_nombres[62]}</h1></a>
                    <br><a href="Personajes/64.html"><h1 align="center">{list_nombres[63]}</h1></a>
                    <br><a href="Personajes/65.html"><h1 align="center">{list_nombres[64]}</h1></a>
                    <br><a href="Personajes/66.html"><h1 align="center">{list_nombres[65]}</h1></a>
                    <br><a href="Personajes/67.html"><h1 align="center">{list_nombres[66]}</h1></a>
                    <br><a href="Personajes/68.html"><h1 align="center">{list_nombres[67]}</h1></a>
                    <br><a href="Personajes/69.html"><h1 align="center">{list_nombres[68]}</h1></a>
                    <br><a href="Personajes/70.html"><h1 align="center">{list_nombres[69]}</h1></a>
                    <br><a href="Personajes/71.html"><h1 align="center">{list_nombres[70]}</h1></a>
                    <br><a href="Personajes/72.html"><h1 align="center">{list_nombres[71]}</h1></a>
                    <br><a href="Personajes/73.html"><h1 align="center">{list_nombres[72]}</h1></a>
                    <br><a href="Personajes/74.html"><h1 align="center">{list_nombres[73]}</h1></a>
                    <br><a href="Personajes/75.html"><h1 align="center">{list_nombres[74]}</h1></a>
                    <br><a href="Personajes/76.html"><h1 align="center">{list_nombres[75]}</h1></a>
                    <br><a href="Personajes/77.html"><h1 align="center">{list_nombres[76]}</h1></a>
                    <br><a href="Personajes/78.html"><h1 align="center">{list_nombres[77]}</h1></a>
                    <br><a href="Personajes/79.html"><h1 align="center">{list_nombres[78]}</h1></a>
                    <br><a href="Personajes/80.html"><h1 align="center">{list_nombres[79]}</h1></a>
                    <br><a href="Personajes/81.html"><h1 align="center">{list_nombres[80]}</h1></a>
                    <br><a href="Personajes/82.html"><h1 align="center">{list_nombres[81]}</h1></a>
                    <br><a href="Personajes/83.html"><h1 align="center">{list_nombres[82]}</h1></a>
                    <br><a href="Personajes/84.html"><h1 align="center">{list_nombres[83]}</h1></a>
                    <br><a href="Personajes/85.html"><h1 align="center">{list_nombres[84]}</h1></a>
                    <br><a href="Personajes/86.html"><h1 align="center">{list_nombres[85]}</h1></a>
                    <br><a href="Personajes/87.html"><h1 align="center">{list_nombres[86]}</h1></a>
                    <br><a href="Personajes/88.html"><h1 align="center">{list_nombres[87]}</h1></a>
                    <br><a href="Personajes/89.html"><h1 align="center">{list_nombres[88]}</h1></a>
                    <br><a href="Personajes/90.html"><h1 align="center">{list_nombres[89]}</h1></a>
                    <br><a href="Personajes/91.html"><h1 align="center">{list_nombres[90]}</h1></a>
                    <br><a href="Personajes/92.html"><h1 align="center">{list_nombres[91]}</h1></a>
                    <br><a href="Personajes/93.html"><h1 align="center">{list_nombres[92]}</h1></a>
                    <br><a href="Personajes/94.html"><h1 align="center">{list_nombres[93]}</h1></a>
                    <br><a href="Personajes/95.html"><h1 align="center">{list_nombres[94]}</h1></a>
                    <br><a href="Personajes/96.html"><h1 align="center">{list_nombres[95]}</h1></a>
                    <br><a href="Personajes/97.html"><h1 align="center">{list_nombres[96]}</h1></a>
                    <br><a href="Personajes/98.html"><h1 align="center">{list_nombres[97]}</h1></a>
                    <br><a href="Personajes/99.html"><h1 align="center">{list_nombres[98]}</h1></a>
                    <br><a href="Personajes/100.html"><h1 align="center">{list_nombres[99]}</h1></a>
                    <br><a href="Personajes/101.html"><h1 align="center">{list_nombres[100]}</h1></a>
                    <br><a href="Personajes/102.html"><h1 align="center">{list_nombres[101]}</h1></a>
                    <br><a href="Personajes/103.html"><h1 align="center">{list_nombres[102]}</h1></a>
                    <br><a href="Personajes/104.html"><h1 align="center">{list_nombres[103]}</h1></a>
                    <br><a href="Personajes/105.html"><h1 align="center">{list_nombres[104]}</h1></a>
                    <br><a href="Personajes/106.html"><h1 align="center">{list_nombres[105]}</h1></a>
                    <br><a href="Personajes/107.html"><h1 align="center">{list_nombres[106]}</h1></a>
                    <br><a href="Personajes/108.html"><h1 align="center">{list_nombres[107]}</h1></a>
                    <br><a href="Personajes/109.html"><h1 align="center">{list_nombres[108]}</h1></a>
                    <br><a href="Personajes/110.html"><h1 align="center">{list_nombres[109]}</h1></a>
                    <br><a href="Personajes/111.html"><h1 align="center">{list_nombres[110]}</h1></a>
                    <br><a href="Personajes/112.html"><h1 align="center">{list_nombres[111]}</h1></a>
                    <br><a href="Personajes/113.html"><h1 align="center">{list_nombres[112]}</h1></a>
                    <br><a href="Personajes/114.html"><h1 align="center">{list_nombres[113]}</h1></a>
                    <br><a href="Personajes/115.html"><h1 align="center">{list_nombres[114]}</h1></a>
                    <br><a href="Personajes/116.html"><h1 align="center">{list_nombres[115]}</h1></a>
                    <br><a href="Personajes/117.html"><h1 align="center">{list_nombres[116]}</h1></a>
                    <br><a href="Personajes/118.html"><h1 align="center">{list_nombres[117]}</h1></a>
                    <br><a href="Personajes/119.html"><h1 align="center">{list_nombres[118]}</h1></a>
                    <br><a href="Personajes/120.html"><h1 align="center">{list_nombres[119]}</h1></a>
                    <br><a href="Personajes/121.html"><h1 align="center">{list_nombres[120]}</h1></a>
                    <br><a href="Personajes/122.html"><h1 align="center">{list_nombres[121]}</h1></a>
                    <br><a href="Personajes/123.html"><h1 align="center">{list_nombres[122]}</h1></a>
                    <br><a href="Personajes/124.html"><h1 align="center">{list_nombres[123]}</h1></a>
                    <br><a href="Personajes/125.html"><h1 align="center">{list_nombres[124]}</h1></a>
                    <br><a href="Personajes/126.html"><h1 align="center">{list_nombres[125]}</h1></a>
                    <br><a href="Personajes/127.html"><h1 align="center">{list_nombres[126]}</h1></a>
                    <br><a href="Personajes/128.html"><h1 align="center">{list_nombres[127]}</h1></a>
                    <br><a href="Personajes/129.html"><h1 align="center">{list_nombres[128]}</h1></a>
                    <br><a href="Personajes/130.html"><h1 align="center">{list_nombres[129]}</h1></a>
                    <br><a href="Personajes/131.html"><h1 align="center">{list_nombres[130]}</h1></a>
                    <br><a href="Personajes/132.html"><h1 align="center">{list_nombres[131]}</h1></a>
                    <br><a href="Personajes/133.html"><h1 align="center">{list_nombres[132]}</h1></a>
                    <br><a href="Personajes/134.html"><h1 align="center">{list_nombres[133]}</h1></a>
                    <br><a href="Personajes/135.html"><h1 align="center">{list_nombres[134]}</h1></a>
                    <br><a href="Personajes/136.html"><h1 align="center">{list_nombres[135]}</h1></a>
                    <br><a href="Personajes/137.html"><h1 align="center">{list_nombres[136]}</h1></a>
                    <br><a href="Personajes/138.html"><h1 align="center">{list_nombres[137]}</h1></a>
                    <br><a href="Personajes/139.html"><h1 align="center">{list_nombres[138]}</h1></a>
                    <br><a href="Personajes/140.html"><h1 align="center">{list_nombres[139]}</h1></a>
                    <br><a href="Personajes/141.html"><h1 align="center">{list_nombres[140]}</h1></a>
                    <br><a href="Personajes/142.html"><h1 align="center">{list_nombres[141]}</h1></a>
                    <br><a href="Personajes/143.html"><h1 align="center">{list_nombres[142]}</h1></a>
                    <br><a href="Personajes/144.html"><h1 align="center">{list_nombres[143]}</h1></a>
                    <br><a href="Personajes/145.html"><h1 align="center">{list_nombres[144]}</h1></a>
                    <br><a href="Personajes/146.html"><h1 align="center">{list_nombres[145]}</h1></a>
                    <br><a href="Personajes/147.html"><h1 align="center">{list_nombres[146]}</h1></a>
                    <br><a href="Personajes/148.html"><h1 align="center">{list_nombres[147]}</h1></a>
                    <br><a href="Personajes/149.html"><h1 align="center">{list_nombres[148]}</h1></a>
                    <br><a href="Personajes/150.html"><h1 align="center">{list_nombres[149]}</h1></a>
                    <br><a href="Personajes/151.html"><h1 align="center">{list_nombres[150]}</h1></a>
                    <br><a href="Personajes/152.html"><h1 align="center">{list_nombres[151]}</h1></a>
                    <br><a href="Personajes/153.html"><h1 align="center">{list_nombres[152]}</h1></a>
                    <br><a href="Personajes/154.html"><h1 align="center">{list_nombres[153]}</h1></a>
                    <br><a href="Personajes/155.html"><h1 align="center">{list_nombres[154]}</h1></a>
                    <br><a href="Personajes/156.html"><h1 align="center">{list_nombres[155]}</h1></a>
                    <br><a href="Personajes/157.html"><h1 align="center">{list_nombres[156]}</h1></a>
                    <br><a href="Personajes/158.html"><h1 align="center">{list_nombres[157]}</h1></a>
                    <br><a href="Personajes/159.html"><h1 align="center">{list_nombres[158]}</h1></a>
                    <br><a href="Personajes/160.html"><h1 align="center">{list_nombres[159]}</h1></a>
                    <br><a href="Personajes/161.html"><h1 align="center">{list_nombres[160]}</h1></a>
                    <br><a href="Personajes/162.html"><h1 align="center">{list_nombres[161]}</h1></a>
                    <br><a href="Personajes/163.html"><h1 align="center">{list_nombres[162]}</h1></a>
                    <br><a href="Personajes/164.html"><h1 align="center">{list_nombres[163]}</h1></a>
                    <br><a href="Personajes/165.html"><h1 align="center">{list_nombres[164]}</h1></a>
                    <br><a href="Personajes/166.html"><h1 align="center">{list_nombres[165]}</h1></a>
                    <br><a href="Personajes/167.html"><h1 align="center">{list_nombres[166]}</h1></a>
                    <br><a href="Personajes/168.html"><h1 align="center">{list_nombres[167]}</h1></a>
                    <br><a href="Personajes/169.html"><h1 align="center">{list_nombres[168]}</h1></a>
                    <br><a href="Personajes/170.html"><h1 align="center">{list_nombres[169]}</h1></a>
                    <br><a href="Personajes/171.html"><h1 align="center">{list_nombres[170]}</h1></a>
                    <br><a href="Personajes/172.html"><h1 align="center">{list_nombres[171]}</h1></a>
                    <br><a href="Personajes/173.html"><h1 align="center">{list_nombres[172]}</h1></a>
                    <br><a href="Personajes/174.html"><h1 align="center">{list_nombres[173]}</h1></a>
                    <br><a href="Personajes/175.html"><h1 align="center">{list_nombres[174]}</h1></a>
                    <br><a href="Personajes/176.html"><h1 align="center">{list_nombres[175]}</h1></a>
                    <br><a href="Personajes/177.html"><h1 align="center">{list_nombres[176]}</h1></a>
                    <br><a href="Personajes/178.html"><h1 align="center">{list_nombres[177]}</h1></a>
                    <br><a href="Personajes/179.html"><h1 align="center">{list_nombres[178]}</h1></a>
                    <br><a href="Personajes/180.html"><h1 align="center">{list_nombres[179]}</h1></a>
                    <br><a href="Personajes/181.html"><h1 align="center">{list_nombres[180]}</h1></a>
                    <br><a href="Personajes/182.html"><h1 align="center">{list_nombres[181]}</h1></a>
                    <br><a href="Personajes/183.html"><h1 align="center">{list_nombres[182]}</h1></a>
                    <br><a href="Personajes/184.html"><h1 align="center">{list_nombres[183]}</h1></a>
                    <br><a href="Personajes/185.html"><h1 align="center">{list_nombres[184]}</h1></a>
                    <br><a href="Personajes/186.html"><h1 align="center">{list_nombres[185]}</h1></a>
                    <br><a href="Personajes/187.html"><h1 align="center">{list_nombres[186]}</h1></a>
                    <br><a href="Personajes/188.html"><h1 align="center">{list_nombres[187]}</h1></a>
                    <br><a href="Personajes/189.html"><h1 align="center">{list_nombres[188]}</h1></a>
                    <br><a href="Personajes/190.html"><h1 align="center">{list_nombres[189]}</h1></a>
                    <br><a href="Personajes/191.html"><h1 align="center">{list_nombres[190]}</h1></a>
                    <br><a href="Personajes/192.html"><h1 align="center">{list_nombres[191]}</h1></a>
                    <br><a href="Personajes/193.html"><h1 align="center">{list_nombres[192]}</h1></a>
                    <br><a href="Personajes/194.html"><h1 align="center">{list_nombres[193]}</h1></a>
                    <br><a href="Personajes/195.html"><h1 align="center">{list_nombres[194]}</h1></a>
                    <br><a href="Personajes/196.html"><h1 align="center">{list_nombres[195]}</h1></a>
                    <br><a href="Personajes/197.html"><h1 align="center">{list_nombres[196]}</h1></a>
                    <br><a href="Personajes/198.html"><h1 align="center">{list_nombres[197]}</h1></a>
                    <br><a href="Personajes/199.html"><h1 align="center">{list_nombres[198]}</h1></a>
                    <br><a href="Personajes/200.html"><h1 align="center">{list_nombres[199]}</h1></a>
                    <br><a href="Personajes/201.html"><h1 align="center">{list_nombres[200]}</h1></a>
                    <br><a href="Personajes/202.html"><h1 align="center">{list_nombres[201]}</h1></a>
                    <br><a href="Personajes/203.html"><h1 align="center">{list_nombres[202]}</h1></a>
                    <br><a href="Personajes/204.html"><h1 align="center">{list_nombres[203]}</h1></a>
                    <br><a href="Personajes/205.html"><h1 align="center">{list_nombres[204]}</h1></a>
                    <br><a href="Personajes/206.html"><h1 align="center">{list_nombres[205]}</h1></a>
                    <br><a href="Personajes/207.html"><h1 align="center">{list_nombres[206]}</h1></a>
                    <br><a href="Personajes/208.html"><h1 align="center">{list_nombres[207]}</h1></a>
                    <br><a href="Personajes/209.html"><h1 align="center">{list_nombres[208]}</h1></a>
                    <br><a href="Personajes/210.html"><h1 align="center">{list_nombres[209]}</h1></a>
                    <br><a href="Personajes/211.html"><h1 align="center">{list_nombres[210]}</h1></a>
                    <br><a href="Personajes/212.html"><h1 align="center">{list_nombres[211]}</h1></a>
                    <br><a href="Personajes/213.html"><h1 align="center">{list_nombres[212]}</h1></a>
                    <br><a href="Personajes/214.html"><h1 align="center">{list_nombres[213]}</h1></a>
                    <br><a href="Personajes/215.html"><h1 align="center">{list_nombres[214]}</h1></a>
                    <br><a href="Personajes/216.html"><h1 align="center">{list_nombres[215]}</h1></a>
                    <br><a href="Personajes/217.html"><h1 align="center">{list_nombres[216]}</h1></a>
                    <br><a href="Personajes/218.html"><h1 align="center">{list_nombres[217]}</h1></a>
                    <br><a href="Personajes/219.html"><h1 align="center">{list_nombres[218]}</h1></a>
                    <br><a href="Personajes/220.html"><h1 align="center">{list_nombres[219]}</h1></a>
                    <br><a href="Personajes/221.html"><h1 align="center">{list_nombres[220]}</h1></a>
                    <br><a href="Personajes/222.html"><h1 align="center">{list_nombres[221]}</h1></a>
                    <br><a href="Personajes/223.html"><h1 align="center">{list_nombres[222]}</h1></a>
                    <br><a href="Personajes/224.html"><h1 align="center">{list_nombres[223]}</h1></a>
                    <br><a href="Personajes/225.html"><h1 align="center">{list_nombres[224]}</h1></a>
                    <br><a href="Personajes/226.html"><h1 align="center">{list_nombres[225]}</h1></a>
                    <br><a href="Personajes/227.html"><h1 align="center">{list_nombres[226]}</h1></a>
                    <br><a href="Personajes/228.html"><h1 align="center">{list_nombres[227]}</h1></a>
                    <br><a href="Personajes/229.html"><h1 align="center">{list_nombres[228]}</h1></a>
                    <br><a href="Personajes/230.html"><h1 align="center">{list_nombres[229]}</h1></a>
                    <br><a href="Personajes/231.html"><h1 align="center">{list_nombres[230]}</h1></a>
                    <br><a href="Personajes/232.html"><h1 align="center">{list_nombres[231]}</h1></a>
                    <br><a href="Personajes/233.html"><h1 align="center">{list_nombres[232]}</h1></a>
                    <br><a href="Personajes/234.html"><h1 align="center">{list_nombres[233]}</h1></a>
                    <br><a href="Personajes/235.html"><h1 align="center">{list_nombres[234]}</h1></a>
                    <br><a href="Personajes/236.html"><h1 align="center">{list_nombres[235]}</h1></a>
                    <br><a href="Personajes/237.html"><h1 align="center">{list_nombres[236]}</h1></a>
                    <br><a href="Personajes/238.html"><h1 align="center">{list_nombres[237]}</h1></a>
                    <br><a href="Personajes/239.html"><h1 align="center">{list_nombres[238]}</h1></a>
                    <br><a href="Personajes/240.html"><h1 align="center">{list_nombres[239]}</h1></a>
                    <br><a href="Personajes/241.html"><h1 align="center">{list_nombres[240]}</h1></a>
                    <br><a href="Personajes/242.html"><h1 align="center">{list_nombres[241]}</h1></a>
                    <br><a href="Personajes/243.html"><h1 align="center">{list_nombres[242]}</h1></a>
                    <br><a href="Personajes/244.html"><h1 align="center">{list_nombres[243]}</h1></a>
                    <br><a href="Personajes/245.html"><h1 align="center">{list_nombres[244]}</h1></a>
                    <br><a href="Personajes/246.html"><h1 align="center">{list_nombres[245]}</h1></a>
                    <br><a href="Personajes/247.html"><h1 align="center">{list_nombres[246]}</h1></a>
                    <br><a href="Personajes/248.html"><h1 align="center">{list_nombres[247]}</h1></a>
                    <br><a href="Personajes/249.html"><h1 align="center">{list_nombres[248]}</h1></a>
                    <br><a href="Personajes/250.html"><h1 align="center">{list_nombres[249]}</h1></a>
                    <br><a href="Personajes/251.html"><h1 align="center">{list_nombres[250]}</h1></a>
                    <br><a href="Personajes/252.html"><h1 align="center">{list_nombres[251]}</h1></a>
                    <br><a href="Personajes/253.html"><h1 align="center">{list_nombres[252]}</h1></a>
                    <br><a href="Personajes/254.html"><h1 align="center">{list_nombres[253]}</h1></a>
                    <br><a href="Personajes/255.html"><h1 align="center">{list_nombres[254]}</h1></a>
                    <br><a href="Personajes/256.html"><h1 align="center">{list_nombres[255]}</h1></a>
                    <br><a href="Personajes/257.html"><h1 align="center">{list_nombres[256]}</h1></a>
                    <br><a href="Personajes/258.html"><h1 align="center">{list_nombres[257]}</h1></a>
                    <br><a href="Personajes/259.html"><h1 align="center">{list_nombres[258]}</h1></a>
                    <br><a href="Personajes/260.html"><h1 align="center">{list_nombres[259]}</h1></a>
                    <br><a href="Personajes/261.html"><h1 align="center">{list_nombres[260]}</h1></a>
                    <br><a href="Personajes/262.html"><h1 align="center">{list_nombres[261]}</h1></a>
                    <br><a href="Personajes/263.html"><h1 align="center">{list_nombres[262]}</h1></a>
                    <br><a href="Personajes/264.html"><h1 align="center">{list_nombres[263]}</h1></a>
                    <br><a href="Personajes/265.html"><h1 align="center">{list_nombres[264]}</h1></a>
                    <br><a href="Personajes/266.html"><h1 align="center">{list_nombres[265]}</h1></a>
                    <br><a href="Personajes/267.html"><h1 align="center">{list_nombres[266]}</h1></a>
                    <br><a href="Personajes/268.html"><h1 align="center">{list_nombres[267]}</h1></a>
                    <br><a href="Personajes/269.html"><h1 align="center">{list_nombres[268]}</h1></a>
                    <br><a href="Personajes/270.html"><h1 align="center">{list_nombres[269]}</h1></a>
                    <br><a href="Personajes/271.html"><h1 align="center">{list_nombres[270]}</h1></a>
                    <br><a href="Personajes/272.html"><h1 align="center">{list_nombres[271]}</h1></a>
                    <br><a href="Personajes/273.html"><h1 align="center">{list_nombres[272]}</h1></a>
                    <br><a href="Personajes/274.html"><h1 align="center">{list_nombres[273]}</h1></a>
                    <br><a href="Personajes/275.html"><h1 align="center">{list_nombres[274]}</h1></a>
                    <br><a href="Personajes/276.html"><h1 align="center">{list_nombres[275]}</h1></a>
                    <br><a href="Personajes/277.html"><h1 align="center">{list_nombres[276]}</h1></a>
                    <br><a href="Personajes/278.html"><h1 align="center">{list_nombres[277]}</h1></a>
                    <br><a href="Personajes/279.html"><h1 align="center">{list_nombres[278]}</h1></a>
                    <br><a href="Personajes/280.html"><h1 align="center">{list_nombres[279]}</h1></a>
                    <br><a href="Personajes/281.html"><h1 align="center">{list_nombres[280]}</h1></a>
                    <br><a href="Personajes/282.html"><h1 align="center">{list_nombres[281]}</h1></a>
                    <br><a href="Personajes/283.html"><h1 align="center">{list_nombres[282]}</h1></a>
                    <br><a href="Personajes/284.html"><h1 align="center">{list_nombres[283]}</h1></a>
                    <br><a href="Personajes/285.html"><h1 align="center">{list_nombres[284]}</h1></a>
                    <br><a href="Personajes/286.html"><h1 align="center">{list_nombres[285]}</h1></a>
                    <br><a href="Personajes/287.html"><h1 align="center">{list_nombres[286]}</h1></a>
                    <br><a href="Personajes/288.html"><h1 align="center">{list_nombres[287]}</h1></a>
                    <br><a href="Personajes/289.html"><h1 align="center">{list_nombres[288]}</h1></a>
                    <br><a href="Personajes/290.html"><h1 align="center">{list_nombres[289]}</h1></a>
                    <br><a href="Personajes/291.html"><h1 align="center">{list_nombres[290]}</h1></a>
                    <br><a href="Personajes/292.html"><h1 align="center">{list_nombres[291]}</h1></a>
                    <br><a href="Personajes/293.html"><h1 align="center">{list_nombres[292]}</h1></a>
                    <br><a href="Personajes/294.html"><h1 align="center">{list_nombres[293]}</h1></a>
                    <br><a href="Personajes/295.html"><h1 align="center">{list_nombres[294]}</h1></a>
                    <br><a href="Personajes/296.html"><h1 align="center">{list_nombres[295]}</h1></a>
                    <br><a href="Personajes/297.html"><h1 align="center">{list_nombres[296]}</h1></a>
                    <br><a href="Personajes/298.html"><h1 align="center">{list_nombres[297]}</h1></a>
                    <br><a href="Personajes/299.html"><h1 align="center">{list_nombres[298]}</h1></a>
                    <br><a href="Personajes/300.html"><h1 align="center">{list_nombres[299]}</h1></a>
                    <br><a href="Personajes/301.html"><h1 align="center">{list_nombres[300]}</h1></a>
                    <br><a href="Personajes/302.html"><h1 align="center">{list_nombres[301]}</h1></a>
                    <br><a href="Personajes/303.html"><h1 align="center">{list_nombres[302]}</h1></a>
                    <br><a href="Personajes/304.html"><h1 align="center">{list_nombres[303]}</h1></a>
                    <br><a href="Personajes/305.html"><h1 align="center">{list_nombres[304]}</h1></a>
                    <br><a href="Personajes/306.html"><h1 align="center">{list_nombres[305]}</h1></a>
                    <br><a href="Personajes/307.html"><h1 align="center">{list_nombres[306]}</h1></a>
                    <br><a href="Personajes/308.html"><h1 align="center">{list_nombres[307]}</h1></a>
                    <br><a href="Personajes/309.html"><h1 align="center">{list_nombres[308]}</h1></a>
                    <br><a href="Personajes/310.html"><h1 align="center">{list_nombres[309]}</h1></a>
                    <br><a href="Personajes/311.html"><h1 align="center">{list_nombres[310]}</h1></a>
                    <br><a href="Personajes/312.html"><h1 align="center">{list_nombres[311]}</h1></a>
                    <br><a href="Personajes/313.html"><h1 align="center">{list_nombres[312]}</h1></a>
                    <br><a href="Personajes/314.html"><h1 align="center">{list_nombres[313]}</h1></a>
                    <br><a href="Personajes/315.html"><h1 align="center">{list_nombres[314]}</h1></a>
                    <br><a href="Personajes/316.html"><h1 align="center">{list_nombres[315]}</h1></a>
                    <br><a href="Personajes/317.html"><h1 align="center">{list_nombres[316]}</h1></a>
                    <br><a href="Personajes/318.html"><h1 align="center">{list_nombres[317]}</h1></a>
                    <br><a href="Personajes/319.html"><h1 align="center">{list_nombres[318]}</h1></a>
                    <br><a href="Personajes/320.html"><h1 align="center">{list_nombres[319]}</h1></a>
                    <br><a href="Personajes/321.html"><h1 align="center">{list_nombres[320]}</h1></a>
                    <br><a href="Personajes/322.html"><h1 align="center">{list_nombres[321]}</h1></a>
                    <br><a href="Personajes/323.html"><h1 align="center">{list_nombres[322]}</h1></a>
                    <br><a href="Personajes/324.html"><h1 align="center">{list_nombres[323]}</h1></a>
                    <br><a href="Personajes/325.html"><h1 align="center">{list_nombres[324]}</h1></a>
                    <br><a href="Personajes/326.html"><h1 align="center">{list_nombres[325]}</h1></a>
                    <br><a href="Personajes/327.html"><h1 align="center">{list_nombres[326]}</h1></a>
                    <br><a href="Personajes/328.html"><h1 align="center">{list_nombres[327]}</h1></a>
                    <br><a href="Personajes/329.html"><h1 align="center">{list_nombres[328]}</h1></a>
                    <br><a href="Personajes/330.html"><h1 align="center">{list_nombres[329]}</h1></a>
                    <br><a href="Personajes/331.html"><h1 align="center">{list_nombres[330]}</h1></a>
                    <br><a href="Personajes/332.html"><h1 align="center">{list_nombres[331]}</h1></a>
                    <br><a href="Personajes/333.html"><h1 align="center">{list_nombres[332]}</h1></a>
                    <br><a href="Personajes/334.html"><h1 align="center">{list_nombres[333]}</h1></a>
                    <br><a href="Personajes/335.html"><h1 align="center">{list_nombres[334]}</h1></a>
                    <br><a href="Personajes/336.html"><h1 align="center">{list_nombres[335]}</h1></a>
                    <br><a href="Personajes/337.html"><h1 align="center">{list_nombres[336]}</h1></a>
                    <br><a href="Personajes/338.html"><h1 align="center">{list_nombres[337]}</h1></a>
                    <br><a href="Personajes/339.html"><h1 align="center">{list_nombres[338]}</h1></a>
                    <br><a href="Personajes/340.html"><h1 align="center">{list_nombres[339]}</h1></a>
                    <br><a href="Personajes/341.html"><h1 align="center">{list_nombres[340]}</h1></a>
                    <br><a href="Personajes/342.html"><h1 align="center">{list_nombres[341]}</h1></a>
                    <br><a href="Personajes/343.html"><h1 align="center">{list_nombres[342]}</h1></a>
                    <br><a href="Personajes/344.html"><h1 align="center">{list_nombres[343]}</h1></a>
                    <br><a href="Personajes/345.html"><h1 align="center">{list_nombres[344]}</h1></a>
                    <br><a href="Personajes/346.html"><h1 align="center">{list_nombres[345]}</h1></a>
                    <br><a href="Personajes/347.html"><h1 align="center">{list_nombres[346]}</h1></a>
                    <br><a href="Personajes/348.html"><h1 align="center">{list_nombres[347]}</h1></a>
                    <br><a href="Personajes/349.html"><h1 align="center">{list_nombres[348]}</h1></a>
                    <br><a href="Personajes/350.html"><h1 align="center">{list_nombres[349]}</h1></a>
                    <br><a href="Personajes/351.html"><h1 align="center">{list_nombres[350]}</h1></a>
                    <br><a href="Personajes/352.html"><h1 align="center">{list_nombres[351]}</h1></a>
                    <br><a href="Personajes/353.html"><h1 align="center">{list_nombres[352]}</h1></a>
                    <br><a href="Personajes/354.html"><h1 align="center">{list_nombres[353]}</h1></a>
                    <br><a href="Personajes/355.html"><h1 align="center">{list_nombres[354]}</h1></a>
                    <br><a href="Personajes/356.html"><h1 align="center">{list_nombres[355]}</h1></a>
                    <br><a href="Personajes/357.html"><h1 align="center">{list_nombres[356]}</h1></a>
                    <br><a href="Personajes/358.html"><h1 align="center">{list_nombres[357]}</h1></a>
                    <br><a href="Personajes/359.html"><h1 align="center">{list_nombres[358]}</h1></a>
                    <br><a href="Personajes/360.html"><h1 align="center">{list_nombres[359]}</h1></a>
                    <br><a href="Personajes/361.html"><h1 align="center">{list_nombres[360]}</h1></a>
                    <br><a href="Personajes/362.html"><h1 align="center">{list_nombres[361]}</h1></a>
                    <br><a href="Personajes/363.html"><h1 align="center">{list_nombres[362]}</h1></a>
                    <br><a href="Personajes/364.html"><h1 align="center">{list_nombres[363]}</h1></a>
                    <br><a href="Personajes/365.html"><h1 align="center">{list_nombres[364]}</h1></a>
                    <br><a href="Personajes/366.html"><h1 align="center">{list_nombres[365]}</h1></a>
                    <br><a href="Personajes/367.html"><h1 align="center">{list_nombres[366]}</h1></a>
                    <br><a href="Personajes/368.html"><h1 align="center">{list_nombres[367]}</h1></a>
                    <br><a href="Personajes/369.html"><h1 align="center">{list_nombres[368]}</h1></a>
                    <br><a href="Personajes/370.html"><h1 align="center">{list_nombres[369]}</h1></a>
                    <br><a href="Personajes/371.html"><h1 align="center">{list_nombres[370]}</h1></a>
                    <br><a href="Personajes/372.html"><h1 align="center">{list_nombres[371]}</h1></a>
                    <br><a href="Personajes/373.html"><h1 align="center">{list_nombres[372]}</h1></a>
                    <br><a href="Personajes/374.html"><h1 align="center">{list_nombres[373]}</h1></a>
                    <br><a href="Personajes/375.html"><h1 align="center">{list_nombres[374]}</h1></a>
                    <br><a href="Personajes/376.html"><h1 align="center">{list_nombres[375]}</h1></a>
                    <br><a href="Personajes/377.html"><h1 align="center">{list_nombres[376]}</h1></a>
                    <br><a href="Personajes/378.html"><h1 align="center">{list_nombres[377]}</h1></a>
                    <br><a href="Personajes/379.html"><h1 align="center">{list_nombres[378]}</h1></a>
                    <br><a href="Personajes/380.html"><h1 align="center">{list_nombres[379]}</h1></a>
                    <br><a href="Personajes/381.html"><h1 align="center">{list_nombres[380]}</h1></a>
                    <br><a href="Personajes/382.html"><h1 align="center">{list_nombres[381]}</h1></a>
                    <br><a href="Personajes/383.html"><h1 align="center">{list_nombres[382]}</h1></a>
                    <br><a href="Personajes/384.html"><h1 align="center">{list_nombres[383]}</h1></a>
                    <br><a href="Personajes/385.html"><h1 align="center">{list_nombres[384]}</h1></a>
                    <br><a href="Personajes/386.html"><h1 align="center">{list_nombres[385]}</h1></a>
                    <br><a href="Personajes/387.html"><h1 align="center">{list_nombres[386]}</h1></a>
                    <br><a href="Personajes/388.html"><h1 align="center">{list_nombres[387]}</h1></a>
                    <br><a href="Personajes/389.html"><h1 align="center">{list_nombres[388]}</h1></a>
                    <br><a href="Personajes/390.html"><h1 align="center">{list_nombres[389]}</h1></a>
                    <br><a href="Personajes/391.html"><h1 align="center">{list_nombres[390]}</h1></a>
                    <br><a href="Personajes/392.html"><h1 align="center">{list_nombres[391]}</h1></a>
                    <br><a href="Personajes/393.html"><h1 align="center">{list_nombres[392]}</h1></a>
                    <br><a href="Personajes/394.html"><h1 align="center">{list_nombres[393]}</h1></a>
                    <br><a href="Personajes/395.html"><h1 align="center">{list_nombres[394]}</h1></a>
                    <br><a href="Personajes/396.html"><h1 align="center">{list_nombres[395]}</h1></a>
                    <br><a href="Personajes/397.html"><h1 align="center">{list_nombres[396]}</h1></a>
                    <br><a href="Personajes/398.html"><h1 align="center">{list_nombres[397]}</h1></a>
                    <br><a href="Personajes/399.html"><h1 align="center">{list_nombres[398]}</h1></a>
                    <br><a href="Personajes/400.html"><h1 align="center">{list_nombres[399]}</h1></a>
                    <br><a href="Personajes/401.html"><h1 align="center">{list_nombres[400]}</h1></a>
                    <br><a href="Personajes/402.html"><h1 align="center">{list_nombres[401]}</h1></a>
                    <br><a href="Personajes/403.html"><h1 align="center">{list_nombres[402]}</h1></a>
                    <br><a href="Personajes/404.html"><h1 align="center">{list_nombres[403]}</h1></a>
                    <br><a href="Personajes/405.html"><h1 align="center">{list_nombres[404]}</h1></a>
                    <br><a href="Personajes/406.html"><h1 align="center">{list_nombres[405]}</h1></a>
                    <br><a href="Personajes/407.html"><h1 align="center">{list_nombres[406]}</h1></a>
                    <br><a href="Personajes/408.html"><h1 align="center">{list_nombres[407]}</h1></a>
                    <br><a href="Personajes/409.html"><h1 align="center">{list_nombres[408]}</h1></a>
                    <br><a href="Personajes/410.html"><h1 align="center">{list_nombres[409]}</h1></a>
                    <br><a href="Personajes/411.html"><h1 align="center">{list_nombres[410]}</h1></a>
                    <br><a href="Personajes/412.html"><h1 align="center">{list_nombres[411]}</h1></a>
                    <br><a href="Personajes/413.html"><h1 align="center">{list_nombres[412]}</h1></a>
                    <br><a href="Personajes/414.html"><h1 align="center">{list_nombres[413]}</h1></a>
                    <br><a href="Personajes/415.html"><h1 align="center">{list_nombres[414]}</h1></a>
                    <br><a href="Personajes/416.html"><h1 align="center">{list_nombres[415]}</h1></a>
                    <br><a href="Personajes/417.html"><h1 align="center">{list_nombres[416]}</h1></a>
                    <br><a href="Personajes/418.html"><h1 align="center">{list_nombres[417]}</h1></a>
                    <br><a href="Personajes/419.html"><h1 align="center">{list_nombres[418]}</h1></a>
                    <br><a href="Personajes/420.html"><h1 align="center">{list_nombres[419]}</h1></a>
                    <br><a href="Personajes/421.html"><h1 align="center">{list_nombres[420]}</h1></a>
                    <br><a href="Personajes/422.html"><h1 align="center">{list_nombres[421]}</h1></a>
                    <br><a href="Personajes/423.html"><h1 align="center">{list_nombres[422]}</h1></a>
                    <br><a href="Personajes/424.html"><h1 align="center">{list_nombres[423]}</h1></a>
                    <br><a href="Personajes/425.html"><h1 align="center">{list_nombres[424]}</h1></a>
                    <br><a href="Personajes/426.html"><h1 align="center">{list_nombres[425]}</h1></a>
                    <br><a href="Personajes/427.html"><h1 align="center">{list_nombres[426]}</h1></a>
                    <br><a href="Personajes/428.html"><h1 align="center">{list_nombres[427]}</h1></a>
                    <br><a href="Personajes/429.html"><h1 align="center">{list_nombres[428]}</h1></a>
                    <br><a href="Personajes/430.html"><h1 align="center">{list_nombres[429]}</h1></a>
                    <br><a href="Personajes/431.html"><h1 align="center">{list_nombres[430]}</h1></a>
                    <br><a href="Personajes/432.html"><h1 align="center">{list_nombres[431]}</h1></a>
                    <br><a href="Personajes/433.html"><h1 align="center">{list_nombres[432]}</h1></a>
                    <br><a href="Personajes/434.html"><h1 align="center">{list_nombres[433]}</h1></a>
                    <br><a href="Personajes/435.html"><h1 align="center">{list_nombres[434]}</h1></a>
                    <br><a href="Personajes/436.html"><h1 align="center">{list_nombres[435]}</h1></a>
                    <br><a href="Personajes/437.html"><h1 align="center">{list_nombres[436]}</h1></a>
                    <br><a href="Personajes/438.html"><h1 align="center">{list_nombres[437]}</h1></a>
                    <br><a href="Personajes/439.html"><h1 align="center">{list_nombres[438]}</h1></a>
                    <br><a href="Personajes/440.html"><h1 align="center">{list_nombres[439]}</h1></a>
                    <br><a href="Personajes/441.html"><h1 align="center">{list_nombres[440]}</h1></a>
                    <br><a href="Personajes/442.html"><h1 align="center">{list_nombres[441]}</h1></a>
                    <br><a href="Personajes/443.html"><h1 align="center">{list_nombres[442]}</h1></a>
                    <br><a href="Personajes/444.html"><h1 align="center">{list_nombres[443]}</h1></a>
                    <br><a href="Personajes/445.html"><h1 align="center">{list_nombres[444]}</h1></a>
                    <br><a href="Personajes/446.html"><h1 align="center">{list_nombres[445]}</h1></a>
                    <br><a href="Personajes/447.html"><h1 align="center">{list_nombres[446]}</h1></a>
                    <br><a href="Personajes/448.html"><h1 align="center">{list_nombres[447]}</h1></a>
                    <br><a href="Personajes/449.html"><h1 align="center">{list_nombres[448]}</h1></a>
                    <br><a href="Personajes/450.html"><h1 align="center">{list_nombres[449]}</h1></a>
                    <br><a href="Personajes/451.html"><h1 align="center">{list_nombres[450]}</h1></a>
                    <br><a href="Personajes/452.html"><h1 align="center">{list_nombres[451]}</h1></a>
                    <br><a href="Personajes/453.html"><h1 align="center">{list_nombres[452]}</h1></a>
                    <br><a href="Personajes/454.html"><h1 align="center">{list_nombres[453]}</h1></a>
                    <br><a href="Personajes/455.html"><h1 align="center">{list_nombres[454]}</h1></a>
                    <br><a href="Personajes/456.html"><h1 align="center">{list_nombres[455]}</h1></a>
                    <br><a href="Personajes/457.html"><h1 align="center">{list_nombres[456]}</h1></a>
                    <br><a href="Personajes/458.html"><h1 align="center">{list_nombres[457]}</h1></a>
                    <br><a href="Personajes/459.html"><h1 align="center">{list_nombres[458]}</h1></a>
                    <br><a href="Personajes/460.html"><h1 align="center">{list_nombres[459]}</h1></a>
                    <br><a href="Personajes/461.html"><h1 align="center">{list_nombres[460]}</h1></a>
                    <br><a href="Personajes/462.html"><h1 align="center">{list_nombres[461]}</h1></a>
                    <br><a href="Personajes/463.html"><h1 align="center">{list_nombres[462]}</h1></a>
                    <br><a href="Personajes/464.html"><h1 align="center">{list_nombres[463]}</h1></a>
                    <br><a href="Personajes/465.html"><h1 align="center">{list_nombres[464]}</h1></a>
                    <br><a href="Personajes/466.html"><h1 align="center">{list_nombres[465]}</h1></a>
                    <br><a href="Personajes/467.html"><h1 align="center">{list_nombres[466]}</h1></a>
                    <br><a href="Personajes/468.html"><h1 align="center">{list_nombres[467]}</h1></a>
                    <br><a href="Personajes/469.html"><h1 align="center">{list_nombres[468]}</h1></a>
                    <br><a href="Personajes/470.html"><h1 align="center">{list_nombres[469]}</h1></a>
                    <br><a href="Personajes/471.html"><h1 align="center">{list_nombres[470]}</h1></a>
                    <br><a href="Personajes/472.html"><h1 align="center">{list_nombres[471]}</h1></a>
                    <br><a href="Personajes/473.html"><h1 align="center">{list_nombres[472]}</h1></a>
                    <br><a href="Personajes/474.html"><h1 align="center">{list_nombres[473]}</h1></a>
                    <br><a href="Personajes/475.html"><h1 align="center">{list_nombres[474]}</h1></a>
                    <br><a href="Personajes/476.html"><h1 align="center">{list_nombres[475]}</h1></a>
                    <br><a href="Personajes/477.html"><h1 align="center">{list_nombres[476]}</h1></a>
                    <br><a href="Personajes/478.html"><h1 align="center">{list_nombres[477]}</h1></a>
                    <br><a href="Personajes/479.html"><h1 align="center">{list_nombres[478]}</h1></a>
                    <br><a href="Personajes/480.html"><h1 align="center">{list_nombres[479]}</h1></a>
                    <br><a href="Personajes/481.html"><h1 align="center">{list_nombres[480]}</h1></a>
                    <br><a href="Personajes/482.html"><h1 align="center">{list_nombres[481]}</h1></a>
                    <br><a href="Personajes/483.html"><h1 align="center">{list_nombres[482]}</h1></a>
                    <br><a href="Personajes/484.html"><h1 align="center">{list_nombres[483]}</h1></a>
                    <br><a href="Personajes/485.html"><h1 align="center">{list_nombres[484]}</h1></a>
                    <br><a href="Personajes/486.html"><h1 align="center">{list_nombres[485]}</h1></a>
                    <br><a href="Personajes/487.html"><h1 align="center">{list_nombres[486]}</h1></a>
                    <br><a href="Personajes/488.html"><h1 align="center">{list_nombres[487]}</h1></a>
                    <br><a href="Personajes/489.html"><h1 align="center">{list_nombres[488]}</h1></a>
                    <br><a href="Personajes/490.html"><h1 align="center">{list_nombres[489]}</h1></a>
                    <br><a href="Personajes/491.html"><h1 align="center">{list_nombres[490]}</h1></a>
                    <br><a href="Personajes/492.html"><h1 align="center">{list_nombres[491]}</h1></a>
                    <br><a href="Personajes/493.html"><h1 align="center">{list_nombres[492]}</h1></a>
                </body>
            </html>
            '''
    f = open("characters-index.html", "w")
    f.write(string_html)
    f.close()


def crear_indexLocation():
    query = get_location()
    list_locaciones = []
    for i in query:
        list_locaciones.append(i.name)

    string_html = f'''<!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <meta http-equiv="X-UA-Compatible" content="ie=edge">
                        <title>Locaciones</title>
                        <div align="center"><img src="Rick_and_Morty_logo.png"></div>
                    </head>
                    <body>
                        <br><a href="Locaciones/1.html"><h1 align="center">{list_locaciones[0]}</h1></a>
                        <br><a href="Locaciones/2.html"><h1 align="center">{list_locaciones[1]}</h1></a>
                        <br><a href="Locaciones/3.html"><h1 align="center">{list_locaciones[2]}</h1></a>
                        <br><a href="Locaciones/4.html"><h1 align="center">{list_locaciones[3]}</h1></a>
                        <br><a href="Locaciones/5.html"><h1 align="center">{list_locaciones[4]}</h1></a>
                        <br><a href="Locaciones/6.html"><h1 align="center">{list_locaciones[5]}</h1></a>
                        <br><a href="Locaciones/7.html"><h1 align="center">{list_locaciones[6]}</h1></a>
                        <br><a href="Locaciones/8.html"><h1 align="center">{list_locaciones[7]}</h1></a>
                        <br><a href="Locaciones/9.html"><h1 align="center">{list_locaciones[8]}</h1></a>
                        <br><a href="Locaciones/10.html"><h1 align="center">{list_locaciones[9]}</h1></a>
                        <br><a href="Locaciones/11.html"><h1 align="center">{list_locaciones[10]}</h1></a>
                        <br><a href="Locaciones/12.html"><h1 align="center">{list_locaciones[11]}</h1></a>
                        <br><a href="Locaciones/13.html"><h1 align="center">{list_locaciones[12]}</h1></a>
                        <br><a href="Locaciones/14.html"><h1 align="center">{list_locaciones[13]}</h1></a>
                        <br><a href="Locaciones/15.html"><h1 align="center">{list_locaciones[14]}</h1></a>
                        <br><a href="Locaciones/16.html"><h1 align="center">{list_locaciones[15]}</h1></a>
                        <br><a href="Locaciones/17.html"><h1 align="center">{list_locaciones[16]}</h1></a>
                        <br><a href="Locaciones/18.html"><h1 align="center">{list_locaciones[17]}</h1></a>
                        <br><a href="Locaciones/19.html"><h1 align="center">{list_locaciones[18]}</h1></a>
                        <br><a href="Locaciones/20.html"><h1 align="center">{list_locaciones[19]}</h1></a>
                        <br><a href="Locaciones/21.html"><h1 align="center">{list_locaciones[20]}</h1></a>
                        <br><a href="Locaciones/22.html"><h1 align="center">{list_locaciones[21]}</h1></a>
                        <br><a href="Locaciones/23.html"><h1 align="center">{list_locaciones[22]}</h1></a>
                        <br><a href="Locaciones/24.html"><h1 align="center">{list_locaciones[23]}</h1></a>
                        <br><a href="Locaciones/25.html"><h1 align="center">{list_locaciones[24]}</h1></a>
                        <br><a href="Locaciones/26.html"><h1 align="center">{list_locaciones[25]}</h1></a>
                        <br><a href="Locaciones/27.html"><h1 align="center">{list_locaciones[26]}</h1></a>
                        <br><a href="Locaciones/28.html"><h1 align="center">{list_locaciones[27]}</h1></a>
                        <br><a href="Locaciones/29.html"><h1 align="center">{list_locaciones[28]}</h1></a>
                        <br><a href="Locaciones/30.html"><h1 align="center">{list_locaciones[29]}</h1></a>
                        <br><a href="Locaciones/31.html"><h1 align="center">{list_locaciones[30]}</h1></a>
                        <br><a href="Locaciones/32.html"><h1 align="center">{list_locaciones[31]}</h1></a>
                        <br><a href="Locaciones/33.html"><h1 align="center">{list_locaciones[32]}</h1></a>
                        <br><a href="Locaciones/34.html"><h1 align="center">{list_locaciones[33]}</h1></a>
                        <br><a href="Locaciones/35.html"><h1 align="center">{list_locaciones[34]}</h1></a>
                        <br><a href="Locaciones/36.html"><h1 align="center">{list_locaciones[35]}</h1></a>
                        <br><a href="Locaciones/37.html"><h1 align="center">{list_locaciones[36]}</h1></a>
                        <br><a href="Locaciones/38.html"><h1 align="center">{list_locaciones[37]}</h1></a>
                        <br><a href="Locaciones/39.html"><h1 align="center">{list_locaciones[38]}</h1></a>
                        <br><a href="Locaciones/40.html"><h1 align="center">{list_locaciones[39]}</h1></a>
                        <br><a href="Locaciones/41.html"><h1 align="center">{list_locaciones[40]}</h1></a>
                        <br><a href="Locaciones/42.html"><h1 align="center">{list_locaciones[41]}</h1></a>
                        <br><a href="Locaciones/43.html"><h1 align="center">{list_locaciones[42]}</h1></a>
                        <br><a href="Locaciones/44.html"><h1 align="center">{list_locaciones[43]}</h1></a>
                        <br><a href="Locaciones/45.html"><h1 align="center">{list_locaciones[44]}</h1></a>
                        <br><a href="Locaciones/46.html"><h1 align="center">{list_locaciones[45]}</h1></a>
                        <br><a href="Locaciones/47.html"><h1 align="center">{list_locaciones[46]}</h1></a>
                        <br><a href="Locaciones/48.html"><h1 align="center">{list_locaciones[47]}</h1></a>
                        <br><a href="Locaciones/49.html"><h1 align="center">{list_locaciones[48]}</h1></a>
                        <br><a href="Locaciones/50.html"><h1 align="center">{list_locaciones[49]}</h1></a>
                        <br><a href="Locaciones/51.html"><h1 align="center">{list_locaciones[50]}</h1></a>
                        <br><a href="Locaciones/52.html"><h1 align="center">{list_locaciones[51]}</h1></a>
                        <br><a href="Locaciones/53.html"><h1 align="center">{list_locaciones[52]}</h1></a>
                        <br><a href="Locaciones/54.html"><h1 align="center">{list_locaciones[53]}</h1></a>
                        <br><a href="Locaciones/55.html"><h1 align="center">{list_locaciones[54]}</h1></a>
                        <br><a href="Locaciones/56.html"><h1 align="center">{list_locaciones[55]}</h1></a>
                        <br><a href="Locaciones/57.html"><h1 align="center">{list_locaciones[56]}</h1></a>
                        <br><a href="Locaciones/58.html"><h1 align="center">{list_locaciones[57]}</h1></a>
                        <br><a href="Locaciones/59.html"><h1 align="center">{list_locaciones[58]}</h1></a>
                        <br><a href="Locaciones/60.html"><h1 align="center">{list_locaciones[59]}</h1></a>
                        <br><a href="Locaciones/61.html"><h1 align="center">{list_locaciones[60]}</h1></a>
                        <br><a href="Locaciones/62.html"><h1 align="center">{list_locaciones[61]}</h1></a>
                        <br><a href="Locaciones/63.html"><h1 align="center">{list_locaciones[62]}</h1></a>
                        <br><a href="Locaciones/64.html"><h1 align="center">{list_locaciones[63]}</h1></a>
                        <br><a href="Locaciones/65.html"><h1 align="center">{list_locaciones[64]}</h1></a>
                        <br><a href="Locaciones/66.html"><h1 align="center">{list_locaciones[65]}</h1></a>
                        <br><a href="Locaciones/67.html"><h1 align="center">{list_locaciones[66]}</h1></a>
                        <br><a href="Locaciones/68.html"><h1 align="center">{list_locaciones[67]}</h1></a>
                        <br><a href="Locaciones/69.html"><h1 align="center">{list_locaciones[68]}</h1></a>
                        <br><a href="Locaciones/70.html"><h1 align="center">{list_locaciones[69]}</h1></a>
                        <br><a href="Locaciones/71.html"><h1 align="center">{list_locaciones[70]}</h1></a>
                        <br><a href="Locaciones/72.html"><h1 align="center">{list_locaciones[71]}</h1></a>
                        <br><a href="Locaciones/73.html"><h1 align="center">{list_locaciones[72]}</h1></a>
                        <br><a href="Locaciones/74.html"><h1 align="center">{list_locaciones[73]}</h1></a>
                        <br><a href="Locaciones/75.html"><h1 align="center">{list_locaciones[74]}</h1></a>
                        <br><a href="Locaciones/76.html"><h1 align="center">{list_locaciones[75]}</h1></a>
                    </body>
                </html>
                '''
    f = open("locations-index.html", "w")
    f.write(string_html)
    f.close()


def crear_indexEpisode():
    query = get_episode()
    list_episode = []
    for i in query:
        list_episode.append(i.name)

    string_html = f'''<!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <meta http-equiv="X-UA-Compatible" content="ie=edge">
                            <title>Episodios</title>
                            <div align="center"><img src="Rick_and_Morty_logo.png"></div>
                        </head>
                        <body>
                            <br><a href="Episodios/1.html"><h1 align="center">{list_episode[0]}</h1></a>
                            <br><a href="Episodios/2.html"><h1 align="center">{list_episode[1]}</h1></a>
                            <br><a href="Episodios/3.html"><h1 align="center">{list_episode[2]}</h1></a>
                            <br><a href="Episodios/4.html"><h1 align="center">{list_episode[3]}</h1></a>
                            <br><a href="Episodios/5.html"><h1 align="center">{list_episode[4]}</h1></a>
                            <br><a href="Episodios/6.html"><h1 align="center">{list_episode[5]}</h1></a>
                            <br><a href="Episodios/7.html"><h1 align="center">{list_episode[6]}</h1></a>
                            <br><a href="Episodios/8.html"><h1 align="center">{list_episode[7]}</h1></a>
                            <br><a href="Episodios/9.html"><h1 align="center">{list_episode[8]}</h1></a>
                            <br><a href="Episodios/10.html"><h1 align="center">{list_episode[9]}</h1></a>
                            <br><a href="Episodios/11.html"><h1 align="center">{list_episode[10]}</h1></a>
                            <br><a href="Episodios/12.html"><h1 align="center">{list_episode[11]}</h1></a>
                            <br><a href="Episodios/13.html"><h1 align="center">{list_episode[12]}</h1></a>
                            <br><a href="Episodios/14.html"><h1 align="center">{list_episode[13]}</h1></a>
                            <br><a href="Episodios/15.html"><h1 align="center">{list_episode[14]}</h1></a>
                            <br><a href="Episodios/16.html"><h1 align="center">{list_episode[15]}</h1></a>
                            <br><a href="Episodios/17.html"><h1 align="center">{list_episode[16]}</h1></a>
                            <br><a href="Episodios/18.html"><h1 align="center">{list_episode[17]}</h1></a>
                            <br><a href="Episodios/19.html"><h1 align="center">{list_episode[18]}</h1></a>
                            <br><a href="Episodios/20.html"><h1 align="center">{list_episode[19]}</h1></a>
                            <br><a href="Episodios/21.html"><h1 align="center">{list_episode[20]}</h1></a>
                            <br><a href="Episodios/22.html"><h1 align="center">{list_episode[21]}</h1></a>
                            <br><a href="Episodios/23.html"><h1 align="center">{list_episode[22]}</h1></a>
                            <br><a href="Episodios/24.html"><h1 align="center">{list_episode[23]}</h1></a>
                            <br><a href="Episodios/25.html"><h1 align="center">{list_episode[24]}</h1></a>
                            <br><a href="Episodios/26.html"><h1 align="center">{list_episode[25]}</h1></a>
                            <br><a href="Episodios/27.html"><h1 align="center">{list_episode[26]}</h1></a>
                            <br><a href="Episodios/28.html"><h1 align="center">{list_episode[27]}</h1></a>
                            <br><a href="Episodios/29.html"><h1 align="center">{list_episode[28]}</h1></a>
                            <br><a href="Episodios/30.html"><h1 align="center">{list_episode[29]}</h1></a>
                            <br><a href="Episodios/31.html"><h1 align="center">{list_episode[30]}</h1></a>
                        </body>
                    </html>
                    '''
    f = open("episodes-index.html", "w")
    f.write(string_html)
    f.close()


def crear_indexCaractersEspec():
    query = get_character()
    ii = 1
    for i in query:

        string_html = f'''<!DOCTYPE html>
                            <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                    <title>Personaje</title>
                                    <div align="center"><img src="Rick_and_Morty_logo.png"></div>
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
        f = open(f'Personajes/{ii}.html', 'w')
        f.write(string_html)
        f.close()
        ii+=1


def crear_indexLocationEspec():
    query = get_location()
    ii = 1
    for i in query:
        string_html = f'''<!DOCTYPE html>
                                <html lang="en">
                                    <head>
                                        <meta charset="UTF-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                        <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                        <title>Locacion</title>
                                        <div align="center"><img src="Rick_and_Morty_logo.png"></div>
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
        f = open(f'Locaciones/{ii}.html', 'w')
        f.write(string_html)
        f.close()
        ii += 1


def crear_indecEpisodeEspec():
    query = get_episode()
    ii = 1
    for i in query:
        string_html = f'''<!DOCTYPE html>
                                    <html lang="en">
                                        <head>
                                            <meta charset="UTF-8">
                                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                            <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                            <title>Episodio</title>
                                            <div align="center"><img src="Rick_and_Morty_logo.png"></div>
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
        f = open(f'Episodios/{ii}.html', 'w')
        f.write(string_html)
        f.close()
        ii += 1

def main():
    crear_indexPrincipal()
    crear_indexCharacters()
    crear_indexLocation()
    crear_indexEpisode()
    crear_indexCaractersEspec()
    crear_indexLocationEspec()
    crear_indecEpisodeEspec()

if __name__ == '__main__':
    main()
