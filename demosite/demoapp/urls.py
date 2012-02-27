# File: urls.py
# Group: 12 (Team Intrinsic)
# Members: Kevin Mann, Derek Fong, Allison Ng
# CMPT470: Technical Evaluation
#
# Date of Creation: Feb 22, 2012
# Revised: Feb 24, 2012
#
# Description: Defines what views to direct URLs to

from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('demoapp.views',
    url(r'^$', 'index'),
	url(r'^(?P<poll_id>\d+)/$', 'detail'),
	url(r'^(?P<poll_id>\d+)/results/$', 'results'),
	url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
	url(r'register/$', 'register'),
	url(r'login/$', login),
	url(r'logout/$', 'logout_view'),
)
