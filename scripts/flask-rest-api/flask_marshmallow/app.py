import os

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "test.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# constructor
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Product Model -> SQLAlchemy
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

    def __repr__(self):
        return f"Product: {self.name}"


# Marshmallow schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "price", "qty")


# init the ma.Schema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)


@app.route("/")
def hello_world():
    return jsonify({"msg": "Hello World"})


# Add new product
@app.route("/product", methods=["POST"])
def add_product():
    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    qty = request.json["qty"]

    new_product = Product(name, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


# update product
@app.route("/product/<prod_id>", methods=["PUT"])
def put(prod_id):
    product = Product.query.get(prod_id)
    if product:
        name = request.json["name"]
        description = request.json["description"]
        price = request.json["price"]
        qty = request.json["qty"]

        product.name = name
        product.description = description
        product.price = price
        product.qty = qty

        db.session.commit()
        return product_schema.jsonify(product)
    return abort(404)


# get all products
@app.route("/product", methods=["GET"])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result.data)


# get one product
@app.route("/product/<product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.query.get(product_id)
    # result = product_schema.dump(product) # method 1
    # return jsonify(result.data)           # method 1
    return product_schema.jsonify(product)  # method 2


# delete product
@app.route("/product/<prod_id>", methods=["DELETE"])
def delete(prod_id):
    product = Product.query.get(prod_id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)


if __name__ == "__main__":
    app.run(debug=True)
