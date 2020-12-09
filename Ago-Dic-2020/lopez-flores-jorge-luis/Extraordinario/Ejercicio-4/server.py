from flask import Flask
from faker import Faker

server = Flask(__name__)
fake = Faker()

@server.route("/")
def hello():
    return f"Hello {fake.unique.first_name()}!"

if __name__ == "__main__":
   server.run(host='0.0.0.0', port=8000)