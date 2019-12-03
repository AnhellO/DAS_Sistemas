"""6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person."""

people = []

person = {
    'first_name': 'Teresa',
    'last_name': 'Guadalupe',
    'age': 28,
    'city': 'San Luis Potosi',
}
people.append(person)

person = {
    'first_name': 'Reynaldo',
    'last_name': 'Rodriguez',
    'age': 19,
    'city': 'Saltillo',
}
people.append(person)

person = {
    'first_name': 'Teresa',
    'last_name': 'Pardo',
    'age': 50,
    'city': 'Saltillo',
}
people.append(person)


for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + ", of " + city + ", is " + age + " years old.")