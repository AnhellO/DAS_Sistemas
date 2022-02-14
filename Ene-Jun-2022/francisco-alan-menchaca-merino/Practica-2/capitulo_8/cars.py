""" 8-14. Cars: Write a function that stores information about a car in a
dictionary. The function should always receive a manufacturer and a model name.
It should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a color
or an optional feature. Your function should work for a call like this one: 
car = make_car('subaru', 'outback', color='blue', tow_package=True).
Print the dictionary that's returned to make sure all the information
was stored correctly. """


def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model_name'] = model

    for key, value in car_info.items():
        car[key] = value

    return car


subaru_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(subaru_car)

bmw_car = make_car('bmw', 'z4', color='black', fuel_tank="52 L")
print(bmw_car)

bmw_car = make_car('tesla', 's', color='red ', power="1,020 hp")
print(bmw_car)
# {'manufacturer': 'subaru', 'model_name': 'outback', 'color': 'blue', 'tow_package': True}
# {'manufacturer': 'bmw', 'model_name': 'z4', 'color': 'black', 'fuel_tank': '52 L'}
# {'manufacturer': 'tesla', 'model_name': 's', 'color': 'red ', 'power': '1,020 hp'}
