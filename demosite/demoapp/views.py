# File: views.py
# Group: 12 (Team Intrinsic)
# Members: Kevin Mann, Derek Fong, Allison Ng
# CMPT470: Technical Evaluation
#
# Date of Creation: Feb 22, 2012
# Revised: Feb 24, 2012
#
# Description: Defines the views (controllers) required for each page

from django.shortcuts import render_to_response, get_object_or_404
from demoapp.models import Choice, Poll, Voted
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from forms import RegisterForm
from django.contrib import auth
import datetime

# The default view for the polls application
# - Gets the five newest polls ordered by pub_date 
# - Sends the latest_poll_list array and sends it to the polls.html template
def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	return render_to_response('polls.html', {'latest_poll_list': latest_poll_list},
					context_instance=RequestContext(request))

# The main view for each poll
# - gets the poll using GET and if the poll doesn't exist, output an HTTP 404 error.
# - pollCheck checks to see whether or not the user has voted for that particular poll
# - Sends the poll and pollCheck to the detail.html template and renders to the viewer
def detail(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	user = request.user
	pollCheck = Voted.objects.filter(pollNumber=poll_id, userNumber=user.id).count()
	return render_to_response('detail.html', {'poll': p, 'pollCheck': pollCheck},
					context_instance=RequestContext(request))

# The view for each poll's results page
# - gets the poll using GET and if the poll doesn't exist, output an HTTP 404 error.
# - sends the poll to the results.html template and renders to the viewer
def results(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('results.html', {'poll': p},
					context_instance=RequestContext(request))

# The view to run the voting operations
# - gets the poll using GET and if the poll doens't exist, output an HTTP 404 error.
# - otherwise, sends an error message and the poll to detail.html and renders to the viewer.
# - if it is successful, incremend the number of votes and go back to results view.
def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render_to_response('detail.html', {
			'poll': p,
			'error_message': "You didn't select a choice.",
		}, context_instance = RequestContext(request))
	else:
		user = request.user
		user_voted = Voted(pollNumber=p.id, userNumber=user.id, vote_time=datetime.datetime.now())
		user_voted.save()
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('demoapp.views.results', args=(p.id,)))

# The view for user registration
# - if the request is an HTML POST request, process the user registration and redirect to home page.
# - other wise, send the registration form to the register.html template
def register(request):
	if request.method == 'POST':
		regForm = RegisterForm(request.POST)
		if regForm.is_valid():
			new_user = regForm.save()
			return HttpResponseRedirect("/")
	else:
		regForm = RegisterForm()

	return render_to_response("register.html", {'regForm': regForm },
					context_instance=RequestContext(request))

#The view for the logout operation
# - processes the logout operation and redirect to the main page.
def logout_view(request):
	auth.logout(request)
	return HttpResponseRedirect("/")
