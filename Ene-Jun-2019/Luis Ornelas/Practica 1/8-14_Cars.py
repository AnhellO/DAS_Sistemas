def carro(marca,modelo,**argumentos):
    auto = {}
    auto['Marca'] = marca
    auto['Modelo'] = modelo
    for key, value in argumentos.items():
        auto[key] = value
    return auto

argumentos = carro('Honda', 'Civic', Color='Rojo', Puertas=3)

print(argumentos)