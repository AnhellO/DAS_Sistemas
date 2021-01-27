import requests as reqs
import pymongo as mo
import os

c = mo.MongoClient("mongodb://db:27017/")
db = c["mo-data"]
users = []

# get num of users
if os.getenv("NUM_USERS", "").isdigit():	num_users = int(os.environ["NUM_USERS"])
else:										num_users = 0

# fetch all users
for k in range(num_users):
	r = reqs.get("https://pipl.ir/v1/getPerson")
	u = r.json()
	u["position"] = k # add attr

	users.append(u)

# insert into db
db.users.insert_many(users)