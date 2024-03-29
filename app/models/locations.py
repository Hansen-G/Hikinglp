from .db import db
from sqlalchemy.sql import func

class Location(db.Model):
    __tablename__ = 'locations'
    # Test

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    name = db.Column(db.String(64), nullable=False)
    details = db.Column(db.String(1000), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    preview_img = db.Column(db.String(1000), nullable=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True),
                          nullable=True, server_default=func.now())
    updatedAt = db.Column(db.DateTime(timezone=True),
                          nullable=True, onupdate=func.now())

    user = db.relationship('User', back_populates='posts')
    posts = db.relationship(
        'Post', back_populates='location', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'details': self.details,
            'preview_img': self.preview_img,
            'lat': self.lat,
            'lng': self.lng,
            "user": self.user.to_dict(),
            "posts": [post.to_dict() for post in self.posts]
        }