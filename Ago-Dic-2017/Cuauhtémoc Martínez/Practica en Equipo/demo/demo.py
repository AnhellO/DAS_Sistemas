# OJO: La parte de base de datos sólo está implementada a manera de prueba de concepto. (FK's fijos, etc.)

# pip install bs4
from bs4 import BeautifulSoup

# Este no recuerdo si lo bajé con pip, si da error debe ser eso.
import requests

# pip install urlextract
from urlextract import URLExtract

# pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Instancia de declarative_base, todas las clases para mapeo la utilizan.
Base = declarative_base()

# Modelamos una clase "Band" para todos los atributos que extraímos.
class Band(Base):
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
class Discography(Base):
    __tablename__ = "Discography"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    release_type = Column('release_type', String)
    year = Column('year', String)
    band_id = Column('band_id', Integer, ForeignKey("Band.id"), nullable=False)


# Modelamos una clase "Member" para todos los atributos que extraímos.
class Member(Base):
    __tablename__ = "Member"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    band_id = Column('band_id', Integer, ForeignKey("Band.id"), nullable=False)



# Se crea el engine para guardar todo en un archivo .db.
# Si no existen las tablas las crea automáticamente y es autoincremental por default.
engine = create_engine('sqlite:///swedish_bands.db', echo=True)
# Estos dos son necesarios para cada sesión de base de datos.
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


def soup_it_up():
    # El URL puede ser cualquier perfil de banda en MA, -debería- funcionar. :D
    url = 'https://www.metal-archives.com/bands/Abomation/3540394749'

    # Va por el response usando el URL anterior.
    r = requests.get(url)

    # Convierte el response en un objeto BeautifulSoup para su uso.
    soup = BeautifulSoup(r.text, 'html.parser')

    # Un pequeño menú para facilitar el uso.
    while True:
        input_string = "¿Qué desea hacer?\n\t1. Obtener atributos generales."
        input_string += "\n\t2. Obtener discografía."
        input_string += "\n\t3. Obtener miembros."
        input_string += "\n\t4. Salir.\n"
        opt = input(input_string)
        if opt != '4':
            if opt == '1':
                get_band_attributes(soup)
                print(">>Los atributos de la banda han sido guardados en base de datos.")
            elif opt == '2':
                get_band_disco(soup)
                print(">>La discografía ha sido guardada en base de datos.")
            elif opt == '3':
                get_band_members(soup)
                print(">>Los miembros han sido guardados en base de datos.")
        else:
            break



def get_band_attributes(soup):
    # Instancias tanto para la sesión como para la clase que definimos para modelar las bandas.
    session = Session()
    band = Band()

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

    # Hacemos una especie de staging a los cambios.
    session.add(band)
    # Guardamos los cambios a base de datos.
    session.commit()
    # Cerramos sesión.
    session.close()


def get_band_disco(soup):
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

    # Toma el primer URL y asignalo a una variable.
    url = disco_url[0]
    # Hace un request con dicho URL.
    r = requests.get(url)

    # Convierte el response en un objeto BeautifulSoup para su uso.
    disco_soup = BeautifulSoup(r.text, 'html.parser')

    # Del objeto "disco_soup" (el contenido será parecido a disco.html) obtiene todos los tags <tr>.
    disco_entries = disco_soup.find_all("tr")

    # Elimina el primero porque no se necesita.
    disco_entries.pop(0)

    # -> Por cada elemento en disco_entries:
    for item in disco_entries:
        # -> Instanciamos la discografía e insertamos.
        discography = Discography()
        discography.band_id = 1
        # -> Con un ciclo mientras x < 3:
        for x in range(3):
            # -> Busca todos los tags <td> usando el índice 'x'.
            try:
                s = item.find_all("td")[x]
            except:
                session.close()
                return
            # -> Como en este caso los atributos de la discografía vienen en 3 partes, condicionamos:
            if x == 0:
                discography.name = str(s.getText())
            if x == 1:
                discography.release_type = str(s.getText())
            if x == 2:
                discography.year = str(s.getText())
            # -> Una vez que termina de construir el row le damos stage.
            session.add(discography)

    # Guardamos los cambios en base de datos.
    session.commit()
    # Cerramos sesión.
    session.close()


def get_band_members(soup):
    # Abrimos sesión con la base de datos.
    session = Session()

    # Del objeto "soup" (el contenido será parecido a band_page.html) encuentra <div id="band_tab_members_current">.
    current_members = soup.find("div", {"id": "band_tab_members_current"})

    # De la búsqueda anterior encuentra todos los <a class="bold">.
    member_finder = current_members.find_all("a", {"class": "bold"})

    # -> Con un ciclo mientras x < tamaño de member_finder.
    for x in range(len(member_finder)):
        # -> Instanciamos la clase miembro e insertamos.
        member = Member()
        member.band_id = 1
        member.name = str(member_finder[x].getText())
        # Stage al row nuevo.
        session.add(member)

    # Guardamos los cambios en base de datos.
    session.commit()
    # Cerramos la sesión.
    session.close()


if __name__ == '__main__':
    soup_it_up()
