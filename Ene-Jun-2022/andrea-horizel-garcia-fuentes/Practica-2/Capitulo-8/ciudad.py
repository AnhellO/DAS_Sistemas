def describe_city(ciudad, pais='Mexico'):
    
    mensaje = ciudad.title() + " esta en "  + pais.title() + "."
    print(mensaje)

describe_city('Ciudad de Mexico')
describe_city('Es un clima frio')
describe_city('El monumento del angel de la indepencia')