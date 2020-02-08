f = open('holamundo.html','w+')

mensaje = """<html>
<head></head>
<body><p>Hola Mundo!</p></body>
</html>"""

f.write(mensaje)
f.close()
