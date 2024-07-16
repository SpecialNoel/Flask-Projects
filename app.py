from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Telling app where the database we intended to use is located
# Here we are using sqlite's test database
# Note that '///' means relateive path, '////' means absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Initialize the database with app
db = SQLAlchemy(app)

class Todo(db.Model):
    # ID column, representing the ids of each entry
    id = db.Column(db.Integer, primary_key=True)    
    # Content column, capped at 200 characters. 
    # This is not nullable, meaning that user cannot leave it blank
    content = db.Column(db.String(200), nullable=False)
    # Datetime column, showing the time the column is created
    date_created = db.Column(db.DateTime, default=datetime.now)
    
    # Return a string of the id that just got created everytime we create a new element
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)