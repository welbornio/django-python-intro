from django.shortcuts import render
# from hotelsite.models import Review

# import mongoengine

# Create your views here.
def home(request):
	return render(request, "hotelsite/home.html")


def about(request):
	return render(request, "hotelsite/about.html")


def reviews(request):
	# user = authenticate(username=username, password=password)
	# assert isinstance(user, mongoengine.django.auth.User)

	# reviews = Review.objects().all()
	return render(request, "hotelsite/reviews.html")