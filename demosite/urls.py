from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template

from mysite import settings

urlpatterns = patterns('',
	url(r'^$', direct_to_template, {'template': 'index.html'}, name="index"),
	url(r'^polls/', include('polls.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^accounts/', include('polls.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('', 
		(r'^include/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)

