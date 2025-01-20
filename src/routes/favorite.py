from flask import Blueprint, jsonify
from models import db, FavPeople, FavPlanet

favorites_bp = Blueprint('favorite', __name__)

@favorites_bp.route('/favorite/<int:user_id>/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(user_id, planet_id):
    
    try:
        fav_planet = FavPlanet(user_id=user_id, planet_id=planet_id)
        db.session.add(fav_planet)
        db.session.commit()
        return jsonify(fav_planet.serialize()), 201
    
    except Exception as e:
        return jsonify({"msg": e}), 500
    
@favorites_bp.route('/favorite/<int:user_id>/people/<int:people_id>', methods=['POST'])
def add_favorite_people(user_id, people_id):
    
    try:
        fav_people = FavPeople(user_id=user_id, people_id=people_id)
        db.session.add(fav_people)
        db.session.commit()
        return jsonify(fav_people.serialize()), 201
    
    except Exception as e:
        return jsonify({"msg": e}), 500
    
@favorites_bp.route('/favorite/<int:user_id>/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(user_id, planet_id):
    
    try:
        fav_planet = FavPlanet.query.filter_by(user_id=user_id, planet_id=planet_id).first()
        db.session.delete(fav_planet)
        db.session.commit()
        return jsonify(fav_planet.serialize()), 200
    
    except Exception as e:
        return jsonify({"msg": e}), 500
    
@favorites_bp.route('/favorite/<int:user_id>/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(user_id, people_id):
    
    try:
        fav_people = FavPeople.query.filter_by(user_id=user_id, people_id=people_id).first()
        db.session.delete(fav_people)
        db.session.commit()
        return jsonify(fav_people.serialize()), 200
    
    except Exception as e:
        return jsonify({"msg": e}), 500
    