import json
import sqlite3

con = sqlite3.connect('users.db')
cursor = con.cursor()

with open('RandomUsers.json') as json_file:
    data = json.load(json_file)
    for result in data['results']:
        if result['gender'] == 'female':
            cursor.execute("insert into Users values ('{}', '{}', 'F', '{}', '{}')".format(result['First'], result['Last'], result['Location'], result['Email']))
        else:
            cursor.execute("insert into Users values ('{}', '{}', 'M', '{}', '{}')".format(result['First'], result['Last'], result['Location'], result['Email']))

con.commit()
con.close()