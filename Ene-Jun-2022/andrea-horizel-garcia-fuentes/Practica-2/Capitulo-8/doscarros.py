def make_car(modelo, manofactura, **opciones):
    
    carro_dict = {
        'modelo': modelo.title(),
        'manofactura': manofactura.title(),
        }
    for opciones, value in opciones.items():
        carro_dict[opciones] = value

    return carro_dict

kia = make_car('rio', 'kia', color='rojo',)
print(kia)

ford = make_car('ford', 'figo', color='blanco',)
print(ford)