from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


class Link(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(80))
    url = db.Column(db.String(80))

    def __init(self,name,url):
        self.name = name
        self.url = url

    def __repr__(self):
        return 'Url - {}'.format(self.url)


class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.String(20))
    spec_id = db.Column(db.Integer(), db.ForeignKey('specs.id'))


class Specs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spec_name = db.Column(db.String(20))
    spec_desc = db.Column(db.Text)
    heroes = db.relationship('heroes', backref='spec')


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20))
