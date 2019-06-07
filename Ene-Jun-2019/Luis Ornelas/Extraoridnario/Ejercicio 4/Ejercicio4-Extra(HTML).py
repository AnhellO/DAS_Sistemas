import peewee
import datetime

db = peewee.SqliteDatabase('Paises.db')

class Pais(peewee.Model):
    Nombre = peewee.TextField()
    Capital = peewee.TextField()
    Region = peewee.TextField()
    Lenguajes = peewee.TextField()
    Bandera = peewee.TextField()

    class Meta:
        database = db
        db_table = 'Paises'


def main():

    list_of_paises = [] # lista para guardar paises
    paises = Pais.select(Pais.Nombre, Pais.Capital, Pais.Region, Pais.Lenguajes, Pais.Bandera)

    for pais in paises:
        pais_dictionary = {}
        pais_dictionary['name'] = pais.Nombre
        pais_dictionary['capital'] = pais.Capital
        pais_dictionary['region'] = pais.Region
        pais_dictionary['languages'] = pais.Lenguajes
        pais_dictionary['flag'] = pais.Bandera
        list_of_paises.append(pais_dictionary) # guardamos pais

        # empezamos a crear el archivo html extrayendo información de las listas creadas anteriormente
    string_html = """<!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
                    <title>Paises</title>
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
                    <script>
                    document.getElementsByClassName('texto').replace(/(?:\\[rn])+/g, "<br>");
                    </script>
            </head>
            <body style="background-color:white;">
            <br><h1 align="center">Countries Site</h1>
            <br><br><br><table align="center" style="width:80%" class="table table-striped">
                <thead style="background-color:indigo; color:white;" class="thead-black">
                    <tr>
                        <th>Paises</th>
                        <th>Información</th>
                    </tr>
                </thead>"""
    for pais in list_of_paises:
        string_html += "<tbody><tr><td>"+pais['name']+"<img class='img-thumbnail' src='" + pais['flag'] + "' width='300' height='300'> </td><td style='text-align:justify' class='texto'><b>Capital:</b> " + pais['capital'] + "<br><b>Region:</b> " + pais['region'] + "<br><b>Lenguajes:</b> " + pais['languages'] + "</td></tr>"

    string_html += """</tbody></table><br><br><br><table align="center" style="width:80%" class="table table-striped">
    <thead style="background-color:indigo; color:white;" class="thead-black">
        </thead>"""

    string_html += "</tbody></table></body></html>"
    with open("Paises_Todos.html", "a", encoding='utf-8') as f:
        f.write(string_html)
        f.close()

if __name__ == "__main__":
    main()
