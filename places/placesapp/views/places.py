from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from placesapp.models import *
import simplejson as json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


def index(request):
	return render(request,'index.html')

@csrf_exempt
def rest(request, ident):
	if request.method == 'GET':
		if int(ident) == 0:
			return places_list(request)
		else:
			return get(request, ident)
	elif request.method == 'POST' or request.method == 'PUT':
		if int(ident) == 0:
			return create(request)
		else:
			return update(request, ident)
	elif request.method == 'DELETE':
		return delete(request, ident)
	else:
		return HttpResponse(json.dumps({
									'success': False, 
									'msg': 'Invalid request method.'
								}), content_type='json')


def places_list(request):
	# import model
	# make the query to get all the places
	# load the view 
	# render the view with the query object
	# return http response

	query = Places.objects.all()
	lista = []

	for l in query:		
		new_obj = {}
		new_obj['title'] = l.title
		new_obj['description'] = l.description
		new_obj['coordinate'] = l.coordinate
		lista.append(new_obj)

	return HttpResponse(json.dumps(lista), content_type='json')

@csrf_exempt
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

			return HttpResponse(json.dumps({
									'success': True, 
									'msg': 'Success'
								}), content_type='json')
		except:
			return HttpResponse(json.dumps({
									'success': False, 
									'msg': 'An error has occurred.'
								}), content_type='json')
	else:
		return HttpResponse(json.dumps({
									'success': False, 
									'msg': 'Invalid request method.'
								}), content_type='json')

def get(request,ident):
	# query the database with ident 
	# verify if exists
	# json

	try:
		p = Places.objects.get(id = ident)
		obj = {}
		obj['id'] = p.id
		obj['title'] = p.title
		return HttpResponse(json.dumps(obj), content_type="json")
	except:
		return HttpResponse(json.dumps({
									'success': False, 
									'msg': 'Does not exist.'
								}), content_type='json')

@csrf_exempt
def update(request, ident):
	# find the object and check if exists
 	# update the object

 	if request.method == 'PUT':
 		title = request.PUT['title']
		description = request.PUT['description']
		coordinate = request.PUT['coordinate']

 	elif request.method == 'POST':
 		title = request.POST['title']
		description = request.POST['description']
		coordinate = request.POST['coordinate']

 	try:
 		p = Places.objects.get(id = ident)
 		p.title = title
 		p.description = description
 		p.coordinate = coordinate
 		p.save()

 		return HttpResponse(json.dumps({'success': True}), 
 				content_type="json")
 	except:
 		return HttpResponse(json.dumps({
								'success': False, 
								'msg': 'Does not exist.'
							}), content_type='json')

def delete(request, ident):
	try:
		p = Places.objects.get(id = ident)
		p.delete()

		return HttpResponse(json.dumps({'success': True}), 
	 				content_type="json")
	except:
 		return HttpResponse(json.dumps({
								'success': False, 
								'msg': 'Does not exist.'
							}), content_type='json')


