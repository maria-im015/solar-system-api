from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
def is_int(value):
    try:
        return int(value)
    except ValueError:
        return False

@planets_bp.route("/<planets_order>", methods=["GET"], strict_slashes=False)
def get_single_planet(planets_order):
    planet = planet
    if not is_int(planets_order):
        return {
            "message": "id must be an integer",
            "success": False
        },400
        
    planet = Planet.query.get(planets_order)
    
    if planet:
        return planet.to_json(), 200
    
    return {
        "message": f"Planet with id {planets_order} was not found",
        "success": False
    }, 404

@planets_bp.route("", methods=["GET"], strict_slashes=False)
def planets_index():
    planets = Planet.query.all()
    planets_response = [] 
    for planet in planets:
        planets_response.append(planet.to_json())
    return jsonify(planet_response), 200

@planets_bp.route("", methods=["POST"], strict_slashes=False)
def planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        order=request_body["order"])

    db.session.add(new_planet)
    db.session.commit()
    
    return {
        "success": True,
        "message": f"Planet {new_planet.name} has been created"
    }, 201