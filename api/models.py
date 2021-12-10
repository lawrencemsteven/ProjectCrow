from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_praetorian import Praetorian
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
guard = Praetorian()

owned_homes = db.Table('owned_homes',
	db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
	db.Column('home_id', db.Integer, db.ForeignKey('homes.id'))
)

class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text, unique=True, nullable=False)
	password = db.Column(db.Text, nullable=False)
	is_active = db.Column(db.Boolean, default=True)
	roles = db.Column(db.Text)
	homes = db.relationship("Home", secondary=owned_homes, backref=db.backref('users', lazy='dynamic'))

	def set_password(self, password):
		self.password = guard.hash_password(password)

	@property
	def rolenames(self):
		try:
			return self.roles.split(',')
		except Exception:
			return []

	@classmethod
	def lookup(cls, username):
		return cls.query.filter_by(username=username).one_or_none()

	@classmethod
	def identify(cls, id):
		return cls.query.get(id)

	@property
	def identity(self):
		return self.id

	def is_valid(self):
		return self.is_active


class Home(db.Model):
	__tablename__ = "homes"

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.Text)
	#created = db.Column(db.DateTime, nullable=False)

	def json(self):
		return {'name': self.name}