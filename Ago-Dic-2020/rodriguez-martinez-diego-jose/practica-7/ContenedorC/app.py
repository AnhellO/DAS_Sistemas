from flask import Flask, render_template
from random import randrange

import view

app = Flask(__name__)

person = ""
name = ""

@app.route('/')
@app.route('/index')
def index():
    try:
        global person
        global name
        
        num = randrange(100)
        person = view.view(num)
        print(person)
        name = person["Personal"]["name"]

        return render_template("index.html", user = name)
    except:
        return render_template("hangInThere.html")

@app.route('/Education')
def education():
    params = {"user": name,
             "certificate": person["Education"]["certificate"],
             "university":  person["Education"]["university"]
            }


    return render_template("Educacion.html", **params)

@app.route('/Personal')
def personal():
    params = {"user": name,
             "age": person["Personal"]["age"],
             "blood":  person["Personal"]["blood"],
             "born_place":  person["Personal"]["born_place"],
             "country":  person["Personal"]["country"],
             "city":  person["Personal"]["city"],
             "last_name":  person["Personal"]["last_name"],
             "gender":  person["Personal"]["gender"],
             "height":  person["Personal"]["height"],
             "weight":  person["Personal"]["weight"],
             "religion":  person["Personal"]["religion"]
            }

    return render_template("Personal.html", **params)

@app.route('/Work')
def work():
    params = {"user": name,
             "position": person["Work"]["position"],
             "salary":  person["Work"]["salary"]
            }

    return render_template("Work.html", **params)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)