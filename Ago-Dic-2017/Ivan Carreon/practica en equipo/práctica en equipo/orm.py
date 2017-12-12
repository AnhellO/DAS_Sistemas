from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import select


BD = declarative_base()

class User(BD):
    __tablename__ = "User"
    nombre = Column('nombre', String)
    biografia = Column('biografia', String)
    comunidades = Column('comunidades',String)
    idusuario = Column('idusuario', String, primary_key=True)
    linkusuario = Column('linkusuario', String)

class Answer(BD):
    __tablename__ = "Answer"
    idrespuesta = Column('id', Integer, primary_key=True)
    respuesta = Column('respuesta', String)
    fecha = Column('fecha', String)
    idusuario = Column('idusuario', String, ForeignKey("User.idusuario"), nullable=False)
    linkrespuesta = Column('linkrespuesta', String)
    idpregunta = Column('idpregunta',String,ForeignKey('Question.idpregunta'), nullable=False)

class Question(BD):
    __tablename__ = "Question"
    idpregunta = Column('idpregunta', String, primary_key=True)
    pregunta = Column('pregunta', String)
    explicacion = Column('explicacion', String)
    userid = Column('userid', String, ForeignKey("User.idusuario"), nullable=False)
    linkpregunta = Column('linkpregunta',String)

class OrmFactory():
    
    def __init__(self):
        self.engine = create_engine('sqlite:///ComunidadStack.db', echo=True)
        self.base = declarative_base()
        self.base.metadata.create_all(bind=engine)
        self.Session = sessionmaker(bind=engine)
        self.session = Session()    
       
    
    def agregaUsuario(self,nombre,biografia,comunidades,idusuario,linkusuario):
        try:
            usuario = User()
            usuario.nombre = nombre
            usuario.biografia = biografia
            usuario.comunidades = comunidades
            usuario.idusuario = idusuario
            usuario.linkusuario = linkusuario
            self.session.add(usuario)
            self.session.commit()
            self.session.close()
        except Exception as inst:
            #~ self.session.close()
            print(inst)
            pass
            
    def agregaRespuesta(self,idpregunta,res,fecha,idusuario,linkrespuesta):
        try:
            respuesta = Answer()
            respuesta.idpregunta = idpregunta
            respuesta.respuesta = res
            respuesta.fecha = fecha
            respuesta.idusuario = idusuario
            respuesta.linkrespuesta = linkrespuesta
            self.session.add(respuesta)
            self.session.commit()
            self.session.close()
        except Exception as inst:
            #~ self.session.close()
            print(inst)
            pass

    def agregaPregunta(self,idpregunta,question,explicacion,userid,linkpregunta):
        try:
            pregunta = Question()
            pregunta.idpregunta = idpregunta
            pregunta.pregunta = question
            pregunta.explicacion = explicacion
            pregunta.userid = userid
            pregunta.linkpregunta = linkpregunta
            self.session.add(pregunta)
            self.session.commit()
            self.session.close()
        except Exception as inst:
            #~ self.session.close()
            print(inst)
            pass
    
engine = create_engine('sqlite:///ComunidadStack.db', echo=True)
#engine = create_engine('sqlite:///Stack.db', echo=True)

BD.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
