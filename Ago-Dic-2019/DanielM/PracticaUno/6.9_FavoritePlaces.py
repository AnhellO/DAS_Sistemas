# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in
# the dictionary, and store one to three favorite places for each person.
# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places.
# Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    'Daniel': ['Piste', 'Monterrey', 'Cancun'],
    'Carlos': ['Guadalajara', 'Acapulco', 'Guanajuato'],
    'Luis': ['Los Cabos', 'San Luis', 'CDMX']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes these places:")
    for place in places:
        print("- " + place.title())