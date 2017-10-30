# -*- coding: utf-8 -*-

import urllib.request, time, json, requests, os
from urlextract import URLExtract
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Instancia de declarative_base, todas las clases para mapeo la utilizan.
Base = declarative_base()

# Patrón de diseño Factory para las clases de ORM.
class fact(object):
    def factory(clase):
        cl = clase.upper()
        if cl == "BAND":
            return Band()
        elif cl == "DISCOGRAPHY":
            return Discography()
        elif cl == "MEMBER":
            return Member()


# Modelamos una clase "Band" para todos los atributos que extraímos.
class Band(Base, fact):
    __tablename__ = "Band"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    country = Column('country', String)
    location = Column('location', String)
    status = Column('status', String)
    formed_in = Column('formed_in', String)
    years_active = Column('years_active', String)
    genre = Column('genre', String)
    lyrical_themes = Column('lyrical_themes', String)
    label = Column('label', String)


# Modelamos una clase "Discography" para todos los atributos que extraímos.
class Discography(Base, fact):
    __tablename__ = "Discography"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    release_type = Column('release_type', String)
    year = Column('year', String)
    band_id = Column('band_id', Integer, ForeignKey("Band.id"), nullable=False)


# Modelamos una clase "Member" para todos los atributos que extraímos.
class Member(Base, fact):
    __tablename__ = "Member"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    band_id = Column('band_id', Integer, ForeignKey("Band.id"), nullable=False)



engine = create_engine('sqlite:///swedish_bands.db', echo=True)
# Estos dos son necesarios para cada sesión de base de datos.
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


def current_target_url(page, display_start):
    # Actualizará el URL para cambiar a la siguiente página del DT si es necesario.
    target_url = 'https://www.metal-archives.com/browse/ajax-country/c/SE/json/1'
    target_url += '?sEcho={}&iColumns=4&sColumns=&iDisplayStart={}&iDisplayLength=500'.format(page, display_start)
    target_url += '&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0'
    target_url += '&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true'
    target_url += '&bSortable_2=true&bSortable_3=false&_=1505682951191'

    return target_url

def get_total_records(target_url):
    # Trae el número de entradas del DataTable entero.
    with urllib.request.urlopen(target_url) as url:
        data = json.loads(url.read().decode())
        total_records = data["iTotalRecords"]

    return total_records

def get_json_data(target_url):
    # Trae datos necesarios del json.
    with urllib.request.urlopen(target_url) as url:
        data = json.loads(url.read().decode())

    return data


def crawler():
    # Instancia de URLExtract.
    extractor = URLExtract()

    # Parametros para iniciar el scraping en el DataTable.
    page = 1
    display_start = 0
    current_records = 0

    # URL inicial.
    target_url = current_target_url(page, display_start)

    # Records totales y entradas de la primera página.
    total_records = get_total_records(target_url)
    json_data = get_json_data(target_url)


    # Mientras no se pase del total de records:
    while current_records < total_records:
        # -> Por cada 500 elementos:
        for x in range(500):
            # -> Condición para cuando no hay más que buscar.
            if current_records == total_records:
                break

            # -> Contador de records actuales.
            current_records += 1

            # -> Castea los datos de las bandas desde el DT a string.
            # -> Busca el URL de su respectivo perfil.
            s_json_data = str(json_data["aaData"][x][0])
            extracted_url = extractor.find_urls(s_json_data)

            # -> Se hace un get al URL extraído (perfil de la banda).
            r = requests.get(extracted_url[0])
            # -> Si el request sale bien:
            if r.status_code == 200:
                soup = BeautifulSoup(r.content, 'html.parser')

                # -> Hacemos el parseo de los atributos junto con la inserción objeto -> BD.
                get_band_attributes(soup)
                get_band_disco(soup, current_records)
                get_band_members(soup, current_records)

            # -> 2 segundos de espera por ciclo.
            time.sleep(2)

        # Cada 500 entradas:
        # -> Cambia de pagina en DataTable.
        page += 1
        # -> Muestra las siguientes 500 bandas.
        display_start += 500

        # Actualización de URL inicial.
        target_url = current_target_url(page, display_start)
        # Actualización de json inicial.
        json_data = get_json_data(target_url)

