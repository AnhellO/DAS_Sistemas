from tacoCRUD import Crud
from recetas import Recetas
from Usuarios import Usuario
from time import sleep


class Main():

    def menu(self):
        enter = '''
Taqueria virtual
    1) Comprar un taco.
    2) Consultar ventas.
    3) Consultar menu de tacos.
    4) Consultar Usuarios.
    5) Agregar Taco (con sus respectivas subrecetas).
    6) Agregar Usuario.
    0) Para salir del menú

    >>> '''
        try:
            entrada = int(input(enter))
            print(entrada)
            while entrada != 0:
                entrada = int(input(enter))
                if entrada == 1:
                    self.comprarTaco()
                if entrada == 2:
                    self.consultarVentas()
                if entrada == 3:
                    self.mostrarMenu()
                if entrada == 4:
                    self.consultarUsuarios()
                if entrada == 5:
                    self.nuevoTaco()
                if entrada == 6:
                    self.agregaUsuario()

            print('Fin del programa')

        except:
            self.menu()

    def consultarUsuarios(self):
        c = Crud()
        users = c.getUsuarios()
        for user in users:
            print('ID: {}\nNombre: {}\nApellido: {}\nCalle: {}\nCiudad: {}\nCorreo: {}\nNombre de usuario: {}\n-----------------'.format(
                user.id, user.nombre, user.apellido, user.calle, user.ciudad, user.correo, user.nombreusuario))

    def mostrarMenu(self):
        try:
            c = Crud()
            tacos = c.getTacos()
            i = 1
            for taco in tacos:
                print('===============\nId: {}\n Nombre del taco:\n {}\n===============\n'.format(taco.id, taco.nombre))
                elige_sub = int(input('1: Consultar subrecetas.\n2: Comprar.\n\n'))
                if elige_sub == 1:
                    recetas = c.getRecetas(taco.id)
                    for receta in recetas:
                        print('Subreceta: {}\n'.format(receta.receta))

                    elige_m = int(input('1: Comprar.\n2: Menú principal\n'))
                    if elige_m == 1:
                        self.comprarTaco()
                    if elige_m == 2:
                        break
                if elige_sub == 2:
                    self.comprarTaco()
                i += 1
        except Exception as inst:
            print(inst)

    def nuevoTaco(self): #agrega los tacos a la base de datos utilizando el metodo agregaTaco desde "tacoCRUD"
        try:
            r = Recetas()
            taco = r.getTaco()
            c = Crud()
            c.agregaTaco(taco.nombreTaco)
            tacofromdb = c.getTacoByNombre(taco.nombreTaco)
            recipes = taco.recipes
            for receta in recipes:
                c.agregaReceta(tacofromdb[0].id, receta)
            print('================\nTaco agregado:\n{}\n=============\n'.format(taco.nombreTaco))
        except Exception as inst:
            print(inst)

    def agregaUsuario(self): #Agrega usuarios a la base de datos utilizando el metodo agregarUsuario desde "tacoCRUD"
        try:
            c = Crud()
            usuario = Usuario()
            u = usuario.getUsuarioRandom()
            c.agregaUsuario(u.nombre, u.apellido, u.calle,u.ciudad, u.correo, u.nombreusuario)
            print('==============\nUsuario agregado exitosamente.\n================')
        except Exception as inst:
            print('Algun error en el agregado de usuario?. {}'.format(inst))

    def comprarTaco(self): #Agrega las ventas a la tabla ventas de la base de datos
        try:
            c = Crud()
            idtaco = int(input('Id del taco a comprar\n'))
            iduser = int(input('Id del usuario:\n'))
            sleep(2)
            c.agregaVenta(idtaco, iduser)
            print('=================\nCompra Realizada.\n====================')
        except Exception as inst:
                print('La venta no ha sido satisfactoria {}'.format(inst))

    def consultarVentas(self):
        try:
            c = Crud()
            ventas = c.getVentas()
            for venta in ventas:
                usuario = c.getUsuarioById(venta.idusuario)
                taco = c.getTacoById(venta.idtaco)
                print('==============\nEl usuario {} {} compró:\n{}\n===================\n'.format(usuario[0].nombre, usuario[0].apellido, taco[0].nombre))
        except:
            print('Error al intentar recuperar datos')


if __name__ == "__main__":
    m = Main()
    m.menu()
