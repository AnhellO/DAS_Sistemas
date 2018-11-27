import time, re, requests, os, errno, json, sqlite3

def getDatos(url,i):
    directorio = 'archivos-de-cache'
    ids = []
    print ('buscando informacion...')
    ids.append(i)
    urls = url + str(i)
    request = requests.get(urls)

    
    id = request.json()[0]['id']
    icon_url = request.json()[0]['icon_url']
    url = request.json()[0]['url']
    value = request.jason()[0]['value']

    for url in urls:
        matenme ='{}/{}.json'.format(directorio, request.json()[0][id])
        print('Escribiendo archivo {}...'.format(matenme))
    if not os.path.exist(os.path.dirname(matenme)):
        try:
            os.makedirs(os.path.dirname(matenme))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    with open(matenme, 'w') as archivo:
        archivo.write(request.text)
        archivo.close()
        print('Archivo Cacheado')
    return (string)

def setDatos(icon_url, id, url, value):
    conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect("LibroChuck.db")
    cursor = conn.cursor()

    if not os.path.isfile("LibroChuck.bd"):
        conn = sqlite3.connect("LibroChuck.bd")

    else:

        pass

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Chuck_Norris (
            id INTEGER PRIMARY KEY,
            icon_url TEXT,
            url TEXT,
            value TEXT
        )'''
    )
    conn.commit()
    cursor.execute(''' INSERT INTO Chuck_Norris Values(?,?,?,?)''', (id, icon_url, url, value))
    conn.commit()

    basesita = cursor.execute('''
        SELECT * FROM Chuck_Norris
        ORDER BY id''')
    base = show(basesita)
    conn.close()
    return (base)

def show (basesita):
    for row in basesita:
        return('\nID: {} \nicon_url: {} \nurl: {} \nvalue: {} '\
               .format(row[0], row[1], row[3], row[4]))

if __name__ == '__main__':
    url = 'http://api.icndb.com/jokes/'
    i=0
    for i in range(1,100):
        base = getDatos(url,i)
        if base:
            print(" {}.- Datos Guardados.".format(i))
            
        else:
            print("Fallo, la tabla esta vacia.")

        i+=1
    print("listo.")

