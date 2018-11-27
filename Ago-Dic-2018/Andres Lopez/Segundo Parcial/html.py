import os, errno, sqlite3

db = sqlite3.connect(':memory:')
db = sqlite3.connect('LibroChuck.db')
cursor = db.cursor()
queryto = cursor.execute('''
	SELECT * FROM Chuck_Norris
	ORDER BY id
''')

for row in queryto:
	nombreArchivo = '/Tabla.html'
	print('Escribiendo {}...'.format(nombreArchivo))

	if not os.path.isfile(os.path.dirname(nombreArchivo)):
		try:
			os.makedirs(os.path.dirname(nombreArchivo))
		except OSError as exc:
			if exc.errno != errno.EEXIST:
				raise

	with open(nombreArchivo, 'w') as archivo:
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
        			    <th>Type</th>
        			    <th>Joke</th>
        			    <th>Categories</th>
        			    <th>Rutajson</th>
        			</tr>
        			<tr>
                        <th>{}</th>
                        <th>{}</th>
                        <th>{}</th>
                        <th>{}</th>
                        <th>{}</th>
                    </tr>
        		</table>
        	</body>
        </html>
		'''.format(row[0], row[1], row[2], row[3], row[4])

		archivo.write(Guardar)
		archivo.close()
		print('html creado.')

db.close()
