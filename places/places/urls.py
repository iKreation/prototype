from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('placesapp.views',
	#url(r'^hello/(?P<ident>\d+)/(?P<category>\d+)$','places.hello'),
	url(r'^places/(?P<ident>\d+)/$','places.rest'),

	#url(r'^places/create/$','places.create'),
	#url(r'^places/list/$', 'places.list'),
	#url(r'^places/get/(?P<ident>\d+)/$','places.get'),
	#url(r'^places/update/(?P<ident>\d+)/$','places.update'),
	#url(r'^places/delete/(?P<ident>\d+)/$','places.delete')
) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)