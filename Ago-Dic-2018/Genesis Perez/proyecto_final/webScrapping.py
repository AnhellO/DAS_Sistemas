import requests, os, errno, sqlite3, json
from bs4 import BeautifulSoup

cnx = sqlite3.connect('taqueria.db')
cursor = cnx.cursor()

class scrappingTacos():
    url = 'http://taco-randomizer.herokuapp.com/'
    for i in range(1,51): # hasta el 51
        idtaco = int(i)
        cursor.execute("INSERT INTO tacos (ID) VALUES (?)",(idtaco,))
        cnx.commit()
        # i es el id de c/taco, en tabla tacos
        # Realizamos la petición a la web
        req = requests.get(url)
        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        soup = BeautifulSoup(req.text, 'html.parser')
        # Encontrar todos los datos dentro de las tags donde están las entradas que necesitamos
        nombresTacos = soup.find_all('h1',{'class':'light'})
        subrecetas = soup.find_all('div',{'class':'twelve columns'})
        # Recorremos todas las entradas para extraer el nombre del taco, las sub-recetas, contribuidores, tags
        for i, nombre in enumerate(nombresTacos):
            # taco es el nombre completo del taco
            taco = nombre.getText()
            cursor.execute("Update tacos SET Nombre_Taco=? WHERE ID=?",(taco,idtaco))
            cnx.commit()
            for i, subreceta in enumerate(subrecetas):
                receta = subreceta.find('div', {'class':'recipe'}).getText()
                # Buscamos la sub-cadena "tags:", devuelve el índice de inicio de las mismas
                indiceTags = receta.find("tags:")
                # Cortamos el texto de la receta para que la sub-cadena "tags:..." ya no aparezcan; desde la posición 0 hasta el índice que nos devolvió el método anterior
                recetaSinTags = receta[:indiceTags]
                # recetaSinTags es solo el nombre y procedimiento de la receta
                # Cortamos la receta para pasar la sub-cadena "tags:" con todo lo que está adelante, debido a que es el último renglón, no se necesita poner un parámetro específico de donde termina
                tags = receta[indiceTags:]
                contribuidores = subreceta.find('h6', {'class':'light'}).getText()
                if i==0:
                    cursor.execute("UPDATE tacos SET BaseLayer=?,Contribuidores_BL=?,Tags_BL=? WHERE ID=?",(recetaSinTags,contribuidores,tags,idtaco))
                    cnx.commit()
                if i==1:
                    cursor.execute("UPDATE tacos SET Mixin=?,Contribuidores_Mix=?,Tags_Mix=? WHERE ID=?",(recetaSinTags,contribuidores,tags,idtaco))
                    cnx.commit()
                if i==2:
                    cursor.execute("UPDATE tacos SET Condiment=?,Contribuidores_Cond=?,Tags_Cond=? WHERE ID=?",(recetaSinTags,contribuidores,tags,idtaco))
                    cnx.commit()
                if i==3:
                    cursor.execute("UPDATE tacos SET Seasoning=?,Contribuidores_Seas=?,Tags_Seas=? WHERE ID=?",(recetaSinTags,contribuidores,tags,idtaco))
                    cnx.commit()
                if i==4:
                    cursor.execute("UPDATE tacos SET Shell=?,Contribuidores_Shell=?,Tags_Shell=? WHERE ID=?",(recetaSinTags,contribuidores,tags,idtaco))
                    cnx.commit()
    cnx.close()

class Clientes():
    def crearClientes():
        for i in range(1,21):
            idcliente = i
            url = 'https://randomuser.me/api/'
            request = requests.get(url)
            datos = request.json()['results']
            nombrecliente = datos[0]['name'].get("first") + " " + datos[0]['name'].get("last")
            genero = datos[0]['gender']
            celular = datos[0]['cell']
            direccion = datos[0]['location'].get("street")
            cursor.execute("INSERT INTO clientes (ID,Nombre,Genero,Celular,Direccion) VALUES (?,?,?,?,?)",(idcliente, nombrecliente, genero, celular, direccion))
            cnx.commit()
            cnx.close()
