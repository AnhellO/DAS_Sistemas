import peewee
db = peewee.SqliteDatabase('ram.db') # usamos orm peewee

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

def create_connect():
    db.connect()
    db.create_tables([Character, Location, Episode], safe=True)


def get_character():
    lista = []
    characters = Character.select(Character.name, Character.status, Character.species,
                                   Character.type, Character.gender, Character.image,
                                   Character.url, Character.created)
    for i in characters:
        lista.append(i)
    return lista


def get_location():
    lista = []
    locations = Location.select(Location.name, Location.type,
                                Location.url, Location.created)
    for i in locations:
        lista.append(i)
    return lista


def get_episode():
    lista = []
    episodes = Episode.select(Episode.name, Episode.url, Episode.created)
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
                <title>Rick y Morty API</title>
            </head>
            <body>
                <br><a href="characters-index.html" target="_blank"><h1 align="center">{tablas[0]}</h1></a>
                <br><a href="episodes-index.html" target="_blank"><h1 align="center">{tablas[1]}</h1></a>
                <br><a href="locations-index.html" target="_blank"><h1 align="center">{tablas[2]}</h1></a>           
            </body>
        </html>
        '''
    f = open("index.html", "w")
    f.write(string_html)
    f.close()


def crear_indexCharacters():
    query = get_character()
    list_character = []
    for i in query:
        list_character.append(i.name)

    string_html = f'''<!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>Character</title>
                    <div align="center"><img src="Rick_and_Morty_logo.png"></div>
                </head>
                <body>
                    <br><a href="Character/1.html" target="_blank"><h1 align="center">{list_character[0]}</h1></a>
                    <br><a href="Character/2.html" target="_blank"><h1 align="center">{list_character[1]}</h1></a>
                    <br><a href="Character/3.html" target="_blank"><h1 align="center">{list_character[2]}</h1></a>
                    <br><a href="Character/4.html" target="_blank"><h1 align="center">{list_character[3]}</h1></a>
                    <br><a href="Character/5.html" target="_blank"><h1 align="center">{list_character[4]}</h1></a>
                    <br><a href="Character/6.html" target="_blank"><h1 align="center">{list_character[5]}</h1></a>
                    <br><a href="Character/7.html" target="_blank"><h1 align="center">{list_character[6]}</h1></a>
                    <br><a href="Character/8.html" target="_blank"><h1 align="center">{list_character[7]}</h1></a>
                    <br><a href="Character/9.html" target="_blank"><h1 align="center">{list_character[8]}</h1></a>
                    <br><a href="Character/10.html" target="_blank"><h1 align="center">{list_character[9]}</h1></a>
                    <br><a href="Character/11.html" target="_blank"><h1 align="center">{list_character[10]}</h1></a>
                    <br><a href="Character/12.html" target="_blank"><h1 align="center">{list_character[11]}</h1></a>
                    <br><a href="Character/13.html" target="_blank"><h1 align="center">{list_character[12]}</h1></a>
                    <br><a href="Character/14.html" target="_blank"><h1 align="center">{list_character[13]}</h1></a>
                    <br><a href="Character/15.html" target="_blank"><h1 align="center">{list_character[14]}</h1></a>
                    <br><a href="Character/16.html" target="_blank"><h1 align="center">{list_character[15]}</h1></a>
                    <br><a href="Character/17.html" target="_blank"><h1 align="center">{list_character[16]}</h1></a>
                    <br><a href="Character/18.html" target="_blank"><h1 align="center">{list_character[17]}</h1></a>
                    <br><a href="Character/19.html" target="_blank"><h1 align="center">{list_character[18]}</h1></a>
                    <br><a href="Character/20.html" target="_blank"><h1 align="center">{list_character[19]}</h1></a>
                    <br><a href="Character/21.html" target="_blank"><h1 align="center">{list_character[20]}</h1></a>
                    <br><a href="Character/22.html" target="_blank"><h1 align="center">{list_character[21]}</h1></a>
                    <br><a href="Character/23.html" target="_blank"><h1 align="center">{list_character[22]}</h1></a>
                    <br><a href="Character/24.html" target="_blank"><h1 align="center">{list_character[23]}</h1></a>
                    <br><a href="Character/25.html" target="_blank"><h1 align="center">{list_character[24]}</h1></a>
                    <br><a href="Character/26.html" target="_blank"><h1 align="center">{list_character[25]}</h1></a>
                    <br><a href="Character/27.html" target="_blank"><h1 align="center">{list_character[26]}</h1></a>
                    <br><a href="Character/28.html" target="_blank"><h1 align="center">{list_character[27]}</h1></a>
                    <br><a href="Character/29.html" target="_blank"><h1 align="center">{list_character[28]}</h1></a>
                    <br><a href="Character/30.html" target="_blank"><h1 align="center">{list_character[29]}</h1></a>
                    <br><a href="Character/31.html" target="_blank"><h1 align="center">{list_character[30]}</h1></a>
                    <br><a href="Character/32.html" target="_blank"><h1 align="center">{list_character[31]}</h1></a>
                    <br><a href="Character/33.html" target="_blank"><h1 align="center">{list_character[32]}</h1></a>
                    <br><a href="Character/34.html" target="_blank"><h1 align="center">{list_character[33]}</h1></a>
                    <br><a href="Character/35.html" target="_blank"><h1 align="center">{list_character[34]}</h1></a>
                    <br><a href="Character/36.html" target="_blank"><h1 align="center">{list_character[35]}</h1></a>
                    <br><a href="Character/37.html" target="_blank"><h1 align="center">{list_character[36]}</h1></a>
                    <br><a href="Character/38.html" target="_blank"><h1 align="center">{list_character[37]}</h1></a>
                    <br><a href="Character/39.html" target="_blank"><h1 align="center">{list_character[38]}</h1></a>
                    <br><a href="Character/40.html" target="_blank"><h1 align="center">{list_character[39]}</h1></a>
                    <br><a href="Character/41.html" target="_blank"><h1 align="center">{list_character[40]}</h1></a>
                    <br><a href="Character/42.html" target="_blank"><h1 align="center">{list_character[41]}</h1></a>
                    <br><a href="Character/43.html" target="_blank"><h1 align="center">{list_character[42]}</h1></a>
                    <br><a href="Character/44.html" target="_blank"><h1 align="center">{list_character[43]}</h1></a>
                    <br><a href="Character/45.html" target="_blank"><h1 align="center">{list_character[44]}</h1></a>
                    <br><a href="Character/46.html" target="_blank"><h1 align="center">{list_character[45]}</h1></a>
                    <br><a href="Character/47.html" target="_blank"><h1 align="center">{list_character[46]}</h1></a>
                    <br><a href="Character/48.html" target="_blank"><h1 align="center">{list_character[47]}</h1></a>
                    <br><a href="Character/49.html" target="_blank"><h1 align="center">{list_character[48]}</h1></a>
                    <br><a href="Character/50.html" target="_blank"><h1 align="center">{list_character[49]}</h1></a>
                    <br><a href="Character/51.html" target="_blank"><h1 align="center">{list_character[50]}</h1></a>
                    <br><a href="Character/52.html" target="_blank"><h1 align="center">{list_character[51]}</h1></a>
                    <br><a href="Character/53.html" target="_blank"><h1 align="center">{list_character[52]}</h1></a>
                    <br><a href="Character/54.html" target="_blank"><h1 align="center">{list_character[53]}</h1></a>
                    <br><a href="Character/55.html" target="_blank"><h1 align="center">{list_character[54]}</h1></a>
                    <br><a href="Character/56.html" target="_blank"><h1 align="center">{list_character[55]}</h1></a>
                    <br><a href="Character/57.html" target="_blank"><h1 align="center">{list_character[56]}</h1></a>
                    <br><a href="Character/58.html" target="_blank"><h1 align="center">{list_character[57]}</h1></a>
                    <br><a href="Character/59.html" target="_blank"><h1 align="center">{list_character[58]}</h1></a>
                    <br><a href="Character/60.html" target="_blank"><h1 align="center">{list_character[59]}</h1></a>
                    <br><a href="Character/61.html" target="_blank"><h1 align="center">{list_character[60]}</h1></a>
                    <br><a href="Character/62.html" target="_blank"><h1 align="center">{list_character[61]}</h1></a>
                    <br><a href="Character/63.html" target="_blank"><h1 align="center">{list_character[62]}</h1></a>
                    <br><a href="Character/64.html" target="_blank"><h1 align="center">{list_character[63]}</h1></a>
                    <br><a href="Character/65.html" target="_blank"><h1 align="center">{list_character[64]}</h1></a>
                    <br><a href="Character/66.html" target="_blank"><h1 align="center">{list_character[65]}</h1></a>
                    <br><a href="Character/67.html" target="_blank"><h1 align="center">{list_character[66]}</h1></a>
                    <br><a href="Character/68.html" target="_blank"><h1 align="center">{list_character[67]}</h1></a>
                    <br><a href="Character/69.html" target="_blank"><h1 align="center">{list_character[68]}</h1></a>
                    <br><a href="Character/70.html" target="_blank"><h1 align="center">{list_character[69]}</h1></a>
                    <br><a href="Character/71.html" target="_blank"><h1 align="center">{list_character[70]}</h1></a>
                    <br><a href="Character/72.html" target="_blank"><h1 align="center">{list_character[71]}</h1></a>
                    <br><a href="Character/73.html" target="_blank"><h1 align="center">{list_character[72]}</h1></a>
                    <br><a href="Character/74.html" target="_blank"><h1 align="center">{list_character[73]}</h1></a>
                    <br><a href="Character/75.html" target="_blank"><h1 align="center">{list_character[74]}</h1></a>
                    <br><a href="Character/76.html" target="_blank"><h1 align="center">{list_character[75]}</h1></a>
                    <br><a href="Character/77.html" target="_blank"><h1 align="center">{list_character[76]}</h1></a>
                    <br><a href="Character/78.html" target="_blank"><h1 align="center">{list_character[77]}</h1></a>
                    <br><a href="Character/79.html" target="_blank"><h1 align="center">{list_character[78]}</h1></a>
                    <br><a href="Character/80.html" target="_blank"><h1 align="center">{list_character[79]}</h1></a>
                    <br><a href="Character/81.html" target="_blank"><h1 align="center">{list_character[80]}</h1></a>
                    <br><a href="Character/82.html" target="_blank"><h1 align="center">{list_character[81]}</h1></a>
                    <br><a href="Character/83.html" target="_blank"><h1 align="center">{list_character[82]}</h1></a>
                    <br><a href="Character/84.html" target="_blank"><h1 align="center">{list_character[83]}</h1></a>
                    <br><a href="Character/85.html" target="_blank"><h1 align="center">{list_character[84]}</h1></a>
                    <br><a href="Character/86.html" target="_blank"><h1 align="center">{list_character[85]}</h1></a>
                    <br><a href="Character/87.html" target="_blank"><h1 align="center">{list_character[86]}</h1></a>
                    <br><a href="Character/88.html" target="_blank"><h1 align="center">{list_character[87]}</h1></a>
                    <br><a href="Character/89.html" target="_blank"><h1 align="center">{list_character[88]}</h1></a>
                    <br><a href="Character/90.html" target="_blank"><h1 align="center">{list_character[89]}</h1></a>
                    <br><a href="Character/91.html" target="_blank"><h1 align="center">{list_character[90]}</h1></a>
                    <br><a href="Character/92.html" target="_blank"><h1 align="center">{list_character[91]}</h1></a>
                    <br><a href="Character/93.html" target="_blank"><h1 align="center">{list_character[92]}</h1></a>
                    <br><a href="Character/94.html" target="_blank"><h1 align="center">{list_character[93]}</h1></a>
                    <br><a href="Character/95.html" target="_blank"><h1 align="center">{list_character[94]}</h1></a>
                    <br><a href="Character/96.html" target="_blank"><h1 align="center">{list_character[95]}</h1></a>
                    <br><a href="Character/97.html" target="_blank"><h1 align="center">{list_character[96]}</h1></a>
                    <br><a href="Character/98.html" target="_blank"><h1 align="center">{list_character[97]}</h1></a>
                    <br><a href="Character/99.html" target="_blank"><h1 align="center">{list_character[98]}</h1></a>
                    <br><a href="Character/100.html" target="_blank"><h1 align="center">{list_character[99]}</h1></a>
                    <br><a href="Character/101.html" target="_blank"><h1 align="center">{list_character[100]}</h1></a>
                    <br><a href="Character/102.html" target="_blank"><h1 align="center">{list_character[101]}</h1></a>
                    <br><a href="Character/103.html" target="_blank"><h1 align="center">{list_character[102]}</h1></a>
                    <br><a href="Character/104.html" target="_blank"><h1 align="center">{list_character[103]}</h1></a>
                    <br><a href="Character/105.html" target="_blank"><h1 align="center">{list_character[104]}</h1></a>
                    <br><a href="Character/106.html" target="_blank"><h1 align="center">{list_character[105]}</h1></a>
                    <br><a href="Character/107.html" target="_blank"><h1 align="center">{list_character[106]}</h1></a>
                    <br><a href="Character/108.html" target="_blank"><h1 align="center">{list_character[107]}</h1></a>
                    <br><a href="Character/109.html" target="_blank"><h1 align="center">{list_character[108]}</h1></a>
                    <br><a href="Character/110.html" target="_blank"><h1 align="center">{list_character[109]}</h1></a>
                    <br><a href="Character/111.html" target="_blank"><h1 align="center">{list_character[110]}</h1></a>
                    <br><a href="Character/112.html" target="_blank"><h1 align="center">{list_character[111]}</h1></a>
                    <br><a href="Character/113.html" target="_blank"><h1 align="center">{list_character[112]}</h1></a>
                    <br><a href="Character/114.html" target="_blank"><h1 align="center">{list_character[113]}</h1></a>
                    <br><a href="Character/115.html" target="_blank"><h1 align="center">{list_character[114]}</h1></a>
                    <br><a href="Character/116.html" target="_blank"><h1 align="center">{list_character[115]}</h1></a>
                    <br><a href="Character/117.html" target="_blank"><h1 align="center">{list_character[116]}</h1></a>
                    <br><a href="Character/118.html" target="_blank"><h1 align="center">{list_character[117]}</h1></a>
                    <br><a href="Character/119.html" target="_blank"><h1 align="center">{list_character[118]}</h1></a>
                    <br><a href="Character/120.html" target="_blank"><h1 align="center">{list_character[119]}</h1></a>
                    <br><a href="Character/121.html" target="_blank"><h1 align="center">{list_character[120]}</h1></a>
                    <br><a href="Character/122.html" target="_blank"><h1 align="center">{list_character[121]}</h1></a>
                    <br><a href="Character/123.html" target="_blank"><h1 align="center">{list_character[122]}</h1></a>
                    <br><a href="Character/124.html" target="_blank"><h1 align="center">{list_character[123]}</h1></a>
                    <br><a href="Character/125.html" target="_blank"><h1 align="center">{list_character[124]}</h1></a>
                    <br><a href="Character/126.html" target="_blank"><h1 align="center">{list_character[125]}</h1></a>
                    <br><a href="Character/127.html" target="_blank"><h1 align="center">{list_character[126]}</h1></a>
                    <br><a href="Character/128.html" target="_blank"><h1 align="center">{list_character[127]}</h1></a>
                    <br><a href="Character/129.html" target="_blank"><h1 align="center">{list_character[128]}</h1></a>
                    <br><a href="Character/130.html" target="_blank"><h1 align="center">{list_character[129]}</h1></a>
                    <br><a href="Character/131.html" target="_blank"><h1 align="center">{list_character[130]}</h1></a>
                    <br><a href="Character/132.html" target="_blank"><h1 align="center">{list_character[131]}</h1></a>
                    <br><a href="Character/133.html" target="_blank"><h1 align="center">{list_character[132]}</h1></a>
                    <br><a href="Character/134.html" target="_blank"><h1 align="center">{list_character[133]}</h1></a>
                    <br><a href="Character/135.html" target="_blank"><h1 align="center">{list_character[134]}</h1></a>
                    <br><a href="Character/136.html" target="_blank"><h1 align="center">{list_character[135]}</h1></a>
                    <br><a href="Character/137.html" target="_blank"><h1 align="center">{list_character[136]}</h1></a>
                    <br><a href="Character/138.html" target="_blank"><h1 align="center">{list_character[137]}</h1></a>
                    <br><a href="Character/139.html" target="_blank"><h1 align="center">{list_character[138]}</h1></a>
                    <br><a href="Character/140.html" target="_blank"><h1 align="center">{list_character[139]}</h1></a>
                    <br><a href="Character/141.html" target="_blank"><h1 align="center">{list_character[140]}</h1></a>
                    <br><a href="Character/142.html" target="_blank"><h1 align="center">{list_character[141]}</h1></a>
                    <br><a href="Character/143.html" target="_blank"><h1 align="center">{list_character[142]}</h1></a>
                    <br><a href="Character/144.html" target="_blank"><h1 align="center">{list_character[143]}</h1></a>
                    <br><a href="Character/145.html" target="_blank"><h1 align="center">{list_character[144]}</h1></a>
                    <br><a href="Character/146.html" target="_blank"><h1 align="center">{list_character[145]}</h1></a>
                    <br><a href="Character/147.html" target="_blank"><h1 align="center">{list_character[146]}</h1></a>
                    <br><a href="Character/148.html" target="_blank"><h1 align="center">{list_character[147]}</h1></a>
                    <br><a href="Character/149.html" target="_blank"><h1 align="center">{list_character[148]}</h1></a>
                    <br><a href="Character/150.html" target="_blank"><h1 align="center">{list_character[149]}</h1></a>
                    <br><a href="Character/151.html" target="_blank"><h1 align="center">{list_character[150]}</h1></a>
                    <br><a href="Character/152.html" target="_blank"><h1 align="center">{list_character[151]}</h1></a>
                    <br><a href="Character/153.html" target="_blank"><h1 align="center">{list_character[152]}</h1></a>
                    <br><a href="Character/154.html" target="_blank"><h1 align="center">{list_character[153]}</h1></a>
                    <br><a href="Character/155.html" target="_blank"><h1 align="center">{list_character[154]}</h1></a>
                    <br><a href="Character/156.html" target="_blank"><h1 align="center">{list_character[155]}</h1></a>
                    <br><a href="Character/157.html" target="_blank"><h1 align="center">{list_character[156]}</h1></a>
                    <br><a href="Character/158.html" target="_blank"><h1 align="center">{list_character[157]}</h1></a>
                    <br><a href="Character/159.html" target="_blank"><h1 align="center">{list_character[158]}</h1></a>
                    <br><a href="Character/160.html" target="_blank"><h1 align="center">{list_character[159]}</h1></a>
                    <br><a href="Character/161.html" target="_blank"><h1 align="center">{list_character[160]}</h1></a>
                    <br><a href="Character/162.html" target="_blank"><h1 align="center">{list_character[161]}</h1></a>
                    <br><a href="Character/163.html" target="_blank"><h1 align="center">{list_character[162]}</h1></a>
                    <br><a href="Character/164.html" target="_blank"><h1 align="center">{list_character[163]}</h1></a>
                    <br><a href="Character/165.html" target="_blank"><h1 align="center">{list_character[164]}</h1></a>
                    <br><a href="Character/166.html" target="_blank"><h1 align="center">{list_character[165]}</h1></a>
                    <br><a href="Character/167.html" target="_blank"><h1 align="center">{list_character[166]}</h1></a>
                    <br><a href="Character/168.html" target="_blank"><h1 align="center">{list_character[167]}</h1></a>
                    <br><a href="Character/169.html" target="_blank"><h1 align="center">{list_character[168]}</h1></a>
                    <br><a href="Character/170.html" target="_blank"><h1 align="center">{list_character[169]}</h1></a>
                    <br><a href="Character/171.html" target="_blank"><h1 align="center">{list_character[170]}</h1></a>
                    <br><a href="Character/172.html" target="_blank"><h1 align="center">{list_character[171]}</h1></a>
                    <br><a href="Character/173.html" target="_blank"><h1 align="center">{list_character[172]}</h1></a>
                    <br><a href="Character/174.html" target="_blank"><h1 align="center">{list_character[173]}</h1></a>
                    <br><a href="Character/175.html" target="_blank"><h1 align="center">{list_character[174]}</h1></a>
                    <br><a href="Character/176.html" target="_blank"><h1 align="center">{list_character[175]}</h1></a>
                    <br><a href="Character/177.html" target="_blank"><h1 align="center">{list_character[176]}</h1></a>
                    <br><a href="Character/178.html" target="_blank"><h1 align="center">{list_character[177]}</h1></a>
                    <br><a href="Character/179.html" target="_blank"><h1 align="center">{list_character[178]}</h1></a>
                    <br><a href="Character/180.html" target="_blank"><h1 align="center">{list_character[179]}</h1></a>
                    <br><a href="Character/181.html" target="_blank"><h1 align="center">{list_character[180]}</h1></a>
                    <br><a href="Character/182.html" target="_blank"><h1 align="center">{list_character[181]}</h1></a>
                    <br><a href="Character/183.html" target="_blank"><h1 align="center">{list_character[182]}</h1></a>
                    <br><a href="Character/184.html" target="_blank"><h1 align="center">{list_character[183]}</h1></a>
                    <br><a href="Character/185.html" target="_blank"><h1 align="center">{list_character[184]}</h1></a>
                    <br><a href="Character/186.html" target="_blank"><h1 align="center">{list_character[185]}</h1></a>
                    <br><a href="Character/187.html" target="_blank"><h1 align="center">{list_character[186]}</h1></a>
                    <br><a href="Character/188.html" target="_blank"><h1 align="center">{list_character[187]}</h1></a>
                    <br><a href="Character/189.html" target="_blank"><h1 align="center">{list_character[188]}</h1></a>
                    <br><a href="Character/190.html" target="_blank"><h1 align="center">{list_character[189]}</h1></a>
                    <br><a href="Character/191.html" target="_blank"><h1 align="center">{list_character[190]}</h1></a>
                    <br><a href="Character/192.html" target="_blank"><h1 align="center">{list_character[191]}</h1></a>
                    <br><a href="Character/193.html" target="_blank"><h1 align="center">{list_character[192]}</h1></a>
                    <br><a href="Character/194.html" target="_blank"><h1 align="center">{list_character[193]}</h1></a>
                    <br><a href="Character/195.html" target="_blank"><h1 align="center">{list_character[194]}</h1></a>
                    <br><a href="Character/196.html" target="_blank"><h1 align="center">{list_character[195]}</h1></a>
                    <br><a href="Character/197.html" target="_blank"><h1 align="center">{list_character[196]}</h1></a>
                    <br><a href="Character/198.html" target="_blank"><h1 align="center">{list_character[197]}</h1></a>
                    <br><a href="Character/199.html" target="_blank"><h1 align="center">{list_character[198]}</h1></a>
                    <br><a href="Character/200.html" target="_blank"><h1 align="center">{list_character[199]}</h1></a>
                    <br><a href="Character/201.html" target="_blank"><h1 align="center">{list_character[200]}</h1></a>
                    <br><a href="Character/202.html" target="_blank"><h1 align="center">{list_character[201]}</h1></a>
                    <br><a href="Character/203.html" target="_blank"><h1 align="center">{list_character[202]}</h1></a>
                    <br><a href="Character/204.html" target="_blank"><h1 align="center">{list_character[203]}</h1></a>
                    <br><a href="Character/205.html" target="_blank"><h1 align="center">{list_character[204]}</h1></a>
                    <br><a href="Character/206.html" target="_blank"><h1 align="center">{list_character[205]}</h1></a>
                    <br><a href="Character/207.html" target="_blank"><h1 align="center">{list_character[206]}</h1></a>
                    <br><a href="Character/208.html" target="_blank"><h1 align="center">{list_character[207]}</h1></a>
                    <br><a href="Character/209.html" target="_blank"><h1 align="center">{list_character[208]}</h1></a>
                    <br><a href="Character/210.html" target="_blank"><h1 align="center">{list_character[209]}</h1></a>
                    <br><a href="Character/211.html" target="_blank"><h1 align="center">{list_character[210]}</h1></a>
                    <br><a href="Character/212.html" target="_blank"><h1 align="center">{list_character[211]}</h1></a>
                    <br><a href="Character/213.html" target="_blank"><h1 align="center">{list_character[212]}</h1></a>
                    <br><a href="Character/214.html" target="_blank"><h1 align="center">{list_character[213]}</h1></a>
                    <br><a href="Character/215.html" target="_blank"><h1 align="center">{list_character[214]}</h1></a>
                    <br><a href="Character/216.html" target="_blank"><h1 align="center">{list_character[215]}</h1></a>
                    <br><a href="Character/217.html" target="_blank"><h1 align="center">{list_character[216]}</h1></a>
                    <br><a href="Character/218.html" target="_blank"><h1 align="center">{list_character[217]}</h1></a>
                    <br><a href="Character/219.html" target="_blank"><h1 align="center">{list_character[218]}</h1></a>
                    <br><a href="Character/220.html" target="_blank"><h1 align="center">{list_character[219]}</h1></a>
                    <br><a href="Character/221.html" target="_blank"><h1 align="center">{list_character[220]}</h1></a>
                    <br><a href="Character/222.html" target="_blank"><h1 align="center">{list_character[221]}</h1></a>
                    <br><a href="Character/223.html" target="_blank"><h1 align="center">{list_character[222]}</h1></a>
                    <br><a href="Character/224.html" target="_blank"><h1 align="center">{list_character[223]}</h1></a>
                    <br><a href="Character/225.html" target="_blank"><h1 align="center">{list_character[224]}</h1></a>
                    <br><a href="Character/226.html" target="_blank"><h1 align="center">{list_character[225]}</h1></a>
                    <br><a href="Character/227.html" target="_blank"><h1 align="center">{list_character[226]}</h1></a>
                    <br><a href="Character/228.html" target="_blank"><h1 align="center">{list_character[227]}</h1></a>
                    <br><a href="Character/229.html" target="_blank"><h1 align="center">{list_character[228]}</h1></a>
                    <br><a href="Character/230.html" target="_blank"><h1 align="center">{list_character[229]}</h1></a>
                    <br><a href="Character/231.html" target="_blank"><h1 align="center">{list_character[230]}</h1></a>
                    <br><a href="Character/232.html" target="_blank"><h1 align="center">{list_character[231]}</h1></a>
                    <br><a href="Character/233.html" target="_blank"><h1 align="center">{list_character[232]}</h1></a>
                    <br><a href="Character/234.html" target="_blank"><h1 align="center">{list_character[233]}</h1></a>
                    <br><a href="Character/235.html" target="_blank"><h1 align="center">{list_character[234]}</h1></a>
                    <br><a href="Character/236.html" target="_blank"><h1 align="center">{list_character[235]}</h1></a>
                    <br><a href="Character/237.html" target="_blank"><h1 align="center">{list_character[236]}</h1></a>
                    <br><a href="Character/238.html" target="_blank"><h1 align="center">{list_character[237]}</h1></a>
                    <br><a href="Character/239.html" target="_blank"><h1 align="center">{list_character[238]}</h1></a>
                    <br><a href="Character/240.html" target="_blank"><h1 align="center">{list_character[239]}</h1></a>
                    <br><a href="Character/241.html" target="_blank"><h1 align="center">{list_character[240]}</h1></a>
                    <br><a href="Character/242.html" target="_blank"><h1 align="center">{list_character[241]}</h1></a>
                    <br><a href="Character/243.html" target="_blank"><h1 align="center">{list_character[242]}</h1></a>
                    <br><a href="Character/244.html" target="_blank"><h1 align="center">{list_character[243]}</h1></a>
                    <br><a href="Character/245.html" target="_blank"><h1 align="center">{list_character[244]}</h1></a>
                    <br><a href="Character/246.html" target="_blank"><h1 align="center">{list_character[245]}</h1></a>
                    <br><a href="Character/247.html" target="_blank"><h1 align="center">{list_character[246]}</h1></a>
                    <br><a href="Character/248.html" target="_blank"><h1 align="center">{list_character[247]}</h1></a>
                    <br><a href="Character/249.html" target="_blank"><h1 align="center">{list_character[248]}</h1></a>
                    <br><a href="Character/250.html" target="_blank"><h1 align="center">{list_character[249]}</h1></a>
                    <br><a href="Character/251.html" target="_blank"><h1 align="center">{list_character[250]}</h1></a>
                    <br><a href="Character/252.html" target="_blank"><h1 align="center">{list_character[251]}</h1></a>
                    <br><a href="Character/253.html" target="_blank"><h1 align="center">{list_character[252]}</h1></a>
                    <br><a href="Character/254.html" target="_blank"><h1 align="center">{list_character[253]}</h1></a>
                    <br><a href="Character/255.html" target="_blank"><h1 align="center">{list_character[254]}</h1></a>
                    <br><a href="Character/256.html" target="_blank"><h1 align="center">{list_character[255]}</h1></a>
                    <br><a href="Character/257.html" target="_blank"><h1 align="center">{list_character[256]}</h1></a>
                    <br><a href="Character/258.html" target="_blank"><h1 align="center">{list_character[257]}</h1></a>
                    <br><a href="Character/259.html" target="_blank"><h1 align="center">{list_character[258]}</h1></a>
                    <br><a href="Character/260.html" target="_blank"><h1 align="center">{list_character[259]}</h1></a>
                    <br><a href="Character/261.html" target="_blank"><h1 align="center">{list_character[260]}</h1></a>
                    <br><a href="Character/262.html" target="_blank"><h1 align="center">{list_character[261]}</h1></a>
                    <br><a href="Character/263.html" target="_blank"><h1 align="center">{list_character[262]}</h1></a>
                    <br><a href="Character/264.html" target="_blank"><h1 align="center">{list_character[263]}</h1></a>
                    <br><a href="Character/265.html" target="_blank"><h1 align="center">{list_character[264]}</h1></a>
                    <br><a href="Character/266.html" target="_blank"><h1 align="center">{list_character[265]}</h1></a>
                    <br><a href="Character/267.html" target="_blank"><h1 align="center">{list_character[266]}</h1></a>
                    <br><a href="Character/268.html" target="_blank"><h1 align="center">{list_character[267]}</h1></a>
                    <br><a href="Character/269.html" target="_blank"><h1 align="center">{list_character[268]}</h1></a>
                    <br><a href="Character/270.html" target="_blank"><h1 align="center">{list_character[269]}</h1></a>
                    <br><a href="Character/271.html" target="_blank"><h1 align="center">{list_character[270]}</h1></a>
                    <br><a href="Character/272.html" target="_blank"><h1 align="center">{list_character[271]}</h1></a>
                    <br><a href="Character/273.html" target="_blank"><h1 align="center">{list_character[272]}</h1></a>
                    <br><a href="Character/274.html" target="_blank"><h1 align="center">{list_character[273]}</h1></a>
                    <br><a href="Character/275.html" target="_blank"><h1 align="center">{list_character[274]}</h1></a>
                    <br><a href="Character/276.html" target="_blank"><h1 align="center">{list_character[275]}</h1></a>
                    <br><a href="Character/277.html" target="_blank"><h1 align="center">{list_character[276]}</h1></a>
                    <br><a href="Character/278.html" target="_blank"><h1 align="center">{list_character[277]}</h1></a>
                    <br><a href="Character/279.html" target="_blank"><h1 align="center">{list_character[278]}</h1></a>
                    <br><a href="Character/280.html" target="_blank"><h1 align="center">{list_character[279]}</h1></a>
                    <br><a href="Character/281.html" target="_blank"><h1 align="center">{list_character[280]}</h1></a>
                    <br><a href="Character/282.html" target="_blank"><h1 align="center">{list_character[281]}</h1></a>
                    <br><a href="Character/283.html" target="_blank"><h1 align="center">{list_character[282]}</h1></a>
                    <br><a href="Character/284.html" target="_blank"><h1 align="center">{list_character[283]}</h1></a>
                    <br><a href="Character/285.html" target="_blank"><h1 align="center">{list_character[284]}</h1></a>
                    <br><a href="Character/286.html" target="_blank"><h1 align="center">{list_character[285]}</h1></a>
                    <br><a href="Character/287.html" target="_blank"><h1 align="center">{list_character[286]}</h1></a>
                    <br><a href="Character/288.html" target="_blank"><h1 align="center">{list_character[287]}</h1></a>
                    <br><a href="Character/289.html" target="_blank"><h1 align="center">{list_character[288]}</h1></a>
                    <br><a href="Character/290.html" target="_blank"><h1 align="center">{list_character[289]}</h1></a>
                    <br><a href="Character/291.html" target="_blank"><h1 align="center">{list_character[290]}</h1></a>
                    <br><a href="Character/292.html" target="_blank"><h1 align="center">{list_character[291]}</h1></a>
                    <br><a href="Character/293.html" target="_blank"><h1 align="center">{list_character[292]}</h1></a>
                    <br><a href="Character/294.html" target="_blank"><h1 align="center">{list_character[293]}</h1></a>
                    <br><a href="Character/295.html" target="_blank"><h1 align="center">{list_character[294]}</h1></a>
                    <br><a href="Character/296.html" target="_blank"><h1 align="center">{list_character[295]}</h1></a>
                    <br><a href="Character/297.html" target="_blank"><h1 align="center">{list_character[296]}</h1></a>
                    <br><a href="Character/298.html" target="_blank"><h1 align="center">{list_character[297]}</h1></a>
                    <br><a href="Character/299.html" target="_blank"><h1 align="center">{list_character[298]}</h1></a>
                    <br><a href="Character/300.html" target="_blank"><h1 align="center">{list_character[299]}</h1></a>
                    <br><a href="Character/301.html" target="_blank"><h1 align="center">{list_character[300]}</h1></a>
                    <br><a href="Character/302.html" target="_blank"><h1 align="center">{list_character[301]}</h1></a>
                    <br><a href="Character/303.html" target="_blank"><h1 align="center">{list_character[302]}</h1></a>
                    <br><a href="Character/304.html" target="_blank"><h1 align="center">{list_character[303]}</h1></a>
                    <br><a href="Character/305.html" target="_blank"><h1 align="center">{list_character[304]}</h1></a>
                    <br><a href="Character/306.html" target="_blank"><h1 align="center">{list_character[305]}</h1></a>
                    <br><a href="Character/307.html" target="_blank"><h1 align="center">{list_character[306]}</h1></a>
                    <br><a href="Character/308.html" target="_blank"><h1 align="center">{list_character[307]}</h1></a>
                    <br><a href="Character/309.html" target="_blank"><h1 align="center">{list_character[308]}</h1></a>
                    <br><a href="Character/310.html" target="_blank"><h1 align="center">{list_character[309]}</h1></a>
                    <br><a href="Character/311.html" target="_blank"><h1 align="center">{list_character[310]}</h1></a>
                    <br><a href="Character/312.html" target="_blank"><h1 align="center">{list_character[311]}</h1></a>
                    <br><a href="Character/313.html" target="_blank"><h1 align="center">{list_character[312]}</h1></a>
                    <br><a href="Character/314.html" target="_blank"><h1 align="center">{list_character[313]}</h1></a>
                    <br><a href="Character/315.html" target="_blank"><h1 align="center">{list_character[314]}</h1></a>
                    <br><a href="Character/316.html" target="_blank"><h1 align="center">{list_character[315]}</h1></a>
                    <br><a href="Character/317.html" target="_blank"><h1 align="center">{list_character[316]}</h1></a>
                    <br><a href="Character/318.html" target="_blank"><h1 align="center">{list_character[317]}</h1></a>
                    <br><a href="Character/319.html" target="_blank"><h1 align="center">{list_character[318]}</h1></a>
                    <br><a href="Character/320.html" target="_blank"><h1 align="center">{list_character[319]}</h1></a>
                    <br><a href="Character/321.html" target="_blank"><h1 align="center">{list_character[320]}</h1></a>
                    <br><a href="Character/322.html" target="_blank"><h1 align="center">{list_character[321]}</h1></a>
                    <br><a href="Character/323.html" target="_blank"><h1 align="center">{list_character[322]}</h1></a>
                    <br><a href="Character/324.html" target="_blank"><h1 align="center">{list_character[323]}</h1></a>
                    <br><a href="Character/325.html" target="_blank"><h1 align="center">{list_character[324]}</h1></a>
                    <br><a href="Character/326.html" target="_blank"><h1 align="center">{list_character[325]}</h1></a>
                    <br><a href="Character/327.html" target="_blank"><h1 align="center">{list_character[326]}</h1></a>
                    <br><a href="Character/328.html" target="_blank"><h1 align="center">{list_character[327]}</h1></a>
                    <br><a href="Character/329.html" target="_blank"><h1 align="center">{list_character[328]}</h1></a>
                    <br><a href="Character/330.html" target="_blank"><h1 align="center">{list_character[329]}</h1></a>
                    <br><a href="Character/331.html" target="_blank"><h1 align="center">{list_character[330]}</h1></a>
                    <br><a href="Character/332.html" target="_blank"><h1 align="center">{list_character[331]}</h1></a>
                    <br><a href="Character/333.html" target="_blank"><h1 align="center">{list_character[332]}</h1></a>
                    <br><a href="Character/334.html" target="_blank"><h1 align="center">{list_character[333]}</h1></a>
                    <br><a href="Character/335.html" target="_blank"><h1 align="center">{list_character[334]}</h1></a>
                    <br><a href="Character/336.html" target="_blank"><h1 align="center">{list_character[335]}</h1></a>
                    <br><a href="Character/337.html" target="_blank"><h1 align="center">{list_character[336]}</h1></a>
                    <br><a href="Character/338.html" target="_blank"><h1 align="center">{list_character[337]}</h1></a>
                    <br><a href="Character/339.html" target="_blank"><h1 align="center">{list_character[338]}</h1></a>
                    <br><a href="Character/340.html" target="_blank"><h1 align="center">{list_character[339]}</h1></a>
                    <br><a href="Character/341.html" target="_blank"><h1 align="center">{list_character[340]}</h1></a>
                    <br><a href="Character/342.html" target="_blank"><h1 align="center">{list_character[341]}</h1></a>
                    <br><a href="Character/343.html" target="_blank"><h1 align="center">{list_character[342]}</h1></a>
                    <br><a href="Character/344.html" target="_blank"><h1 align="center">{list_character[343]}</h1></a>
                    <br><a href="Character/345.html" target="_blank"><h1 align="center">{list_character[344]}</h1></a>
                    <br><a href="Character/346.html" target="_blank"><h1 align="center">{list_character[345]}</h1></a>
                    <br><a href="Character/347.html" target="_blank"><h1 align="center">{list_character[346]}</h1></a>
                    <br><a href="Character/348.html" target="_blank"><h1 align="center">{list_character[347]}</h1></a>
                    <br><a href="Character/349.html" target="_blank"><h1 align="center">{list_character[348]}</h1></a>
                    <br><a href="Character/350.html" target="_blank"><h1 align="center">{list_character[349]}</h1></a>
                    <br><a href="Character/351.html" target="_blank"><h1 align="center">{list_character[350]}</h1></a>
                    <br><a href="Character/352.html" target="_blank"><h1 align="center">{list_character[351]}</h1></a>
                    <br><a href="Character/353.html" target="_blank"><h1 align="center">{list_character[352]}</h1></a>
                    <br><a href="Character/354.html" target="_blank"><h1 align="center">{list_character[353]}</h1></a>
                    <br><a href="Character/355.html" target="_blank"><h1 align="center">{list_character[354]}</h1></a>
                    <br><a href="Character/356.html" target="_blank"><h1 align="center">{list_character[355]}</h1></a>
                    <br><a href="Character/357.html" target="_blank"><h1 align="center">{list_character[356]}</h1></a>
                    <br><a href="Character/358.html" target="_blank"><h1 align="center">{list_character[357]}</h1></a>
                    <br><a href="Character/359.html" target="_blank"><h1 align="center">{list_character[358]}</h1></a>
                    <br><a href="Character/360.html" target="_blank"><h1 align="center">{list_character[359]}</h1></a>
                    <br><a href="Character/361.html" target="_blank"><h1 align="center">{list_character[360]}</h1></a>
                    <br><a href="Character/362.html" target="_blank"><h1 align="center">{list_character[361]}</h1></a>
                    <br><a href="Character/363.html" target="_blank"><h1 align="center">{list_character[362]}</h1></a>
                    <br><a href="Character/364.html" target="_blank"><h1 align="center">{list_character[363]}</h1></a>
                    <br><a href="Character/365.html" target="_blank"><h1 align="center">{list_character[364]}</h1></a>
                    <br><a href="Character/366.html" target="_blank"><h1 align="center">{list_character[365]}</h1></a>
                    <br><a href="Character/367.html" target="_blank"><h1 align="center">{list_character[366]}</h1></a>
                    <br><a href="Character/368.html" target="_blank"><h1 align="center">{list_character[367]}</h1></a>
                    <br><a href="Character/369.html" target="_blank"><h1 align="center">{list_character[368]}</h1></a>
                    <br><a href="Character/370.html" target="_blank"><h1 align="center">{list_character[369]}</h1></a>
                    <br><a href="Character/371.html" target="_blank"><h1 align="center">{list_character[370]}</h1></a>
                    <br><a href="Character/372.html" target="_blank"><h1 align="center">{list_character[371]}</h1></a>
                    <br><a href="Character/373.html" target="_blank"><h1 align="center">{list_character[372]}</h1></a>
                    <br><a href="Character/374.html" target="_blank"><h1 align="center">{list_character[373]}</h1></a>
                    <br><a href="Character/375.html" target="_blank"><h1 align="center">{list_character[374]}</h1></a>
                    <br><a href="Character/376.html" target="_blank"><h1 align="center">{list_character[375]}</h1></a>
                    <br><a href="Character/377.html" target="_blank"><h1 align="center">{list_character[376]}</h1></a>
                    <br><a href="Character/378.html" target="_blank"><h1 align="center">{list_character[377]}</h1></a>
                    <br><a href="Character/379.html" target="_blank"><h1 align="center">{list_character[378]}</h1></a>
                    <br><a href="Character/380.html" target="_blank"><h1 align="center">{list_character[379]}</h1></a>
                    <br><a href="Character/381.html" target="_blank"><h1 align="center">{list_character[380]}</h1></a>
                    <br><a href="Character/382.html" target="_blank"><h1 align="center">{list_character[381]}</h1></a>
                    <br><a href="Character/383.html" target="_blank"><h1 align="center">{list_character[382]}</h1></a>
                    <br><a href="Character/384.html" target="_blank"><h1 align="center">{list_character[383]}</h1></a>
                    <br><a href="Character/385.html" target="_blank"><h1 align="center">{list_character[384]}</h1></a>
                    <br><a href="Character/386.html" target="_blank"><h1 align="center">{list_character[385]}</h1></a>
                    <br><a href="Character/387.html" target="_blank"><h1 align="center">{list_character[386]}</h1></a>
                    <br><a href="Character/388.html" target="_blank"><h1 align="center">{list_character[387]}</h1></a>
                    <br><a href="Character/389.html" target="_blank"><h1 align="center">{list_character[388]}</h1></a>
                    <br><a href="Character/390.html" target="_blank"><h1 align="center">{list_character[389]}</h1></a>
                    <br><a href="Character/391.html" target="_blank"><h1 align="center">{list_character[390]}</h1></a>
                    <br><a href="Character/392.html" target="_blank"><h1 align="center">{list_character[391]}</h1></a>
                    <br><a href="Character/393.html" target="_blank"><h1 align="center">{list_character[392]}</h1></a>
                    <br><a href="Character/394.html" target="_blank"><h1 align="center">{list_character[393]}</h1></a>
                    <br><a href="Character/395.html" target="_blank"><h1 align="center">{list_character[394]}</h1></a>
                    <br><a href="Character/396.html" target="_blank"><h1 align="center">{list_character[395]}</h1></a>
                    <br><a href="Character/397.html" target="_blank"><h1 align="center">{list_character[396]}</h1></a>
                    <br><a href="Character/398.html" target="_blank"><h1 align="center">{list_character[397]}</h1></a>
                    <br><a href="Character/399.html" target="_blank"><h1 align="center">{list_character[398]}</h1></a>
                    <br><a href="Character/400.html" target="_blank"><h1 align="center">{list_character[399]}</h1></a>
                    <br><a href="Character/401.html" target="_blank"><h1 align="center">{list_character[400]}</h1></a>
                    <br><a href="Character/402.html" target="_blank"><h1 align="center">{list_character[401]}</h1></a>
                    <br><a href="Character/403.html" target="_blank"><h1 align="center">{list_character[402]}</h1></a>
                    <br><a href="Character/404.html" target="_blank"><h1 align="center">{list_character[403]}</h1></a>
                    <br><a href="Character/405.html" target="_blank"><h1 align="center">{list_character[404]}</h1></a>
                    <br><a href="Character/406.html" target="_blank"><h1 align="center">{list_character[405]}</h1></a>
                    <br><a href="Character/407.html" target="_blank"><h1 align="center">{list_character[406]}</h1></a>
                    <br><a href="Character/408.html" target="_blank"><h1 align="center">{list_character[407]}</h1></a>
                    <br><a href="Character/409.html" target="_blank"><h1 align="center">{list_character[408]}</h1></a>
                    <br><a href="Character/410.html" target="_blank"><h1 align="center">{list_character[409]}</h1></a>
                    <br><a href="Character/411.html" target="_blank"><h1 align="center">{list_character[410]}</h1></a>
                    <br><a href="Character/412.html" target="_blank"><h1 align="center">{list_character[411]}</h1></a>
                    <br><a href="Character/413.html" target="_blank"><h1 align="center">{list_character[412]}</h1></a>
                    <br><a href="Character/414.html" target="_blank"><h1 align="center">{list_character[413]}</h1></a>
                    <br><a href="Character/415.html" target="_blank"><h1 align="center">{list_character[414]}</h1></a>
                    <br><a href="Character/416.html" target="_blank"><h1 align="center">{list_character[415]}</h1></a>
                    <br><a href="Character/417.html" target="_blank"><h1 align="center">{list_character[416]}</h1></a>
                    <br><a href="Character/418.html" target="_blank"><h1 align="center">{list_character[417]}</h1></a>
                    <br><a href="Character/419.html" target="_blank"><h1 align="center">{list_character[418]}</h1></a>
                    <br><a href="Character/420.html" target="_blank"><h1 align="center">{list_character[419]}</h1></a>
                    <br><a href="Character/421.html" target="_blank"><h1 align="center">{list_character[420]}</h1></a>
                    <br><a href="Character/422.html" target="_blank"><h1 align="center">{list_character[421]}</h1></a>
                    <br><a href="Character/423.html" target="_blank"><h1 align="center">{list_character[422]}</h1></a>
                    <br><a href="Character/424.html" target="_blank"><h1 align="center">{list_character[423]}</h1></a>
                    <br><a href="Character/425.html" target="_blank"><h1 align="center">{list_character[424]}</h1></a>
                    <br><a href="Character/426.html" target="_blank"><h1 align="center">{list_character[425]}</h1></a>
                    <br><a href="Character/427.html" target="_blank"><h1 align="center">{list_character[426]}</h1></a>
                    <br><a href="Character/428.html" target="_blank"><h1 align="center">{list_character[427]}</h1></a>
                    <br><a href="Character/429.html" target="_blank"><h1 align="center">{list_character[428]}</h1></a>
                    <br><a href="Character/430.html" target="_blank"><h1 align="center">{list_character[429]}</h1></a>
                    <br><a href="Character/431.html" target="_blank"><h1 align="center">{list_character[430]}</h1></a>
                    <br><a href="Character/432.html" target="_blank"><h1 align="center">{list_character[431]}</h1></a>
                    <br><a href="Character/433.html" target="_blank"><h1 align="center">{list_character[432]}</h1></a>
                    <br><a href="Character/434.html" target="_blank"><h1 align="center">{list_character[433]}</h1></a>
                    <br><a href="Character/435.html" target="_blank"><h1 align="center">{list_character[434]}</h1></a>
                    <br><a href="Character/436.html" target="_blank"><h1 align="center">{list_character[435]}</h1></a>
                    <br><a href="Character/437.html" target="_blank"><h1 align="center">{list_character[436]}</h1></a>
                    <br><a href="Character/438.html" target="_blank"><h1 align="center">{list_character[437]}</h1></a>
                    <br><a href="Character/439.html" target="_blank"><h1 align="center">{list_character[438]}</h1></a>
                    <br><a href="Character/440.html" target="_blank"><h1 align="center">{list_character[439]}</h1></a>
                    <br><a href="Character/441.html" target="_blank"><h1 align="center">{list_character[440]}</h1></a>
                    <br><a href="Character/442.html" target="_blank"><h1 align="center">{list_character[441]}</h1></a>
                    <br><a href="Character/443.html" target="_blank"><h1 align="center">{list_character[442]}</h1></a>
                    <br><a href="Character/444.html" target="_blank"><h1 align="center">{list_character[443]}</h1></a>
                    <br><a href="Character/445.html" target="_blank"><h1 align="center">{list_character[444]}</h1></a>
                    <br><a href="Character/446.html" target="_blank"><h1 align="center">{list_character[445]}</h1></a>
                    <br><a href="Character/447.html" target="_blank"><h1 align="center">{list_character[446]}</h1></a>
                    <br><a href="Character/448.html" target="_blank"><h1 align="center">{list_character[447]}</h1></a>
                    <br><a href="Character/449.html" target="_blank"><h1 align="center">{list_character[448]}</h1></a>
                    <br><a href="Character/450.html" target="_blank"><h1 align="center">{list_character[449]}</h1></a>
                    <br><a href="Character/451.html" target="_blank"><h1 align="center">{list_character[450]}</h1></a>
                    <br><a href="Character/452.html" target="_blank"><h1 align="center">{list_character[451]}</h1></a>
                    <br><a href="Character/453.html" target="_blank"><h1 align="center">{list_character[452]}</h1></a>
                    <br><a href="Character/454.html" target="_blank"><h1 align="center">{list_character[453]}</h1></a>
                    <br><a href="Character/455.html" target="_blank"><h1 align="center">{list_character[454]}</h1></a>
                    <br><a href="Character/456.html" target="_blank"><h1 align="center">{list_character[455]}</h1></a>
                    <br><a href="Character/457.html" target="_blank"><h1 align="center">{list_character[456]}</h1></a>
                    <br><a href="Character/458.html" target="_blank"><h1 align="center">{list_character[457]}</h1></a>
                    <br><a href="Character/459.html" target="_blank"><h1 align="center">{list_character[458]}</h1></a>
                    <br><a href="Character/460.html" target="_blank"><h1 align="center">{list_character[459]}</h1></a>
                    <br><a href="Character/461.html" target="_blank"><h1 align="center">{list_character[460]}</h1></a>
                    <br><a href="Character/462.html" target="_blank"><h1 align="center">{list_character[461]}</h1></a>
                    <br><a href="Character/463.html" target="_blank"><h1 align="center">{list_character[462]}</h1></a>
                    <br><a href="Character/464.html" target="_blank"><h1 align="center">{list_character[463]}</h1></a>
                    <br><a href="Character/465.html" target="_blank"><h1 align="center">{list_character[464]}</h1></a>
                    <br><a href="Character/466.html" target="_blank"><h1 align="center">{list_character[465]}</h1></a>
                    <br><a href="Character/467.html" target="_blank"><h1 align="center">{list_character[466]}</h1></a>
                    <br><a href="Character/468.html" target="_blank"><h1 align="center">{list_character[467]}</h1></a>
                    <br><a href="Character/469.html" target="_blank"><h1 align="center">{list_character[468]}</h1></a>
                    <br><a href="Character/470.html" target="_blank"><h1 align="center">{list_character[469]}</h1></a>
                    <br><a href="Character/471.html" target="_blank"><h1 align="center">{list_character[470]}</h1></a>
                    <br><a href="Character/472.html" target="_blank"><h1 align="center">{list_character[471]}</h1></a>
                    <br><a href="Character/473.html" target="_blank"><h1 align="center">{list_character[472]}</h1></a>
                    <br><a href="Character/474.html" target="_blank"><h1 align="center">{list_character[473]}</h1></a>
                    <br><a href="Character/475.html" target="_blank"><h1 align="center">{list_character[474]}</h1></a>
                    <br><a href="Character/476.html" target="_blank"><h1 align="center">{list_character[475]}</h1></a>
                    <br><a href="Character/477.html" target="_blank"><h1 align="center">{list_character[476]}</h1></a>
                    <br><a href="Character/478.html" target="_blank"><h1 align="center">{list_character[477]}</h1></a>
                    <br><a href="Character/479.html" target="_blank"><h1 align="center">{list_character[478]}</h1></a>
                    <br><a href="Character/480.html" target="_blank"><h1 align="center">{list_character[479]}</h1></a>
                    <br><a href="Character/481.html" target="_blank"><h1 align="center">{list_character[480]}</h1></a>
                    <br><a href="Character/482.html" target="_blank"><h1 align="center">{list_character[481]}</h1></a>
                    <br><a href="Character/483.html" target="_blank"><h1 align="center">{list_character[482]}</h1></a>
                    <br><a href="Character/484.html" target="_blank"><h1 align="center">{list_character[483]}</h1></a>
                    <br><a href="Character/485.html" target="_blank"><h1 align="center">{list_character[484]}</h1></a>
                    <br><a href="Character/486.html" target="_blank"><h1 align="center">{list_character[485]}</h1></a>
                    <br><a href="Character/487.html" target="_blank"><h1 align="center">{list_character[486]}</h1></a>
                    <br><a href="Character/488.html" target="_blank"><h1 align="center">{list_character[487]}</h1></a>
                    <br><a href="Character/489.html" target="_blank"><h1 align="center">{list_character[488]}</h1></a>
                    <br><a href="Character/490.html" target="_blank"><h1 align="center">{list_character[489]}</h1></a>
                    <br><a href="Character/491.html" target="_blank"><h1 align="center">{list_character[490]}</h1></a>
                    <br><a href="Character/492.html" target="_blank"><h1 align="center">{list_character[491]}</h1></a>
                    <br><a href="Character/493.html" target="_blank"><h1 align="center">{list_character[492]}</h1></a>
                </body>
            </html>
            '''
    f = open("characters-index.html", "w")
    f.write(string_html)
    f.close()


def crear_indexLocation():
    query = get_location()
    list_Location = []
    for i in query:
        list_Location.append(i.name)

    string_html = f'''<!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <meta http-equiv="X-UA-Compatible" content="ie=edge">
                        <title>Locations</title>
                    </head>
                    <body>
                        <br><a href="Location/1.html" target="_blank"><h1 align="center">{list_Location[0]}</h1></a>
                        <br><a href="Location/2.html" target="_blank"><h1 align="center">{list_Location[1]}</h1></a>
                        <br><a href="Location/3.html" target="_blank"><h1 align="center">{list_Location[2]}</h1></a>
                        <br><a href="Location/4.html" target="_blank"><h1 align="center">{list_Location[3]}</h1></a>
                        <br><a href="Location/5.html" target="_blank"><h1 align="center">{list_Location[4]}</h1></a>
                        <br><a href="Location/6.html" target="_blank"><h1 align="center">{list_Location[5]}</h1></a>
                        <br><a href="Location/7.html" target="_blank"><h1 align="center">{list_Location[6]}</h1></a>
                        <br><a href="Location/8.html" target="_blank"><h1 align="center">{list_Location[7]}</h1></a>
                        <br><a href="Location/9.html" target="_blank"><h1 align="center">{list_Location[8]}</h1></a>
                        <br><a href="Location/10.html" target="_blank"><h1 align="center">{list_Location[9]}</h1></a>
                        <br><a href="Location/11.html" target="_blank"><h1 align="center">{list_Location[10]}</h1></a>
                        <br><a href="Location/12.html" target="_blank"><h1 align="center">{list_Location[11]}</h1></a>
                        <br><a href="Location/13.html" target="_blank"><h1 align="center">{list_Location[12]}</h1></a>
                        <br><a href="Location/14.html" target="_blank"><h1 align="center">{list_Location[13]}</h1></a>
                        <br><a href="Location/15.html" target="_blank"><h1 align="center">{list_Location[14]}</h1></a>
                        <br><a href="Location/16.html" target="_blank"><h1 align="center">{list_Location[15]}</h1></a>
                        <br><a href="Location/17.html" target="_blank"><h1 align="center">{list_Location[16]}</h1></a>
                        <br><a href="Location/18.html" target="_blank"><h1 align="center">{list_Location[17]}</h1></a>
                        <br><a href="Location/19.html" target="_blank"><h1 align="center">{list_Location[18]}</h1></a>
                        <br><a href="Location/20.html" target="_blank"><h1 align="center">{list_Location[19]}</h1></a>
                        <br><a href="Location/21.html" target="_blank"><h1 align="center">{list_Location[20]}</h1></a>
                        <br><a href="Location/22.html" target="_blank"><h1 align="center">{list_Location[21]}</h1></a>
                        <br><a href="Location/23.html" target="_blank"><h1 align="center">{list_Location[22]}</h1></a>
                        <br><a href="Location/24.html" target="_blank"><h1 align="center">{list_Location[23]}</h1></a>
                        <br><a href="Location/25.html" target="_blank"><h1 align="center">{list_Location[24]}</h1></a>
                        <br><a href="Location/26.html" target="_blank"><h1 align="center">{list_Location[25]}</h1></a>
                        <br><a href="Location/27.html" target="_blank"><h1 align="center">{list_Location[26]}</h1></a>
                        <br><a href="Location/28.html" target="_blank"><h1 align="center">{list_Location[27]}</h1></a>
                        <br><a href="Location/29.html" target="_blank"><h1 align="center">{list_Location[28]}</h1></a>
                        <br><a href="Location/30.html" target="_blank"><h1 align="center">{list_Location[29]}</h1></a>
                        <br><a href="Location/31.html" target="_blank"><h1 align="center">{list_Location[30]}</h1></a>
                        <br><a href="Location/32.html" target="_blank"><h1 align="center">{list_Location[31]}</h1></a>
                        <br><a href="Location/33.html" target="_blank"><h1 align="center">{list_Location[32]}</h1></a>
                        <br><a href="Location/34.html" target="_blank"><h1 align="center">{list_Location[33]}</h1></a>
                        <br><a href="Location/35.html" target="_blank"><h1 align="center">{list_Location[34]}</h1></a>
                        <br><a href="Location/36.html" target="_blank"><h1 align="center">{list_Location[35]}</h1></a>
                        <br><a href="Location/37.html" target="_blank"><h1 align="center">{list_Location[36]}</h1></a>
                        <br><a href="Location/38.html" target="_blank"><h1 align="center">{list_Location[37]}</h1></a>
                        <br><a href="Location/39.html" target="_blank"><h1 align="center">{list_Location[38]}</h1></a>
                        <br><a href="Location/40.html" target="_blank"><h1 align="center">{list_Location[39]}</h1></a>
                        <br><a href="Location/41.html" target="_blank"><h1 align="center">{list_Location[40]}</h1></a>
                        <br><a href="Location/42.html" target="_blank"><h1 align="center">{list_Location[41]}</h1></a>
                        <br><a href="Location/43.html" target="_blank"><h1 align="center">{list_Location[42]}</h1></a>
                        <br><a href="Location/44.html" target="_blank"><h1 align="center">{list_Location[43]}</h1></a>
                        <br><a href="Location/45.html" target="_blank"><h1 align="center">{list_Location[44]}</h1></a>
                        <br><a href="Location/46.html" target="_blank"><h1 align="center">{list_Location[45]}</h1></a>
                        <br><a href="Location/47.html" target="_blank"><h1 align="center">{list_Location[46]}</h1></a>
                        <br><a href="Location/48.html" target="_blank"><h1 align="center">{list_Location[47]}</h1></a>
                        <br><a href="Location/49.html" target="_blank"><h1 align="center">{list_Location[48]}</h1></a>
                        <br><a href="Location/50.html" target="_blank"><h1 align="center">{list_Location[49]}</h1></a>
                        <br><a href="Location/51.html" target="_blank"><h1 align="center">{list_Location[50]}</h1></a>
                        <br><a href="Location/52.html" target="_blank"><h1 align="center">{list_Location[51]}</h1></a>
                        <br><a href="Location/53.html" target="_blank"><h1 align="center">{list_Location[52]}</h1></a>
                        <br><a href="Location/54.html" target="_blank"><h1 align="center">{list_Location[53]}</h1></a>
                        <br><a href="Location/55.html" target="_blank"><h1 align="center">{list_Location[54]}</h1></a>
                        <br><a href="Location/56.html" target="_blank"><h1 align="center">{list_Location[55]}</h1></a>
                        <br><a href="Location/57.html" target="_blank"><h1 align="center">{list_Location[56]}</h1></a>
                        <br><a href="Location/58.html" target="_blank"><h1 align="center">{list_Location[57]}</h1></a>
                        <br><a href="Location/59.html" target="_blank"><h1 align="center">{list_Location[58]}</h1></a>
                        <br><a href="Location/60.html" target="_blank"><h1 align="center">{list_Location[59]}</h1></a>
                        <br><a href="Location/61.html" target="_blank"><h1 align="center">{list_Location[60]}</h1></a>
                        <br><a href="Location/62.html" target="_blank"><h1 align="center">{list_Location[61]}</h1></a>
                        <br><a href="Location/63.html" target="_blank"><h1 align="center">{list_Location[62]}</h1></a>
                        <br><a href="Location/64.html" target="_blank"><h1 align="center">{list_Location[63]}</h1></a>
                        <br><a href="Location/65.html" target="_blank"><h1 align="center">{list_Location[64]}</h1></a>
                        <br><a href="Location/66.html" target="_blank"><h1 align="center">{list_Location[65]}</h1></a>
                        <br><a href="Location/67.html" target="_blank"><h1 align="center">{list_Location[66]}</h1></a>
                        <br><a href="Location/68.html" target="_blank"><h1 align="center">{list_Location[67]}</h1></a>
                        <br><a href="Location/69.html" target="_blank"><h1 align="center">{list_Location[68]}</h1></a>
                        <br><a href="Location/70.html" target="_blank"><h1 align="center">{list_Location[69]}</h1></a>
                        <br><a href="Location/71.html" target="_blank"><h1 align="center">{list_Location[70]}</h1></a>
                        <br><a href="Location/72.html" target="_blank"><h1 align="center">{list_Location[71]}</h1></a>
                        <br><a href="Location/73.html" target="_blank"><h1 align="center">{list_Location[72]}</h1></a>
                        <br><a href="Location/74.html" target="_blank"><h1 align="center">{list_Location[73]}</h1></a>
                        <br><a href="Location/75.html" target="_blank"><h1 align="center">{list_Location[74]}</h1></a>
                        <br><a href="Location/76.html" target="_blank"><h1 align="center">{list_Location[75]}</h1></a>
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
                            <title>Episodes</title>
                        </head>
                        <body>
                            <br><a href="Episode/1.html" target="_blank"><h1 align="center">{list_episode[0]}</h1></a>
                            <br><a href="Episode/2.html" target="_blank"><h1 align="center">{list_episode[1]}</h1></a>
                            <br><a href="Episode/3.html" target="_blank"><h1 align="center">{list_episode[2]}</h1></a>
                            <br><a href="Episode/4.html" target="_blank"><h1 align="center">{list_episode[3]}</h1></a>
                            <br><a href="Episode/5.html" target="_blank"><h1 align="center">{list_episode[4]}</h1></a>
                            <br><a href="Episode/6.html" target="_blank"><h1 align="center">{list_episode[5]}</h1></a>
                            <br><a href="Episode/7.html" target="_blank"><h1 align="center">{list_episode[6]}</h1></a>
                            <br><a href="Episode/8.html" target="_blank"><h1 align="center">{list_episode[7]}</h1></a>
                            <br><a href="Episode/9.html" target="_blank"><h1 align="center">{list_episode[8]}</h1></a>
                            <br><a href="Episode/10.html" target="_blank"><h1 align="center">{list_episode[9]}</h1></a>
                            <br><a href="Episode/11.html" target="_blank"><h1 align="center">{list_episode[10]}</h1></a>
                            <br><a href="Episode/12.html" target="_blank"><h1 align="center">{list_episode[11]}</h1></a>
                            <br><a href="Episode/13.html" target="_blank"><h1 align="center">{list_episode[12]}</h1></a>
                            <br><a href="Episode/14.html" target="_blank"><h1 align="center">{list_episode[13]}</h1></a>
                            <br><a href="Episode/15.html" target="_blank"><h1 align="center">{list_episode[14]}</h1></a>
                            <br><a href="Episode/16.html" target="_blank"><h1 align="center">{list_episode[15]}</h1></a>
                            <br><a href="Episode/17.html" target="_blank"><h1 align="center">{list_episode[16]}</h1></a>
                            <br><a href="Episode/18.html" target="_blank"><h1 align="center">{list_episode[17]}</h1></a>
                            <br><a href="Episode/19.html" target="_blank"><h1 align="center">{list_episode[18]}</h1></a>
                            <br><a href="Episode/20.html" target="_blank"><h1 align="center">{list_episode[19]}</h1></a>
                            <br><a href="Episode/21.html" target="_blank"><h1 align="center">{list_episode[20]}</h1></a>
                            <br><a href="Episode/22.html" target="_blank"><h1 align="center">{list_episode[21]}</h1></a>
                            <br><a href="Episode/23.html" target="_blank"><h1 align="center">{list_episode[22]}</h1></a>
                            <br><a href="Episode/24.html" target="_blank"><h1 align="center">{list_episode[23]}</h1></a>
                            <br><a href="Episode/25.html" target="_blank"><h1 align="center">{list_episode[24]}</h1></a>
                            <br><a href="Episode/26.html" target="_blank"><h1 align="center">{list_episode[25]}</h1></a>
                            <br><a href="Episode/27.html" target="_blank"><h1 align="center">{list_episode[26]}</h1></a>
                            <br><a href="Episode/28.html" target="_blank"><h1 align="center">{list_episode[27]}</h1></a>
                            <br><a href="Episode/29.html" target="_blank"><h1 align="center">{list_episode[28]}</h1></a>
                            <br><a href="Episode/30.html" target="_blank"><h1 align="center">{list_episode[29]}</h1></a>
                            <br><a href="Episode/31.html" target="_blank"><h1 align="center">{list_episode[30]}</h1></a>
                        </body>
                    </html>
                    '''
    f = open("episodes-index.html", "w")
    f.write(string_html)
    f.close()


def crear_indexCharacterEspecifico():
    query = get_character()
    ii = 1
    for i in query:

        string_html = f'''<!DOCTYPE html>
                            <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                    <title>Character</title>
                                    <div><h1 align="left">Menu</h1></div>
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
        f = open(f'Character/{ii}.html', 'w')
        f.write(string_html)
        f.close()
        ii+=1


