# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through.
# One key-value pair might be 'nile': 'egypt'.

# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.


rivers = {
            'bravo': 'mexico',
            'nile': 'egypt',
            'mississippi': 'united states',
            'volga': 'russia',
            'danube': 'germany',
         }

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

print("\nThese rivers are included in this dictionary:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThese countries are included in this dictionary:")
for country in rivers.values():
    print("- " + country.title())