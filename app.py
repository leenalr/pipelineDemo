import os

from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)
# metrics.register_endpoint('/metrics')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('PSQL_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'hi'

db = SQLAlchemy(app)


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.String(120), nullable=False)

    def __init__(self, pname, age):
        self.pname = pname
        self.age = age


@app.route('/')
def home():
    return '<a href="/addperson"><button> Click here </button></a>'


@app.route("/addperson")
def addperson():
    return render_template("index.html")


@app.route("/personadd", methods=['POST'])
def personadd():
    pname = request.form["pname"]
    age = request.form["age"]
    entry = People(pname, age)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")


if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0")
