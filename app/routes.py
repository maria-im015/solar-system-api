from flask import Blueprint

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("/<planets_order>", methods=["GET"], strict_slashes=False)
def get_single_planet(planets_order):
    planet = planet
