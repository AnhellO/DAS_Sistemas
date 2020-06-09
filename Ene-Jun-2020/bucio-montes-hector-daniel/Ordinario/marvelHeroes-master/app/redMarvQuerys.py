import redis
from querys import *
class redMarQuerys():

    
    def __init__(self):
        self.redis_db = redis.StrictRedis(host="marvelRedis_E", port=6379, db=0, charset="utf-8", decode_responses=True)
        #self.redis_db = redis.StrictRedis(host="localhost", port=6379, db=0, charset="utf-8", decode_responses=True)
        self.query=querys()

    def existId(self,id):
        return self.redis_db.sismember('herosIds',id)

    def getHeroes(self):
        return self.redis_db.hgetall('heroesIdsNames')

    def getHero(self,id):
        print("from gethero redis")
        id_r="hero:"+str(id)
        return self.redis_db.hgetall(id_r)

    def setIds(self):
        print("from setids redis")
        try:
            my_set=self.query.getIdsSet()
            for x in my_set:
                redis_db.sadd('herosIds',x)
            return 0
        except:
            return 1

    def setHeros(self):
        print("from setheros redis")
        try:
            my_set=self.query.getHeroes1()
            redis_db.hmset('heroesIdsNames',my_set)
            return 0
        except:
            return 1

    def setHero(self, id):
        print("from sethero redis")
        try:
            my_set=self.query.getHero(id)
            id_r="hero:"+str(my_set['id'])
            self.redis_db.hmset(id_r,my_set)
            return 0
        except:
            return 1
  

