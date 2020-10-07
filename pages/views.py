from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AboutView(TemplateView):
	template_name='pages/about.html'


class HomeView(TemplateView):
	template_name='pages/index.html'
