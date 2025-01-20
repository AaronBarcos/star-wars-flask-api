from flask import Blueprint, jsonify
from models import db, Planet

planets_bp = Blueprint('planets', __name__)

@planets_bp.route('/planets', methods=['GET'])
def get_planets():
    
    try:
        all_planets =  Planet.query.all()
        all_planets = [x.serialize() for x in Planet.query.all()]
        return jsonify(all_planets), 200
    
    except Exception as e:
        return jsonify({"msg": e}), 500
    
@planets_bp.route('/planets/<int:id>', methods=['GET'])
def get_planets_by_id(id):
    
    try:
        planet = Planet.query.get(id)
        return jsonify(planet.serialize()), 200
    
    except Exception as e:
        return jsonify({"msg": e}), 500
