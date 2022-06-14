from fileinput import filename
from faker import Faker
import re


def replace_words(line):
    faker = Faker()

    while re.search("Python|python", line):
        fake_name = faker.name()
        line = re.sub("Python|python", fake_name, line, 1)

    return line


def modify_file_words(filename):
    new_readme_list = []

    with open(filename, "r", encoding="utf-8") as file_object:
        for line in file_object:
            new_line = replace_words(line)
            new_readme_list.append(new_line)

    return new_readme_list


original_readme = "Practica-4/README.md"
modified_readme = "Practica-4/README-ALTERADO.md"
modified_file = modify_file_words(original_readme)

with open(modified_readme, "w", encoding="utf-8") as f:
    f.writelines(modified_file)
