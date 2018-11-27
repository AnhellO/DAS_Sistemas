import os, errno, sqlite3

db = sqlite3.connect(':memory:')
db = sqlite3.connect('Characters.db')
cursor = db.cursor()
queryto = cursor.execute('''
	SELECT * FROM Personajes
	ORDER BY Nombre
''')

for row in queryto:
	nombreArchivo = '/TablaContenidos.html'
	print('Escribiendo archivo {}...'.format(nombreArchivo))

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
        			    <th>Nombre</th>
        			    <th>Fecha de Nacimiento</th>
        			    <th>Sexo</th>
        			    <th>Masa</th>
        			    <th>Planeta de Origen</th>
        			    <th>JSONPATH</th>
        			</tr>
        			<tr>
                        <th>{}</th>
                        <th>{}</th>
                        <th>{}</th>
                        <th>{}</th>
                        <th>{}</th>
                        <th>{}</th>
                    </tr>
        		</table>
        	</body>
        </html>
		'''.format(row[0], row[1], row[2], row[3], row[4], row[5])

		archivo.write(Guardar)
		archivo.close()
		print('Archivo creado.')

db.close()
