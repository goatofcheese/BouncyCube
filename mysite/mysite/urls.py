from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^bouncycube/', include('bouncycube.urls', namespace="bouncycube")),
	url(r'^admin/', include(admin.site.urls)),
)
