import requests, os, errno, json, sqlite3

url = 'https://www.metaweather.com/api/location/search/?query=s'

request = requests.get(url)

db = sqlite3.connect('base_de_datos.db')

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ubicaciones_que_incluyen_S (
        title TEXT,
        location_type TEXT,
        woeid INTEGER,
        latt_long REAL,
        rutajson TEXT
    )'''
)

lista_ubicaciones = request.json()

for i in range(0, len(lista_ubicaciones)):
    json = "jsons/{}.json".format(lista_ubicaciones[i]['title'])
    if not os.path.exists(os.path.dirname(json)):
        try:
            os.makedirs(os.path.dirname(json))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    with open(json, 'w') as archivo:
        archivo.write(str(lista_ubicaciones[i]))
        archivo.close()
        print('Archivo cacheado')
    cursor.execute('''
        INSERT INTO ubicaciones_que_incluyen_S (
        title,
        location_type,
        woeid,
        latt_long,
        rutajson
        )
        VALUES (
            ?,
            ?,
            ?,
            ?,
            ?
            );''',(lista_ubicaciones[i]['title'], lista_ubicaciones[i]['location_type'], lista_ubicaciones[i]['woeid'], lista_ubicaciones[i]['latt_long'], json)
        )

queryto = cursor.execute('''
    SELECT * FROM ubicaciones_que_incluyen_S
''')
db.commit()

html = 'hhtml/Tablon.html'

if not os.path.exists(os.path.dirname(html)):
    try:
        os.makedirs(os.path.dirname(html))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

with open(html, 'w') as archivo:
    guardarhtml = '''
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                table {
                    font-family: arial, sans-serif;
                    border-collapse: collapse;
                    width: 100%;
                }

                td, th {
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }

                tr:nth-child(even) {
                    background-color: #dddddd;
                }
            </style>
        </head>
        <body>
            <h2>Datos de la ubicacion</h2>
            <table>
                <tr>
                    <th>Title</th>
                    <th>Location_Type</th>
                    <th>Woeid</th>
                    <th>Latt_Long</th>
                    <th>RutaJson</th>
                </tr>
                <tr> ... </tr>
            </table>
        </body>
    </html>


    '''
    archivo.write(guardarhtml)
    archivo.close()
    print('Archivito cacheado :D!')










db.close()
