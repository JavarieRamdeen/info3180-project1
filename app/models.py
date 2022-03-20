from . import db
from werkzeug.security import generate_password_hash

class properties(db.Model):
    __tablename__ = 'properties'

    property_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.Integer)
    type = db.Column(db.String(80))
    title = db.Column(db.String(80))
    description= db.Column(db.String(1000))
    photo = db.Column(db.String(80))

    def __init__(self, property_id, title, bedrooms, bathrooms, location, price, type, description, photo):

        self.property_id = property_id
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo = photo

    def get_id(self):
        return str(self.property_id)  # python 3 support