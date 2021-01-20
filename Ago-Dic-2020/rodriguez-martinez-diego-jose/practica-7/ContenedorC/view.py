import pymongo

def view(random_number: int) -> dict:
    client = pymongo.MongoClient("mongodb://mongo:27017/")
    db = client["mi-db"]

    return db.person.find_one({"id": random_number})