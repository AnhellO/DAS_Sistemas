from flask import Flask, render_template
from flask_mongoengine import MongoEngine
import os

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_issues',
    'host': 'mongodb',
    'port': 27017,
    'username': "root",
    'password': "mongo"
}

db = MongoEngine()
db.init_app(app)


class issues_short(db.Document):
    number = db.StringField()
    title = db.StringField()
    user = db.StringField()
    state = db.StringField()
    url = db.StringField()


@app.route('/')
def query_records():
    issue_short = issues_short.objects.all()
    return render_template('table_template.html', issue=issue_short)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
