from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from placesapp.models import *

def hello(request, ident, category):
	obj = {} # create dict
	obj['ident'] = ident # set value of ident
	obj['cenas'] = 'QUALQUER COISA'
	obj['category'] = category

	t = loader.get_template('hello_world.html')
	return HttpResponse(t.render(RequestContext(request, obj)))

def list(request):
	# import model
	# make the query to get all the places
	# load the view 
	# render the view with the query object
	# return http response

	query = Places.objects.all()
	obj = {}
	obj['query'] = query

	t = loader.get_template('list_view.html')
	return HttpResponse(t.render(RequestContext(request, obj)))


def create(request):
	# grant it's a post
	# read the POSTed data
	# create the object to send to the model

	if request.method == 'POST':
		title = request.POST['title']
		description = request.POST['description']
		coordinate = request.POST['coordinate']

		try:
			Places.objects.create(user_id = 1,
								  title = title, 
								  description = description, 
								  coordinate = coordinate)

			return HttpResponseRedirect('/')
		except:
			return HttpResponseRedirect('/')

	else:
		return HttpResponseRedirect('/')

def get(request,ident):
	pass

def update(request, ident):
	pass

def delete(request, ident):
	pass
