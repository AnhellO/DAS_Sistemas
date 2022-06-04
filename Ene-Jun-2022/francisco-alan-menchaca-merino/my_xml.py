### EJERCICIO 1 ###
import xml.etree.ElementTree as ET

# Leer el archivo sample.xml
sample_xml_tree = ET.parse('sample.xml')
people = sample_xml_tree.findall("./person")


def show_people_list(people):
    for person in people:
        for person_var in person:
            print(f"- {person_var.tag}: {person_var.text}")

        print("-"*40)


def search_even_id(people):
    """Imprimir una lista de todas las personas cuyo
    nodo de id ser un número par."""

    people_even_id = []

    for person in people:
        person_id = int(person.find("id").text)
        is_even_person_id = (person_id % 2) == 0

        if is_even_person_id:
            people_even_id.append(person)

    return people_even_id


people_even_id = search_even_id(people)
show_people_list(people_even_id)


def search_by_email_domain(people):
    """Imprimir una lista de todas las personas cuyo correo
    electrónico tengo el dominio .edu o .gov"""

    people_edu_gov_emails = []

    for person in people:
        person_email = person.find("email").text
        email_contains_edu = ".edu" in person_email
        email_contains_gov = ".gov" in person_email
        is_email_edu_gov = (email_contains_edu) or (email_contains_gov)

        if is_email_edu_gov:
            people_edu_gov_emails.append(person)

    return people_edu_gov_emails


people_emails = search_by_email_domain(people)
show_people_list(people_emails)


def change_ip_address(tree):
    """Manipular el contenido del archivo original de tal manera
    que todos los nodos de ip_address ahora sean iguales a la IP 127.0.0.1
    y guardar el resultado en un nuevo archivo llamado updated.xml"""

    tree_root = tree.getroot()

    for person_ip in tree_root.iter("ip_address"):
        person_ip.text = "127.0.0.1"

    tree.write("updated.xml")

change_ip_address(sample_xml_tree)
