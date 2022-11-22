from django.views.generic.base import TemplateView
from django.shortcuts import render


def home_view(request):
    return render(request, 'home/index.html')