from db import db

class HelloModel(db.Model):
    __tablename__ = 'hellodata'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    place = db.Column(db.String(66))
    number = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)