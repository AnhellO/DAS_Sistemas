import time, re, requests, os, errno, json, sqlite3

directorio = 'archivitos-de-html'
url = 'https://api.punkapi.com/v2/beers'

for i in range(1, 4):
    request = requests.get(url, params={'page': i, 'per_page':80})
    db = sqlite3.connect(':memory:')
    db = sqlite3.connect('basesita-de-datos.db')
    cur = db.cursor()
    lasfrias = request.json()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS chelas (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    image_url VARCHAR(200),
    abv REAL,
    food_pairing BLOB,
    ph REAL,
    contributed_by VARCHAR(200),
    attenuation_level INTEGER,
    tagline VARCHAR(200)
    )'''
    )
    if i == 3:
        for a in range(0,74):
            cur.execute('''
            INSERT INTO chelas (
            id,
            name,
            description,
            image_url,
            abv,
            food_pairing,
            ph,
            contributed_by,
            attenuation_level,
            tagline
            )
            VALUES (?,?,?,?,?,?,?,?,?,?);''',(lasfrias[a]['id'],lasfrias[a]['name'],lasfrias[a]['description'],lasfrias[a]['image_url'],lasfrias[a]['adv'],lasfrias[a]['food_pairing'],lasfrias[a]['ph'],lasfrias[a]['contributed_by'],lasfrias[a]['attenuation_level'],lasfrias[a]['tagline']))
    else:
        for d in range(0,80):
            cur.execute('''
            INSERT INTO chelas (
            id,
            name,
            description,
            image_url,
            abv,
            food_pairing,
            ph,
            contributed_by,
            attenuation_level,
            tagline
            )
            VALUES (?,?,?,?,?,?,?,?,?,?);''',(lasfrias[d]['id'],lasfrias[d]['name'],lasfrias[d]['description'],lasfrias[d]['image_url'],lasfrias[d]['adv'],lasfrias[d]['food_pairing'],lasfrias[d]['ph'],lasfrias[d]['contributed_by'],lasfrias[d]['attenuation_level'],lasfrias[d]['tagline']))
    query = cur.execute('''
        SELECT * FROM chelas
        ORDER BY id ''')
    print(query.fetchall())
db.close()
