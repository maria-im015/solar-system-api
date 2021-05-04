from app import db
from .models.planet import Planet
from flask import request, Blueprint, make_response, jsonify, Response

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
def is_int(value):
    try:
        return int(value)
    except ValueError:
        return False

''' @planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet == None:
        return Response("", status=404) '''

@planets_bp.route("/<planets_id>", methods=["GET"], strict_slashes=False)
def get_single_planet(planets_id):
    
    if not is_int(planets_id):
        return {
            "message": "id must be an integer",
            "success": False
        },400
    
    #handle_planet(planet_id, method=["GET"])
    planet = Planet.query.get(planets_id)
    
    if planet == None:
        return Response("",status=404)
    
    if planet:
        return planet.to_json(), 200
    
    return {
        "message": f"Planet with id {planets_id} was not found",
        "success": False
    }, 404

@planets_bp.route("", methods=["GET"], strict_slashes=False)
def planets_index():
    planets = Planet.query.all()

    planets_response = [] 
    for planet in planets:
        planets_response.append(planet.to_json())
    return jsonify(planets_response), 200

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

@planets_bp.route("/<planet_id>", methods=["PUT"], strict_slashes=False)
def update_planet(planet_id):
    #handle_planet(planet_id, method=["PUT"])
    planet = Planet.query.get(planet_id)
    
    if planet == None:
        return Response("", status=404)
    
    if planet: 
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]

        db.session.commit()

        return Response(f"Planet #{planet.id} successfully updated", status=200)

@planets_bp.route("/<planet_id>", methods=["DELETE"], strict_slashes=False)    
def delete_single_planet(planet_id):
    #handle_planet(planet_id, method=["DELETE"])
    planet = Planet.query.get(planet_id)

    if planet == None:
        return Response("", status=404)

    if planet:
        db.session.delete(planet)
        db.session.commit()
        return Response(f"Planet #{planet.id} successfully deleted", status=200)