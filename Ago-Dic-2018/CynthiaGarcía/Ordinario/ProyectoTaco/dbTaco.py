from sqlalchemy import create_engine, Column, text, delete, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import select
import logging

BD = declarative_base()

#se crean las tablas en forma de forma de clases utilizando los tipos de datos de sqlalchemy en este caso (Integer y String)
class UsuarioBD(BD):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column('nombre', String)
    apellido = Column('apellido', String)
    calle = Column('calle', String)
    ciudad = Column('ciudad', String)
    correo = Column('correo', String)
    nombreusuario = Column('nombreusuario', String)
    __table_args__ = (UniqueConstraint('nombreusuario'),{'sqlite_autoincrement': True}) 


class TacoBD(BD):
    __tablename__ = 'Taco'
    id = Column(Integer, primary_key=True)
    nombre = Column('nombre', String)
    __table_args__ = (UniqueConstraint('nombre'),{'sqlite_autoincrement': True})


class RecetaBD(BD):
    __tablename__ = 'Receta'
    id = Column(Integer, primary_key=True)
    idtaco = Column(Integer, ForeignKey('Taco.id')) #llave foranea "idtaco" que es tomada del "id" de la tabla taco.
    receta = Column('receta', String)
    __table_args__ = (UniqueConstraint('receta'), {'sqlite_autoincrement': True}) #incrementos de Rowid=pseudocolumna unica para cada fila


class VentaBD(BD):
    __tablename__ = 'Venta'
    id = Column(Integer, primary_key=True)
    idusuario = Column(Integer, ForeignKey('Usuario.id')) #llave foranea "idusuario" que es tomada del "id" de la tabla usuario.
    idtaco = Column(Integer, ForeignKey('Taco.id'))  #llave foranea "idtaco" que es tomada del "id" de la tabla taco.
    __table__args = ({'sqlite_autoincrement': True})


engine = create_engine('sqlite:///Taco.db', echo=True) #hace la conexión a la base de datos mediante el archivo
BD.metadata.create_all(bind=engine)    #esta linea genera la base de datos BD
Session = sessionmaker(bind=engine)    #
