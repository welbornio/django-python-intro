from django.shortcuts import render
from hotelsite.models import Review
from django.shortcuts import redirect
from google.appengine.ext import db

import datetime
import logging
import random

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
	return render(request, "hotelsite/home.html")


def about(request):
	return render(request, "hotelsite/about.html")

def review(request, identifier):
	reviews = db.GqlQuery("SELECT * FROM Review WHERE identifier = :1", identifier)
	logging.info("The id is: " + identifier)
	return render(request, "hotelsite/review.html", {'reviews': reviews})

def reviews(request):
	reviews = db.GqlQuery("SELECT * FROM Review ORDER BY date")
	return render(request, "hotelsite/reviews.html", {'reviews': reviews})

def add_review(request):
	if request.method == 'POST':
		items = request.POST
		r = Review(location=items['location'], description=items['review'], title=items['title'], star_rating=int(items['stars']))
		r.date = datetime.datetime.now().date()
		r.identifier = str(random.getrandbits(32))
		r.put()
		return redirect('/reviews')
	else:
		return render(request, 'hotelsite/add_review.html')