import datetime

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/linklog.db'

db = SQLAlchemy(app)

db.create_all()

class Link(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    uri = db.Column(db.String(512), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Link {self.uri}>'


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        db.session.add(Link(uri=request.form['link']))
        db.session.commit()

    links = Link.query.all()
    return render_template('link_list.html', links=links)
