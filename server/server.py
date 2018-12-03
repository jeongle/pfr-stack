from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://Jeongdizzle@localhost:5432/practice'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, unique=False, nullable=False)
    location = db.Column(db.String(120), unique=False, nullable=False)
    xcoordinate = db.Column(db.Float, unique=False, nullable=False)
    ycoordinate = db.Column(db.Float, unique=False, nullable=False)
    bedrooms = db.Column(db.Integer, unique=False, nullable=False)
    bathrooms = db.Column(db.Integer, unique=False, nullable=False)


@app.route("/hello")
def hello():
    return "hi"

@app.route("/listings")
def showListings():
    listings = Listing.query.all()
    listingList = []
    for entry in listings:
        listing = {}
        listing['id'] = entry.id
        listing['price'] = entry.price
        listing['location'] = entry.location
        listing['xcoordinate'] = entry.xcoordinate
        listing['ycoordinate'] = entry.ycoordinate
        listing['bedrooms'] = entry.bedrooms
        listing['bathrooms'] = entry.bathrooms
        listingList.append(listing)

    return jsonify(listingList)

@app.route("/rawlistings")
def showListingsRaw():
    query = 'SELECT * FROM listing'
    listings = db.engine.execute(query)
    listings=list(listings)
    return json.dumps(listings)
  
@app.route("/listings2")
def showListings2():
    listings = Listing.query.first()
    return jsonify(listings)