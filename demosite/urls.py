from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
	url(r'^$', direct_to_template, {'template': 'head.html'}, name="index"),
	url(r'^polls/', include('demoapp.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^accounts/', include('demoapp.urls')),
)

