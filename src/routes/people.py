from flask import Blueprint, jsonify
from models import db, People

people_bp = Blueprint('people_bp', __name__)

@people_bp.route('/people', methods=['GET'])
def get_people():
    
    try:
        all_people =  People.query.all()
        all_people = [x.serialize() for x in People.query.all()]
        return jsonify(all_people), 200
    
    except Exception as e:
        return jsonify({"msg": e}), 500
    
@people_bp.route('/people/<int:id>', methods=['GET'])
def get_people_by_id(id):
    
    try:
        person = People.query.get(id)
        return jsonify(person.serialize()), 200
    
    except Exception as e:
        return jsonify({"msg": e}), 500
