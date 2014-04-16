from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hotelsite.views.home', name='home'),
    url(r'^about/', 'hotelsite.views.about', name='about'),
    url(r'^review/(?P<identifier>\w{0,256})/$', 'hotelsite.views.review', name='review'),
    url(r'^reviews/add', 'hotelsite.views.add_review', name='add_review'),
    url(r'^reviews/', 'hotelsite.views.reviews', name='reviews'),

    url(r'^admin/', include(admin.site.urls)),
)
