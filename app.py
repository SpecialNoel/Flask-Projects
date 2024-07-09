# app.py

import re
from datetime import datetime
from flask import Flask
from flask import render_template

# app.py is the default file that Flask's development server uses
# To use a filename other than app.py, you will need to define an environment variable 
#   named FLASK_APP and set its value to your chosen file. 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template(
        'hello.html',
        name=name,
        date=datetime.now()
    );

@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')

