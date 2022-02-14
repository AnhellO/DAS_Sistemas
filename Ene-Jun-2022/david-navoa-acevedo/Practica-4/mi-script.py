from faker import Faker

word = Faker()

file = "Ene-Jun-2022/david-navoa-acevedo/Practica-4/README.md"
#new_file = "Ene-Jun-2022/david-navoa-acevedo/Practica-4/README-ALTERADO.md"

with open(file) as opened_file:
    readme = opened_file.readlines()

#for each_line in readme:
#    with open(new_file, 'a') as opened_file:
#        opened_file.write(each_line.rstrip().replace("python", str(word)))

for each_line in readme:
    print(each_line.rstrip().replace("python", str(word)))
