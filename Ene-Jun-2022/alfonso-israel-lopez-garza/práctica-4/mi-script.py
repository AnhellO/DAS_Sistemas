from faker import Faker
newfile = 'README-ALTERADO.md'
faker = Faker()


def archivo(filename):
    with open(filename) as f_obj:
        lines = f_obj.readlines()

    for line in lines:
        line.replace('Python' or 'python',faker.word())

    with open(newfile,'a') as f_obj:
        for line in lines:
            f_obj.write(line)


    with open(newfile) as file_object:
        contents = file_object.read()
    print(contents.rstrip())


filename = 'README.md'
archivo(filename)