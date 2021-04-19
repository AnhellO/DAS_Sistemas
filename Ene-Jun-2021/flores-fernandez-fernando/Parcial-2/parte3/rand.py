import random
import pymongo
import redis
# clase que crea numeros random 
class RandomNumber:
    # genera mil numeros random de entre mil y un millon, los guarda en una lista la cual regresa
    def randNumber():
        randlist = []
        for i in range(1000):
            randlist.append(random.randint(1000,1000000))
        return randlist

    # pide una lista con numero y los divide entre pares e impares, regresa las dos listas 
    def evenOrOdd(randlist):
        evenlist = []
        oddlist = []
        for number in range(0,len(randlist)):
            if(randlist[number]%2 == 0):
                evenlist.append(randlist[number])
            else:
                oddlist.append(randlist[number])
        return evenlist,oddlist

class Connect:
    
    def insertMongo(randlist):
        myclient = pymongo.MongoClient("mongodb://0.0.0.0:27017/")
        mydb = myclient["RandomNumbers"]
        mycol = mydb["EvenNumbers"]
        mongolist =[]
        for number in range(0, len(randlist)):
            row = {'name': randlist[number]}
            mongolist.append(row)
        print(f'Mongo: {len(mongolist)}')
        x = mycol.insert_many(mongolist)  
        
        #for x in mycol.find():
            #print(x)
    
    def insertRedis(randlist):
        r_server = redis.Redis(host = "0.0.0.0",port = 6379)
        r_server.set("name","redis")
        for number in range(0, len(randlist)):
            r_server.rpush("num", randlist[number])
        print(f'Redis: {r_server.llen("number")}')
    
    


def main():
    lrand = RandomNumber.randNumber()
    
    even,odd= RandomNumber.evenOrOdd(lrand)
    Connect.insertMongo(even)
    
    Connect.insertRedis(odd)
 


if __name__ == "__main__":
    main()
