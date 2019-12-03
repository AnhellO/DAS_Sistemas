"""6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places."""

favorite_places = {
    'Reynaldo': ['Scalea', 'Real de catorce', 'Pizza Rock'],
    'Rosendo': ['Cine', 'Mazatlan'],
    'Teresa': ['Monterrey', 'Cine', 'Timon']
    }

for name, places in favorite_places.items():
    print("\nA " + name.title() + " le gustan los siguientes lugares:")
    for place in places:
        print("- " + place.title())