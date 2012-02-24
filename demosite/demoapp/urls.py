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
