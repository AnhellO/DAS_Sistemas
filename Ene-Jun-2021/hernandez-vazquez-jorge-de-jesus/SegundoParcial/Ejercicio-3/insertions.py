import redis
import json
                        #ip-container
rediss = redis.Redis(host='172.22.0.2',port=6379)

with open("mock_data.json", "r") as datass:
    e = json.load(datass)
    if e == None or e == "":
        print( "Nothing here")
    else:
        for index in e:
            a = index["id"]
            b = index["first_name"]
            c = index["last_name"]
            d = str(a) +"-"+ str(b) +"-"+ str(c) 
               
            rediss.set(d, "'"+str(index)+"'")
        print("SUCCESS")
 