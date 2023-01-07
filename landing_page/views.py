from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

#TODO: Finish responsive menu button and use paralax in some sections;
#TODO: Add new section for exchange and online classes
# Desconto para empresas parceiras, permutas, redes sociais e indicações;

class LandingPageView(TemplateView):
    template_name: str = 'landing_page/index.html'