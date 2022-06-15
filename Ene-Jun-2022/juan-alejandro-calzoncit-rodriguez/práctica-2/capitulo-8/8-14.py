def make_car(manufacturer, model_name, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model_name'] = model_name

    for key, value in car_info.items():
        car[key] = value

    return car


car = make_car('Subaru', 'Wrx STI', color = 'black', tow_package =True)
print(car)