def get_band_attributes(soup):
    # Instancias tanto para la sesión como para la clase que definimos para modelar las bandas.
    session = Session()
    band = fact.factory("band")

    # Del objeto "soup" (el contenido será parecido a band_page.html) que viene como parámetro:
    # -> Busca <h1 class="band_name">, que es el tag donde se encuentra el nombre de la banda.
    band_name = soup.find("h1", {"class": "band_name"})


    # -> Buscamos en <dd> que es donde se encuentran los atributos generales.
    # -> Regresa una lista de tags y su contenido.
    attributes = soup.find_all("dd")

    # Una lista para usar los datos sin los whitespaces molestos que trae 'years_active'.
    formatted_attributes = []
    # -> Por cada elemento de la lista.
    for atr in attributes:
        # -> Separa los strings en listas.
        s_list = atr.getText().split()
        # -> Se junta de nuevo como string pero con whitespaces normales.
        s = " ".join(map(str, s_list))
        # -> Se pasa a lista de nuevo ya spliteado.
        formatted_attributes.append(s)

    # Añadimos a base de datos.
    # No se requieren queries para insertar, sólo asignar al objeto instanciado.
    band.name = band_name.getText()
    band.country = formatted_attributes[0]
    band.location = formatted_attributes[1]
    band.status = formatted_attributes[2]
    band.formed_in = formatted_attributes[3]
    band.genre = formatted_attributes[4]
    band.lyrical_themes = formatted_attributes[5]
    band.label = formatted_attributes[6]
    band.years_active = formatted_attributes[7]

    # Creamos el row.
    session.add(band)
    # Guardamos los cambios a base de datos.
    session.commit()
    # Cerramos sesión.
    session.close()


def get_band_disco(soup, current_records):
    # Instancia de URLExtract.
    extractor = URLExtract()

    # Abrimos sesión con la base de datos.
    session = Session()

    # Del objeto "soup" (el contenido será parecido a band_page.html) encuentra <div id="band_disco">.
    disco_finder = soup.find("div", {"id": "band_disco"})
    # Los tags resultantes pasan a string.
    s_disco_finder = str(disco_finder)
    # Extrae todos los URLs presentes.
    disco_url = extractor.find_urls(s_disco_finder)

    # Toma el primer URL y asigna a una variable.
    url = disco_url[0]
    # Hace un request con dicho URL.
    r = requests.get(url)

    # Algo para los caracteres raros, por si los hay.
    r.encoding = 'utf-8'

    # Convierte el response en un objeto BeautifulSoup para su uso.
    disco_soup = BeautifulSoup(r.content, 'html.parser')

    # Del objeto "disco_soup" (el contenido será parecido a disco.html) obtiene todos los tags <tr>.
    disco_entries = disco_soup.find_all("tr")

    # Elimina el primero porque no se necesita.
    disco_entries.pop(0)

    # -> Por cada elemento en disco_entries:
    for item in disco_entries:
        # -> Instanciamos la discografía e insertamos.
        discography = fact.factory("discography")
        discography.band_id = current_records
        # -> Intentamos:
        try:
            # -> En un ciclo de x < 3:
            for x in range(3):
                # -> Busca todos los tags <td> usando el índice 'x'.
                s = item.find_all("td")[x]
                # -> Como en este caso los atributos de la discografía vienen en 3 partes, condicionamos:
                if x == 0:
                    discography.name = str(s.getText())
                if x == 1:
                    discography.release_type = str(s.getText())
                if x == 2:
                    discography.year = str(s.getText())
                # -> Agregamos el row.
                session.add(discography)
            # Guardamos cambios.
            session.commit()
            # Cerramos sesión.
            session.close()
        except:
            # En caso de que la banda no tenga releases sólo pasa al siguiente.
            session.close()


def get_band_members(soup, current_records):
    # Abrimos sesión con la base de datos.
    session = Session()

    # Del objeto "soup" (el contenido será parecido a band_page.html) encuentra <div id="band_tab_members_current">.
    current_members = soup.find("div", {"id": "band_tab_members_current"})

    # De la búsqueda anterior encuentra todos los <a class="bold">.
    member_finder = current_members.find_all("a", {"class": "bold"})

    # -> Con un ciclo mientras x < tamaño de member_finder.
    for x in range(len(member_finder)):
        # -> Instanciamos la clase miembro e insertamos.
        member = fact.factory("member")
        member.band_id = current_records
        member.name = str(member_finder[x].getText())
        # Agregamos el row nuevo.
        session.add(member)
    # Guardamos los cambios.
    session.commit()
    # Cerramos sesión.
    session.close()


if __name__ == '__main__':
    crawler()
