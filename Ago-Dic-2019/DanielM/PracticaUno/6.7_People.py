# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
# Loop through your list of people. As you loop through the list, print everything you know about each person.

# This is an empty list to store people :v
people = []

# People to add to the list xd
person = {
    'first_name': 'Luis',
    'last_name': 'Tovar',
    'age': 24,
    'city': 'Saltillo',
}
people.append(person)

person = {
    'first_name': 'Carlos',
    'last_name': 'Montes',
    'age': 46,
    'city': 'Saltillo',
}
people.append(person)

person = {
    'first_name': 'Emmanuel',
    'last_name': 'Gaytan',
    'age': 30,
    'city': 'Saltillo',
}
people.append(person)

# Dictionary
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + ", of " + city + ", is " + age + " years old.")