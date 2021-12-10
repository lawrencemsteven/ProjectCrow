from flask import Blueprint, request, jsonify
from flask_praetorian import auth_required, current_user
from datetime import datetime, timedelta
from ..models import db, User, Home

homes = Blueprint("homes", __name__)


@homes.route("/", methods=["GET", "POST"])
@auth_required
def get_moods():
	user = current_user()

	all_homes = []
	for home in user.homes:
		all_homes.append(home.json())
	
	return jsonify({"homes": all_homes})