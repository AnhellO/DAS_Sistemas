### EJERCICIO 2 ###
import json

# Leer el archivo sample.json
with open("sample.json") as json_file:
    sample_json = json.load(json_file)

people = sample_json["people"]["person"]


def show_people_list(people):
    for person in people:
        for attribute, value in person.items():
            print(f"- {attribute}: {value}")

        print("-"*40)


def search_odd_id(people):
    """Imprimir una lista de todas las personas cuyo
    nodo de id ser un número impar."""

    people_odd_id = []

    for person in people:
        person_id = int(person["id"])
        is_odd_person_id = (person_id % 2) != 0

        if is_odd_person_id:
            people_odd_id.append(person)

    return people_odd_id


people_odd_id = search_odd_id(people)
show_people_list(people_odd_id)


def filter_by_company_name(people):
    """Imprimir una lista de todas las personas cuyo nombre de
    la compañía tenga una longitud de entre 4 y 6 letras."""

    filtered_people = []

    for person in people:
        person_company = person["company"]
        lower_interval_bound = len(person_company) >= 4
        upper_interval_bound = len(person_company) <= 6
        is_correct_length = (lower_interval_bound and upper_interval_bound)

        if is_correct_length:
            filtered_people.append(person)

    return filtered_people


filtered_people = filter_by_company_name(people)
show_people_list(filtered_people)


def change_phone_numbers(people):
    """Manipular el contenido del archivo original de tal manera
    que todos los nodos de phone_number ahora sean iguales al
    string XX-XX-XXX y guardar el resultado en un nuevo archivo
    llamado updated.json"""

    for person in people:
        person["phone_number"] = "XX-XX-XXX"

    persons = {}
    people_dict = {}

    persons["person"] = people
    people_dict["people"] = persons

    with open("updated.json", "w") as write_file:
        json.dump(people_dict, write_file)


change_phone_numbers(people)
