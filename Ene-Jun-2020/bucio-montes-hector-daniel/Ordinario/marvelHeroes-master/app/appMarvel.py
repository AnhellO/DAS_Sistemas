from flask import Flask, render_template
from peewee import *
from playhouse.shortcuts import model_to_dict
from modelsMarvel import *
from querys import *
from redMarvQuerys import *
import time

app = Flask(__name__, static_url_path='/static')
query=querys()
queryR=redMarQuerys()


@app.route('/')
def index():
    
    if(queryR.redis_db.ping()):
        if(queryR.redis_db.exists('heroesIdsNames')):
            heros=queryR.getHeroes()
        else:
            if (queryR.redis_db.info()['loading']==0):
                if((queryR.setHeros())==0):
                    heros=queryR.getHeroes()
                else:
                    heros=query.getHeroes1()  
            # query
            else:
                heros=query.getHeroes1()
    else:
        heros=query.getHeroes1() 

    return render_template('index.html',heroes =heros)

@app.route('/hero/<string:idHero>')
def heroById(idHero):
    if(idHero.isdigit()):
        if(0<int(idHero)<735):
            idExists=False
            if(queryR.redis_db.ping()):
                if(queryR.redis_db.exists('herosIds')):
                    idExists=queryR.existId(idHero)
                else:
                    if (queryR.redis_db.info()['loading']==0):
                        if(queryR.setIds()==0):
                            idExists=queryR.existId(idHero)
                        else:
                            idExists=query.existId(idHero)  
                    else:
                        idExists=query.existId(idHero)
            else:
                idExists=query.existId(idHero)         

            if(idExists):
                if(queryR.redis_db.ping()):
                    if(queryR.redis_db.exists('hero:'+str(idHero))):
                        hero=queryR.getHero(idHero)
                    else:
                        if (queryR.redis_db.info()['loading']==0):
                            if(queryR.setHero('hero:'+str(idHero))==0):
                                hero=queryR.getHero(idHero)
                            else:
                                hero=query.getHero(idHero)  
                        else:
                            hero=query.getHero(idHero)
                else:
                    hero=query.getHero(idHero)      
                try:    
                    if(len(hero) >0):
                        hero=query.heroToSchema(hero)
                        return render_template('hero.html',hero =hero)
                except:
                    return "<h2>something has gone wrong</h2>"
    return render_template('heroNotFound.html',  id_Hero=idHero)


@app.route('/test')
def test():

    print("STARTING TESTS ...")

    id_test=732
    range_test=735

    #pruebas a postgres

    start=time.time()
    query.existId(id_test)
    elapsedDB1 = time.time() - start

    start=time.time()    
    heros=query.getHeroes1()
    elapsedDB2 = time.time() - start

    start=time.time()    
    hero=query.getHero(id_test) 
    elapsedDB3 = time.time() - start

    start=time.time()
    for i in range(range_test):    
        hero=query.getHero(i) 
    elapsedDB4 = time.time() - start

    res1=[elapsedDB1,elapsedDB2, elapsedDB3, elapsedDB4 ]

     #pruebas a redis

    start=time.time()
    queryR.existId(id_test)
    elapsedRD1 = time.time() - start

    start=time.time()    
    heros=queryR.getHeroes()
    elapsedRD2 = time.time() - start

    start=time.time()    
    hero=queryR.getHero(id_test) 
    elapsedRD3 = time.time() - start   

    start=time.time()
    for i in range(range_test):    
        hero=queryR.getHero(i) 
    elapsedRD4 = time.time() - start
       
    res2=[elapsedRD1,elapsedRD2, elapsedRD3, elapsedRD4 ]
    strings=["TEST EXIST ID","TEST GET HEROES IDS NAMES", "TEST GET HERO", "TEST GET ALL FROM HEROES" ]   

    print("END TESTS ...")    

    return render_template('test.html',  stringst=strings, res1t=res1, res2t=res2, ranget=range_test, idt=id_test )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    psql_db.close()
