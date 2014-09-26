from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from django.views.generic import View, TemplateView

# Create your views here.

class IndexView(TemplateView):
	template_name = "bouncycube/index.html"
	
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		return context

#TODO class these suckers up
def about(request):
	template = loader.get_template('bouncycube/about.html')
	context = Context()
	return HttpResponse(template.render(context))

def play(request):
	template = loader.get_template('bouncycube/play.html')
	context = Context()
	return HttpResponse(template.render(context))
