from server.server import db


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, unique=False, nullable=False)
    location = db.Column(db.String(120), unique=True, nullable=False)
    xcoordinate = db.Column(db.Float, unique=False, nullable=False)
    ycoordinate = db.Column(db.Float, unique=False, nullable=False)
    bedrooms = db.Column(db.Integer, unique=True, nullable=False)
    bathrooms = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<listing %r price %r>' % (self.id, self.price)