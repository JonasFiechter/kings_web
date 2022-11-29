from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

#TODO: Finish responsive menu button and use paralax in some sections;

class LandingPageView(TemplateView):
    template_name: str = 'landing_page/index.html'