import time, re, requests, os, errno, json, sqlite3

def getDatos(url,i):
    directorio = 'Json'
    ids=[]
    print ('Buscando informacion...')
    ids.append(i)
    urls = url + str(i)
    request = requests.get(urls)
    try:
        id_ = request.json()['value']['id']
    except:
        id_=i
        type_=None
        joke='No existe.'
        categories=None
        pass
    try:
        type_ = request.json()['type']
        joke = request.json()['value']['joke']
        categories = request.json()['value']['categories'][0]
    except:
        categories = None
        pass
    for url in urls:
        archivojson ='{}/{}.json'.format(directorio, id_)
        print('Escribiendo archivo {}...'.format(archivojson))
        if not os.path.isfile(os.path.dirname(archivojson)):
            try:
                os.makedirs(os.path.dirname(archivojson))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        with open(archivojson, 'w') as archivo:
            archivo.write(request.text)
            archivo.close()
            print('Json guardado')
        js= os.path.dirname(archivojson)
        base = setDatos(id_,type_,joke,categories,js)
        print('Guardando datos...')
        return(base)

def setDatos(id_,type_,joke,categories,js):
    conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect("LibroChuck.db")
    cursor = conn.cursor()
    if not os.path.isfile("LibroChuck.db"):
        conn = sqlite3.connect("LibroChuck.db")
    else:
        pass
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Chuck_Norris (
			id INTEGER PRIMARY KEY,
			type TEXT,
			joke TEXT,
			categories TEXT,
			rutajson TEXT
		)''')
    conn.commit()
    cursor.execute(''' INSERT INTO Chuck_Norris VALUES (?,?,?,?,?)''', (id_,type_,joke,categories,js))
    conn.commit()
    basesita = cursor.execute('''
        SELECT * FROM Chuck_Norris
        ORDER BY id''')
    base = show(basesita)
    conn.close()
    print('Valores Insertados.')
    return(base)

def show(basesita):
    for row in basesita:
        return('\nID: {} \nType: {} \nJoke: {} \nCategories: {} \nRutajson: {}'\
        .format(row[0],row[1],row[2],row[3],row[4]))

if __name__ == '__main__':
    url = 'https://api.icndb.com/jokes/'
    i=0
    for i in range(1,101):
        base = getDatos(url,i)
        if base:
            print(" \n{}.- Datos Guardados.".format(i))
        else:
            print("Fallo, la tabla esta vacía.")
        i+=1
    print("listo.")