def crear_indexLocationEspecifica():
    query = get_location()
    ii = 1
    for i in query:
        string_html = f'''<!DOCTYPE html>
                                <html lang="en">
                                    <head>
                                        <meta charset="UTF-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                        <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                        <title>Location</title>
                                        <div><h1 align="left">Menu</h1></div>
                                    </head>
                                    <body>
                                        <br><h1 align="center">Name -> {i.name}</h1></a>
                                        <br><h1 align="center">Type -> {i.type}</h1></a>
                                        <br><h1 align="center">Url -> {i.url}</h1></a>
                                        <br><h1 align="center">Created -> {i.created}</h1></a>
                                    </body>
                                </html>
            '''
        f = open(f'Character/{ii}.html', 'w')
        f.write(string_html)
        f.close()
        ii += 1


def crear_indexEpisodeEspececifico():
    query = get_episode()
    ii = 1
    for i in query:
        string_html = f'''<!DOCTYPE html>
                                    <html lang="en">
                                        <head>
                                            <meta charset="UTF-8">
                                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                            <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                            <title>Episode</title>
                                            <div><h1 align="left">Menu</h1></div>
                                        </head>
                                        <body>
                                            <br><h1 align="center">Name -> {i.name}</h1></a>
                                            <br><h1 align="center">Url -> {i.url}</h1></a>
                                            <br><h1 align="center">Created -> {i.created}</h1></a>
                                        </body>
                                    </html>
                '''
        f = open(f'Episode/{ii}.html', 'w')
        f.write(string_html)
        f.close()
        ii += 1

def main():
    crear_indexPrincipal()
    crear_indexCharacters()
    crear_indexLocation()
    crear_indexEpisode()
    crear_indexCharacterEspecifico()
    crear_indexLocationEspecifica()
    crear_indexEpisodeEspececifico()

if __name__ == '__main__':
    main()
