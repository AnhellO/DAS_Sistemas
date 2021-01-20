import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["db"]

# Name
print("Nombre de la DB: ", db.name)

# Crea colección e inserta un registro
print(db.pet.insert_many([
    {
        "name": "Frairo",
        "owner": "David",
        "specie": "perro"
    },
    {
        "name": "Princesa",
        "owner": "Keyla",
        "specie": "perra"
    },
    {
        "name": "garfield",
        "owner": "Alejandro",
        "specie": "gato"
    },
    {
        "name": "Pepo",
        "owner": "Giovani",
        "specie": "Cerdo"
    },
    {
        "name": "solovino",
        "owner": "Carlos",
        "specie": "perro"
    },
])) 