""" Write a function that stores information about a car in a diction-
ary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the func-
tion with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that’s returned to make sure all the information was
stored correctly.
"""

def make_car(manufacturer, model_name, **extras):
    """ Build a dictionary containing everything we know about a car """
    description={}
    description['manufacturer'] = manufacturer.title()
    description['model name'] = model_name.title()
    for key, value in extras.items():
        description[key]= value
    return description


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
