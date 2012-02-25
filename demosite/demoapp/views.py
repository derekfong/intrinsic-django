# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from demoapp.models import Choice, Poll, Voted
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from forms import RegisterForm
from django.contrib import auth
import datetime

def index(request):

	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	return render_to_response('polls.html', {'latest_poll_list': latest_poll_list},
					context_instance=RequestContext(request))

def detail(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	user = request.user
	pollCheck = Voted.objects.filter(pollNumber=poll_id, userNumber=user.id).count()
	return render_to_response('detail.html', {'poll': p, 'pollCheck': pollCheck},
					context_instance=RequestContext(request))

def results(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('results.html', {'poll': p},
					context_instance=RequestContext(request))

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

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = RegisterForm()

	return render_to_response("register.html", {'form': form },
					context_instance=RequestContext(request))

def logout_view(request):
	auth.logout(request)
	return HttpResponseRedirect("/")
