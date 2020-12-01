
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mongo"]

print("##### RECORDS #####")
for hooman in client["mi-db"].hoomans.find():
    print(hooman)