import musicbrainzngs
from artist import artist
from disk import disk

class apiconnection():


    def __init__(self):
        pass

    def searach_Artist_in_Area(self,area,country,tag,limit):#tag=['rock','metal']
        result=musicbrainzngs.search_artists(area=area,country=country,tag=tag,limit=limit)
        return result

    def resultToArtistObj(self,result):
        artis=None
        artists=[]
        for x in result['artist-list']:

            area=x['area']['name']
            name=x['name']
            score=x['ext:score']
            try:
                date=x['life-span']['begin']
                gender=x['gender']
                type=x['type']
            except:
                date="EMPTY"
                gender="EMPTY"
                type="EMPTY"
            artis=artist(area,date,name,gender,type,score)
            artists.append(artis)
        return artists



    def searach_Disc_in_Area_by_Artist(self,artist,country,limit):#tag=['rock','metal']
        result=musicbrainzngs.search_releases(artist=artist, country=country, limit=limit)
        return result

    def resultToDiscObj(self,result):

        artis=None
        dis=None
        co=None
        disks=[]

        for y in result:
            for x in y['release-list']:
                dis=x['artist-credit'][0]['name']
                artis=x['title']
                try:
                    co=x['country']

                except:
                    co="EMPTY"
                dis=disk(dis,artis,co)
                disks.append(dis)


        return disks
