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
