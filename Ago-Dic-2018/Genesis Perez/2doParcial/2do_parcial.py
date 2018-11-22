import time, re, requests, os, errno, json, sqlite3

mi_repo = 'Genesis Perez'
directorio = '2do_parcial'
subdirectorio = 'html'
url = 'http://jsonplaceholder.typicode.com/comments'

ids = range(0,100)
ids1 = list(ids)

# Ejercicio 2: Crear BD, 5 columnas y 1 extra
db = sqlite3.connect(':memory:')
db = sqlite3.connect('bdjsonplaceholder.db')

cursor = db.cursor()
cursor.execute('''
	CREATE TABLE IF NOT EXISTS comments (
		id INTEGER,
		postid INTEGER,
		name TEXT,
		email VARCHAR(200),
        body VARCHAR(350),
        url_archivo VARCHAR(20)
	)'''
)

#Ejercicio 1: 100 elementos y archivo json
for id in ids1:
    request = requests.get(url, params={'ids':str(id)})
    nombreArchivo = '{}/{}.json'.format(subdirectorio, request.json()[id]['id'])
    print('Escribiendo archivo {}...'.format(nombreArchivo))

    if not os.path.exists(os.path.dirname(nombreArchivo)):
        try:
            os.makedirs(os.path.dirname(nombreArchivo))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    with open(nombreArchivo, 'w') as archivo:
        archivo.write(str(request.json()[id]))
        archivo.close()
        print('Archivo JSON guardado')

for id in ids1:
    request = requests.get(url, params={'ids':str(id)})
    datos = request.json()

    cursor = db.cursor()
    if cursor.execute('''
        INSERT INTO comments VALUES (
        :id, :postid, :name, :email, :body, :url_archivo)''',
        {'id':datos[id].get("id"), 'postid':datos[id].get("postId"), 'name':datos[id].get("name"), 'email':datos[id].get("email"), 'body':datos[id].get("body"), 'url_archivo':'{}/{}/{}'.format(mi_repo, directorio, subdirectorio)}) :
        print("Comentario agregado a la bd")
    else:
        print("NO se agregó")

    db.commit()
    #time.sleep(3)

queryto = cursor.execute('''
	SELECT * FROM comments
	ORDER BY id
''')

tablahtml = '{}/tablahtml.html'.format(directorio)
if not os.path.exists(os.path.dirname(tablahtml)):
    try:
        os.makedirs(os.path.dirname(tablahtml))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

"""with open(tablahtml, 'w') as archivo:
    for row in queryto:
        Guardar = '''
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
		        <h2>Items de la Base de Datos</h2>
		        <table>
		  	           <tr>
			               <th>ID</th>
			               <th>PostId</th>
			               <th>Name</th>
			               <th>Email</th>
			               <th>Body</th>
			               <th>Url Archivo</th>
			           </tr>
                       <?php
                       for ($i=0; $i<5; $i++)
                       {
                            echo<tr>{}</tr>
                            echo<tr>{}</tr>
                            echo<tr>{}</tr>
                            echo<tr>{}</tr>
                            echo<tr>{}</tr>
                            echo<tr>{}</tr>
                        }
                        ?>
		        </table>
	     </body>
         </html>
		'''.format(row[1], row[0], row[2], row[3], row[4], row[5])

archivo.write(Guardar)
archivo.close()

print('Tabla html hecha')
"""

db.close()
