from faker import Faker
import re

original = "Practica-4/README.md"
modified = "Practica-4/README-ALTERADO.md"
new_readme_list = []

with open(original) as file_object:
    for line in file_object:
        faker = Faker()

        while re.search("Python|python", line):
            fake_name = faker.name()
            line = re.sub("Python|python", fake_name, line, 1)

        new_readme_list.append(line)

with open(modified, "w") as f:
    f.writelines(new_readme_list)
