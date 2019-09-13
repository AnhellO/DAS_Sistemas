favorite_places = {
    'Juan': ['Mexico', 'EUA', 'España'],
    'Diego': ['Italia', 'Canada','Peru'],
    'Pedro': ['Alaska', 'Egipto', 'Inglaterra']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " Le gustan estos lugares:")
    for place in places:
        print("- " + place.title())