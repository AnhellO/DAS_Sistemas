import redis
import lastfmapi
from pylast import *

from app.lastfmAPI import artist
from app.querys import querys


class lastQuerys():

    def __init__(self):
        self.redis_db = redis.StrictRedis(host="lastfmredis", port=6379, db=0, charset="utf-8", decode_responses=True)
        # self.redis_db = redis.StrictRedis(host="localhost", port=6379, db=0, charset="utf-8", decode_responses=True)
        self.query = querys()

    def get_information():
        for i in range(100):
                nombre = artist()
                tracks = tracks()


                print( nombre)

                def existId(self, id):
                    return self.redis_db.sismember('artistIds', id)

                def getartists(self):
                    return self.redis_db.hgetall('artistsIdsNames')

                def getartist(self, id):
                    print("from getartist redis")
                    id_r = "artist:" + str(id)
                    return self.redis_db.hgetall(id_r)

                def setIds(self):
                    print("from setids redis")
                    try:
                        my_set = self.query.getIdsSet()
                        for x in my_set:
                            redis_db.sadd('artistsIds', x)
                        return 0
                    except:
                        return 1

                def setartists(self):
                    print("from setartists redis")
                    try:
                        my_set = self.query.getartists1()
                        redis_db.hmset('artistsIdsNames', my_set)
                        return 0
                    except:
                        return 1

                def setartist(self, id):
                    print("from setartist redis")
                    try:
                        my_set = self.query.getartist(id)
                        id_r = "artist:" + str(my_set['id'])
                        self.redis_db.hmset(id_r, my_set)
                        return 0
                    except:
                        return 1


