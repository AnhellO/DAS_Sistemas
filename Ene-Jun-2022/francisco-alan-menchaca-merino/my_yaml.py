### EJERCICIO 3 ###
import yaml
from yaml import Loader

# Leer el archivo sample.yml
with open("sample.yml") as yaml_file:
    sample_yaml = yaml.load(yaml_file, Loader=Loader)

people = sample_yaml["people"]["person"]


def show_people_list(people):
    for person in people:
        for attribute, value in person.items():
            print(f"- {attribute}: {value}")

        print("-"*40)


def search_three_multiple_id(people):
    """Imprimir una lista de todas las personas cuyo
    nodo de id sea un número múltiplo de 3."""

    people_three_multiple = []

    for person in people:
        person_id = int(person["id"])
        is_multiple_three = (person_id % 3) == 0

        if is_multiple_three:
            people_three_multiple.append(person)

    return people_three_multiple


people_three_multiple = search_three_multiple_id(people)
show_people_list(people_three_multiple)


def filter_by_name(people):
    """Imprimir una lista de todas las personas cuyo nombre
    o apellido tenga una longitud exacta de 5 letras"""

    filtered_people = []

    for person in people:
        fn_is_exactly_five = (len(person["first_name"]) == 5)
        ln_is_exactly_five = (len(person["last_name"]) == 5)
        is_exactly_five = (fn_is_exactly_five or ln_is_exactly_five)

        if is_exactly_five:
            filtered_people.append(person)

    return filtered_people


filtered_people = filter_by_name(people)
show_people_list(filtered_people)


def change_email(people):
    """Manipular el contenido del archivo original de tal manera
    que todos los nodos de email ahora sean iguales al string ---
    y guardar el resultado en un nuevo archivo llamado updated.yml"""

    for person in people:
        person["email"] = "---"

    persons = {}
    people_dict = {}

    persons["person"] = people
    people_dict["people"] = persons

    with open("updated.yaml", "w") as write_file:
        yaml.dump(people_dict, write_file, sort_keys=False)


change_email(people)
