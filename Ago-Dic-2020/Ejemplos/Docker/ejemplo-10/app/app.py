from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    name = request.form['name'] if request.method == 'POST' and 'name' in request.form else 'Anonymous'
    return render_template('hello.html', name=name)
