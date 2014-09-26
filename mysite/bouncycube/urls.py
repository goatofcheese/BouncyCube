from django.conf.urls import patterns, url

from bouncycube import views

urlpatterns = patterns('',
	# /bouncycube/
	url(r'^$', views.IndexView.as_view(), name='index'),
	# /bouncycube/about
	url(r'^about/$', views.about, name='about'),
	# /bouncycube/play
	url(r'^play/$', views.play, name='play'),
)
