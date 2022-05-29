import pymongo
import xml.etree.ElementTree as ET

# Creamos conexión a MongoDB
client = pymongo.MongoClient("mongodb://root:ejemplo123@mongo_compose:27017/")
db = client["practica"]
coll = db["people"]

# Leemos archivo XML
tree = ET.parse('people.xml')
people = tree.getroot()
bulk = []
for person in people:
    insert_data = {}
    for data in person:
        if data.tag == 'id':
            insert_data['_id'] = data.text
            continue

        insert_data[data.tag] = data.text
    bulk.append(insert_data)

# Insertamos datos
result = coll.insert_many(bulk)
print(f"¡Se ha terminado la inserción de datos!: {result.inserted_ids}")