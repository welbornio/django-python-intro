from django.db import models
from google.appengine.ext import db
from google.appengine.api import users
import webapp2
import datetime


# Create your models here.
class Review(db.Model):
	location 			= db.StringProperty(required=True)
	description 	= db.StringProperty(required=True)
	title 				= db.StringProperty(required=True)
	star_rating 	= db.IntegerProperty(default=0)
	date					= db.DateProperty()
	identifier 		= db.StringProperty()

	meta = {
		'indexes': [
			'location',
			'title',
			'star_rating',
			'id'
		]
	}