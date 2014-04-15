from django.db import models
# from mongoengine import *
from google.appengine.api import users
import webapp2

class MyHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
        (user.nickname(), users.create_logout_url('/')))
    else:
      greeting = ('<a href="%s">Sign in or register</a>.' %
        users.create_login_url('/'))

      self.response.out.write('<html><body>%s</body></html>' % greeting)

# Create your models here.
# class Review(Document):
# 	location 			= StringField(max_length=256)
# 	description 	= StringField(max_length=1024)
# 	title 				= StringField(max_length=256)
# 	star_rating 	= IntField(default=0)
# 	date					= DateTimeField()

	# meta = {
	# 	'indexes': [
	# 		'location',
	# 		'title',
	# 		'star_rating'
	# 	]
	# }