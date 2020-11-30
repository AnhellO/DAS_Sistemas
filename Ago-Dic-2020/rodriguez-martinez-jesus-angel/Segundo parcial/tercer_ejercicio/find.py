import pymongo

client = pymongo.MongoClient("mongodb://172.17.0.2:27017/")

print("##### RECORDS #####")
for hooman in client["mi-db"].hoomans.find():
    print(hooman)