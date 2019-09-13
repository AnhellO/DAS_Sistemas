from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import select
from dbTaco import UsuarioBD, RecetaBD, TacoBD, VentaBD
import logging


class Crud():
    def __init__(self):
        logging.basicConfig()
        logging.getLogger('sqlalchemy').setLevel(logging.ERROR)
        self.engine = create_engine('sqlite:///Taco.db') #conexion a la base de datos
        self.base = declarative_base()  #Se crea una instancia de MetaData si no se proporciona ninguna.
        self.base.metadata.create_all(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def agregaUsuario(self, nombre, apellido, calle, ciudad, correo, nombreusuario):
        try:
            usuario = UsuarioBD()
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.calle = calle
            usuario.ciudad = ciudad
            usuario.correo = correo
            usuario.nombreusuario = nombreusuario
            self.session.add(usuario) #mantiene el objeto en la sesion
            self.session.commit()
            self.session.close()
        except Exception as inst:
            print(inst)

    def getUsuarios(self):
        users = []
        for usuario in self.session.query(UsuarioBD):
            users.append(usuario)
        return users

    def getUsuarioById(self, id):
        users = self.session.query(UsuarioBD).filter_by(id=id)
        return users


##########################################################################################
    def agregaReceta(self, idtaco, recipe):
        try:
            receta = RecetaBD()
            receta.idtaco = idtaco
            receta.receta = recipe
            self.session.add(receta)
            self.session.commit()
            self.session.close()
        except Exception as inst:
            print(inst)

    def getRecetas(self, idtaco):
        recetas = self.session.query(RecetaBD).filter_by(idtaco=idtaco)
        return recetas

############################################################################################
    def agregaTaco(self, nombre):
        try:
            taco = TacoBD()
            taco.nombre = nombre
            self.session.add(taco)
            self.session.commit()
            self.session.close()
        except Exception as inst:
            print(inst)

    def getTacos(self):
        taco = self.session.query(TacoBD) #devuelve un objeto consulta como un "select" generado por el ORM 
        return taco

    def getTacoById(self, idt):
        taco = self.session.query(TacoBD).filter_by(id=idt) #objeto filtrado por "idt"
        return taco

    def getTacoByNombre(self, nombre):
        taco = self.session.query(TacoBD).filter_by(nombre=nombre) #objeto filtrado por "nombre"
        return taco

#############################################################################################        

    def agregaVenta(self, idtaco, idusuario):
        try:
            venta = VentaBD()
            venta.idtaco = idtaco
            venta.idusuario = idusuario
            self.session.add(venta)
            self.session.commit()
            self.session.close()
        except Exception as inst:
            print(inst)

    def getVentas(self):
        ventas = self.session.query(VentaBD)
        return ventas

   



