import UsersBD

print("---------Seleccione una opción----------\n")
print(('1)Consultar usuarios\n2)Eliminar usuarios\n3)Consultar usuario en específico '))
op = int(input('Escriba un valor: '))

if op == 1:
    UsersBD.VisualizarUsuarios()

if op == 2:
    identificador = input('Escriba el Id del usuario a eliminar: ')
    UsersBD.EliminarUsuario(identificador)

if op == 3:
    identificador = input('Escirba el Id del usuario a consultar: ')
    UsersBD.VisualizarUsuarioPorId(identificador)




