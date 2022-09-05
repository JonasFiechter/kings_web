from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class LandingPageView(TemplateView):
    template_name: str = 'landing_page/index.html'