from flask import Blueprint, jsonify
from models import db, User, FavPeople, FavPlanet

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    
    try:
        all_users =  User.query.all()
        all_users = [x.serialize() for x in User.query.all()]
        return jsonify(all_users), 200
    
    except Exception as e:
        return jsonify({"msg": e}), 500

@users_bp.route('/users/<int:id>', methods=['GET'])
def get_users_by_id(id):
    
    try:
        user = User.query.get(id)
        return jsonify(user.serialize()), 200
    
    except Exception as e:
        return jsonify({"msg": e}), 500

@users_bp.route('/users/<int:id>/favorites', methods=['GET'])
def get_favorites(id):

    try:
        fav_people = FavPeople.query.filter_by(user_id=id)
        fav_people = [x.serialize() for x in fav_people]

        fav_planet = FavPlanet.query.filter_by(user_id=id)
        fav_planet = [x.serialize() for x in fav_planet]

        return jsonify({"fav_people": fav_people, "fav_planet": fav_planet}), 200

    except Exception as e:
        return jsonify({"msg": e}), 500