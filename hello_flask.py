from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/ktuite/Desktop/shdh/cats.db'
db = SQLAlchemy(app)

### Models ###
class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    color = db.Column(db.String)

    def __init__(self, name, color):
        self.name = name
        self.color = color


### Routes ###
@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/cats/", methods=['GET', 'POST'])
def cats():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['color']
        cat = Cat(name, color)
        db.session.add(cat)
        db.session.commit()

    cats = Cat.query.all()
    return render_template('cats.html', cats=cats)

if __name__ == "__main__":
    app.run(debug=True)

def setup():
    db.create_all()
    mpeg = Cat("MPEG", "calico")
    db.session.add(mpeg)
    db.session.commit()
    for cat in Cat.query.all():
        print "cat in database: %d) %s - %s" % (cat.id, cat.name, cat.color)