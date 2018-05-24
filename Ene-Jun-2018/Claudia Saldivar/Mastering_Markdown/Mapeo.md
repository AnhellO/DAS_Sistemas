#Mapeo objeto-relacional

**El mapeo objeto-relacional** (más conocido por su nombre en inglés, Object-Relational mapping, o sus siglas O/RM, ORM, y O/R mapping) es una técnica de programación para convertir datos entre el **sistema de tipos** utilizado en un lenguaje de programación **orientado a objetos** y la utilización de una base de datos relacional como motor de persistencia. En la práctica esto crea una base de datos orientada a objetos virtual, sobre la base de datos relacional. Esto posibilita el uso de las características propias de la orientación a objetos (básicamente **herencia y polimorfismo**). Hay paquetes comerciales y de uso libre disponibles que desarrollan el mapeo relacional de objetos, aunque algunos programadores prefieren crear sus propias herramientas ORM.

##Implementaciones

Los tipos de bases de datos usados mayoritariamente son las bases de datos **SQL**, cuya aparición precedió al crecimiento de la programación orientada a objetos en los 1990s. Las bases de datos SQL usan una serie de tablas para organizar datos. Los datos en distintas tablas están asociados a través del uso de restricciones declarativas en lugar de punteros o enlaces explícitos. Los mismos datos que pueden almacenarse en un solo objeto podrían requerir ser almacenados a través de varias tablas.

Una implementación del mapeo relacional de objetos podría necesitar elegir de manera sistemática y predictiva qué tablas usar y generar las sentencias SQL necesarias.

Muchos paquetes han sido desarrollados para reducir el tedioso proceso de desarrollo de sistemas de mapeo relacional de objetos proveyendo bibliotecas de clases que son capaces de realizar mapeos automáticamente. Dada una lista de tablas en la base de datos, y objetos en el programa, ellos pueden automáticamente mapear solicitudes de un sentido a otro. Preguntar a un objeto persona por sus números telefónicos resultará en la creación y envío de la consulta apropiada a la base de datos, y los resultados son traducidos directamente en objetos de números telefónicos dentro del programa.

Desde el punto de vista de un programador, el sistema debe lucir como un almacén de objetos persistentes. Uno puede crear objetos y trabajar normalmente con ellos, los cambios que sufran terminarán siendo reflejados en la base de datos.

Sin embargo, en la práctica no es tan simple. Todos los sistemas ORM tienden a hacerse visibles en varias formas, reduciendo en cierto grado la capacidad de ignorar la base de datos. Peor aún, la capa de traducción puede ser lenta e ineficiente (comparada en términos de las sentencias SQL que escribe), provocando que el programa sea más lento y utilice más memoria que el código "escrito a mano".

Un buen número de sistemas de mapeo objeto-relacional se han desarrollado a lo largo de los años, pero su efectividad en el mercado ha sido diversa. NeXT's Enterprise Objects Framework (EOF) fue una de las primeras implementaciones, pero no tuvo éxito debido a que estaba estrechamente ligado a todo el kit de NeXT's, OpenStep [cita requerida]. Fue integrado más tarde en NeXT's WebObjects, el primer servidor web de aplicaciones orientado a objetos. Desde que Apple compró NeXT's en 1997, EOF proveyó la tecnología detrás de los sitios web de comercio electrónico de Apple: los servicios .Mac y la tienda de música iTunes. Apple provee EOF en dos implementaciones: la implementación en Objective-C que viene con Apple Developers Tools y la implementación Pure Java que viene en WebObjects 5.2. Inspirado por EOF es el open source Apache Cayenne. Cayenne tiene metas similares a las de EOF e intenta estar acorde a los estándares **JPA**.

Una aproximación alternativa ha sido tomada por tecnologías como RDF y **SPARQL**, y el concepto de "triplestore". RDF es una serialización del concepto objeto-sujeto-predicado, RDF/XML es una representación en XML de aquello, SPARQL es un lenguaje de consulta similar al SQL, y un "triplestore" es una descripción general de una base de datos que trabaja con un tercer componente.

Más recientemente, un sistema similar ha comenzado a evolucionar en el mundo Java, conocido como Java Data Objects (JDO). A diferencia de EOF, JDO es un estándar, y muchas implementaciones están disponibles por parte de distintos distribuidores de software. La especificación 3.0 de Enterprise Java Beans (EJB) también cubre la misma área. Han existido algunos conflictos de estándares entre ambas especificaciones en términos de preeminencia. **JDO** tiene muchas implementaciones comerciales, mientras que EJB 3.0 está aún en desarrollo. Sin embargo, recientemente otro estándar ha sido anunciado por JCP para abarcar estos dos estándares de manera conjunta y lograr que el futuro estándar trabaje en diversas arquitecturas de Java. Otro ejemplo a mencionar es Hibernate, el framework de mapeo objeto-relacional más usado en Java que inspiró la especificación EJB 3.

En el framework de desarrollo web **Ruby on Rails**, el mapeo objeto-relacional juega un rol preponderante y es manejado por la herramienta ActiveRecord. Un rol similar es el que tiene el módulo DBIx::Class para el framework basado en Perl Catalyst, aunque otras elecciones también son posibles.

##ejemplo
Hiperlink: [ESQUEMA][]
[esquema]:https://alexanderae.com/sqlalchemy-orm-para-python-1.html#fn-2S

```Python

###Primero, debemos mapear el modelo o esquema de la base de datos por medio de sqlalchemy, para lo cual escribí lo siguiente en un archivo al que llamé models.py:

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey,String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///libros.db', echo=True)
Base = declarative_base()

etiqueta_libro = Table('etiqueta_libro', Base.metadata,
    Column('libro_id', Integer, ForeignKey('libro.id')),
    Column('etiqueta_id', Integer, ForeignKey('etiqueta.id'))
)

autor_libro = Table('autor_libro', Base.metadata,
    Column('libro_id', Integer, ForeignKey('libro.id')),
    Column('autor_id', Integer, ForeignKey('autor.id'))
)

class Libro(Base):

    __tablename__ = 'libro'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(120), index=True, nullable=False)
    fecha_publicacion = Column(Date)
    isbn = Column(String(13))
    etiquetas = relationship("Etiqueta", secondary=etiqueta_libro)
    autores = relationship("Autor", secondary=autor_libro)

    def __init__(self, titulo, fecha_publicacion, isbn):
        self.titulo = titulo
        self.fecha_publicacion = fecha_publicacion
        self.isbn = isbn

    def __repr__(self):
        return unicode(self.titulo)

class Etiqueta(Base):

    __tablename__ = 'etiqueta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre

class Autor(Base):

    __tablename__ = 'autor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre

Base.metadata.create_all(engine)

```
```Python

###El acceso, inserción o modificación de datos, lo podemos realizar de la siguiente manera:

from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Autor, Etiqueta, Libro

engine = create_engine('sqlite:///libros.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

autor_1 = Autor('Patrick Rothfuss')
autor_2 = Autor('Fred Saberhagen')
lista_autores = (autor_1, autor_2)
session.add_all(lista_autores)
session.commit()

etiqueta_1 = Etiqueta('aventuras')
session.add(etiqueta_1)

libro_1 = Libro('El nombre del fuego', date(2009, 5, 30), '978-8401337208')
libro_1.etiquetas.append(etiqueta_1)
libro_1.autores.append(autor_1)
session.add(libro_1)
session.commit()

libro = session.query(Libro).filter(Libro.isbn=='978-8401337208').first()
print libro

libro.titulo = 'El nombre del viento'
session.commit()

print libro

```
