import ORM
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Tablas</h1>
    <ul>
    <li><a href='/episodios'>episodios</a></li><br>
    <li><a href='/locaciones'>locaciones</a></li><br>
    <li><a href='/personajes'>personajes</a></li>
    </ul>
    """

@app.route('/episodios')
def episodios():
    episo = ORM.get_episodios()
    content = """
    <a href='/episodios/todo'>Ver Todo</a><br><br>"""
    for i in range(0, len(episo)):

        cap = episo[i]
        dato = """
            <p>Id_Episodio: {} </p>
            <p>Nombre: <a href='/episodios/{}'>{}</a> </p> 

            <p>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
            """.format(cap._Id_Episodio, i+1, cap._Nombre)
        content += dato
    return content

@app.route('/episodios/todo')
def episodios_todo():
    episo = ORM.get_episodios()
    content=''
    for i in range(0, len(episo)):
        cap = episo[i]
        data = """
        <p>Fecha de Lanzamiento: {} </p>
        <p>Personajes: {} </p> 
        <p>Fecha de Creacion: {} </p> 
        <p>Episodio: {} </p> 
        <p>Id_Episodio: {} </p>
        <p>Nombre: {} </p> 
        <p>Url: {} </p>
        <p>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
            
        """.format(cap._FechaLanzamiento, cap._Personajes, cap._FechaCreacion, cap._CodEpisodio, cap._Id_Episodio, cap._Nombre, cap._URL)
        content += data
    return content
        

@app.route('/episodios/<string:id_episodio>')
def episodio_especifico(id_episodio):
    # id_episodio = request.form.get('id_episodio')
    # id_episodio= request.form.id_episodio
    episo = ORM.get_episodio_especifico(id_episodio)
    content=''
    for i in range(0, len(episo)):

        cap = episo[i]
        dato = """
        <p>Fecha de Lanzamiento: {} </p>
        <p>Personajes: {} </p> 
        <p>Fecha de Creacion: {} </p> 
        <p>Episodio: {} </p> 
        <p>Id_Episodio: {} </p>
        <p>Nombre: {} </p> 
        <p>Url: {} </p>
        <p>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
            
        """.format(cap._FechaLanzamiento, cap._Personajes, cap._FechaCreacion, cap._CodEpisodio, cap._Id_Episodio, cap._Nombre, cap._URL)
        content += dato
    return content

@app.route('/locaciones')
def locaciones():
    loc = ORM.get_locations()
    content ="<a href= '/locaciones/todo'>Ver todo</a><br><br>"
    for i in range(0, len(loc)):
        lugar = loc[i]
        dato = """
            <p>Id_Locacion: {} </p>
            <p>Nombre: <a href='/locaciones/{}'>{}</a> </p> 
            <p>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
            """.format(lugar._Id_Locacion, i+1, lugar._Nombre)
        content += dato
    return content

@app.route('/locaciones/todo')
def locaciones_todo():
    loc = ORM.get_locations()
    content =''
    for i in range(0, len(loc)):
        lugar = loc[i]
        dato = """
            <p>Fecha_Creacion: {}</p>
            <p>Dimension: {}</p>
            <p>Id_Locacion: {}</p>
            <p>Nombre: {}</p>
            <p>Residentes: {}</p>
            <p>Tipo: {}</p>
            <p>URL: {}</p>
            <p>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
            """.format(lugar._FechaCreacion, lugar._Dimension, lugar._Id_Locacion, lugar._Nombre, lugar._Residentes, lugar._Tipo, lugar._URL)
        content += dato
    return content

@app.route('/locaciones/<string:id_locacion>')
def locacion_especifica(id_locacion):
    loc = ORM.get_locations_especifico(id_locacion)
    content =''
    for i in range(0, len(loc)):
        lugar = loc[i]
        dato = """
            <p>Fecha_Creacion: {}</p>
            <p>Dimension: {}</p>
            <p>Id_Locacion: {}</p>
            <p>Nombre: {}</p>
            <p>Residentes: {}</p>
            <p>Tipo: {}</p>
            <p>URL: {}</p>
            <p>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
            """.format(lugar._FechaCreacion, lugar._Dimension, lugar._Id_Locacion, lugar._Nombre, lugar._Residentes, lugar._Tipo, lugar._URL)
        content += dato
    return content

@app.route('/personajes')
def personajes():
    person = ORM.get_personajes()
    content ="<a href= '/personajes/todo'>Ver todo</a><br><br>"
    for i in range(0, len(person)):
        character = person[i]
        dato = """
            <p>Id_Personaje: {} </p>
            <p>Nombre: <a href='/personajes/{}'>{}</a> </p> 
            <p>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
            """.format(character._Id_Personaje, i+1, character._Nombre)
        content += dato
    return content

@app.route('/personajes/todo')
def personajes_todo():
    person = ORM.get_personajes()
    content =""
    for i in range(0, len(person)):
        character = person[i]
        dato = """
            <p>FechaDeCreacion: {}</p>
            <p>EpisodiosDondeAparece: {}</p>
            <p>NumeroEpisodiosDondeAparece: {}</p>
            <p>Genero: {}</p>
            <p>Id_Personaje: {}</p>
            <p>Imagen: {}</p>
            <p>Location_Name: {}</p>
            <p>Location_URL: {}</p>
            <p>Nombre: {}</p>
            <p>Origen_Name: {}</p>
            <p>Origen_URL: {}</p>
            <p>Especie: {}</p>
            <p>Status: {}</p>
            <p>Tipo: {}</p>
            <p>URL: {}</p>
            <p>------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
            """.format(character._FechaDeCreacion, character._EpisodiosDondeAparece, character._NumeroEpisodiosDondeAparece, character._Genero, character._Id_Personaje, character._Imagen, character._Location_Name, character._Location_URL, character._Nombre, character._Origen_Name, character._Origen_URL, character._Especie, character._Status, character._Tipo, character._URL)
        content += dato
    return content

@app.route('/personajes/<string:id_personaje>')
def personaje_especifico(id_personaje):
    person = ORM.get_personaje_especifico(id_personaje)
    content =""
    for i in range(0, len(person)):
        character = person[i]
        dato = """
            <p>FechaDeCreacion: {}</p>
            <p>EpisodiosDondeAparece: {}</p>
            <p>NumeroEpisodiosDondeAparece: {}</p>
            <p>Genero: {}</p>
            <p>Id_Personaje: {}</p>
            <p>Imagen: {}</p>
            <p>Location_Name: {}</p>
            <p>Location_URL: {}</p>
            <p>Nombre: {}</p>
            <p>Origen_Name: {}</p>
            <p>Origen_URL: {}</p>
            <p>Especie: {}</p>
            <p>Status: {}</p>
            <p>Tipo: {}</p>
            <p>URL: {}</p>
            """.format(character._FechaDeCreacion, character._EpisodiosDondeAparece, character._NumeroEpisodiosDondeAparece, character._Genero, character._Id_Personaje, character._Imagen, character._Location_Name, character._Location_URL, character._Nombre, character._Origen_Name, character._Origen_URL, character._Especie, character._Status, character._Tipo, character._URL)
        content += dato
    return content

if __name__ == '__main__':
    app.run(use_reloader=True)