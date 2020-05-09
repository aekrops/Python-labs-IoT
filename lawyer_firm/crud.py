from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from lawyer_firm.classes.lawyer import Lawyer

import os
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"]
)

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class VirtualLawyer(Lawyer, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=False)
    age = db.Column(db.Integer, unique=False)
    price_in_uah = db.Column(db.Integer, unique=False)
    have_neural_network = db.Column(db.Boolean, unique=False)

    def __init__(self, name=None, age=None, price_in_uah=None, have_neural_network=None):
        super().__init__(name, age, price_in_uah)
        self.have_neural_network = have_neural_network


class VirtualLawyerSchema(ma.Schema):
    class Meta:
        fields = ('name', 'age', 'price_in_uah', 'have_neural_network')


virtual_lawyer_schema = VirtualLawyerSchema()
virtual_lawyers_schema = VirtualLawyerSchema(many=True)


@app.route("/virtual_lawyer", methods=["POST"])
def add_virtual_lawyer():
    name = request.json['name']
    age = request.json['age']
    price_in_uah = request.json['price_in_uah']
    have_neural_network = request.json['have_neural_network']
    virtual_lawyer = VirtualLawyer(name, age, price_in_uah, have_neural_network)
    db.session.add(virtual_lawyer)
    db.session.commit()
    return virtual_lawyer_schema.jsonify(virtual_lawyer)


@app.route("/virtual_lawyer", methods=["GET"])
def get_virtual_lawyers():
    all_virtual_lawyers = VirtualLawyer.query.all()
    result = virtual_lawyers_schema.dump(all_virtual_lawyers)
    return jsonify({'virtual_lawyers': result})


@app.route("/virtual_lawyer/<id>", methods=["GET"])
def get_virtual_lawyer_by_id(id):
    virtual_lawyer = VirtualLawyer.query.get(id)
    if not virtual_lawyer:
        abort(404)
    return virtual_lawyer_schema.jsonify(virtual_lawyer)


@app.route("/virtual_lawyer/<id>", methods=["PUT"])
def virtual_lawyer_update(id):
    virtual_lawyer = VirtualLawyer.query.get(id)
    if not virtual_lawyer:
        abort(404)
    old_virtual_lawyer = copy.deepcopy(virtual_lawyer)
    virtual_lawyer.name = request.json['name']
    virtual_lawyer.age = request.json['age']
    virtual_lawyer.price_in_uah = request.json['price_in_uah']
    virtual_lawyer.have_neural_network = request.json['have_neural_network']
    db.session.commit()
    return virtual_lawyer_schema.jsonify(old_virtual_lawyer)


@app.route("/virtual_lawyer/<id>", methods=["DELETE"])
def virtual_lawyer_delete(id):
    virtual_lawyer = VirtualLawyer.query.get(id)
    if not virtual_lawyer:
        abort(404)
    db.session.delete(virtual_lawyer)
    db.session.commit()
    return virtual_lawyer_schema.jsonify(virtual_lawyer)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
