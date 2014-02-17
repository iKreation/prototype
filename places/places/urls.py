from django.conf.urls import patterns, include, url

urlpatterns = patterns('placesapp.views',
	url(r'^hello/(?P<ident>\d+)/(?P<category>\d+)$','places.hello'),
	url(r'^places/create/$','places.create'),
	url(r'^places/list/$', 'places.list'),
	url(r'^places/get/(?P<ident>\d+)/$','places.get'),
	url(r'^places/update/(?P<ident>\d+)/$','places.update'),
	url(r'^places/delete/(?P<ident>\d+)/$','places.delete')
)

