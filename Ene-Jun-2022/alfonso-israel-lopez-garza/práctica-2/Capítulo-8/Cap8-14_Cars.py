def make_car(model_name,manufacturer,**information):
    '''crea un diccionario con la informacion del carro.'''
    carro = {}
    carro['Manufacturer'] = manufacturer
    carro['Model_Name'] = model_name
    for key, value in information.items():
        carro[key] = value

    return carro

car = make_car('Subaru','outback',color ='blue',two_package = True)
print(car)