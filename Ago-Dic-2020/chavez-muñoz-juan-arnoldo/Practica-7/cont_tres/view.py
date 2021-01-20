from flask import Flask
from flask import render_template
from random import randrange
import pymongo 
import time

app = Flask(__name__)

@app.route("/")
def index():
    #time.sleep(45)
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mi-db"]
    number = randrange(0, 100)
    count = 1
    for person in db.Persons.find():
        if count == number:
            return render_template("index.html", person = person)
        else:
            count += 1
    #return render_template("index.html")
    
    #return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True, port=5000)