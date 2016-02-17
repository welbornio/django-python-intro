from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hotelsite.views.home', name='home'),
    url(r'^about/', 'hotelsite.views.about', name='about'),
    url(r'^reviews/', 'hotelsite.views.reviews', name='reviews'),

    url(r'^admin/', include(admin.site.urls)),
)
