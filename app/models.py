# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    poster = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def init(self, title, description, poster, created_at):
        self.title=title
        self.description=description
        self.poster=poster
        self.created_at=created_at
    

    def is_active(self):
        return True


    def repr(self):
        return '<Movie %r>' % (self.title)
