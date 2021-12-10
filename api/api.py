from flask import Blueprint
from .pages.login import login
from .pages.homes import homes


def register_blueprints(app):
	app.register_blueprint(login, url_prefix='/api/login')
	app.register_blueprint(homes, url_prefix='/api/homes')