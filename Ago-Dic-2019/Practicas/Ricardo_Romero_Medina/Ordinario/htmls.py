import ORMDB

def crear_index():
    f=open("Ordinario/index.html","w")

    texto = """<html>
    <head>
    <style type="text/css">
    h1{text-align:center}
    </style>
    </head>
    <body>
    <h1>Entidades</h1>
    <p><a href = "file:///C:/Users/narut/Documents/ClaseDise%C3%B1o/Ordinario/indicePersonajes.html"</a>Personajes</p>
    <p><a href = "file:///C:/Users/narut/Documents/ClaseDise%C3%B1o/Ordinario/indiceLocaciones.html"</a>Locacion</p>
    <p><a href = "file:///C:/Users/narut/Documents/ClaseDise%C3%B1o/Ordinario/indiceEpisodios.html"</a>Episodios</p>
    </body>
    </html>"""

    f.write(texto)
    f.close

def indice_personaje():
    datos = ORMDB.traer_personaje() 
    inf = ''
    for i in range(0,len(datos)): 
        pers = datos[i]
        info = """
        <p>Id = {}</p>
        <p>Nombre Personaje = <a href = "file:///C:/Users/narut/Documents/ClaseDise%C3%B1o/Ordinario/Personajes/Personaje-{}.html">{}</a></p>
        <p>-------------------------------</p>
        """.format(pers._Id,i+1,pers._Nombre)
        inf += info
    f=open("Ordinario/indicePersonajes.html","w", encoding='utf-8')
    f.write(inf)
    f.close
    
def indice_locacion():
    datos = ORMDB.traer_locacion() 
    inf = ''
    for i in range(0,len(datos)): 
        locac = datos[i]
        info = """
        <p>Id = {}</p>
        <p>Nombre Locacion = <a href = "file:///C:/Users/narut/Documents/ClaseDise%C3%B1o/Ordinario/Locaciones/Locacion-{}.html">{}</a></p>
        <p>Dimension = {}</p>
        <p>-------------------------------</p>
        """.format(locac._Id,i+1,locac._Nombre,locac._Dimension)
        inf += info
    f=open("Ordinario/indiceLocaciones.html","w", encoding='utf-8')
    f.write(inf)
    f.close

def indice_episodios():
    datos = ORMDB.traer_episodio() 
    inf = ''
    for i in range(0,len(datos)): 
        epi = datos[i]
        info = """
        <p>Id = {}</p>
        <p>Nombre Capitulo = <a href = "file:///C:/Users/narut/Documents/ClaseDise%C3%B1o/Ordinario/Episodios/Episodio-{}.html">{}</a></p>
        <p>Fecha Lanzamiento = {}</p>
        <p>-------------------------------</p>
        """.format(epi._Id,i+1,epi._Nombre,epi._Al_Aire)
        inf += info
    f=open("Ordinario/indiceEpisodios.html","w", encoding='utf-8')
    f.write(inf)
    f.close

def personaje():
    datos = ORMDB.traer_personaje()
    for i in range(0,len(datos)):
        pers = datos[i]
        f=open("Ordinario/Personajes/Personaje-{}.html".format(i+1),"w", encoding='utf-8')
        info = """
        <p>Id = {}</p>
        <p>Nombre Personajen = {}</p>
        <p>Status = {}</p>
        <p>Specie = {}</p>
        <p>Origen = {}</p>
        <p>Tipo = {}</p>
        <p>Locacion = {}</p>
        <p>Id Locacion = {}</p>
        <p>Episodio = {}</p>
        <p>Id Episodio = {}</p>
        <p>URL Personaje = {}</p>
        """.format(pers._Id,pers._Nombre,pers._Status,pers._Species,pers._Origen,pers._Tipo,pers._Location,pers._Id_Locacion,pers._Episode,pers._Id_Episodio,pers._Url)
        f.write(info)
        f.close

def locacion():
    datos = ORMDB.traer_locacion()
    for i in range(0,len(datos)):
        loc = datos[i]
        f=open("Ordinario/Locaciones/Locacion-{}.html".format(i+1),"w", encoding='utf-8')
        info = """
        <p>Id = {}</p>
        <p>Nombre Capitulo = {}</p>
        <p>Tipo = {}</p>
        <p>Dimension = {}</p>
        <p>Personaje = {}</p>
        <p>Numero Personaje = {}</p>
        <p>URL Locacion = {}</p>
        """.format(loc._Id,loc._Nombre,loc._Tipo,loc._Dimension,loc._Residentes,loc._Id_Residente,loc._Url)
        f.write(info)
        f.close

def episodio():
    datos = ORMDB.traer_episodio()
    for i in range(0,len(datos)):
        epi = datos[i]
        f=open("Ordinario/Episodios/Episodio-{}.html".format(i+1),"w", encoding='utf-8')
        info = """
        <p>Id = {}</p>
        <p>Nombre Capitulo = {}</p>
        <p>Fecha Lanzamiento = {}</p>
        <p>Episodio = {}</p>
        <p>Personajes = {}</p>
        <p>Numero Personaje = {}</p>
        <p>URL Episodio = {}</p>
        """.format(epi._Id,epi._Nombre,epi._Al_Aire,epi._Episodio,epi._Personaje,epi._Id_Personaje,epi._Url)
        f.write(info)
        f.close




crear_index()
indice_episodios()
indice_personaje()
indice_locacion()
episodio()
locacion()
personaje()