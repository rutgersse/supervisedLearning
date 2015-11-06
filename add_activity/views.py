from django.shortcuts import render
from django.http import HttpResponse
from add_activity.forms import *
from add_activity.models import *
def leaderboard (request):
	"""
	Functiona Name : leaderboard
	Args : request
	Return : leader board
	"""
	location_list = Location.objects.order_by('-vote_count')[:10]
	return render( request, 'leaderboard.html', locals() )

def add_activity(request):
	if request.method == 'POST':
		form = askAct(request.POST)
		if form.is_valid():
			form = askAct()
	else:
		form = askAct()


	return render(request,'addActivity.html',locals())	

def add_team(request):
	if request == 'POST':
		form = askTeam(request.POST)
		if form.is_valid():
			forminfo.object.create(ask_activity = form.cleaned_data['ask_activity'])
			form = askTeam()
			return render(request,'addTeam.html',local())
		else:
			form = askAct()
			return render(request,'addActivity.html',locals())
	else:
		form = askAct()
		return render(request,'addActivity.html',locals())

