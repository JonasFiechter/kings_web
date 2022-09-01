from django.views.generic import ListView
from django.shortcuts import render
from .models import Post

# Create your views here.
def home_view(request):
    return render(request, 'home/index.html')

class PersonList(ListView):
    template_name = 'home/index.html'
    model = Post